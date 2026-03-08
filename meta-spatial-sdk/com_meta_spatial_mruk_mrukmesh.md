# MRUKMesh Class

*Modifiers:
final*

Represents a 3D mesh data structure containing vertex positions, normals, and triangle indices.

## Signature

```kotlin
data class MRUKMesh(val positions: FloatArray, val normals: FloatArray, val indices: IntArray)
```

## Constructors

| **MRUKMesh** ( positions , normals , indices ) | Signature ```kotlin constructor(positions: FloatArray, normals: FloatArray, indices: IntArray) ``` Parameters positions: FloatArray Array of vertex positions in 3D space, stored as x1, y1, z1, x2, y2, z2, ... normals: FloatArray Array of vertex normal vectors, stored as nx1, ny1, nz1, nx2, ny2, nz2, ... indices: IntArray Array of triangle indices that define the mesh faces, where each index references a vertex (every 3 consecutive floats in positions/normals) Returns [MRUKMesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukmesh) |
| --- | --- |

## Properties

| **indices** : IntArray [Get] | Signature ```kotlin val indices: IntArray ``` |
| --- | --- |
| **normals** : FloatArray [Get] | Signature ```kotlin val normals: FloatArray ``` |
| **positions** : FloatArray [Get] | Signature ```kotlin val positions: FloatArray ``` |