from BaseClasses import Item, ItemClassification
from typing import NamedTuple

GAME_NAME = "Kerbal Space Program 1.12"
BASE_ID = 1969000


class ItemData(NamedTuple):
    id: int
    classification: ItemClassification
    # KSP internal RDTech.techID for part bundles; None for other items
    tech_id: str | None = None


# One part bundle per tech tree node (62 total - all researchable nodes).
# Ordered to match TechTree.cfg tier order; IDs are BASE_ID + index.
# Item name = "Parts: {in-game node title}"
# tech_id  = KSP's RDTech.techID string
PART_BUNDLE_ITEMS: dict[str, ItemData] = {
    # --- Tier 1 (start node - cannot be researched; unlocked via AP item) ---
    "Parts: Start":                          ItemData(BASE_ID + 62, ItemClassification.progression, "start"),
    # --- Tier 2 ---
    "Parts: Basic Rocketry":               ItemData(BASE_ID +  0, ItemClassification.progression, "basicRocketry"),
    "Parts: Engineering 101":              ItemData(BASE_ID +  1, ItemClassification.progression, "engineering101"),
    # --- Tier 3 ---
    "Parts: Survivability":                ItemData(BASE_ID +  2, ItemClassification.progression, "survivability"),
    "Parts: Stability":                    ItemData(BASE_ID +  3, ItemClassification.progression, "stability"),
    "Parts: General Rocketry":             ItemData(BASE_ID +  4, ItemClassification.progression, "generalRocketry"),
    "Parts: Aviation":                     ItemData(BASE_ID +  5, ItemClassification.progression, "aviation"),
    "Parts: Basic Science":                ItemData(BASE_ID +  6, ItemClassification.useful,      "basicScience"),
    "Parts: Flight Control":               ItemData(BASE_ID +  7, ItemClassification.progression, "flightControl"),
    # --- Tier 4 ---
    "Parts: Advanced Rocketry":            ItemData(BASE_ID +  8, ItemClassification.progression, "advRocketry"),
    "Parts: General Construction":         ItemData(BASE_ID +  9, ItemClassification.progression, "generalConstruction"),
    "Parts: Propulsion Systems":           ItemData(BASE_ID + 10, ItemClassification.progression, "propulsionSystems"),
    "Parts: Space Exploration":            ItemData(BASE_ID + 11, ItemClassification.useful,      "spaceExploration"),
    "Parts: Advanced Flight Control":      ItemData(BASE_ID + 12, ItemClassification.progression, "advFlightControl"),
    "Parts: Landing":                      ItemData(BASE_ID + 13, ItemClassification.progression, "landing"),
    "Parts: Aerodynamics":                 ItemData(BASE_ID + 14, ItemClassification.progression, "aerodynamicSystems"),
    "Parts: Electrics":                    ItemData(BASE_ID + 15, ItemClassification.progression, "electrics"),
    # --- Tier 5 ---
    "Parts: Heavy Rocketry":               ItemData(BASE_ID + 16, ItemClassification.progression, "heavyRocketry"),
    "Parts: Fuel Systems":                 ItemData(BASE_ID + 17, ItemClassification.progression, "fuelSystems"),
    "Parts: Advanced Construction":        ItemData(BASE_ID + 18, ItemClassification.progression, "advConstruction"),
    "Parts: Miniaturization":              ItemData(BASE_ID + 19, ItemClassification.progression, "miniaturization"),
    "Parts: Actuators":                    ItemData(BASE_ID + 20, ItemClassification.progression, "actuators"),
    "Parts: Command Modules":              ItemData(BASE_ID + 21, ItemClassification.progression, "commandModules"),
    "Parts: Heavier Rocketry":             ItemData(BASE_ID + 22, ItemClassification.progression, "heavierRocketry"),
    "Parts: Precision Engineering":        ItemData(BASE_ID + 23, ItemClassification.progression, "precisionEngineering"),
    "Parts: Advanced Exploration":         ItemData(BASE_ID + 24, ItemClassification.useful,      "advExploration"),
    "Parts: Specialized Control":          ItemData(BASE_ID + 25, ItemClassification.progression, "specializedControl"),
    "Parts: Advanced Landing":             ItemData(BASE_ID + 26, ItemClassification.progression, "advLanding"),
    # --- Tier 6 ---
    "Parts: Supersonic Flight":            ItemData(BASE_ID + 27, ItemClassification.progression, "supersonicFlight"),
    "Parts: Adv. Fuel Systems":            ItemData(BASE_ID + 28, ItemClassification.progression, "advFuelSystems"),
    "Parts: Advanced Electrics":           ItemData(BASE_ID + 29, ItemClassification.progression, "advElectrics"),
    "Parts: Specialized Construction":     ItemData(BASE_ID + 30, ItemClassification.progression, "specializedConstruction"),
    "Parts: Precision Propulsion":         ItemData(BASE_ID + 31, ItemClassification.progression, "precisionPropulsion"),
    "Parts: Advanced Aerodynamics":        ItemData(BASE_ID + 32, ItemClassification.progression, "advAerodynamics"),
    "Parts: Heavy Landing":                ItemData(BASE_ID + 33, ItemClassification.progression, "heavyLanding"),
    "Parts: Scanning Tech":                ItemData(BASE_ID + 34, ItemClassification.useful,      "scienceTech"),
    "Parts: Unmanned Tech":                ItemData(BASE_ID + 35, ItemClassification.progression, "unmannedTech"),
    # --- Tier 7 ---
    "Parts: Nuclear Propulsion":           ItemData(BASE_ID + 36, ItemClassification.progression, "nuclearPropulsion"),
    "Parts: Advanced MetalWorks":          ItemData(BASE_ID + 37, ItemClassification.useful,      "advMetalworks"),
    "Parts: Field Science":                ItemData(BASE_ID + 38, ItemClassification.useful,      "fieldScience"),
    "Parts: High Altitude Flight":         ItemData(BASE_ID + 39, ItemClassification.progression, "highAltitudeFlight"),
    "Parts: Large Volume Containment":     ItemData(BASE_ID + 40, ItemClassification.useful,      "largeVolumeContainment"),
    "Parts: Composites":                   ItemData(BASE_ID + 41, ItemClassification.progression, "composites"),
    "Parts: Electronics":                  ItemData(BASE_ID + 42, ItemClassification.progression, "electronics"),
    "Parts: High-Power Electrics":         ItemData(BASE_ID + 43, ItemClassification.progression, "largeElectrics"),
    "Parts: Heavy Aerodynamics":           ItemData(BASE_ID + 44, ItemClassification.progression, "heavyAerodynamics"),
    "Parts: Ion Propulsion":               ItemData(BASE_ID + 45, ItemClassification.useful,      "ionPropulsion"),
    "Parts: Hypersonic Flight":            ItemData(BASE_ID + 46, ItemClassification.progression, "hypersonicFlight"),
    # --- Tier 8 ---
    "Parts: Nanolathing":                  ItemData(BASE_ID + 47, ItemClassification.useful,      "nanolathing"),
    "Parts: Advanced Unmanned Tech":       ItemData(BASE_ID + 48, ItemClassification.useful,      "advUnmanned"),
    "Parts: Meta-Materials":               ItemData(BASE_ID + 49, ItemClassification.useful,      "metaMaterials"),
    "Parts: Very Heavy Rocketry":          ItemData(BASE_ID + 50, ItemClassification.progression, "veryHeavyRocketry"),
    "Parts: Advanced Science Tech":        ItemData(BASE_ID + 51, ItemClassification.useful,      "advScienceTech"),
    "Parts: Advanced Motors":              ItemData(BASE_ID + 52, ItemClassification.useful,      "advancedMotors"),
    "Parts: Specialized Electrics":        ItemData(BASE_ID + 53, ItemClassification.useful,      "specializedElectrics"),
    "Parts: High-Performance Fuel Systems": ItemData(
        BASE_ID + 54, ItemClassification.progression, "highPerformanceFuelSystems"
    ),
    "Parts: Experimental Aerodynamics":    ItemData(BASE_ID + 55, ItemClassification.useful,      "experimentalAerodynamics"),
    # --- Tier 9 ---
    "Parts: Automation":                   ItemData(BASE_ID + 56, ItemClassification.useful,      "automation"),
    "Parts: Aerospace Tech":               ItemData(BASE_ID + 57, ItemClassification.useful,      "aerospaceTech"),
    "Parts: Large Probes":                 ItemData(BASE_ID + 58, ItemClassification.useful,      "largeUnmanned"),
    # --- Tier 10 ---
    "Parts: Experimental Science":         ItemData(BASE_ID + 59, ItemClassification.useful,      "experimentalScience"),
    "Parts: Experimental Motors":          ItemData(BASE_ID + 60, ItemClassification.useful,      "experimentalMotors"),
    "Parts: Experimental Electrics":       ItemData(BASE_ID + 61, ItemClassification.useful,      "experimentalElectrics"),
}

