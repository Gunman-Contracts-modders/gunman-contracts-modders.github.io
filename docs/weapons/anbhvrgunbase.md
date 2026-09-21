---
description: Base class of the game's VR guns. Fire, reload, cocking and grabbing. Also drives the bow's flatscreen fallback.
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
:   Play recoil on the hand holding the gun. It counts as two-handed if the other hand holds a second grip point (foregrip, rail). Shotguns and automatic rifles get their own feel. Enemy guns and bows are skipped (see [`HVRPhysicsBow`](hvrphysicsbow.md)).

Not used
:   `direction`

### `ReleaseAmmo`

`ReleaseAmmo()`

Triggered when
:   The magazine is released from the gun.

Hook
:   Postfix

We use it to
:   Play the mag-eject effect on the hand holding the gun.

### `OnAmmoSocketed`

`OnAmmoSocketed()`

Triggered when
:   Ammo is inserted into the gun.

Hook
:   Postfix

We use it to
:   Play the reload effect on the hand holding the gun. Skipped if no hand holds it.

### `OnHandGrabbed`

`OnHandGrabbed()`

Triggered when
:   A hand grabs the gun.

Hook
:   Postfix

We use it to
:   Play the mag-eject effect on the hand holding the gun, as grab feedback.

### `AddShotgunShell`

`AddShotgunShell()`

Triggered when
:   A shell is loaded into a shotgun.

Hook
:   Postfix

We use it to
:   Play the reload effect on the hand holding the gun.

### `OnCockingHandleEjected`

`OnCockingHandleEjected()`

Triggered when
:   The cocking handle is pulled back.

Hook
:   Postfix

We use it to
:   Play the slide-back effect on the hand holding the gun.

### `OnCockingHandleReleased`

`OnCockingHandleReleased()`

Triggered when
:   The cocking handle is released.

Hook
:   Postfix

We use it to
:   Play the slide-forward effect on the hand holding the gun.

## Variables

| Variable | Type | Meaning | Function |
|---|---|---|---|
| `EnemyGun` | `bool` | The gun belongs to an enemy. | `OnFire` |
| `isBow` | `bool` | The weapon is a bow. | `OnFire` |
| `isShotgun` | `bool` | The weapon is a shotgun. | `OnFire` |
| `FireType` | `GunFireType` | Firing mode. `Automatic` counts as a rifle for us. | `OnFire` |
| `myGrabbable` | grabbable | Main grip point of the gun. | `OnFire` |
| `myGrabbable.IsRightHandGrabbed` | `bool` | Held by the right hand. | `OnFire` |
| `myGrabbable.IsLeftHandGrabbed` | `bool` | Held by the left hand. Both true means two-handed. | `OnFire` |
| `HapticGrabbables` | list of grabbables | Extra grip points (foregrip, rail). We check whether the other hand holds one. | `OnFire` |
| `gunInHand` | `string` | The hand holding the gun. We check for `Right` and `none`; anything else counts as left. | `ReleaseAmmo`, `OnAmmoSocketed`, `OnHandGrabbed`, `AddShotgunShell`, `OnCockingHandleEjected`, `OnCockingHandleReleased` |
