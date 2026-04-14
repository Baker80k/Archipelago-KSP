from Options import Choice, PerGameCommonOptions
from dataclasses import dataclass


class Goal(Choice):
    """
    Win condition for the KSP Archipelago run.

    full        - All KSC buildings upgraded to max level AND flags on Mun and Minmus.
    flags_only  - Flags on Mun and Minmus only (no building requirement).
    """
    display_name = "Goal"
    option_full       = 0
    option_flags_only = 1
    default = 0


@dataclass
class KSPOptions(PerGameCommonOptions):
    goal: Goal
