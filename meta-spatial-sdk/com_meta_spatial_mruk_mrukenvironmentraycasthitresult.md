# MRUKEnvironmentRaycastHitResult Enum

Represents the possible outcomes of an environment raycast operation in the mixed reality scene.

## Signature

```kotlin
enum MRUKEnvironmentRaycastHitResult : Enum<MRUKEnvironmentRaycastHitResult>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| SUCCESS | The raycast successfully hit a surface in the environment |
| NOT_READY | The environment raycaster is not ready to perform raycasts |
| NO_HIT | The raycast did not intersect with any surface in the environment |
| HIT_POINT_OUTSIDE_OF_FOV | The hit point is outside the field of view |
| HIT_POINT_OCCLUDED | The hit point is occluded by another object |
| RAY_OCCLUDED | The ray itself is occluded before reaching the hit point |