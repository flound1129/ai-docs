# StringSortCriterion Class

Extends
[SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion)
*Modifiers:
final*

Represents a sorting criterion based on a StringAttribute.

## Signature

```kotlin
class StringSortCriterion(val attrId: Int) : SortCriterion
```

## Constructors

| **StringSortCriterion** ( attrId ) | Signature ```kotlin constructor(attrId: Int) ``` Parameters attrId: Int The attribute id to sort by. Returns [StringSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_stringsortcriterion) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **propCode** : Int [Get][Set] | Signature ```kotlin var propCode: Int ``` |
| **sortOption** : Int [Get][Set] | Signature ```kotlin var sortOption: Int ``` |

## Functions

| **asc** () | function to set the sorting order to ascending Signature ```kotlin fun asc(): SortCriterion ``` Returns [SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion) |
| --- | --- |
| **ascCaseInsensitive** () | Specifies that the sort order should be ascending, ignoring case. Signature ```kotlin fun ascCaseInsensitive(): StringSortCriterion ``` Returns [StringSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_stringsortcriterion) The current instance of StringSortCriterion for method chaining. |
| **desc** () | function to set the sorting order to descending Signature ```kotlin fun desc(): SortCriterion ``` Returns [SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion) |
| **descCaseInsensitive** () | Specifies that the sort order should be descending, ignoring case. Signature ```kotlin fun descCaseInsensitive(): StringSortCriterion ``` Returns [StringSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_stringsortcriterion) The current instance of StringSortCriterion for method chaining. |