# SOI permits gate access to planetary bodies.
# Moons within a system also require their parent body's permit (enforced by SOI
# explosion in the C# plugin and modelled in AP logic via region nesting).
SOI_PERMIT_ITEMS: dict[str, ItemData] = {
    # Kerbin system
    "Mun Permit":    ItemData(BASE_ID +  90, ItemClassification.progression),
    "Minmus Permit": ItemData(BASE_ID +  91, ItemClassification.progression),
    # Inner planets
    "Moho Permit":   ItemData(BASE_ID +  92, ItemClassification.progression),
    "Eve Permit":    ItemData(BASE_ID +  93, ItemClassification.progression),
    "Gilly Permit":  ItemData(BASE_ID +  94, ItemClassification.progression),
    # Duna system
    "Duna Permit":   ItemData(BASE_ID +  95, ItemClassification.progression),
    "Ike Permit":    ItemData(BASE_ID +  96, ItemClassification.progression),
    # Dres
    "Dres Permit":   ItemData(BASE_ID +  97, ItemClassification.progression),
    # Jool system (Jool itself is a gas giant; moons also need Jool Permit)
    "Jool Permit":   ItemData(BASE_ID +  98, ItemClassification.progression),
    "Laythe Permit": ItemData(BASE_ID +  99, ItemClassification.progression),
    "Vall Permit":   ItemData(BASE_ID + 100, ItemClassification.progression),
    "Tylo Permit":   ItemData(BASE_ID + 101, ItemClassification.progression),
    "Bop Permit":    ItemData(BASE_ID + 102, ItemClassification.progression),
    "Pol Permit":    ItemData(BASE_ID + 103, ItemClassification.progression),
    # Eeloo
    "Eeloo Permit":  ItemData(BASE_ID + 104, ItemClassification.progression),
}

