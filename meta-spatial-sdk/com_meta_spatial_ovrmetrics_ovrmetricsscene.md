# OVRMetricsScene Class

Extends
[OVRMetricsGroup](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsgroup)
*Modifiers:
final*

## Signature

```kotlin
class OVRMetricsScene(val getScene: () -> Scene?, init: OVRMetricsScene.() -> Unit = {}) : OVRMetricsGroup
```

## Constructors

| **OVRMetricsScene** ( getScene , init ) | Signature ```kotlin constructor(getScene: () -> Scene?, init: OVRMetricsScene.() -> Unit = {}) ``` Parameters getScene: Function0 init: Function1 Returns [OVRMetricsScene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsscene) |
| --- | --- |

## Properties

| **getScene** : Function0 [Get] | Signature ```kotlin val getScene: () -> Scene? ``` |
| --- | --- |
| **groupName** : String [Get] | Signature ```kotlin val groupName: String ``` |
| **metrics** : mutableListOf<OVRMetric>() [Get] | Signature ```kotlin val metrics: mutableListOf<OVRMetric>() ``` |
| **overlayMessages** : mutableListOf<() -> String>() [Get] | Signature ```kotlin val overlayMessages: mutableListOf<() -> String>() ``` |

## Functions

| **numberOfObjects** () | Signature ```kotlin fun numberOfObjects(): OVRMetricsScene ``` Returns [OVRMetricsScene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsscene) |
| --- | --- |
| **viewOrigin** () | Signature ```kotlin fun viewOrigin(): OVRMetricsScene ``` Returns [OVRMetricsScene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsscene) |
| **viewRotationX** () | Signature ```kotlin fun viewRotationX(): OVRMetricsScene ``` Returns [OVRMetricsScene](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsscene) |