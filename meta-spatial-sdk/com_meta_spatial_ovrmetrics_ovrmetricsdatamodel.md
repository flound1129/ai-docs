# OVRMetricsDataModel Class

Extends
[OVRMetricsGroup](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsgroup)
*Modifiers:
final*

## Signature

```kotlin
class OVRMetricsDataModel(init: OVRMetricsDataModel.() -> Unit = {}) : OVRMetricsGroup
```

## Constructors

| **OVRMetricsDataModel** ( init ) | Signature ```kotlin constructor(init: OVRMetricsDataModel.() -> Unit = {}) ``` Parameters init: Function1 Returns [OVRMetricsDataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsdatamodel) |
| --- | --- |

## Properties

| **groupName** : String [Get] | Signature ```kotlin val groupName: String ``` |
| --- | --- |
| **metrics** : mutableListOf<OVRMetric>() [Get] | Signature ```kotlin val metrics: mutableListOf<OVRMetric>() ``` |
| **overlayMessages** : mutableListOf<() -> String>() [Get] | Signature ```kotlin val overlayMessages: mutableListOf<() -> String>() ``` |

## Functions

| **numberOfGrabbables** () | Signature ```kotlin fun numberOfGrabbables(): OVRMetricsDataModel ``` Returns [OVRMetricsDataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsdatamodel) |
| --- | --- |
| **numberOfMeshes** () | Signature ```kotlin fun numberOfMeshes(): OVRMetricsDataModel ``` Returns [OVRMetricsDataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsdatamodel) |
| **numberOfPanels** () | Signature ```kotlin fun numberOfPanels(): OVRMetricsDataModel ``` Returns [OVRMetricsDataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricsdatamodel) |