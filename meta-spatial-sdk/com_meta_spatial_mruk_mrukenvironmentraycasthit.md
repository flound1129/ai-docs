# MRUKEnvironmentRaycastHit Class

*Modifiers:
final*

Represents the result of an environment raycast operation in the mixed reality scene.

## Signature

```kotlin
data class MRUKEnvironmentRaycastHit(val result: MRUKEnvironmentRaycastHitResult, val point: Vector3, val normal: Vector3)
```

## Constructors

| **MRUKEnvironmentRaycastHit** ( result , point , normal ) | Signature ```kotlin constructor(result: MRUKEnvironmentRaycastHitResult, point: Vector3, normal: Vector3) ``` Parameters result: [MRUKEnvironmentRaycastHitResult](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukenvironmentraycasthitresult) The outcome status of the raycast operation point: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The 3D position where the ray intersected with the environment normal: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The surface normal vector at the intersection point Returns [MRUKEnvironmentRaycastHit](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukenvironmentraycasthit) |
| --- | --- |

## Properties

| **normal** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | The surface normal vector at the intersection point Signature ```kotlin val normal: Vector3 ``` |
| --- | --- |
| **point** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | The 3D position where the ray intersected with the environment Signature ```kotlin val point: Vector3 ``` |
| **result** : [MRUKEnvironmentRaycastHitResult](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukenvironmentraycasthitresult) [Get] | The outcome status of the raycast operation Signature ```kotlin val result: MRUKEnvironmentRaycastHitResult ``` |