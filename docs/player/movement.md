---
description: Basically all the flatscreen movement mechanics.
---

# Movement

This class controls Movement Speeds and a BUNCH of other Movement stuff. Can be found in "Assembly-Csharp.dll"

## Functions

### `speedAiming`

`speedAiming(Type parameter)`

Triggered when
:   The moment the game calls it (player action, event, every frame ...).

Hook
:   Postfix, Prefix, or "none" if we only read from it.

Usage example
:   Make the speed while aiming faster or slower.

Not used
:   Parameters or fields we saw but did not need. Delete this row if empty.

## Variables

| Variable | Type | Meaning | Function |
|---|---|---|---|
| `fieldName` | `float` | What it holds. | `aimingSpeed` |
