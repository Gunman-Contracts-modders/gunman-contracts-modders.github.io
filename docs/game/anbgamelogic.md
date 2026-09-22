---
description: The game's central logic. Damage, death, holsters, ammo and pickups run through it.
---

# ANBGameLogic

The game's central logic class. Many of the events a mod cares about (getting hurt,
dying, holstering, ammo, pickups) run through it. Check here first.

## Functions

### `HurtPlayer`

`HurtPlayer(string type, float dmg, ANBBasicNPC attacker)`

Triggered when
:   The player is hurt.

Parameters
:   `attacker` (`ANBBasicNPC`) — the NPC that did it, or empty. We read `attacker.transform.position` to get the hit direction.

Usage example
:   Play an impact effect from the direction of the attacker.

Not used
:   `type`, `dmg`

### `PlayerDeadCall`

`PlayerDeadCall()`

Triggered when
:   The player dies.

Usage example
:   Stop the heartbeat effect.

### `endRun`

`endRun()`

Triggered when
:   A run ends.

Usage example
:   Stop the heartbeat effect.

### `holsterGun`

`holsterGun(string side)`

Triggered when
:   A gun is put into a holster.

Parameters
:   `side` (`string`) — holster slot. We check for `right`, `backRight` and `backLeft`; anything else counts as the left hip.

Usage example
:   Play the holster-in effect on the matching side, hip or back.

### `unholsterGun`

`unholsterGun(string side)`

Triggered when
:   A gun is drawn from a holster.

Parameters
:   `side` (`string`) — holster slot. We check for `right`, `backRight` and `backLeft`; anything else counts as the left hip.

Usage example
:   Play the holster-out effect on the matching side, hip or back.

### `holsterKnife`

`holsterKnife(string side)`

Triggered when
:   A knife is put into a holster.

Parameters
:   `side` (`string`) — holster slot. We check for `right`, `backRight` and `backLeft`; anything else counts as the left hip.

Usage example
:   Play the holster-in effect on the matching side, hip or back.

### `unholsterKnife`

`unholsterKnife(string side)`

Triggered when
:   A knife is drawn from a holster.

Parameters
:   `side` (`string`) — holster slot. We check for `right`, `backRight` and `backLeft`; anything else counts as the left hip.

Usage example
:   Play the holster-out effect on the matching side, hip or back.

### `creditAmmo`

`creditAmmo()`

Triggered when
:   Ammo is credited to the player.

Usage example
:   Play the ammo pouch effect.

### `substractAmmo`

`substractAmmo()`

Triggered when
:   Ammo is taken from the player. The name is spelled like this in the game.

Usage example
:   Play the ammo pouch effect.

### `collectibleCollected`

`collectibleCollected()`

Triggered when
:   A collectible is picked up.

Usage example
:   Play the ammo pouch effect.

### `collectCoinWallet`

`collectCoinWallet()`

Triggered when
:   Coins are collected into the wallet.

Usage example
:   Play the ammo pouch effect.

### `DeathByRook`

`DeathByRook()`

Triggered when
:   The player is killed by a "Rook", as the function is named.

Usage example
:   Play the big explosion effect.


## Tested class variables

The mod reads no variables in these functions.
