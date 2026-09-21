---
description: Trigger box for challenges. On contract boxes it runs a countdown, which we treat as a bomb timer.
---

# ANBChallengeTriggerbox

Trigger box for challenges. On contract boxes it runs a countdown, which we treat as a
bomb timer. The three hooks work together: `startCounting` starts it, `ButtonPushed`
stops it, and `Update` watches the time left.

## Functions

### `startCounting`

`startCounting()`

Triggered when
:   The countdown starts.

Hook
:   Postfix

We use it to
:   Remember that the timer is running.

### `ButtonPushed`

`ButtonPushed()`

Triggered when
:   The button is pushed.

Hook
:   Postfix

We use it to
:   Remember that the timer is no longer running.

### `Update`

`Update()`

Triggered when
:   Every frame.

Hook
:   Postfix

We use it to
:   While our timer is running on an active contract box, wait 1.5 seconds after `timeCurrent` reaches 0, then play the big explosion effect.

## Variables

| Variable | Type | Meaning | Function |
|---|---|---|---|
| `isActive` | `bool` | The box is active. | `Update` |
| `isContractBox` | `bool` | The box belongs to a contract. | `Update` |
| `timeCurrent` | `float` | Time left on the countdown. | `Update` |
