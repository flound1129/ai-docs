# MRUKRoomFace Class

*Modifiers:
final*

Represents a face/surface of a room mesh with semantic labeling and geometric data.

A room face defines a specific surface within a room's mesh geometry, such as a portion of a wall, floor, or ceiling. Each face contains vertex indices that reference positions in the parent room mesh and includes semantic information about what type of surface it represents.

## Signature

```kotlin
data class MRUKRoomFace(val uuid: UUID, val parentUuid: UUID, val label: MRUKLabel, val indices: IntArray)
```

## Constructors

| **MRUKRoomFace** ( uuid , parentUuid , label , indices ) | Signature ```kotlin constructor(uuid: UUID, parentUuid: UUID, label: MRUKLabel, indices: IntArray) ``` Parameters uuid: UUID Unique identifier for this face parentUuid: UUID Identifier of the parent anchor/surface this face belongs to label: [MRUKLabel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mruklabel) The semantic label indicating what type of surface this face represents indices: IntArray Array of vertex indices that define this face's geometry Returns [MRUKRoomFace](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroomface) |
| --- | --- |

## Properties

| **indices** : IntArray [Get] | Signature ```kotlin val indices: IntArray ``` |
| --- | --- |
| **label** : [MRUKLabel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mruklabel) [Get] | Signature ```kotlin val label: MRUKLabel ``` |
| **parentUuid** : UUID [Get] | Signature ```kotlin val parentUuid: UUID ``` |
| **uuid** : UUID [Get] | Signature ```kotlin val uuid: UUID ``` |