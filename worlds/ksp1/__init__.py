"""
Kerbal Space Program - Career Mode APWorld

Locations
---------
- Tech tree nodes (62): checked when the player researches a node via R&D.
- KSC building upgrades (18): checked when each building reaches level 2 or 3.
- Flag plants (15): checked when a flag is planted on any solid-surface body.

Items
-----
- Part bundles (63): one per tech node including the 'start' node. Each bundle
  makes parts from that node buildable in the VAB/SPH. Receiving a bundle for a
  researchable node also unlocks it in R&D.
- SOI permits (15): one per reachable body. Without a permit, entering that body's
  SOI instantly destroys the vessel.
- KSC upgrade items (4): gate access to Mun/Minmus and beyond.
  - Tracking Station Level 2: required to reach any body beyond Kerbin.
  - VAB Level 2, Launch Pad Level 2, Astronaut Complex Level 2: required to plant
    a flag on any body beyond Kerbin.
- Filler items: Funds/Reputation boosts.

Starting inventory
------------------
The player starts with one randomly-selected command pod, parachute, SRB, and one
terrestrial-compatible science experiment (mystery goo, thermometer, barometer,
seismic accelerometer, atmospheric analyzer, or gravity detector), all chosen from
ALL KSP parts (any tech node). Selection is deterministic per AP seed. Those parts
are always buildable; all other parts in those tech nodes are hidden until the
corresponding AP bundle is received.

Win condition (default: 'full')
-------------------------------
All 9 KSC buildings at level 3 AND flags planted on Mun AND Minmus.
"""

from worlds.AutoWorld import WebWorld, World
from BaseClasses import Region, Tutorial
from typing import Any

from .Items import (
    KSPItem, ALL_ITEMS, PART_BUNDLE_ITEMS, SOI_PERMIT_ITEMS,
    KSC_UPGRADE_ITEMS, FILLER_ITEMS,
    item_name_to_id, GAME_NAME,
)
from .Locations import (
    KSPLocation, ALL_LOCATIONS, TECH_LOCATIONS, KSC_UPGRADE_LOCATIONS, FLAG_LOCATIONS,
    location_name_to_id,
    tech_id_to_location_id, facility_to_location_id, body_to_location_id,
)
from .Options import KSPOptions


class KSPWebWorld(WebWorld):
    theme = "ice"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Kerbal Space Program Archipelago mod.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Baker80k"],
    )
    tutorials = [setup_en]


