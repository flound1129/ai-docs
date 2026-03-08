# MeshCreationSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

MeshCreationSystem is responsible for creating the mesh for an entity when the [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) component is added.

This system comes default with Meta Spatial SDK and operates on entities with [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) components. It uses the [MeshManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_meshmanager) to load and create meshes from various sources (mesh://, file://, http://, etc.) and attaches them to entities. It also handles cleanup when entities are deleted.

This System is a core part of the rendering pipeline and is registered early in the system execution order to ensure meshes are available for other systems.

## Signature

```kotlin
class MeshCreationSystem(val meshManager: MeshManager) : SystemBase
```

## Constructors

| **MeshCreationSystem** ( meshManager ) | Signature ```kotlin constructor(meshManager: MeshManager) ``` Parameters meshManager: [MeshManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_meshmanager) The mesh manager to use for creating the mesh. Returns [MeshCreationSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_meshcreationsystem) |
| --- | --- |

## Properties

| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| --- | --- |
| **meshManager** : [MeshManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_meshmanager) [Get] | The mesh manager to use for creating the mesh. Signature ```kotlin val meshManager: MeshManager ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **delete** ( entity ) | System should do any housekeeping based on [MeshCreationSystem.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_meshcreationsystem#delete) being removed from the scene Signature ```kotlin open override fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open override fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **preloadMesh** ( mesh , defaultShaderOverride , defaultSceneOverride ) | Preloads a mesh without attaching it to any entity for faster loading later. This method loads and caches a mesh from the specified URI so that when it's later assigned to an entity via the [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) component, it will be available immediately. This is useful for performance optimization when you know certain meshes will be needed soon. Signature ```kotlin fun preloadMesh(mesh: Uri, defaultShaderOverride: String = "", defaultSceneOverride: Int = 0) ``` Parameters mesh: Uri The URI of the mesh to preload defaultShaderOverride: String Optional shader override to use when loading the mesh defaultSceneOverride: Int Optional scene index override to use when loading the mesh |