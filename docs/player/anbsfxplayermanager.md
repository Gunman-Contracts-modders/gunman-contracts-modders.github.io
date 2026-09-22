---
description: Player sound and effect manager. Marks last-HP, healing and slow-motion moments.
---

# ANBSFXPlayerManager

Player sound and effect manager. Its functions mark moments like being on last HP,
healing and slow motion.

## Functions

### `TakeDamageLastHP`

`TakeDamageLastHP()`

Triggered when
:   The player is down to their last HP.

Hook
:   Postfix

Usage example
:   Start the heartbeat effect.

### `Heal`

`Heal()`

Triggered when
:   The player is healed.

Hook
:   Postfix

Usage example
:   Stop the heartbeat effect and play a healing effect.

### `StartSlowmotion`

`StartSlowmotion()`

Triggered when
:   Slow motion starts.

Hook
:   Postfix

Usage example
:   Play a slow-motion start effect.

## Tested class variables

The mod reads no variables in these functions.
