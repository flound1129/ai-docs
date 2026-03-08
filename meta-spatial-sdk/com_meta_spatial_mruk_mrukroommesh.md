# MRUKRoomMesh Class

*Modifiers:
final*

Represents the complete mesh geometry of a room including vertex positions and face definitions.

MRUKRoomMesh is only available on a room with High Fidelity Scene (Scene V2). It provides a watertight representation of the room's walls, floor, ceiling, and windows. MRUK internally generates MRUKAnchor objects from the individual faces of this room mesh.

The positions array stores all vertex coordinates in the mesh, while the faces array contains semantic face definitions that reference these vertices through indices.

## Signature

```kotlin
data class MRUKRoomMesh(val positions: FloatArray, val faces: Array<MRUKRoomFace>)
```

## Constructors

| **MRUKRoomMesh** ( positions , faces ) | Signature ```kotlin constructor(positions: FloatArray, faces: Array<MRUKRoomFace>) ``` Parameters positions: FloatArray Array of vertex positions stored as x1, y1, z1, x2, y2, z2, ... in 3D space faces: Array Array of face definitions that reference vertex positions and include semantic labels Returns [MRUKRoomMesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroommesh) |
| --- | --- |

## Properties

| **faces** : Array [Get] | Signature ```kotlin val faces: Array<MRUKRoomFace> ``` |
| --- | --- |
| **positions** : FloatArray [Get] | Signature ```kotlin val positions: FloatArray ``` |