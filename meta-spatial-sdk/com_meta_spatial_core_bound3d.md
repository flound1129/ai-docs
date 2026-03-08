# Bound3D Class

*Modifiers:
final*

Represents a 3D bounding box with minimum and maximum coordinates.

## Signature

```kotlin
data class Bound3D(var min: Vector3 = Vector3(0f, 0f, 0f), var max: Vector3 = Vector3(0f, 0f, 0f))
```

## Constructors

| **Bound3D** ( min , max ) | Signature ```kotlin constructor(min: Vector3 = Vector3(0f, 0f, 0f), max: Vector3 = Vector3(0f, 0f, 0f)) ``` Parameters min: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) max: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) Returns [Bound3D](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bound3d) |
| --- | --- |

## Properties

| **max** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | Signature ```kotlin var max: Vector3 ``` |
| --- | --- |
| **min** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | Signature ```kotlin var min: Vector3 ``` |

## Functions

| **center** () | Calculates the center of the bounding box. Signature ```kotlin fun center(): Vector3 ``` Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The center of the bounding box as a Vector3. |
| --- | --- |
| **contains** ( v ) | Checks if a given vector is within the bounds of the bounding box. Signature ```kotlin fun contains(v: Vector3): Boolean ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The vector to check. Returns Boolean True if the vector is within the bounds of the bounding box, false otherwise. |
| **encapsulate** ( bounds ) | Encapsulates another bounding box within this one. Signature ```kotlin fun encapsulate(bounds: Bound3D) ``` Parameters bounds: [Bound3D](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bound3d) The other bounding box to encapsulate. |
| **extents** () | Calculates the extents of the bounding box. Signature ```kotlin fun extents(): Vector3 ``` Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The extents of the bounding box as a Vector3. |
| **getVolume** () | Calculates the volume of this 3D bounding box. Signature ```kotlin fun Bound3D.getVolume(): Float ``` Returns Float The volume in cubic units, computed as width × height × depth |
| **size** () | Calculates the size of the bounding box. Signature ```kotlin fun size(): Vector3 ``` Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The size of the bounding box as a Vector3. |
| **toString** () | Returns a string representation of this object in the format `(min, max)` . Signature ```kotlin open override fun toString(): String ``` Returns String A string representing the object. |