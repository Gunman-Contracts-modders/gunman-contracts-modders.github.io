---
description: Physics-based bow from the HurricaneVR framework.
---

# HVRPhysicsBow

Physics-based bow from the HurricaneVR framework, so other VR games built on it
use the same class.

## Functions

### `ShootArrow`

`ShootArrow(Vector3 direction)`

Triggered when
:   An arrow is shot from the bow.

Hook
:   Postfix

We use it to
:   Play the bow-shot effect on the side of the bow hand.

Not used
:   `direction`

## Variables

| Variable | Type | Meaning | Function |
|---|---|---|---|
| `BowHand.IsRightHand` | `bool` | The bow hand is the right hand. | `ShootArrow` |
