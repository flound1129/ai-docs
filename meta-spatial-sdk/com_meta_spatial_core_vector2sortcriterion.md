# Vector2SortCriterion Class

Extends
[SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion)
*Modifiers:
final*

Represents a sorting criterion based on a Vector2 attribute.

## Signature

```kotlin
class Vector2SortCriterion(val attrId: Int) : SortCriterion
```

## Constructors

| **Vector2SortCriterion** ( attrId ) | Signature ```kotlin constructor(attrId: Int) ``` Parameters attrId: Int The ID of the attribute to sort by. Returns [Vector2SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2sortcriterion) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **propCode** : Int [Get][Set] | Signature ```kotlin var propCode: Int ``` |
| **sortOption** : Int [Get][Set] | Signature ```kotlin var sortOption: Int ``` |

## Functions

| **asc** () | function to set the sorting order to ascending Signature ```kotlin fun asc(): SortCriterion ``` Returns [SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion) |
| --- | --- |
| **byX** () | Specifies that the sorting should be based on the X property of the Vector2 attribute. Signature ```kotlin fun byX(): Vector2SortCriterion ``` Returns [Vector2SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2sortcriterion) The current instance of Vector2SortCriterion for method chaining. |
| **byY** () | Specifies that the sorting should be based on the Y property of the Vector2 attribute. Signature ```kotlin fun byY(): Vector2SortCriterion ``` Returns [Vector2SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2sortcriterion) The current instance of Vector2SortCriterion for method chaining. |
| **desc** () | function to set the sorting order to descending Signature ```kotlin fun desc(): SortCriterion ``` Returns [SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion) |