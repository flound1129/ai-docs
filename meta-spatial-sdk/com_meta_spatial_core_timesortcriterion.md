# TimeSortCriterion Class

Extends
[SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion)
*Modifiers:
final*

Represents a sorting criterion based on a Time attribute.

## Signature

```kotlin
class TimeSortCriterion(val attrId: Int) : SortCriterion
```

## Constructors

| **TimeSortCriterion** ( attrId ) | Signature ```kotlin constructor(attrId: Int) ``` Parameters attrId: Int The ID of the attribute to sort by. Returns [TimeSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_timesortcriterion) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **propCode** : Int [Get][Set] | Signature ```kotlin var propCode: Int ``` |
| **sortOption** : Int [Get][Set] | Signature ```kotlin var sortOption: Int ``` |

## Functions

| **asc** () | function to set the sorting order to ascending Signature ```kotlin fun asc(): SortCriterion ``` Returns [SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion) |
| --- | --- |
| **desc** () | function to set the sorting order to descending Signature ```kotlin fun desc(): SortCriterion ``` Returns [SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion) |