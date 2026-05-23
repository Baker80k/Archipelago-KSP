from BaseClasses import Location
from typing import NamedTuple

GAME_NAME = "Kerbal Space Program"
BASE_ID       = 1969000
TECH_LOC_BASE = BASE_ID + 1000   # 1970000
KSC_LOC_BASE  = BASE_ID + 2000   # 1971000
FLAG_LOC_BASE = BASE_ID + 3000   # 1972000


class LocationData(NamedTuple):
    id: int
    # KSP-internal key used to trigger this check:
    #   tech locations:    RDTech.techID  e.g. "basicRocketry"
    #   KSC locations:     "facilityID:newLevel" (0-indexed new level: 1 = upgraded to L2, 2 = upgraded to L3)
    #   flag locations:    CelestialBody.name  e.g. "Mun"
    ksp_key: str


# --- Tier 2 ---
TECH_TIER_2: dict[str, LocationData] = {
    "Tech: Basic Rocketry":               LocationData(TECH_LOC_BASE +  0, "basicRocketry"),
    "Tech: Engineering 101":              LocationData(TECH_LOC_BASE +  1, "engineering101"),
}

# --- Tier 3 ---
TECH_TIER_3: dict[str, LocationData] = {
    "Tech: Survivability":                LocationData(TECH_LOC_BASE +  2, "survivability"),
    "Tech: Stability":                    LocationData(TECH_LOC_BASE +  3, "stability"),
    "Tech: General Rocketry":             LocationData(TECH_LOC_BASE +  4, "generalRocketry"),
}

# --- Tier 4 ---, everything beyond this I don't really care about
TECH_TIER_4: dict[str, LocationData] = {
    "Tech: Aviation":                     LocationData(TECH_LOC_BASE +  5, "aviation"),
    "Tech: Basic Science":                LocationData(TECH_LOC_BASE +  6, "basicScience"),
    "Tech: Flight Control":               LocationData(TECH_LOC_BASE +  7, "flightControl"),
    "Tech: Advanced Rocketry":            LocationData(TECH_LOC_BASE +  8, "advRocketry"),
    "Tech: General Construction":         LocationData(TECH_LOC_BASE +  9, "generalConstruction"),
    "Tech: Propulsion Systems":           LocationData(TECH_LOC_BASE + 10, "propulsionSystems"),
    "Tech: Space Exploration":            LocationData(TECH_LOC_BASE + 11, "spaceExploration"),
    "Tech: Advanced Flight Control":      LocationData(TECH_LOC_BASE + 12, "advFlightControl"),
    "Tech: Landing":                      LocationData(TECH_LOC_BASE + 13, "landing"),
    "Tech: Aerodynamics":                 LocationData(TECH_LOC_BASE + 14, "aerodynamicSystems"),
    "Tech: Electrics":                    LocationData(TECH_LOC_BASE + 15, "electrics"),
}

# --- Tier 5 ---
TECH_TIER_5: dict[str, LocationData] = {
    "Tech: Heavy Rocketry":               LocationData(TECH_LOC_BASE + 16, "heavyRocketry"),
    "Tech: Fuel Systems":                 LocationData(TECH_LOC_BASE + 17, "fuelSystems"),
    "Tech: Advanced Construction":        LocationData(TECH_LOC_BASE + 18, "advConstruction"),
    "Tech: Miniaturization":              LocationData(TECH_LOC_BASE + 19, "miniaturization"),
    "Tech: Actuators":                    LocationData(TECH_LOC_BASE + 20, "actuators"),
    "Tech: Command Modules":              LocationData(TECH_LOC_BASE + 21, "commandModules"),
    "Tech: Heavier Rocketry":             LocationData(TECH_LOC_BASE + 22, "heavierRocketry"),
    "Tech: Precision Engineering":        LocationData(TECH_LOC_BASE + 23, "precisionEngineering"),
    "Tech: Advanced Exploration":         LocationData(TECH_LOC_BASE + 24, "advExploration"),
    "Tech: Specialized Control":          LocationData(TECH_LOC_BASE + 25, "specializedControl"),
    "Tech: Advanced Landing":             LocationData(TECH_LOC_BASE + 26, "advLanding"),
}

# --- Tier 6 ---
TECH_TIER_6: dict[str, LocationData] = {
    "Tech: Supersonic Flight":            LocationData(TECH_LOC_BASE + 27, "supersonicFlight"),
    "Tech: Adv. Fuel Systems":            LocationData(TECH_LOC_BASE + 28, "advFuelSystems"),
    "Tech: Advanced Electrics":           LocationData(TECH_LOC_BASE + 29, "advElectrics"),
    "Tech: Specialized Construction":     LocationData(TECH_LOC_BASE + 30, "specializedConstruction"),
    "Tech: Precision Propulsion":         LocationData(TECH_LOC_BASE + 31, "precisionPropulsion"),
    "Tech: Advanced Aerodynamics":        LocationData(TECH_LOC_BASE + 32, "advAerodynamics"),
    "Tech: Heavy Landing":                LocationData(TECH_LOC_BASE + 33, "heavyLanding"),
    "Tech: Scanning Tech":                LocationData(TECH_LOC_BASE + 34, "scienceTech"),
    "Tech: Unmanned Tech":                LocationData(TECH_LOC_BASE + 35, "unmannedTech"),
}

