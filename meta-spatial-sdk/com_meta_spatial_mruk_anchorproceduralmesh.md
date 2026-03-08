# AnchorProceduralMesh Class

*Modifiers:
final*

The AnchorProceduralMesh is designed to automatically generate meshes for the given labels in a room. It is able to generate planes and boxes. In addition, it's possible to cut holes into planes. This can be useful for windows. It's also possible to spawn physics colliders for the generated meshes. AnchorProceduralMesh is intended for use in conjunction with the [MRUKFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukfeature) . This class automatically spawns meshes in a room when new anchors are loaded by the MRUKFeature, ensuring that the meshes remain synchronized with the current anchors. The spawning behavior can be customized using the spawnMode. For usage examples, refer to the MrukSampleActivity. If you want to be able to spawn 3D meshes from glb or gltf files refer to AnchorMeshSpawner. It is crucial to invoke the `destroy()` method when the AnchorMeshSpawner instance is no longer in use.

## Signature

```kotlin
class AnchorProceduralMesh(val mrukFeature: MRUKFeature, var labelToConfig: Map<MRUKLabel, AnchorProceduralMeshConfig>, val spawnMode: MRUKSpawnMode = MRUKSpawnMode.CURRENT_ROOM_ONLY, var wallTexCoordModeU: MRUKWallTexCoordModeU = MRUKWallTexCoordModeU.METRIC, var wallTexCoordModeV: MRUKWallTexCoordModeV = MRUKWallTexCoordModeV.METRIC, var anchorTexCoordMode: MRUKAnchorTexCoordMode = MRUKAnchorTexCoordMode.STRETCH, var cutHoleLabels: List<MRUKLabel> = listOf(MRUKLabel.WINDOW_FRAME, MRUKLabel.DOOR_FRAME))
```

## Constructors

| **AnchorProceduralMesh** ( mrukFeature , labelToConfig , spawnMode , wallTexCoordModeU , wallTexCoordModeV , anchorTexCoordMode , cutHoleLabels ) | Signature ```kotlin constructor(mrukFeature: MRUKFeature, labelToConfig: Map<MRUKLabel, AnchorProceduralMeshConfig>, spawnMode: MRUKSpawnMode = MRUKSpawnMode.CURRENT_ROOM_ONLY, wallTexCoordModeU: MRUKWallTexCoordModeU = MRUKWallTexCoordModeU.METRIC, wallTexCoordModeV: MRUKWallTexCoordModeV = MRUKWallTexCoordModeV.METRIC, anchorTexCoordMode: MRUKAnchorTexCoordMode = MRUKAnchorTexCoordMode.STRETCH, cutHoleLabels: List<MRUKLabel> = listOf(MRUKLabel.WINDOW_FRAME, MRUKLabel.DOOR_FRAME)) ``` Parameters mrukFeature: [MRUKFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukfeature) labelToConfig: Map spawnMode: [MRUKSpawnMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukspawnmode) wallTexCoordModeU: [MRUKWallTexCoordModeU](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukwalltexcoordmodeu) wallTexCoordModeV: [MRUKWallTexCoordModeV](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukwalltexcoordmodev) anchorTexCoordMode: [MRUKAnchorTexCoordMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukanchortexcoordmode) cutHoleLabels: List Returns [AnchorProceduralMesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_anchorproceduralmesh) |
| --- | --- |

## Properties

| **anchorTexCoordMode** : [MRUKAnchorTexCoordMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukanchortexcoordmode) [Get][Set] | The texture coordinate mode for planes and volumes that are not walls. Depending on that mode the texture will appear differently. Signature ```kotlin var anchorTexCoordMode: MRUKAnchorTexCoordMode ``` |
| --- | --- |
| **cutHoleLabels** : List [Get][Set] | A list of labels that cut holes into their parent anchors. For example, a door or windows parent will be the wall. That means if this list contains the window and door label, holes will be cut into the wall meshes. The anchor hierarchy gets determined by which anchors sit on top of other anchors. Signature ```kotlin var cutHoleLabels: List<MRUKLabel> ``` |
| **labelToConfig** : Map [Get][Set] | A mapping that tells the AnchorProceduralMesh for which labels procedural meshes should be generated. Signature ```kotlin var labelToConfig: Map<MRUKLabel, AnchorProceduralMeshConfig> ``` |
| **mrukFeature** : [MRUKFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukfeature) [Get] | The MRUKFeature to which this AnchorProceduralMesh is tied. The AnchorProceduralMesh gets its anchor data from the MRUKFeature. Signature ```kotlin val mrukFeature: MRUKFeature ``` |
| **spawnMode** : [MRUKSpawnMode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukspawnmode) [Get] | The spawnMode determines if the AnchorProceduralMesh should spawn meshes automatically whenever the mrukFeature has new anchors loaded. If the spawnMode is set to NONE spawnMeshes() needs to be invoked manually. Signature ```kotlin val spawnMode: MRUKSpawnMode ``` |
| **wallTexCoordModeU** : [MRUKWallTexCoordModeU](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukwalltexcoordmodeu) [Get][Set] | The texture coordinate mode for the U channel that should be used when generating wall meshes. Depending on that mode the texture will appear differently. Signature ```kotlin var wallTexCoordModeU: MRUKWallTexCoordModeU ``` |
| **wallTexCoordModeV** : [MRUKWallTexCoordModeV](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukwalltexcoordmodev) [Get][Set] | The texture coordinate mode for the V channel that should be used when generating wall meshes. Depending on that mode the texture will appear differently. Signature ```kotlin var wallTexCoordModeV: MRUKWallTexCoordModeV ``` |

## Functions

| **destroy** () | Destroys the AnchorProceduralMesh. It's important to call this function before the AnchorProceduralMesh gets out of scope, otherwise it might lead to memory leaks. Signature ```kotlin fun destroy() ``` |
| --- | --- |
| **spawnMeshes** ( rooms ) | Spawn meshes for a given list of rooms. This should only be invoked manually if spawnMode is set to NONE. Signature ```kotlin fun spawnMeshes(rooms: List<MRUKRoom>): List<AnchorProceduralMesh.MeshAndPhysicEntity> ``` Parameters rooms: List Returns List |
| **spawnMeshes** ( room ) | Spawn meshes for a given room. This should only be invoked manually if spawnMode is set to NONE. Signature ```kotlin fun spawnMeshes(room: MRUKRoom): List<AnchorProceduralMesh.MeshAndPhysicEntity> ``` Parameters room: [MRUKRoom](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroom) Returns List |

## Companion Object

### Companion Object Properties

| **TAG** : String [Get] | Signature ```kotlin const val TAG: String ``` |
| --- | --- |

## Inner Class

### MeshAndPhysicEntity Class

*Modifiers:
final*

Container for mesh and physics entities spawned for an anchor.

Signature
```kotlin
data class MeshAndPhysicEntity(val mesh: Entity?, val physics: Entity?)
```

Constructors
| **MeshAndPhysicEntity** ( mesh , physics ) | Signature ```kotlin constructor(mesh: Entity?, physics: Entity?) ``` Parameters mesh: [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity containing the visual mesh component, or null if no material was configured. physics: [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity containing the physics collider component, or null if physics was not enabled. Returns AnchorProceduralMesh.MeshAndPhysicEntity |
| --- | --- |

Properties
| **mesh** : [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get] | The entity containing the visual mesh component, or null if no material was configured. Signature ```kotlin val mesh: Entity? ``` |
| --- | --- |
| **physics** : [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get] | The entity containing the physics collider component, or null if physics was not enabled. Signature ```kotlin val physics: Entity? ``` |