# OVRMetricsTickTrackingSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

System for tracking tick rate performance metrics.

This system measures ticks-per-second (TPS) and maximum tick time, which can be used for performance monitoring and debugging. The tick data is updated every tick in execute().

## Signature

```kotlin
class OVRMetricsTickTrackingSystem : SystemBase
```

## Constructors

| **OVRMetricsTickTrackingSystem** () | Signature ```kotlin constructor() ``` Returns [OVRMetricsTickTrackingSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsticktrackingsystem) |
| --- | --- |

## Properties

| **currentTPS** : Int [Get] | Current ticks per second as a rolling average, updated once per second. Signature ```kotlin var currentTPS: Int ``` |
| --- | --- |
| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| **maxTickTimeDurationSeconds** : Int [Get] | Duration in seconds over which max tick time is tracked. Default is 1 second. Signature ```kotlin var maxTickTimeDurationSeconds: Int ``` |
| **maxTickTimeMs** : Int [Get] | Maximum tick time in milliseconds during the last measurement period. Signature ```kotlin var maxTickTimeMs: Int ``` |
| **systemManager** : [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) [Get][Set] | The system manager that this system is associated with. Signature ```kotlin lateinit var systemManager: SystemManager ``` |

## Functions

| **associateSystemManager** ( systemManager ) | Associates this system with a system manager, used in the Spatial SDK. Signature ```kotlin fun associateSystemManager(systemManager: SystemManager) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The system manager to associate with. |
| --- | --- |
| **delete** ( entity ) | System should do any housekeeping based on [SystemBase.delete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase#delete) being removed from the scene Signature ```kotlin open fun delete(entity: Entity) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **destroy** () | System should clean up any and all resources for shutdown Signature ```kotlin open fun destroy() ``` |
| **equals** ( other ) | Checks if this system is equal to another object. Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? The object to compare with. Returns Boolean True if this system is equal to the other object, false otherwise. |
| **execute** () | System should perform all the operations based on relevant entities. Signature ```kotlin open override fun execute() ``` |
| **getDependencies** () | Returns the dependencies of this system. Signature ```kotlin open fun getDependencies(): SystemDependencies? ``` Returns [SystemDependencies?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemdependencies) The dependencies of this system, or null if there are no dependencies. |
| **getScene** () | Returns the scene that this system is associated with. Signature ```kotlin fun getScene(): Scene ``` Returns [Scene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scene) The scene that this system is associated with. |
| **hashCode** () | Returns the hash code of this system. Signature ```kotlin open override fun hashCode(): Int ``` Returns Int The hash code of this system. |
| **setMaxTickTimeDuration** ( durationSeconds ) | Sets the duration in seconds over which max tick time is tracked. Signature ```kotlin fun setMaxTickTimeDuration(durationSeconds: Int) ``` Parameters durationSeconds: Int The number of seconds to track max tick time over (minimum 1) |
| **setTPSSampleCount** ( sampleCount ) | Sets the number of samples to use for the TPS rolling average. Signature ```kotlin fun setTPSSampleCount(sampleCount: Int) ``` Parameters sampleCount: Int The number of samples to average over (minimum 1) |