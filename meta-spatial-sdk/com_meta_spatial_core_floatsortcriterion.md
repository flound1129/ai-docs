# FloatSortCriterion Class

Extends
[SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion)
*Modifiers:
final*

Sort criterion based on float attribute.

## Signature

```kotlin
class FloatSortCriterion(val attrId: Int) : SortCriterion
```

## Constructors

| **FloatSortCriterion** ( attrId ) | Signature ```kotlin constructor(attrId: Int) ``` Parameters attrId: Int The attribute id to sort by. Returns [FloatSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatsortcriterion) |
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