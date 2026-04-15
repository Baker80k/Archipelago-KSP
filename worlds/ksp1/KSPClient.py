"""
KSP Archipelago Client
======================
Bridges the KSP C# plugin (via a local HTTP server on port 52420) to the
Archipelago multiworld server.

Usage
-----
Run from the ksp_attempt/ directory:

    python -m apksp.KSPClient [--connect archipelago.gg:38281] [--name SlotName]

Or from the Archipelago/ subdirectory:

    cd Archipelago
    python ../apksp/KSPClient.py [server:port] [--name SlotName]

The C# plugin communicates with this client via:
    GET  /status          -> {"connected": bool, "slot": str}
    GET  /items           -> {"items": [str, ...], "index": int}
    POST /check           -> body: {"location_id": int}
    POST /connect         -> body: {"server": str, "slot": str, "password": str}

Start this client BEFORE launching KSP. Use F8 in-game to open the connection UI.
"""

import asyncio
import json
import logging
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Optional

# Add Archipelago-KSP/ to path so CommonClient etc. are importable
_this_dir = os.path.dirname(os.path.abspath(__file__))
_archipelago_dir = os.path.join(os.path.dirname(_this_dir), "Archipelago-KSP")
if os.path.isdir(_archipelago_dir) and _archipelago_dir not in sys.path:
    sys.path.insert(0, _archipelago_dir)

from CommonClient import (
    CommonContext,
    ClientCommandProcessor,
    get_base_parser,
    gui_enabled,
    logger,
    server_loop,
)
from Utils import async_start

GAME_NAME = "Kerbal Space Program"
BRIDGE_PORT = 52420


# ---------------------------------------------------------------------------
# Command processor
# ---------------------------------------------------------------------------

class KSPCommandProcessor(ClientCommandProcessor):
    def _cmd_status(self) -> bool:
        """Show AP connection and item status."""
        connected = bool(self.ctx.server and not self.ctx.server.socket.closed)
        self.output(f"Connected:        {connected}")
        self.output(f"Items received:   {len(self.ctx.items_received)}")
        self.output(f"Locations sent:   {len(self.ctx.locations_checked)}")
        return True


# ---------------------------------------------------------------------------
# Client context
# ---------------------------------------------------------------------------

class KSPContext(CommonContext):
    game = GAME_NAME
    items_handling = 0b111  # receive all items from all sources
    command_processor = KSPCommandProcessor

    def __init__(self, server_address: Optional[str], password: Optional[str]):
        super().__init__(server_address, password)
        # Slot data populated on Connected packet
        self.part_bundle_to_tech_id: dict = {}
        self.starting_pod:   str = ""
        self.starting_chute: str = ""
        self.starting_srb:   str = ""
        self.starting_experiment: str = ""

    async def server_auth(self, password_requested: bool = False) -> None:
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict) -> None:
        if cmd == "Connected":
            sd = args.get("slot_data", {})
            self.part_bundle_to_tech_id = sd.get("part_bundle_to_tech_id", {})
            self.starting_pod   = sd.get("starting_pod",   "")
            self.starting_chute = sd.get("starting_chute", "")
            self.starting_srb   = sd.get("starting_srb",   "")
            self.starting_experiment = sd.get("starting_experiment", "")
            logger.info("[APKSP] Slot data received.")

    # ------------------------------------------------------------------
    # Data helpers for the bridge HTTP server
    # ------------------------------------------------------------------

    def items_list(self) -> list:
        """All received item names in order (index = position in list)."""
        out = []
        for net_item in self.items_received:
            name = self.item_names.lookup_in_game(net_item.item)
            out.append(name)
        return out

    def status_dict(self) -> dict:
        connected = bool(self.server and not self.server.socket.closed)
        return {
            "connected": connected,
            "slot": self.auth or "",
            "game": self.game,
            "starting_pod":        self.starting_pod,
            "starting_chute":      self.starting_chute,
            "starting_srb":        self.starting_srb,
            "starting_experiment": self.starting_experiment,
        }


# ---------------------------------------------------------------------------
# Local HTTP bridge server
# ---------------------------------------------------------------------------

def make_bridge_handler(ctx: KSPContext, loop: asyncio.AbstractEventLoop):
    """Return a BaseHTTPRequestHandler class closed over ctx and loop."""

    class BridgeHandler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            # Suppress per-request access log to keep the console clean.
            pass

        # ---- helpers ----

        def send_json(self, code: int, obj: object) -> None:
            body = json.dumps(obj).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def read_json_body(self) -> Optional[dict]:
            length = int(self.headers.get("Content-Length", 0))
            if length == 0:
                return {}
            raw = self.rfile.read(length)
            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                return None

        # ---- GET ----

        def do_GET(self):
            if self.path == "/items":
                items = ctx.items_list()
                self.send_json(200, {"items": items, "index": len(items)})
            elif self.path == "/status":
                self.send_json(200, ctx.status_dict())
            else:
                self.send_json(404, {"error": "not found"})

        # ---- POST ----

        def do_POST(self):
            body = self.read_json_body()
            if body is None:
                self.send_json(400, {"error": "invalid JSON"})
                return

            if self.path == "/check":
                loc_id = body.get("location_id")
                if loc_id is None:
                    self.send_json(400, {"error": "missing location_id"})
                    return
                future = asyncio.run_coroutine_threadsafe(
                    ctx.check_locations([int(loc_id)]), loop
                )
                try:
                    new_locs = future.result(timeout=5.0)
                    self.send_json(200, {"ok": True, "new": int(loc_id) in new_locs})
                except Exception as exc:
                    logger.warning(f"[APKSP] check_locations error: {exc}")
                    self.send_json(200, {"ok": False, "error": str(exc)})

            elif self.path == "/connect":
                server = body.get("server", "").strip()
                slot = body.get("slot", "").strip()
                password = body.get("password", "").strip() or None
                if not server or not slot:
                    self.send_json(400, {"error": "server and slot required"})
                    return
                ctx.auth = slot
                ctx.password = password
                asyncio.run_coroutine_threadsafe(ctx.connect(server), loop)
                logger.info(f"[APKSP] Connecting to {server} as {slot}...")
                self.send_json(200, {"ok": True})

            else:
                self.send_json(404, {"error": "not found"})

    return BridgeHandler


def run_bridge(ctx: KSPContext, loop: asyncio.AbstractEventLoop) -> None:
    handler = make_bridge_handler(ctx, loop)
    httpd = HTTPServer(("127.0.0.1", BRIDGE_PORT), handler)
    logger.info(f"[APKSP] Bridge listening on 127.0.0.1:{BRIDGE_PORT}")
    httpd.serve_forever()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

async def main(args) -> None:
    ctx = KSPContext(args.connect, args.password)
    if hasattr(args, "name") and args.name:
        ctx.auth = args.name

    loop = asyncio.get_event_loop()

    bridge_thread = threading.Thread(
        target=run_bridge, args=(ctx, loop), daemon=True, name="APKSP-bridge"
    )
    bridge_thread.start()

    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    await ctx.exit_event.wait()
    await ctx.shutdown()


if __name__ == "__main__":
    import colorama

    parser = get_base_parser(
        description="Kerbal Space Program Archipelago Client. "
        "Run this before launching KSP, then use F8 in-game to connect."
    )
    parser.add_argument("--name", default=None, help="Slot name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection URL.")
    args = parser.parse_args()

    colorama.just_fix_windows_console()
    asyncio.run(main(args))
    colorama.deinit()
