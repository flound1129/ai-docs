# OVRMetricsTool Class

*Modifiers:
final*

## Signature

```kotlin
class OVRMetricsTool
```

## Constructors

| **OVRMetricsTool** () | Signature ```kotlin constructor() ``` Returns [OVRMetricsTool](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricstool) |
| --- | --- |

## Companion Object

### Companion Object Properties

| **json** : Json [Get] | Signature ```kotlin val json: Json ``` |
| --- | --- |

### Companion Object Functions

| **appendCsvDebugString** ( debugString ) | Signature ```kotlin fun appendCsvDebugString(debugString: String) ``` Parameters debugString: String |
| --- | --- |
| **defineMetrics** ( metrics ) | Signature ```kotlin fun defineMetrics(metrics: List<OVRMetric>): Boolean ``` Parameters metrics: List Returns Boolean |
| **defineMetrics** ( json ) | Signature ```kotlin fun defineMetrics(json: String): Boolean ``` Parameters json: String Returns Boolean |
| **destroy** () | Signature ```kotlin fun destroy() ``` |
| **init** ( context , loadLibraryCallback ) | Signature ```kotlin fun init(context: Context, loadLibraryCallback: (String) -> Unit) ``` Parameters context: Context loadLibraryCallback: Function1 |
| **setOverlayDebugString** ( debugString ) | Signature ```kotlin fun setOverlayDebugString(debugString: String) ``` Parameters debugString: String |
| **submitMetrics** ( metrics ) | Signature ```kotlin fun submitMetrics(metrics: List<OVRMetric>): Boolean ``` Parameters metrics: List Returns Boolean |
| **submitMetrics** ( json ) | Signature ```kotlin fun submitMetrics(json: String): Boolean ``` Parameters json: String Returns Boolean |