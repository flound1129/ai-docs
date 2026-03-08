# Vector3SortCriterion Class

Extends
[SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion)
*Modifiers:
final*

Represents a sorting criterion based on a Vector3 attribute.

## Signature

```kotlin
class Vector3SortCriterion(val attrId: Int) : SortCriterion
```

## Constructors

| **Vector3SortCriterion** ( attrId ) | Signature ```kotlin constructor(attrId: Int) ``` Parameters attrId: Int The ID of the attribute to sort by. Returns [Vector3SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3sortcriterion) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **propCode** : Int [Get][Set] | Signature ```kotlin var propCode: Int ``` |
| **sortOption** : Int [Get][Set] | Signature ```kotlin var sortOption: Int ``` |

## Functions

| **asc** () | function to set the sorting order to ascending Signature ```kotlin fun asc(): SortCriterion ``` Returns [SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion) |
| --- | --- |
| **byX** () | Specifies that the sorting should be based on the X property of the Vector3 attribute. Signature ```kotlin fun byX(): Vector3SortCriterion ``` Returns [Vector3SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3sortcriterion) The current instance of Vector3SortCriterion for method chaining. |
| **byY** () | Specifies that the sorting should be based on the Y property of the Vector3 attribute. Signature ```kotlin fun byY(): Vector3SortCriterion ``` Returns [Vector3SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3sortcriterion) The current instance of Vector3SortCriterion for method chaining. |
| **byZ** () | Specifies that the sorting should be based on the Z property of the Vector3 attribute. Signature ```kotlin fun byZ(): Vector3SortCriterion ``` Returns [Vector3SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3sortcriterion) The current instance of Vector3SortCriterion for method chaining. |
| **desc** () | function to set the sorting order to descending Signature ```kotlin fun desc(): SortCriterion ``` Returns [SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion) |