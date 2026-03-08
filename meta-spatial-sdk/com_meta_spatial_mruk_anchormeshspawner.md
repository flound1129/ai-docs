# AnchorMeshSpawner Class

*Modifiers:
final*

The AnchorMeshSpawner class is designed to facilitate the spawning of 3D meshes (glb/gltf) at scene anchor locations. It is intended for use in conjunction with the [MRUKFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukfeature) . This class automatically spawns meshes in a room when new anchors are loaded by the [MRUKFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukfeature) , ensuring that the meshes remain synchronized with the current anchors. The spawning behavior can be customized using the spawnMode. For usage examples, refer to the MrukSampleActivity. Note that if you want to generate walls and floors without providing meshes for it refer to the AnchorProceduralMesh. The spawnGroups parameter specifies which meshes to spawn based on a label. It is crucial to invoke the `destroy()` method when the AnchorMeshSpawner instance is no longer in use.

## Signature

```kotlin
class AnchorMeshSpawner(val mrukFeature: MRUKFeature, var spawnGroups: Map<MRUKLabel, AnchorMeshSpawner.AnchorMeshGroup>, val spawnMode: MRUKSpawnMode = MRUKSpawnMode.CURRENT_ROOM_ONLY)
```

## Constructors

| **AnchorMeshSpawner** ( mrukFeature , spawnGroups , spawnMode ) | Signature ```kotlin constructor(mrukFeature: MRUKFeature, spawnGroups: Map<MRUKLabel, AnchorMeshSpawner.AnchorMeshGroup>, spawnMode: MRUKSpawnMode = MRUKSpawnMode.CURRENT_ROOM_ONLY) ``` Parameters mrukFeature: [MRUKFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukfeature) spawnGroups: Map spawnMode: [MRUKSpawnMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukspawnmode) Returns [AnchorMeshSpawner](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_anchormeshspawner) |
| --- | --- |

## Properties

| **mrukFeature** : [MRUKFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukfeature) [Get] | The MRUKFeature to which this AnchorMeshSpawner is tied. The AnchorMeshSpawner gets its anchor data from the MRUKFeature. Signature ```kotlin val mrukFeature: MRUKFeature ``` |
| --- | --- |
| **spawnGroups** : Map [Get][Set] | A map of label to the meshes to spawn. Signature ```kotlin var spawnGroups: Map<MRUKLabel, AnchorMeshSpawner.AnchorMeshGroup> ``` |
| **spawnMode** : [MRUKSpawnMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukspawnmode) [Get] | The spawnMode determines if the AnchorMeshSpawner should spawn meshes automatically whenever the mrukFeature has new anchors loaded. If the spawnMode is set to NONE spawnMeshes() needs to be invoked manually. Signature ```kotlin val spawnMode: MRUKSpawnMode ``` |

## Functions

| **destroy** () | Destroys the AnchorMeshSpawner. It's important to call this function before the AnchorMeshSpawner gets out of scope because it might lead to memory leaks otherwise. Signature ```kotlin fun destroy() ``` |
| --- | --- |
| **spawnMeshes** ( rooms ) | Spawn meshes for a given list of rooms. This should only be invoked manually if spawnMode is set to NONE. Signature ```kotlin fun spawnMeshes(rooms: List<MRUKRoom>): List<Entity> ``` Parameters rooms: List Returns List |
| **spawnMeshes** ( room ) | Spawn meshes for a given room. This should only be invoked manually if spawnMode is set to NONE. Signature ```kotlin fun spawnMeshes(room: MRUKRoom): List<Entity> ``` Parameters room: [MRUKRoom](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroom) Returns List |

## Companion Object

Companion object containing utility functions and caches for mesh operations.

### Companion Object Properties

| **boundsCache** : HashMap<String, Bound3D> [Get] | Cache storing computed bounds for mesh files to avoid redundant calculations. Signature ```kotlin val boundsCache: HashMap<String, Bound3D> ``` |
| --- | --- |

### Companion Object Functions

| **getMeshBounds** ( mesh ) | Retrieves the bounding box for a mesh file, using cached values when available. Signature ```kotlin fun getMeshBounds(mesh: String): Bound3D ``` Parameters mesh: String The file path of the mesh to get bounds for. Returns [Bound3D](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bound3d) The computed or cached [Bound3D](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bound3d) for the mesh. |
| --- | --- |

## Inner Class

### AnchorMeshGroup Class

*Modifiers:
final*

The AnchorMeshGroup contains the information needed to spawn a mesh for a label. See spawnGroups on the AnchorMeshSpawner.

Signature
```kotlin
data class AnchorMeshGroup(val meshes: List<String>, val selectionMode: AnchorMeshSelectionMode = AnchorMeshSelectionMode.RANDOM, val scalingMode: AnchorMeshScalingMode = AnchorMeshScalingMode.STRETCH, val matchAspectRatio: Boolean = false)
```

Constructors
| **AnchorMeshGroup** ( meshes , selectionMode , scalingMode , matchAspectRatio ) | Signature ```kotlin constructor(meshes: List<String>, selectionMode: AnchorMeshSelectionMode = AnchorMeshSelectionMode.RANDOM, scalingMode: AnchorMeshScalingMode = AnchorMeshScalingMode.STRETCH, matchAspectRatio: Boolean = false) ``` Parameters meshes: List selectionMode: [AnchorMeshSelectionMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_anchormeshselectionmode) scalingMode: [AnchorMeshScalingMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_anchormeshscalingmode) matchAspectRatio: Boolean Returns AnchorMeshSpawner.AnchorMeshGroup |
| --- | --- |

Properties
| **matchAspectRatio** : Boolean [Get] | Ensures that the mesh gets rotated in a way to match the aspect ratio of the anchor. Signature ```kotlin val matchAspectRatio: Boolean = false ``` |
| --- | --- |
| **meshes** : List [Get] | A list of meshes considered for spawning. The selection of meshes for spawning is determined by the selectionMode. Signature ```kotlin val meshes: List<String> ``` |
| **scalingMode** : [AnchorMeshScalingMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_anchormeshscalingmode) [Get] | Determines the scaling mode that should be used when scaling a mesh from that group. Signature ```kotlin val scalingMode: AnchorMeshScalingMode ``` |
| **selectionMode** : [AnchorMeshSelectionMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_anchormeshselectionmode) [Get] | Determines the selection method for the meshes in that group. Signature ```kotlin val selectionMode: AnchorMeshSelectionMode ``` |