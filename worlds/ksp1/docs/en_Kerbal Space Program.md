# Kerbal Space Program

>There is [another Archipelago KSP](https://github.com/nickdavies/Archipelago) world being developed.
>Here's their [description](https://github.com/nickdavies/Archipelago/blob/ksp1/worlds/ksp1/docs/en_Kerbal%20Space%20Program%201.md) and [setup guide](https://github.com/nickdavies/Archipelago/blob/ksp1/worlds/ksp1/docs/setup_en.md). After playing it, I found their progression system to be more chaotically enjoyable than the one implemented here. I will leave this repo up but do not plan on developing it further.

Setup guide can be found [here](https://github.com/Baker80k/Archipelago-KSP/blob/main/worlds/ksp1/docs/setup_en.md)

## Where is the settings page for the game?

Not implemented yet! Your player file is `ksp_template.yaml`, in the [companion repo](https://github.com/Baker80k/KSP1-Random).

## What does randomization do to this game?

### Items

All ship parts are removed from the game and shuffled into the multiworld item pool.
The player starts with one randomly selected command pod, parachute, solid rocket booster, and science experiment chosen from the full part catalog.
All other parts must be received as items from the multiworld before they can be used in the VAB or SPH.

Tech nodes still require Science to research, but researching a node checks that AP location. The node's parts are not available until the matching AP item is received.

An additional set of items are SOI permits.
Entering a celestial body's sphere of influence without the matching SOI permit causes the vessel to instantly explode,
so the player must also receive permits to safely explore each body.

### Locations

Locations are split across three categories:

- **Tech tree nodes** - checked when the player researches a node in R&D (62 locations)
- **KSC building upgrades** - checked when each building reaches level 2 or level 3 (18 locations)
- **Flag plants** - checked when a flag is planted on a solid-surface body (15 locations)
    - Kerbin, Mun, Minmus, Moho, Eve, Gilly, Duna, Ike, Dres, Laythe, Vall, Tylo, Bop, Pol, Eeloo

### Logic

The player is guaranteed to receive at least one rocket fuel part and at least one reasonably-sized rocket engine before needing to upgrade any KSC buildings or plant any flags.

## What is the goal when randomized?

The default goal (`full`) requires all 9 KSC buildings to be upgraded to level 3 and flags planted on every planet and
moon in the Kerbol system. An alternative goal (`flags_only`) requires only the flags with no building requirement.

## Generative AI Disclosure
I vibe coded the majority of this over the course of an afternoon with Claude Code. As such, it may not follow best software practices nor may it be fully functional. Be warned!
