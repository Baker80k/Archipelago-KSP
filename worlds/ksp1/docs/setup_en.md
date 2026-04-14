# Kerbal Space Program Archipelago Setup Guide

## Required Software

- [Kerbal Space Program 1](https://store.steampowered.com/app/220200/Kerbal_Space_Program/) (Steam or DRM-free)
- [Python 3.11+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python package manager)
- The Archipelago KSP mod from this repository

## Installation

### 1. Install the C# Plugin Mod

Build and deploy the plugin from the repository root:

```bash
./00_dotnet.sh
```

This builds `ArchipelagoKSP.dll` and copies it to `ArchipelagoKSP/GameData/ArchipelagoKSP/Plugins/`.
Copy the `ArchipelagoKSP/GameData/ArchipelagoKSP/` folder into your KSP `GameData/` directory.

Restart KSP to load the mod.

### 2. Generate a Multiworld Game

Create or edit `player_files/ksp_template.yaml` with your desired options, then run:

```bash
./01_generate.sh
```

Output lands in `Archipelago/output/`.

### 3. Start the AP Client Bridge

Before launching KSP, start the client bridge:

```bash
./02_client.sh
```

This starts a local HTTP bridge on `127.0.0.1:52420` that relays between KSP and the Archipelago server.

### 4. Connect In-Game

1. Launch KSP and start a **Career Mode** save.
2. Press **F8** to open the Archipelago connection window.
3. Enter the server address, slot name, and password.
4. Click **Connect**.

## Options

| Option | Description | Default |
|---|---|---|
| `goal` | Win condition: `full` (all KSC buildings max + all flags) or `flags_only` (flags only) | `full` |

## Gameplay Notes

- The player starts with one randomly selected command pod, parachute, and solid rocket booster.
- All other parts must be received from the multiworld before they can be used.
- Entering a body's sphere of influence without the matching SOI permit instantly destroys the vessel.
- Tech nodes still require Science to research, but researching a node checks that AP location.
  The node's parts are not available until the matching AP item is received.

## Troubleshooting

- KSP log is at `<KSP install>/KSP.log`.
- The client bridge must be running before connecting in-game.
- If the connection window does not appear, confirm `ArchipelagoKSP.dll` is in `GameData/ArchipelagoKSP/Plugins/`.
