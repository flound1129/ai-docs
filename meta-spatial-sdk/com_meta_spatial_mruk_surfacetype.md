# SurfaceType Enum

Defines the types of surfaces that can be used for raycasting operations.

Surface types can be combined using bitwise OR operations to raycast against multiple surface types simultaneously.

## See Also

## Signature

```kotlin
enum SurfaceType : Enum<SurfaceType>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| NONE | No surface type |
| PLANE | Flat surfaces like walls, floors, and ceilings |
| VOLUME | 3D volumes like furniture and objects |
| MESH | Mesh surfaces for detailed geometry |
| PLANE_VOLUME | Combination of plane and volume surfaces |
| PLANE_MESH | Combination of plane and mesh surfaces |
| VOLUME_MESH | Combination of volume and mesh surfaces |
| ALL | All surface types |

## Properties

| **value** : Int [Get] | The bitmask value representing this surface type Signature ```kotlin val value: Int ``` |
| --- | --- |