# --- Tier 7 ---
TECH_TIER_7: dict[str, LocationData] = {
    "Tech: Nuclear Propulsion":           LocationData(TECH_LOC_BASE + 36, "nuclearPropulsion"),
    "Tech: Advanced MetalWorks":          LocationData(TECH_LOC_BASE + 37, "advMetalworks"),
    "Tech: Field Science":                LocationData(TECH_LOC_BASE + 38, "fieldScience"),
    "Tech: High Altitude Flight":         LocationData(TECH_LOC_BASE + 39, "highAltitudeFlight"),
    "Tech: Large Volume Containment":     LocationData(TECH_LOC_BASE + 40, "largeVolumeContainment"),
    "Tech: Composites":                   LocationData(TECH_LOC_BASE + 41, "composites"),
    "Tech: Electronics":                  LocationData(TECH_LOC_BASE + 42, "electronics"),
    "Tech: High-Power Electrics":         LocationData(TECH_LOC_BASE + 43, "largeElectrics"),
    "Tech: Heavy Aerodynamics":           LocationData(TECH_LOC_BASE + 44, "heavyAerodynamics"),
    "Tech: Ion Propulsion":               LocationData(TECH_LOC_BASE + 45, "ionPropulsion"),
    "Tech: Hypersonic Flight":            LocationData(TECH_LOC_BASE + 46, "hypersonicFlight"),
}

# --- Tier 8 ---
TECH_TIER_8: dict[str, LocationData] = {
    "Tech: Advanced Unmanned Tech":       LocationData(TECH_LOC_BASE + 48, "advUnmanned"),
    "Tech: Meta-Materials":               LocationData(TECH_LOC_BASE + 49, "metaMaterials"),
    "Tech: Very Heavy Rocketry":          LocationData(TECH_LOC_BASE + 50, "veryHeavyRocketry"),
    "Tech: Advanced Science Tech":        LocationData(TECH_LOC_BASE + 51, "advScienceTech"),
    "Tech: Advanced Motors":              LocationData(TECH_LOC_BASE + 52, "advancedMotors"),
    "Tech: Specialized Electrics":        LocationData(TECH_LOC_BASE + 53, "specializedElectrics"),
    "Tech: High-Performance Fuel Systems":LocationData(TECH_LOC_BASE + 54, "highPerformanceFuelSystems"),
    "Tech: Experimental Aerodynamics":    LocationData(TECH_LOC_BASE + 55, "experimentalAerodynamics"),
}

# --- Tier 9 ---
TECH_TIER_9: dict[str, LocationData] = {
    "Tech: Automation":                   LocationData(TECH_LOC_BASE + 56, "automation"),
    "Tech: Aerospace Tech":               LocationData(TECH_LOC_BASE + 57, "aerospaceTech"),
    "Tech: Large Probes":                 LocationData(TECH_LOC_BASE + 58, "largeUnmanned"),
}

# --- Tier 10 ---
TECH_TIER_10: dict[str, LocationData] = {
    "Tech: Experimental Science":         LocationData(TECH_LOC_BASE + 59, "experimentalScience"),
    "Tech: Experimental Electrics":       LocationData(TECH_LOC_BASE + 61, "experimentalElectrics"),
}

# Tech tree node locations - one per researchable node (60 total, tiers 2-10).
TECH_LOCATIONS: dict[str, LocationData] = {
    **TECH_TIER_2,
    **TECH_TIER_3,
    **TECH_TIER_4,
    **TECH_TIER_5,
    **TECH_TIER_6,
    **TECH_TIER_7,
    **TECH_TIER_8,
    **TECH_TIER_9,
    **TECH_TIER_10,
}

# --- KSC Level 2 upgrades ---
KSC_LEVEL_2: dict[str, LocationData] = {
    "KSC: VAB Level 2":               LocationData(KSC_LOC_BASE +  0, "SpaceCenter/VehicleAssemblyBuilding:1"),
    "KSC: SPH Level 2":               LocationData(KSC_LOC_BASE +  2, "SpaceCenter/SpaceplaneHangar:1"),
    "KSC: Research Lab Level 2":      LocationData(KSC_LOC_BASE +  4, "SpaceCenter/ResearchAndDevelopment:1"),
    "KSC: Mission Control Level 2":   LocationData(KSC_LOC_BASE +  6, "SpaceCenter/MissionControl:1"),
    "KSC: Tracking Station Level 2":  LocationData(KSC_LOC_BASE +  8, "SpaceCenter/TrackingStation:1"),
    "KSC: Astronaut Complex Level 2": LocationData(KSC_LOC_BASE + 10, "SpaceCenter/AstronautComplex:1"),
    "KSC: Launch Pad Level 2":        LocationData(KSC_LOC_BASE + 12, "SpaceCenter/LaunchPad:1"),
    "KSC: Runway Level 2":            LocationData(KSC_LOC_BASE + 14, "SpaceCenter/Runway:1"),
    "KSC: Administration Level 2":    LocationData(KSC_LOC_BASE + 16, "SpaceCenter/Administration:1"),
}

