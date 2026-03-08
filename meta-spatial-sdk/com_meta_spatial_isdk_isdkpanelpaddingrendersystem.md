# IsdkPanelPaddingRenderSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

State-driven visual system for panel grab handles.

This system tracks the interaction state (unhovered/hovered/grabbed) for each panel's grab handles using a queue-based update mechanism. State updates are queued from input events and processed each frame in execute().

## Signature

```kotlin
class IsdkPanelPaddingRenderSystem : SystemBase
```

## Constructors

| **IsdkPanelPaddingRenderSystem** () | Signature ```kotlin constructor() ``` Returns [IsdkPanelPaddingRenderSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdkpanelpaddingrendersystem) |
| --- | --- |

## Properties

| **dropAudio** : [SceneAudioAsset](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneaudioasset) [Get][Set] | Signature ```kotlin lateinit var dropAudio: SceneAudioAsset ``` |
| --- | --- |
| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| **grabAudio** : [SceneAudioAsset](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_sceneaudioasset) [Get][Set] | Signature ```kotlin lateinit var grabAudio: SceneAudioAsset ``` |
| **grabbableCornerMesh** : [SceneMesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenemesh) [Get][Set] | Signature ```kotlin lateinit var grabbableCornerMesh: SceneMesh ``` |
| **grabbableEdgeMesh** : [SceneMesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenemesh) [Get][Set] | Signature ```kotlin lateinit var grabbableEdgeMesh: SceneMesh ``` |
| **resizeCornerMesh** : [SceneMesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenemesh) [Get][Set] | Signature ```kotlin lateinit var resizeCornerMesh: SceneMesh ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **delete** ( entity ) | System should do any housekeeping based on [IsdkPanelPaddingRenderSystem.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdkpanelpaddingrendersystem#delete) being removed from the scene Signature ```kotlin open override fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |