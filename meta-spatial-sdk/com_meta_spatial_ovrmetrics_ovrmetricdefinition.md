# OVRMetricDefinition Class

*Modifiers:
final*

## Signature

```kotlin
data class OVRMetricDefinition(val Name: String, val DisplayName: String, val Group: String? = null, val RangeMin: Int = 0, val RangeMax: Int = 100, val ShowGraph: Boolean = true, val ShowStat: Boolean = true)
```

## Constructors

| **OVRMetricDefinition** ( Name , DisplayName , Group , RangeMin , RangeMax , ShowGraph , ShowStat ) | Signature ```kotlin constructor(Name: String, DisplayName: String, Group: String? = null, RangeMin: Int = 0, RangeMax: Int = 100, ShowGraph: Boolean = true, ShowStat: Boolean = true) ``` Parameters Name: String DisplayName: String Group: String? RangeMin: Int RangeMax: Int ShowGraph: Boolean ShowStat: Boolean Returns [OVRMetricDefinition](/reference/spatial-sdk/v0.10.1/com_meta_spatial_ovrmetrics_ovrmetricdefinition) |
| --- | --- |

## Properties

| **DisplayName** : String [Get] | Signature ```kotlin val DisplayName: String ``` |
| --- | --- |
| **Group** : String? [Get] | Signature ```kotlin val Group: String? = null ``` |
| **Name** : String [Get] | Signature ```kotlin val Name: String ``` |
| **RangeMax** : Int [Get] | Signature ```kotlin val RangeMax: Int = 100 ``` |
| **RangeMin** : Int [Get] | Signature ```kotlin val RangeMin: Int = 0 ``` |
| **ShowGraph** : Boolean [Get] | Signature ```kotlin val ShowGraph: Boolean = true ``` |
| **ShowStat** : Boolean [Get] | Signature ```kotlin val ShowStat: Boolean = true ``` |