# --- KSC Level 3 upgrades ---
KSC_LEVEL_3: dict[str, LocationData] = {
    "KSC: VAB Level 3":               LocationData(KSC_LOC_BASE +  1, "SpaceCenter/VehicleAssemblyBuilding:2"),
    "KSC: SPH Level 3":               LocationData(KSC_LOC_BASE +  3, "SpaceCenter/SpaceplaneHangar:2"),
    "KSC: Research Lab Level 3":      LocationData(KSC_LOC_BASE +  5, "SpaceCenter/ResearchAndDevelopment:2"),
    "KSC: Mission Control Level 3":   LocationData(KSC_LOC_BASE +  7, "SpaceCenter/MissionControl:2"),
    "KSC: Tracking Station Level 3":  LocationData(KSC_LOC_BASE +  9, "SpaceCenter/TrackingStation:2"),
    "KSC: Astronaut Complex Level 3": LocationData(KSC_LOC_BASE + 11, "SpaceCenter/AstronautComplex:2"),
    "KSC: Launch Pad Level 3":        LocationData(KSC_LOC_BASE + 13, "SpaceCenter/LaunchPad:2"),
    "KSC: Runway Level 3":            LocationData(KSC_LOC_BASE + 15, "SpaceCenter/Runway:2"),
    "KSC: Administration Level 3":    LocationData(KSC_LOC_BASE + 17, "SpaceCenter/Administration:2"),
}

# KSC building upgrade locations - 9 buildings x 2 upgrades (18 total).
KSC_UPGRADE_LOCATIONS: dict[str, LocationData] = {
    **KSC_LEVEL_2,
    **KSC_LEVEL_3,
}

FLAG_LOCATIONS: dict[str, LocationData] = {
    # Kerbin system
    "Flag: Kerbin":  LocationData(FLAG_LOC_BASE +  0, "Kerbin"),
    "Flag: Mun":     LocationData(FLAG_LOC_BASE +  1, "Mun"),
    "Flag: Minmus":  LocationData(FLAG_LOC_BASE +  2, "Minmus"),
    # Inner planets
    "Flag: Moho":    LocationData(FLAG_LOC_BASE +  3, "Moho"),
    "Flag: Eve":     LocationData(FLAG_LOC_BASE +  4, "Eve"),
    "Flag: Gilly":   LocationData(FLAG_LOC_BASE +  5, "Gilly"),
    # Duna system
    "Flag: Duna":    LocationData(FLAG_LOC_BASE +  6, "Duna"),
    "Flag: Ike":     LocationData(FLAG_LOC_BASE +  7, "Ike"),
    # Dres
    "Flag: Dres":    LocationData(FLAG_LOC_BASE +  8, "Dres"),
    # Jool moons (Jool itself is a gas giant - no flag)
    "Flag: Laythe":  LocationData(FLAG_LOC_BASE +  9, "Laythe"),
    "Flag: Vall":    LocationData(FLAG_LOC_BASE + 10, "Vall"),
    "Flag: Tylo":    LocationData(FLAG_LOC_BASE + 11, "Tylo"),
    "Flag: Bop":     LocationData(FLAG_LOC_BASE + 12, "Bop"),
    "Flag: Pol":     LocationData(FLAG_LOC_BASE + 13, "Pol"),
    # Eeloo
    "Flag: Eeloo":   LocationData(FLAG_LOC_BASE + 14, "Eeloo"),
}

ALL_LOCATIONS: dict[str, LocationData] = {
    **TECH_LOCATIONS,
    **KSC_UPGRADE_LOCATIONS,
    **FLAG_LOCATIONS,
}

location_name_to_id: dict[str, int] = {name: data.id for name, data in ALL_LOCATIONS.items()}

# Reverse lookup tables for slot_data (C# plugin cross-check).
tech_id_to_location_id: dict[str, int] = {
    data.ksp_key: data.id for data in TECH_LOCATIONS.values()
}
facility_to_location_id: dict[str, int] = {
    data.ksp_key: data.id for data in KSC_UPGRADE_LOCATIONS.values()
}
body_to_location_id: dict[str, int] = {
    data.ksp_key: data.id for data in FLAG_LOCATIONS.values()
}


class KSPLocation(Location):
    game = GAME_NAME
