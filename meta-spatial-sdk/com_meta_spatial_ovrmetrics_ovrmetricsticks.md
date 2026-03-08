# OVRMetricsTicks Class

Extends
[OVRMetricsGroup](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsgroup)
*Modifiers:
final*

Metrics group for tick rate performance monitoring.

Tick data is calculated in OVRMetricsTickTrackingSystem.execute() which runs every tick. The OVRMetricsTickTrackingSystem is lazily registered only when [OVRMetricsTicks.ticksPerSecond](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsticks#tickspersecond) or [OVRMetricsTicks.maxTickTimeMs](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsticks#maxticktimems) is called, avoiding unnecessary overhead if tick metrics aren't used.

## Signature

```kotlin
class OVRMetricsTicks(systemManager: SystemManager, init: OVRMetricsTicks.() -> Unit = {}) : OVRMetricsGroup
```

## Constructors

| **OVRMetricsTicks** ( systemManager , init ) | Signature ```kotlin constructor(systemManager: SystemManager, init: OVRMetricsTicks.() -> Unit = {}) ``` Parameters systemManager: [SystemManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_systemmanager) The SystemManager used to register the OVRMetricsTickTrackingSystem when needed. init: Function1 Returns [OVRMetricsTicks](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsticks) |
| --- | --- |

## Properties

| **groupName** : String [Get] | Signature ```kotlin val groupName: String ``` |
| --- | --- |
| **metrics** : mutableListOf<OVRMetric>() [Get] | Signature ```kotlin val metrics: mutableListOf<OVRMetric>() ``` |
| **overlayMessages** : mutableListOf<() -> String>() [Get] | Signature ```kotlin val overlayMessages: mutableListOf<() -> String>() ``` |

## Functions

| **maxTickTimeMs** ( durationSeconds ) | Adds a max tick time metric showing the worst tick duration in milliseconds over the specified duration. Signature ```kotlin fun maxTickTimeMs(durationSeconds: Int = 1): OVRMetricsTicks ``` Parameters durationSeconds: Int The number of seconds to track max tick time over (default: 1, minimum: 1) Returns [OVRMetricsTicks](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsticks) |
| --- | --- |
| **ticksPerSecond** ( sampleCount ) | Adds a ticks-per-second metric with a graph ranging from 0-90 TPS. Signature ```kotlin fun ticksPerSecond(sampleCount: Int = 5): OVRMetricsTicks ``` Parameters sampleCount: Int The number of samples to use for the rolling average (default: 5, minimum: 1). Higher values provide smoother readings but slower response to changes. Returns [OVRMetricsTicks](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsticks) |