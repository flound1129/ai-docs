# AnchorMeshScalingMode Enum

Scaling mode when a mesh gets spawned.

## Signature

```kotlin
enum AnchorMeshScalingMode : Enum<AnchorMeshScalingMode>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| STRETCH | Stretch the mesh to match the bounds of the anchor. |
| UNIFORM_SCALING | Scale the mesh to match the anchor but scale each axis uniform. This means the mesh may be not filling the bounding box of the anchor completely. |
| UNIFORM_XZ_SCALING | Same as UNIFORM_SCALING, but only scales the X and Z axis uniform. |
| NO_SCALING | Do not apply any scaling. |