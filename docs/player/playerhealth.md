---
description: Holds the player's health and applies incoming damage.
---

# PlayerHealth

Holds the player's health and applies incoming damage.

## Functions

### `TakeDamage`

`TakeDamage(DamageData damage)`

Triggered when
:   The player takes damage.

Hook
:   Postfix

We use it to
:   Play a directional impact effect from the hit direction. Start a heartbeat at 25 % health or below, stop it above. Stop all effects on a deadly hit or at 0 health.

## Variables

| Variable | Type | Meaning | Function |
|---|---|---|---|
| `health` | `float` | Current health. | `TakeDamage` |
| `startHealth` | `float` | Health at full; the 25 % threshold is measured against it. | `TakeDamage` |
| `damage.HitDirection` | `Vector3` | Direction the hit came from. | `TakeDamage` |
| `damage.Deadly` | `bool` | The hit is lethal. | `TakeDamage` |
