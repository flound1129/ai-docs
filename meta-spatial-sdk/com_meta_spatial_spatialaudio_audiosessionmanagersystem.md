# AudioSessionManagerSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

## Signature

```kotlin
class AudioSessionManagerSystem : SystemBase
```

## Constructors

| **AudioSessionManagerSystem** () | Signature ```kotlin constructor() ``` Returns [AudioSessionManagerSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_spatialaudio_audiosessionmanagersystem) |
| --- | --- |

## Properties

| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| --- | --- |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **calculateSoundfieldOrientation** ( orientationType , relativePose ) | Calculates the soundfield orientation based on the orientation type and relative pose. Signature ```kotlin fun calculateSoundfieldOrientation(orientationType: SoundfieldOrientationType, relativePose: Pose): Quaternion ``` Parameters orientationType: [SoundfieldOrientationType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_spatialaudio_soundfieldorientationtype) The type of soundfield orientation to use relativePose: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The relative pose between head and audio emitter Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The calculated orientation as a Quaternion |
| **calculateStereoObjectWorldPositions** ( entity , audioEmitterPose ) | Signature ```kotlin fun calculateStereoObjectWorldPositions(entity: Entity, audioEmitterPose: Pose): Pair<Vector3, Vector3> ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) audioEmitterPose: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) Returns Pair<Vector3, Vector3> |
| **delete** ( entity ) | System should do any housekeeping based on [AudioSessionManagerSystem.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_spatialaudio_audiosessionmanagersystem#delete) being removed from the scene Signature ```kotlin open override fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **registerAudioSessionId** ( registerId , sessionId ) | Signature ```kotlin fun registerAudioSessionId(registerId: Int, sessionId: Int) ``` Parameters registerId: Int sessionId: Int |
| **setAudioManagerHandle** ( handle ) | Signature ```kotlin fun setAudioManagerHandle(handle: Long) ``` Parameters handle: Long |