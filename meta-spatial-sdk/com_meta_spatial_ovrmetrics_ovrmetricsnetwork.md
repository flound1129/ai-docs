# OVRMetricsNetwork Class

Extends
[OVRMetricsGroup](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsgroup)
*Modifiers:
final*

## Signature

```kotlin
class OVRMetricsNetwork(val getNetworking: () -> NetworkingBase?, init: OVRMetricsNetwork.() -> Unit = {}) : OVRMetricsGroup
```

## Constructors

| **OVRMetricsNetwork** ( getNetworking , init ) | Signature ```kotlin constructor(getNetworking: () -> NetworkingBase?, init: OVRMetricsNetwork.() -> Unit = {}) ``` Parameters getNetworking: Function0 init: Function1 Returns [OVRMetricsNetwork](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsnetwork) |
| --- | --- |

## Properties

| **getNetworking** : Function0 [Get] | Signature ```kotlin val getNetworking: () -> NetworkingBase? ``` |
| --- | --- |
| **groupName** : String [Get] | Signature ```kotlin val groupName: String ``` |
| **metrics** : mutableListOf<OVRMetric>() [Get] | Signature ```kotlin val metrics: mutableListOf<OVRMetric>() ``` |
| **overlayMessages** : mutableListOf<() -> String>() [Get] | Signature ```kotlin val overlayMessages: mutableListOf<() -> String>() ``` |

## Functions

| **packetLoss** () | Signature ```kotlin fun packetLoss(): OVRMetricsNetwork ``` Returns [OVRMetricsNetwork](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsnetwork) |
| --- | --- |
| **receiveBandwidth** () | Signature ```kotlin fun receiveBandwidth(): OVRMetricsNetwork ``` Returns [OVRMetricsNetwork](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsnetwork) |
| **rtt** () | Signature ```kotlin fun rtt(): OVRMetricsNetwork ``` Returns [OVRMetricsNetwork](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsnetwork) |
| **sendBandwidth** () | Signature ```kotlin fun sendBandwidth(): OVRMetricsNetwork ``` Returns [OVRMetricsNetwork](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsnetwork) |