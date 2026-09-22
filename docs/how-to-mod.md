# How to mod

Mods for this game run on MelonLoader. The short version:

## 1. Install MelonLoader

Download the installer (and if needed requirements) from the [MelonLoader website](https://melonwiki.xyz/#/?id=requirements), point it at the game and install. Start the game once. On the first start, MelonLoader generates the readable game libraries for you (usually in the game's `MelonLoader/Il2CppAssemblies` folder). You will need them in step 4.

## 2. Create your mod

Follow the instructions on the [MelonLoader wiki](https://melonwiki.xyz). They walk you through setting up a project and writing a first mod.

For a working example that hooks game functions with Harmony, see the [bHaptics mod for this game](https://github.com/floh-bhaptics/GunmanContracts_bhaptics).

## 3. Look in ANBGameLogic

Many, many valuable functions are in the game's own `ANBGameLogic` class: getting hurt, dying, holstering, ammo, pickups and more. The hooks in the example mod above show how much is in there. See the [ANBGameLogic page](game/anbgamelogic.md) for the list.

## 4. Read the libraries

Open the generated libraries in a decompiler to browse classes and functions:

- [dnSpy](https://github.com/dnSpyEx/dnSpy) (community-maintained fork), free
- [dotPeek](https://www.jetbrains.com/decompiler/) by JetBrains, free

Search for words like `Fire`, `Damage` or `Grab` to find candidates, then hook them from your mod. Some variables and parameters already used and confirmed are documented here, but there are certainly a lot more available in the libraries.

Found something useful? Add it to these notes: see [Contributing](contributing.md).
