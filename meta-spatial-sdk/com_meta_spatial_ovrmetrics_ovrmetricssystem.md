# OVRMetricsSystem Class

Extends
[SystemBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systembase)
*Modifiers:
final*

## Signature

```kotlin
class OVRMetricsSystem(metrics: List<OVRMetric> = emptyList(), overlayMessages: Map<String, () -> String> = emptyMap()) : SystemBase
```

## Constructors

| **OVRMetricsSystem** ( metrics , overlayMessages ) | Signature ```kotlin constructor(metrics: List<OVRMetric> = emptyList(), overlayMessages: Map<String, () -> String> = emptyMap()) ``` Parameters metrics: List overlayMessages: Map Returns [OVRMetricsSystem](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricssystem) |
| --- | --- |

## Properties

| **defineIntervalInMillis** : Long [Get] | Signature ```kotlin val defineIntervalInMillis: Long = 5000 ``` |
| --- | --- |
| **executeCount** : Long [Get] | The number of times the system has been executed. Signature ```kotlin var executeCount: Long ``` |
| **isDisabled** : Boolean [Get][Set] | Signature ```kotlin var isDisabled: Boolean ``` |
| **isMetricsDefined** : Boolean [Get][Set] | Signature ```kotlin var isMetricsDefined: Boolean ``` |
| **lastTimeInMillis** : Long [Get][Set] | Signature ```kotlin var lastTimeInMillis: Long ``` |
| **overlayMessageKeys** : Set [Get] | Returns an immutable copy of the currently registered overlay message keys. Signature ```kotlin val overlayMessageKeys: Set<String> ``` |
| **registeredMetrics** : List [Get] | Returns an immutable copy of the currently registered metrics. Signature ```kotlin val registeredMetrics: List<OVRMetric> ``` |
| **submitIntervalInMillis** : Long [Get] | Signature ```kotlin val submitIntervalInMillis: Long = 1000 ``` |
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
| **registerMetric** ( metric ) | Registers a new metric at runtime. If metrics have already been defined with OVRMetricsTool, they will be redefined to include the new metric. Signature ```kotlin fun registerMetric(metric: OVRMetric) ``` Parameters metric: [OVRMetric](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetric) The metric to register |
| **registerMetrics** ( newMetrics ) | Registers multiple metrics at runtime. If metrics have already been defined with OVRMetricsTool, they will be redefined to include the new metrics. Signature ```kotlin fun registerMetrics(newMetrics: List<OVRMetric>) ``` Parameters newMetrics: List The metrics to register |
| **registerOverlayMessage** ( key , message ) | Registers a new overlay message at runtime with a unique key. The message will be displayed in subsequent overlay updates. If a message with the same key already exists, it will be replaced. Signature ```kotlin fun registerOverlayMessage(key: String, message: () -> String) ``` Parameters key: String A unique identifier for this overlay message message: Function0 A function that returns the message string to display |
| **unregisterMetric** ( name ) | Unregisters a metric by its name at runtime. If metrics have already been defined with OVRMetricsTool, they will be redefined without the removed metric. Signature ```kotlin fun unregisterMetric(name: String): Boolean ``` Parameters name: String The name of the metric to unregister (matches OVRMetricDefinition.Name) Returns Boolean true if the metric was found and removed, false otherwise |
| **unregisterOverlayMessage** ( key ) | Unregisters an overlay message by its key. Signature ```kotlin fun unregisterOverlayMessage(key: String): Boolean ``` Parameters key: String The key of the overlay message to unregister Returns Boolean true if the message was found and removed, false otherwise |