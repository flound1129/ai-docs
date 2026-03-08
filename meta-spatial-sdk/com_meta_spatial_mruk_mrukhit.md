# MRUKHit Class

*Modifiers:
final*

Represents the result of a raycast hit against a spatial anchor in the mixed reality environment.

## Signature

```kotlin
data class MRUKHit(val hitDistance: Float, val hitPosition: Vector3, val hitNormal: Vector3, val roomAnchorUuid: UUID, val sceneAnchorUuid: UUID)
```

## Constructors

| **MRUKHit** ( hitDistance , hitPosition , hitNormal , roomAnchorUuid , sceneAnchorUuid ) | Signature ```kotlin constructor(hitDistance: Float, hitPosition: Vector3, hitNormal: Vector3, roomAnchorUuid: UUID, sceneAnchorUuid: UUID) ``` Parameters hitDistance: Float The distance from the ray origin to the hit point hitPosition: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The 3D position where the ray intersected with the anchor hitNormal: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The surface normal vector at the hit point roomAnchorUuid: UUID The unique identifier of the room containing the hit anchor sceneAnchorUuid: UUID The unique identifier of the specific anchor that was hit Returns [MRUKHit](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukhit) |
| --- | --- |

## Properties

| **hitDistance** : Float [Get] | The distance from the ray origin to the hit point Signature ```kotlin val hitDistance: Float ``` |
| --- | --- |
| **hitNormal** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | The surface normal vector at the hit point Signature ```kotlin val hitNormal: Vector3 ``` |
| **hitPosition** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | The 3D position where the ray intersected with the anchor Signature ```kotlin val hitPosition: Vector3 ``` |
| **roomAnchorUuid** : UUID [Get] | The unique identifier of the room containing the hit anchor Signature ```kotlin val roomAnchorUuid: UUID ``` |
| **sceneAnchorUuid** : UUID [Get] | The unique identifier of the specific anchor that was hit Signature ```kotlin val sceneAnchorUuid: UUID ``` |