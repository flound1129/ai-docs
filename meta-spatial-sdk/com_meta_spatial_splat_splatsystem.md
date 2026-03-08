# SplatSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

System that manages Splat logic for initializing the Splat Renderer, loading splat data and updating the splat data transform at the Splat Renderer level.

## Signature

```kotlin
class SplatSystem(val context: SpatialContext) : SystemBase
```

## Constructors

| **SplatSystem** ( context ) | Signature ```kotlin constructor(context: SpatialContext) ``` Parameters context: [SpatialContext](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialcontext) Returns [SplatSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_splat_splatsystem) |
| --- | --- |

## Properties

| **context** : [SpatialContext](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialcontext) [Get] | Signature ```kotlin val context: SpatialContext ``` |
| --- | --- |
| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **delete** ( entity ) | System should do any housekeeping based on [SplatSystem.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_splat_splatsystem#delete) being removed from the scene Signature ```kotlin open override fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open override fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **isPlyFile** ( file ) | Signature ```kotlin fun isPlyFile(file: File): Boolean ``` Parameters file: File Returns Boolean |
| **isSplatRendererInitialized** () | Signature ```kotlin fun isSplatRendererInitialized(): Boolean ``` Returns Boolean |
| **isSpzFile** ( file ) | Signature ```kotlin fun isSpzFile(file: File): Boolean ``` Parameters file: File Returns Boolean |
| **loadFileFromUri** ( context , uri ) | Load file from any source (file://, apk://, http://, https://) Signature ```kotlin suspend fun loadFileFromUri(context: Context, uri: Uri): Result<Pair<ByteArray, SplatFormat>> ``` Parameters context: Context uri: Uri Returns Result<Pair<ByteArray, SplatFormat>> |
| **loadSplatAsync** ( entity , context , uri ) | Signature ```kotlin fun loadSplatAsync(entity: Entity, context: SpatialContext, uri: Uri) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) context: [SpatialContext](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialcontext) uri: Uri |
| **setSplatVisibility** ( entityID , visibility ) | Signature ```kotlin fun setSplatVisibility(entityID: Long, visibility: Boolean) ``` Parameters entityID: Long visibility: Boolean |
| **shouldBeVisible** ( entity ) | Signature ```kotlin fun shouldBeVisible(entity: Entity): Boolean ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) Returns Boolean |
| **updateSplatTransform** ( entityID , pose , scale ) | Signature ```kotlin fun updateSplatTransform(entityID: Long, pose: Pose, scale: Vector3) ``` Parameters entityID: Long pose: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) scale: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) |