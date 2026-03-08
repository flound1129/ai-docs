# MRUKSceneEventListener Interface

Listener interface for Mixed Reality Utility Kit (MRUK) scene events.

Implement this interface to receive callbacks when rooms and anchors are added, removed, or updated in the scene. All methods have default no-op implementations, so only override the methods relevant to your use case.

## See Also

- [MRUKFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukfeature)

## Signature

```kotlin
interface MRUKSceneEventListener
```

## Functions

| **onAnchorAdded** ( room , anchor ) | Called when a new anchor is added to a room. Signature ```kotlin open fun onAnchorAdded(room: MRUKRoom, anchor: Entity) ``` Parameters room: [MRUKRoom](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroom) The MRUKRoom containing the anchor anchor: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The Entity anchor that was added |
| --- | --- |
| **onAnchorRemoved** ( room , anchor ) | Called when an anchor is removed from a room. Signature ```kotlin open fun onAnchorRemoved(room: MRUKRoom, anchor: Entity) ``` Parameters room: [MRUKRoom](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroom) The MRUKRoom that contained the anchor anchor: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The Entity anchor that was removed |
| **onAnchorUpdated** ( room , anchor ) | Called when an anchor's properties change. Signature ```kotlin open fun onAnchorUpdated(room: MRUKRoom, anchor: Entity) ``` Parameters room: [MRUKRoom](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroom) The MRUKRoom containing the anchor anchor: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The Entity anchor that was updated |
| **onRoomAdded** ( room ) | Called when a new room is discovered and added to the scene. Signature ```kotlin open fun onRoomAdded(room: MRUKRoom) ``` Parameters room: [MRUKRoom](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroom) The MRUKRoom instance that was added |
| **onRoomRemoved** ( room ) | Called when a room is removed from the scene. Signature ```kotlin open fun onRoomRemoved(room: MRUKRoom) ``` Parameters room: [MRUKRoom](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroom) The MRUKRoom instance that was removed |
| **onRoomUpdated** ( room ) | Called when an existing room's properties or anchors change. Signature ```kotlin open fun onRoomUpdated(room: MRUKRoom) ``` Parameters room: [MRUKRoom](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroom) The MRUKRoom instance that was updated |