# Kerbal Space Program Archipelago Setup Guide

## Required Software

- [Kerbal Space Program 1](https://store.steampowered.com/app/220200/Kerbal_Space_Program/) (Steam or DRM-free)
- [Python 3.11+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python package manager)
- [Archipelago KSP mod](https://github.com/Baker80k/KSP1-Random)

### 0. MAKE A BACKUP OF YOUR KSP SAVES BEFORE PROCEEDING

This mod implements some custom save file logic to account for items being awarded across saving/loading, but this is largely untested. Use at your own peril!

### 1. Set Up Project Directories

Make a new directory and clone the repositories.
```sh
mkdir ap_ksp
cd ap_ksp
git clone git@github.com:Baker80k/Archipelago-KSP.git
git clone git@github.com:Baker80k/KSP1-Random.git
mkdir player_files
```

The resulting file structure should look like this:
ap_ksp
- Archipelago-KSP
- KSP1-Random
- player_files

### 2. Install the KSP Mod

Move the file `KSP1-Random/ArchipelagoKSP.dll` in your KSP folder under `GameData/ArchipelagoKSP/Plugins`

The resulting structure should look like this:
Kerbal Space Program
- GameData
- - ArchipelagoKSP
- - - Plugins
- - - - ArchipelagoKSP.dll

Restart KSP to load the mod.

### 3. Set up Python Environment

This project is still under development so we're running the Archipelago generation and client raw,
but before that we need to set up a virtual environment.

The following script should do everything for you, just hit enter and agree to everything.
```sh
cd KSP1-Random
./scripts/01_setup_venv.sh
```

### 4. Generate a Multiworld Game

Copy `KSP1-Random/ksp_template.yaml` and place it in `player_files`, along with files from additional players.

Edit the `ksp_template.yaml` to have the KSP player's name at the top.

Then run the following script:
```sh
cd KSP1-Random
./scripts/02_generate.sh
```

Upload the resulting .zip file to [Archipelago](https://archipelago.gg/uploads) to host the game.
Make note of the port number

### 5. Start the AP Client Bridge

Before launching KSP, start the client bridge:

```sh
cd KSP1-Random
./scripts/03_client.sh
```

This starts a local HTTP bridge on `127.0.0.1:52420` that relays between KSP and the Archipelago server. Connect to the archipelago server with the port and slot name.

### 6. Connect In-Game

1. Launch KSP and start a **Career Mode** save.
2. Press **F8** to open the Archipelago connection window.
3. Enter the server address, slot name, and password.
4. Click **Connect to Archipelago**.

It may take ~5 seconds to connect, you'll know the connection is good once it says `Connected as: Name`

## Final Notes

If you're connected to the APClient and load a save with many techs unlocked and/or KSC facilities upgraded, the corresponding location checks will trigger and items will be given to the APWorld.

If you connect to the APClient once, you need to fully close the game for it to disconnect.

If a connection issue happens, at any time you can click **Sync from AP** from the F8 menu to trigger a resync.

Open KSP's in-game console with right shift + F12. On resync, there should be plenty of logs to see the present gamestate.

## Options

| Option | Description | Default |
|---|---|---|
| `goal` | Win condition: `full` (all KSC buildings max + all flags) or `flags_only` (flags only) | `full` |


## Troubleshooting

- KSP log is at `<KSP install>/KSP.log`.
- The client bridge must be running before connecting in-game.
- If the connection window does not appear, confirm `ArchipelagoKSP.dll` is in `GameData/ArchipelagoKSP/Plugins/`.
