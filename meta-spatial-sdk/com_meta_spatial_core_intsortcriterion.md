# IntSortCriterion Class

Extends
[SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion)
*Modifiers:
final*

Sort criterion based on int attribute.

## Signature

```kotlin
class IntSortCriterion(val attrId: Int) : SortCriterion
```

## Constructors

| **IntSortCriterion** ( attrId ) | Signature ```kotlin constructor(attrId: Int) ``` Parameters attrId: Int The attribute id to sort by. Returns [IntSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intsortcriterion) |
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