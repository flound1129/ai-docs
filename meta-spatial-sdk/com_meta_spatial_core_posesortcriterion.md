# PoseSortCriterion Class

Extends
[SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion)
*Modifiers:
final*

Represents a sorting criterion based on a Pose attribute.

## Signature

```kotlin
class PoseSortCriterion(val attrId: Int) : SortCriterion
```

## Constructors

| **PoseSortCriterion** ( attrId ) | Signature ```kotlin constructor(attrId: Int) ``` Parameters attrId: Int The ID of the attribute to sort by. Returns [PoseSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_posesortcriterion) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **propCode** : Int [Get][Set] | Signature ```kotlin var propCode: Int ``` |
| **sortOption** : Int [Get][Set] | Signature ```kotlin var sortOption: Int ``` |

## Functions

| **asc** () | function to set the sorting order to ascending Signature ```kotlin fun asc(): SortCriterion ``` Returns [SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion) |
| --- | --- |
| **byOrientationW** () | Specifies that the sorting should be based on the W orientation of the Pose attribute. Signature ```kotlin fun byOrientationW(): PoseSortCriterion ``` Returns [PoseSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_posesortcriterion) The current instance of PoseSortCriterion for method chaining. |
| **byOrientationX** () | Specifies that the sorting should be based on the X orientation of the Pose attribute. Signature ```kotlin fun byOrientationX(): PoseSortCriterion ``` Returns [PoseSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_posesortcriterion) The current instance of PoseSortCriterion for method chaining. |
| **byOrientationY** () | Specifies that the sorting should be based on the Y orientation of the Pose attribute. Signature ```kotlin fun byOrientationY(): PoseSortCriterion ``` Returns [PoseSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_posesortcriterion) The current instance of PoseSortCriterion for method chaining. |
| **byOrientationZ** () | Specifies that the sorting should be based on the Z orientation of the Pose attribute. Signature ```kotlin fun byOrientationZ(): PoseSortCriterion ``` Returns [PoseSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_posesortcriterion) The current instance of PoseSortCriterion for method chaining. |
| **byPositionX** () | Specifies that the sorting should be based on the X position of the Pose attribute. Signature ```kotlin fun byPositionX(): PoseSortCriterion ``` Returns [PoseSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_posesortcriterion) The current instance of PoseSortCriterion for method chaining. |
| **byPositionY** () | Specifies that the sorting should be based on the Y position of the Pose attribute. Signature ```kotlin fun byPositionY(): PoseSortCriterion ``` Returns [PoseSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_posesortcriterion) The current instance of PoseSortCriterion for method chaining. |
| **byPositionZ** () | Specifies that the sorting should be based on the Z position of the Pose attribute. Signature ```kotlin fun byPositionZ(): PoseSortCriterion ``` Returns [PoseSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_posesortcriterion) The current instance of PoseSortCriterion for method chaining. |
| **desc** () | function to set the sorting order to descending Signature ```kotlin fun desc(): SortCriterion ``` Returns [SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriterion) |