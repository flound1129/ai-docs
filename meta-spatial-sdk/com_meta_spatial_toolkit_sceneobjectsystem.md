# SceneObjectSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

System to manage SceneObjects. This acts as a registry for other systems to get the SceneObject associated with an entity.

Example using SceneObjectSystem to get a SceneObject and adding an input listener:

```kotlin systemManager.findSystem<SceneObjectSystem>().getSceneObject(myEntity)?.thenAccept { so -> so.addInputListener(myInputListener) } ```

Note on the example above: You will likely get null if you call 'getSceneObject()' immediately after attaching a [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) component to an entity. You will likely need to call this in a System to ensure [MeshCreationSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_meshcreationsystem) has run by leveraging [SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase) getDependencies function.

## Signature

```kotlin
class SceneObjectSystem : SystemBase
```

## Constructors

| **SceneObjectSystem** () | Signature ```kotlin constructor() ``` Returns [SceneObjectSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_sceneobjectsystem) |
| --- | --- |

## Properties

| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| --- | --- |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **addSceneObject** ( entity , sceneObjectFuture ) | Adds a `SceneObject` future to the registry to allow other systems to get the `SceneObject` associated with the entity. The future is expected to be completed by the caller once the `SceneObject` is done loading. Signature ```kotlin fun addSceneObject(entity: Entity, sceneObjectFuture: CompletableFuture<SceneObject>) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity that represents the `SceneObject` . sceneObjectFuture: CompletableFuture The future that will be completed (by the caller) when the `SceneObject` is created. |
| --- | --- |
| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| **delete** ( entity ) | System should do any housekeeping based on [SceneObjectSystem.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_sceneobjectsystem#delete) being removed from the scene Signature ```kotlin open override fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **getSceneObject** ( entity ) | Returns a future for the SceneObject associated with the entity. A null return represents no load has started for this Entity. Note: You will likely get null if you call this immediately after attaching a [Mesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_mesh) component to an entity. You will likely need to call this in a System to ensure [MeshCreationSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_meshcreationsystem) has run by leveraging [SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase) getDependencies function. Signature ```kotlin fun getSceneObject(entity: Entity): CompletableFuture<SceneObject>? ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) the entity to get Returns CompletableFuture? |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **removeSceneObject** ( entity ) | Remove a SceneObject from the registry. Signature ```kotlin fun removeSceneObject(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) the associated entity for the `SceneObject` |