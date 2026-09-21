---
description: Base class of the game's VR guns. Also drives the bow's flatscreen fallback.
---

# ANBHVRGunBase

Base class of the game's VR guns. It also drives the bow's flatscreen fallback, so
`OnFire` runs for bows as well.

## Functions

### `OnFire`

`OnFire(Vector3 direction)`

Triggered when
:   A gun fires.

Hook
:   Postfix

We use it to
:   Play recoil on the hand or hands holding the gun, with a different feel for shotguns, automatic rifles and one- or two-handed grips. Bows are skipped here (see [`HVRPhysicsBow`](hvrphysicsbow.md)).

Not used
:   `direction`, and `gunStabilized` (the mod has a line for it, but commented out).

## Variables

| Variable | Type | Meaning | Function |
|---|---|---|---|
| `isBow` | `bool` | The weapon is a bow. | `OnFire` |
| `isShotgun` | `bool` | The weapon is a shotgun. | `OnFire` |
| `FireType` | `GunFireType` | Firing mode. `Automatic` counts as a rifle for us. | `OnFire` |
| `myGrabbable.IsRightHandGrabbed` | `bool` | Held by the right hand. | `OnFire` |
| `myGrabbable.IsLeftHandGrabbed` | `bool` | Held by the left hand. Both true means two-handed. | `OnFire` |
