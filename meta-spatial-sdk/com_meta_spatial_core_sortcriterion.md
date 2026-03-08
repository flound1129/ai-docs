# SortCriterion Class

*Modifiers:
abstract*

Sort criterion for sorting a list of entities.

A sort criterion defines how entities should be ordered based on a specific attribute. Each criterion includes:

- An attribute ID (attrId) identifying which attribute to sort by - An optional property code (propCode) for vector/pose attributes to specify which component (X, Y or Z) to use - A sort option (sortOption) determining the direction and case sensitivity

## Signature

```kotlin
abstract class SortCriterion(val attrId: Int, var propCode: Int = 0, var sortOption: Int = 0)
```

## Constructors

| **SortCriterion** ( attrId , propCode , sortOption ) | Signature ```kotlin constructor(attrId: Int, propCode: Int = 0, sortOption: Int = 0) ``` Parameters attrId: Int propCode: Int sortOption: Int Returns [SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion) |
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