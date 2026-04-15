# Kerbal Space Program

## Where is the settings page for the game?

Not implemented yet! Your player file is `ksp_template.yaml`, in the companion repo 

## What does randomization do to this game?

All ship parts and sphere-of-influence permits are removed from the game and shuffled into the multiworld item pool.
The player starts with one randomly selected command pod, parachute, solid rocket booster, and science experiment chosen from the full
part catalog. All other parts must be received as items from the multiworld before they can be used in the VAB or SPH.

Entering a celestial body's sphere of influence without the matching SOI permit causes the vessel to instantly explode,
so the player must also receive permits to safely explore each body.

Tech nodes still require Science to research, but researching a node checks that AP location. The node's parts are not available until the matching AP item is received.

Locations are split across three categories:

- **Tech tree nodes** - checked when the player researches a node in R&D (62 locations)
- **KSC building upgrades** - checked when each building reaches level 2 or level 3 (18 locations)
- **Flag plants** - checked when a flag is planted on a solid-surface body (15 locations)

## What is the goal when randomized?

The default goal (`full`) requires all 9 KSC buildings to be upgraded to level 3 and flags planted on every planet and
moon in the Kerbol system. An alternative goal (`flags_only`) requires only the flags with no building requirement.
