---
description: Breakable objects. Some of them explode.
---

# ANBBreakable

Breakable objects. Some of them explode when they break.

## Functions

### `shatterMe`

`shatterMe()`

Triggered when
:   A breakable object shatters.

Usage example
:   If it explodes, play an explosion effect. Use the slow-motion version if slow motion is forced, comes with the break, or is already running (`Time.timeScale` below 1).

## Tested class variables

| Variable | Type | Meaning | Function |
|---|---|---|---|
| `explosionOnBreak` | `bool` | The object explodes when it breaks. | `shatterMe` |
| `forceSlomo` | `bool` | Slow motion is forced. | `shatterMe` |
| `slomoOnBreak` | `bool` | Breaking triggers slow motion. | `shatterMe` |
