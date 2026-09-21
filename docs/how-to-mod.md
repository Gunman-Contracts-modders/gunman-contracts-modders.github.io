# How to mod

Mods for this game run on MelonLoader. The short version:

## 1. Install MelonLoader

Download the installer from the [MelonLoader releases](https://github.com/LavaGang/MelonLoader/releases), point it at the game's `.exe` and install. Start the game once. On the first start, MelonLoader generates the readable game libraries for you (usually in the game's `MelonLoader/Il2CppAssemblies` folder). You will need them in step 4.

## 2. Create your mod

Follow the instructions on the [MelonLoader wiki](https://melonwiki.xyz). They walk you through setting up a project and writing a first mod.

For a working example that hooks game functions with Harmony, see the [bHaptics mod for this game](https://github.com/floh-bhaptics/GunmanContracts_bhaptics).

## 3. Look in HurricaneVR first

Most of the functions you will want to hook are not in the game's own code but in the **HurricaneVR** framework, the VR toolkit the game is built on. It handles grabbing, guns and bows. In mod code its namespaces get an `Il2Cpp` prefix (`Il2CppHurricaneVR...`), in a decompiler they don't.

## 4. Read the libraries

Open the generated libraries in a decompiler to browse classes and functions:

- [dnSpy](https://github.com/dnSpyEx/dnSpy) (community-maintained fork), free
- [dotPeek](https://www.jetbrains.com/decompiler/) by JetBrains, free

Search for words like `Fire`, `Damage` or `Grab` to find candidates, then hook them from your mod.

Found something useful? Add it to these notes: see [Contributing](contributing.md).
