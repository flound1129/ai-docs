# MeshManager Class

*Modifiers:
final*

Manages 3D meshes for entities in the Aether framework.

MeshManager is responsible for loading, attaching, and destroying meshes for entities. It supports different mesh sources (mesh://, gfx://, file://, http://, https://) and manages the lifecycle of SceneObjects and SceneMeshes. It also handles input events for meshes and forwards them to the data model.

Example usage:

```kotlin // Register a custom mesh creator with URI parameters
meshManager.registerMeshCreator("mesh://custom/sphere") { entity, uri ->
    val radius = uri.getQueryParameter("radius")?.toFloatOrNull() ?: 1.0f
    SceneMesh.sphere(radius, material)
}
// Set a mesh for an entity using a URI with parameters
entity.setComponent(Mesh(Uri.parse("mesh://custom/sphere?radius=2.5")))
// Set a mesh for an entity using a file URI
meshManager.setMeshForEntity(
    entity,
    Uri.parse("models/cube.glb"),
    Uri.parse("file:///data/data/com.example.app/files/models/cube.glb"),
    "",  // default shader override
    -1,  // default scene override
    true // use cache
)
// Set a mesh directly for an entity
meshManager.setMeshForEntityDirectly(entity, sceneMesh) ```

## Signature

```kotlin
class MeshManager(val scene: Scene, val meshCreators: HashMap<String, (ent: Entity) -> SceneMesh>, val sceneObjectSystem: SceneObjectSystem)
```

## Constructors

| **MeshManager** ( scene , meshCreators , sceneObjectSystem ) | Signature ```kotlin constructor(scene: Scene, meshCreators: HashMap<String, (ent: Entity) -> SceneMesh>, sceneObjectSystem: SceneObjectSystem) ``` Parameters scene: [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The Scene instance used for rendering meshCreators: HashMap Map of URI schemes to mesh creator functions (deprecated, use registerMeshCreator) sceneObjectSystem: [SceneObjectSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_sceneobjectsystem) System for managing SceneObjects Returns [MeshManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_meshmanager) |
| --- | --- |

## Properties

| **meshCreators** : HashMap [Get] | Map of URI schemes to mesh creator functions (deprecated, use registerMeshCreator) Signature ```kotlin val meshCreators: HashMap<String, (ent: Entity) -> SceneMesh> ``` |
| --- | --- |
| **scene** : [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) [Get] | The Scene instance used for rendering Signature ```kotlin val scene: Scene ``` |
| **sceneObjectSystem** : [SceneObjectSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_sceneobjectsystem) [Get] | System for managing SceneObjects Signature ```kotlin val sceneObjectSystem: SceneObjectSystem ``` |

## Functions

| **deleteMeshForEntity** ( entity ) | This method removes the SceneObject associated with the entity and destroys any meshes that were created for it. Signature ```kotlin fun deleteMeshForEntity(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity to remove the mesh from |
| --- | --- |
| **destroy** () | Signature ```kotlin fun destroy() ``` |
| **preloadMesh** ( meshSimpleUri , meshFullPathUri , defaultShaderOverride , defaultSceneOverride , useCache ) | Preloads a mesh without attaching it to any entity for faster loading later. This method loads and caches a mesh from the specified URI so that when it's later attached to an entity, it will be available immediately. It supports the same URI schemes as setMeshForEntity: - file:// - Loads a mesh from a local file - http://, https:// - Loads a mesh from a network location - apk:// - Loads a mesh from the APK assets Note: mesh:// and gfx:// schemes are not supported for preloading as they require entity-specific context. Signature ```kotlin fun preloadMesh(meshSimpleUri: Uri, meshFullPathUri: Uri, defaultShaderOverride: String, defaultSceneOverride: Int, useCache: Boolean = true) ``` Parameters meshSimpleUri: Uri A simple URI used for identification and caching meshFullPathUri: Uri The full URI path to the mesh resource defaultShaderOverride: String Optional shader override to use when loading the mesh defaultSceneOverride: Int Optional scene index override to use when loading the mesh useCache: Boolean Whether to use cached meshes (default: true) |
| **registerMeshCreator** ( baseUrl , creator ) | Registers a mesh creator for a base URL pattern. The creator will be invoked for any mesh URI that matches the base URL (scheme + authority + path). Query parameters from the full URI will be passed to the creator for customization. Example: ```kotlin meshManager.registerMeshCreator("mesh://custom/sphere") { entity, uri -> val radius = uri.getQueryParameter("radius")?.toFloatOrNull() ?: 1.0f SceneMesh.sphere(radius, material) } ``` Parameters baseUrl: String The base URL to match (scheme + authority + path, query params ignored) creator: Function2 Function that takes an Entity and full URI, returns a SceneMesh |
| **retrieveAssociatedMeshFilesForEntity** ( entity ) | Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) Returns Array? |
| **setMeshForEntity** ( entity , meshSimpleUri , meshFullPathUri , defaultShaderOverride , defaultSceneOverride , useCache ) | Attaches a mesh to an Entity based on the provided URIs. Avoid using this method directly and instead assign the [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) component the Entity. This method loads a mesh from the specified URI and attaches it to the entity. It supports different URI schemes: - mesh:// - Uses a registered mesh creator function - gfx:// - Loads a mesh from the GFX system - file:// - Loads a mesh from a local file - http://, https:// - Loads a mesh from a network location Any previous mesh attached to the entity will be destroyed. Signature ```kotlin fun setMeshForEntity(entity: Entity, meshSimpleUri: Uri, meshFullPathUri: Uri, defaultShaderOverride: String, defaultSceneOverride: Int, useCache: Boolean = true) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity to attach the mesh to meshSimpleUri: Uri A simple URI used for identification and caching meshFullPathUri: Uri The full URI path to the mesh resource defaultShaderOverride: String Optional shader override to use when loading the mesh defaultSceneOverride: Int Optional scene index override to use when loading the mesh useCache: Boolean Whether to use cached meshes (default: true) |
| **setMeshForEntityDirectly** ( entity , mesh ) | Attaches a mesh directly to an Entity, bypassing the data model. Should use the [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) component instead. This method should be used sparingly as it is not reflected by the data model. It's intended as an escape hatch when the mesh creators don't fit well with the standard workflow. Any previous mesh attached to the entity will be destroyed. Signature ```kotlin fun setMeshForEntityDirectly(entity: Entity, mesh: SceneMesh) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity to attach the mesh to mesh: [SceneMesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenemesh) The SceneMesh to attach |
| **unregisterMeshCreator** ( baseUrl ) | Unregisters a mesh creator for the given base URL. Signature ```kotlin fun unregisterMeshCreator(baseUrl: String) ``` Parameters baseUrl: String The base URL that was registered |