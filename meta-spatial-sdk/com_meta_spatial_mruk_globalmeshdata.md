# GlobalMeshData Class

*Modifiers:
final*

Represents global mesh data containing vertex positions and triangle indices.

## Signature

```kotlin
data class GlobalMeshData(val positions: FloatArray, val indices: IntArray)
```

## Constructors

| **GlobalMeshData** ( positions , indices ) | Signature ```kotlin constructor(positions: FloatArray, indices: IntArray) ``` Parameters positions: FloatArray indices: IntArray Returns [GlobalMeshData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_globalmeshdata) |
| --- | --- |

## Properties

| **indices** : IntArray [Get] | Array of triangle indices where every 3 consecutive values form a triangle. Signature ```kotlin val indices: IntArray ``` |
| --- | --- |
| **positions** : FloatArray [Get] | Flat array of vertex positions stored as x, y, z coordinates. Signature ```kotlin val positions: FloatArray ``` |