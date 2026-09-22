---
description: Rook bomb. Runs a countdown and explodes.
---

# ANBChallengeTriggerbox

The weirdly named ChallengeTriggerBox is what in game is called "Rook", and it's the huge bomb at the end of contract 1 and in the middle of contract 3,
the same class is used for both.

## Functions

### `startCounting`

`startCounting()`

Triggered when
:   The countdown starts.

Hook
:   Postfix

Usage example
:   Remember that the timer is running.

### `ButtonPushed`

`ButtonPushed()`

Triggered when
:   The button is pushed.

Hook
:   Postfix

Usage example
:   Remember that the timer is no longer running.

### `Update`

`Update()`

Triggered when
:   Every frame.

Hook
:   Postfix

Usage example
:   While our timer is running on an active contract box, when `timeCurrent` reaches 0, play the big explosion effect.

## Tested class variables

| Variable | Type | Meaning | Function |
|---|---|---|---|
| `isActive` | `bool` | The box is active. | `Update` |
| `isContractBox` | `bool` | The box belongs to a contract. | `Update` |
| `timeCurrent` | `float` | Time left on the countdown. | `Update` |