class KSPWorld(World):
    """
    Kerbal Space Program is a space flight simulation game. Build rockets and spacecraft,
    manage a space program, and explore a solar system of planets and moons. In Archipelago
    career mode, all ship parts and sphere-of-influence permits are randomized into the
    multiworld. Research the tech tree, upgrade the KSC, and plant flags on every body to win.
    """
    game = GAME_NAME
    web = KSPWebWorld()
    options_dataclass = KSPOptions
    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    def create_regions(self) -> None:
        p = self.player

        # ----- Menu region: tech tree, KSC upgrades, Kerbin flag -----
        menu = Region("Menu", p, self.multiworld)
        for name, loc_data in {**TECH_LOCATIONS, **KSC_UPGRADE_LOCATIONS}.items():
            menu.locations.append(KSPLocation(p, name, loc_data.id, menu))
        menu.locations.append(
            KSPLocation(p, "Flag: Kerbin", FLAG_LOCATIONS["Flag: Kerbin"].id, menu)
        )

        # ----- Access rule helpers -----
        def has_flag_infra(state) -> bool:
            """Prerequisites to plant a flag on any non-Kerbin body."""
            return (
                state.has("VAB Level 2",               p) and
                state.has("Launch Pad Level 2",        p) and
                state.has("Astronaut Complex Level 2", p)
            )

        def can_reach_beyond_kerbin(state) -> bool:
            """Tracking station + access to at least one Kerbin-system moon."""
            return (
                state.has("Tracking Station Level 2", p) and
                (state.has("Mun Permit", p) or state.has("Minmus Permit", p))
            )

        # ----- Helper: build a region with one flag location -----
        def flag_region(name: str, flag_extra_rule=None) -> Region:
            """Create a Region containing only 'Flag: <name>'."""
            r = Region(name, p, self.multiworld)
            loc = KSPLocation(p, f"Flag: {name}", FLAG_LOCATIONS[f"Flag: {name}"].id, r)
            if flag_extra_rule is not None:
                loc.access_rule = flag_extra_rule
            r.locations.append(loc)
            return r

        # ----- Mun -----
        mun = flag_region("Mun", lambda state: has_flag_infra(state))
        e = menu.create_exit("To Mun")
        e.access_rule = lambda state: (
            state.has("Mun Permit", p) and
            state.has("Tracking Station Level 2", p)
        )
        e.connect(mun)

        # ----- Minmus -----
        minmus = flag_region("Minmus", lambda state: has_flag_infra(state))
        e = menu.create_exit("To Minmus")
        e.access_rule = lambda state: (
            state.has("Minmus Permit", p) and
            state.has("Tracking Station Level 2", p)
        )
        e.connect(minmus)

        # ----- Outer solar system helpers -----
        # All outer bodies require TS L2 + (Mun or Minmus Permit) to reach.
        # Flags on all outer bodies additionally require flag infrastructure.

        def outer_entry(permit: str):
            """Entry rule from Menu to an outer-system body."""
            return lambda state, _permit=permit: (
                can_reach_beyond_kerbin(state) and
                state.has(_permit, p)
            )

        def moon_entry(permit: str):
            """Entry rule from a parent-body region to one of its moons."""
            return lambda state, _permit=permit: state.has(_permit, p)

        def outer_flag_infra(state) -> bool:
            """Flag plant on any outer body needs both flag infra and outer access."""
            return has_flag_infra(state) and can_reach_beyond_kerbin(state)

        # ----- Moho -----
        moho = flag_region("Moho", outer_flag_infra)
        e = menu.create_exit("To Moho")
        e.access_rule = outer_entry("Moho Permit")
        e.connect(moho)

        # ----- Eve system -----
        eve = flag_region("Eve", outer_flag_infra)
        e = menu.create_exit("To Eve")
        e.access_rule = outer_entry("Eve Permit")
        e.connect(eve)

        gilly = flag_region("Gilly", outer_flag_infra)
        e = eve.create_exit("To Gilly")
        e.access_rule = moon_entry("Gilly Permit")
        e.connect(gilly)

        # ----- Duna system -----
        duna = flag_region("Duna", outer_flag_infra)
        e = menu.create_exit("To Duna")
        e.access_rule = outer_entry("Duna Permit")
        e.connect(duna)

        ike = flag_region("Ike", outer_flag_infra)
        e = duna.create_exit("To Ike")
        e.access_rule = moon_entry("Ike Permit")
        e.connect(ike)

        # ----- Dres -----
        dres = flag_region("Dres", outer_flag_infra)
        e = menu.create_exit("To Dres")
        e.access_rule = outer_entry("Dres Permit")
        e.connect(dres)

        # ----- Jool system (Jool itself has no solid surface) -----
        jool = Region("Jool", p, self.multiworld)
        e = menu.create_exit("To Jool")
        e.access_rule = outer_entry("Jool Permit")
        e.connect(jool)

        for moon_name, moon_permit in [
            ("Laythe", "Laythe Permit"),
            ("Vall",   "Vall Permit"),
            ("Tylo",   "Tylo Permit"),
            ("Bop",    "Bop Permit"),
            ("Pol",    "Pol Permit"),
        ]:
            moon_r = flag_region(moon_name, outer_flag_infra)
            e = jool.create_exit(f"To {moon_name}")
            e.access_rule = moon_entry(moon_permit)
            e.connect(moon_r)

        # ----- Eeloo -----
        eeloo = flag_region("Eeloo", outer_flag_infra)
        e = menu.create_exit("To Eeloo")
        e.access_rule = outer_entry("Eeloo Permit")
        e.connect(eeloo)

        # ----- Register all regions -----
        self.multiworld.regions += [
            menu, mun, minmus,
            moho, eve, gilly,
            duna, ike,
            dres,
            jool,
        ]
        # Jool moon regions were connected above; collect them via traversal
        for exit_ in jool.exits:
            if exit_.connected_region is not None:
                self.multiworld.regions.append(exit_.connected_region)
        self.multiworld.regions += [eeloo]

    def create_items(self) -> None:
        pool = [
            self.create_item(name)
            for name in {**PART_BUNDLE_ITEMS, **SOI_PERMIT_ITEMS, **KSC_UPGRADE_ITEMS}
        ]

        filler_names = list(FILLER_ITEMS.keys())
        needed = len(ALL_LOCATIONS) - len(pool)
        for i in range(needed):
            pool.append(self.create_item(filler_names[i % len(filler_names)]))

        self.multiworld.itempool += pool

    def set_rules(self) -> None:
        use_full_goal = self.options.goal == 0

        def completion(state) -> bool:
            if not state.can_reach("Flag: Mun", "Location", self.player):
                return False
            if not state.can_reach("Flag: Minmus", "Location", self.player):
                return False
            if use_full_goal:
                return all(
                    state.can_reach(name, "Location", self.player)
                    for name in KSC_UPGRADE_LOCATIONS
                    if name.endswith("Level 3")
                )
            return True

        self.multiworld.completion_condition[self.player] = completion

    def generate_basic(self) -> None:
        """Pre-place one rocketry bundle at an early tech location.

        Guarantee: given ANY one of the tier-2/3 locations checked, the player
        receives at least one of the four rocketry progression bundles.
        This prevents a seed where no usable rocket engines arrive early.
        """
        early_locations = [
            "Tech: Basic Rocketry",
            "Tech: Engineering 101",
            "Tech: Survivability",
            "Tech: Stability",
            "Tech: General Rocketry",
        ]
        rocketry_items = [
            "Parts: Basic Rocketry",
            "Parts: General Rocketry",
            "Parts: Advanced Rocketry",
            "Parts: Heavier Rocketry",
        ]
        loc_name  = self.random.choice(early_locations)
        item_name = self.random.choice(rocketry_items)
        loc = self.multiworld.get_location(loc_name, self.player)
        # Remove one matching item from the pool (create_items already placed it).
        item_to_remove = next(
            (item for item in self.multiworld.itempool
             if item.player == self.player and item.name == item_name),
            None,
        )
        if item_to_remove is not None:
            self.multiworld.itempool.remove(item_to_remove)
        loc.place_locked_item(self.create_item(item_name))

    def get_filler_item_name(self) -> str:
        return self.random.choice(list(FILLER_ITEMS.keys()))

    def create_item(self, name: str) -> KSPItem:
        data = ALL_ITEMS[name]
        return KSPItem(name, data.classification, data.id, self.player)

    # Manned command pods (no probe cores; no _v2/_v3 variants).
    # AvailablePart.name values from KSP's part database.
    _STARTING_PODS = [
        "Mark1Cockpit",       # Mk1 Cockpit
        "Mark2Cockpit",       # Mk1 Inline Cockpit
        "mk2Cockpit_Standard",# Mk2 Standard Cockpit
        "mk2Cockpit_Inline",  # Mk2 Inline Cockpit
        "mk1pod_v2",          # Mk1 Command Pod (only version; original deprecated)
        "mk1-3pod",           # Mk1-3 Command Pod
        "landerCabinSmall",   # Mk1 Lander Can
        "mk2LanderCabin",     # Mk2 Lander Can
        "cupola",             # Cupola Module
    ]

    # Full parachutes only (no drogue chutes; no _v2/_v3 variants).
    _STARTING_CHUTES = [
        "parachuteSingle",    # Mk1 Parachute
        "parachuteRadial",    # Mk2-R Radial Parachute
        "parachuteLarge",     # Mk16-XL Parachute
    ]

    # Solid-fuel boosters (no Sepratron, no LES; no _v2/_v3 variants).
    _STARTING_SRBS = [
        "Mite",               # FM1 "Mite" Solid Fuel Booster
        "Shrimp",             # F3S0 "Shrimp" Solid Fuel Booster
        "solidBooster1-1",    # BACC "Thumper" Solid Fuel Booster
        "MassiveBooster",     # S1 SRB-KD25k "Kickback" Solid Fuel Booster
        "Thoroughbred",       # S2-17 "Thoroughbred" Solid Fuel Booster
        "Clydesdale",         # S2-33 "Clydesdale" Solid Fuel Booster
    ]

    # Terrestrial-compatible science experiments granted at game start.
    # Excludes: infrared telescope and magnetometer boom (space-only),
    # and materials study (Science Jr.) which makes the start too easy.
    _STARTING_EXPERIMENTS = [
        "mysteryGoo",        # Mystery Goo Containment Unit
        "temperatureScan",   # 2HOT Thermometer
        "barometerScan",     # PresMat Barometer
        "seismicScan",       # Seismic Accelerometer
        "atmosphereAnalysis",# SCAN Atmospheric Analyzer
        "gravityScan",       # GRAVMAX Negative Gravioli Detector
    ]

    def fill_slot_data(self) -> dict[str, Any]:
        """
        Passed to the client on connection. Gives the C# plugin the ID tables it needs
        to map KSP events to AP location IDs and AP item names to KSP tech IDs.
        The C# plugin also has these hardcoded; slot_data is a cross-check / future
        extension point.
        """
        return {
            "tech_id_to_location_id":   tech_id_to_location_id,
            "facility_to_location_id":  facility_to_location_id,
            "body_to_location_id":      body_to_location_id,
            "part_bundle_to_tech_id": {
                name: data.tech_id
                for name, data in PART_BUNDLE_ITEMS.items()
                if data.tech_id is not None
            },
            # AvailablePart.name for the three always-available starting parts.
            # The C# plugin looks each up by name in PartLoader and makes it visible.
            "starting_pod":        self.random.choice(self._STARTING_PODS),
            "starting_chute":      self.random.choice(self._STARTING_CHUTES),
            "starting_srb":        self.random.choice(self._STARTING_SRBS),
            # KSP ModuleScienceExperiment.experimentID for the starting science part.
            "starting_experiment": self.random.choice(self._STARTING_EXPERIMENTS),
        }
