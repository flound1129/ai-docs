# clampYAngle Function

*Modifiers:
final*

Clamp the Y angle of a vector to a given range. This function ensures that the Y angle of the vector is within the specified range, while maintaining the length and XZ components

## Signature

```kotlin
fun clampYAngle(vector: Vector3, minAngleDegrees: Float, maxAngleDegrees: Float): Vector3
```

## Parameters

vector:
[Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3)
minAngleDegrees:
Float
maxAngleDegrees:
Float
## Returns

[Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3)