# KSC upgrade items gate region access and flag-plant checks.
# Tracking Station L2: needed to reach Mun/Minmus and any outer body.
# VAB L2, Launch Pad L2, Astronaut Complex L2: needed to plant a flag anywhere
# beyond Kerbin (required for EVA, heavy launches, and patched-conic planning).
KSC_UPGRADE_ITEMS: dict[str, ItemData] = {
    "Tracking Station Level 2":  ItemData(BASE_ID + 200, ItemClassification.progression),
    "VAB Level 2":               ItemData(BASE_ID + 201, ItemClassification.progression),
    "Launch Pad Level 2":        ItemData(BASE_ID + 202, ItemClassification.progression),
    "Astronaut Complex Level 2": ItemData(BASE_ID + 203, ItemClassification.progression),
}

# Filler items: in-game currency/resource bonuses.
FILLER_ITEMS: dict[str, ItemData] = {
    "Funds Boost":      ItemData(BASE_ID + 150, ItemClassification.filler),
    "Science Boost":    ItemData(BASE_ID + 151, ItemClassification.filler),
    "Reputation Boost": ItemData(BASE_ID + 152, ItemClassification.filler),
}

ALL_ITEMS: dict[str, ItemData] = {
    **PART_BUNDLE_ITEMS,
    **SOI_PERMIT_ITEMS,
    **KSC_UPGRADE_ITEMS,
    **FILLER_ITEMS,
}

item_name_to_id: dict[str, int] = {name: data.id for name, data in ALL_ITEMS.items()}


class KSPItem(Item):
    game = GAME_NAME
