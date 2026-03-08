# OVRMetric Class

*Modifiers:
final*

## Signature

```kotlin
data class OVRMetric(val definition: OVRMetricDefinition, val getValue: () -> Int)
```

## Constructors

| **OVRMetric** ( definition , getValue ) | Signature ```kotlin constructor(definition: OVRMetricDefinition, getValue: () -> Int) ``` Parameters definition: [OVRMetricDefinition](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricdefinition) getValue: Function0 Returns [OVRMetric](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetric) |
| --- | --- |

## Properties

| **definition** : [OVRMetricDefinition](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricdefinition) [Get] | Signature ```kotlin val definition: OVRMetricDefinition ``` |
| --- | --- |
| **getValue** : Function0 [Get] | Signature ```kotlin val getValue: () -> Int ``` |

## Functions

| **getName** () | Signature ```kotlin fun getName(): String ``` Returns String |
| --- | --- |