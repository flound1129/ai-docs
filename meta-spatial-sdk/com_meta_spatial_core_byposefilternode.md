# ByPoseFilterNode Class

Extends
[FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode)
*Modifiers:
final*

A class representing a filter node for Pose values.

This class is used to create filter nodes that represent conditions on Pose attributes or their individual components (position X/Y/Z or orientation W/X/Y/Z). It can be used both for comparing entire Pose values and for component-wise comparisons.

When used for component-wise filtering, the propId parameter specifies which component to operate on (0-2 for position X/Y/Z, 3-6 for orientation W/X/Y/Z).

## Signature

```kotlin
class ByPoseFilterNode(attrId: Int, propId: Int, filterNodeType: FilterNodeType = FilterNodeType.FILTER, val filterBuilder: FilterBuilder) : FilterNode
```

## Constructors

| **ByPoseFilterNode** ( attrId , propId , filterNodeType , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, propId: Int, filterNodeType: FilterNodeType = FilterNodeType.FILTER, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the filter node. propId: Int The property id indicating which component to filter on. filterNodeType: [FilterNodeType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternodetype) The type of filter node (FILTER for leaf nodes, AND/OR for composite nodes). filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByPoseFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilternode) |
| --- | --- |

## Properties

| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | Signature ```kotlin val filterBuilder: FilterBuilder ``` |
| --- | --- |
| **filterFunctionInfo** : FilterFunctionInfo? [Get] | Signature ```kotlin val filterFunctionInfo: FilterFunctionInfo? = null ``` |
| **left** : [FilterNode?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode) [Get][Set] | Signature ```kotlin var left: FilterNode? ``` |
| **parent** : [FilterNode?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode) [Get][Set] | Signature ```kotlin var parent: FilterNode? ``` |
| **right** : [FilterNode?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode) [Get][Set] | Signature ```kotlin var right: FilterNode? ``` |
| **type** : [FilterNodeType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternodetype) [Get] | Signature ```kotlin val type: FilterNodeType ``` |

## Functions

| **and** ( b ) | Performs a logical AND operation with another filter node. Signature ```kotlin infix fun and(b: FilterNode): FilterNode ``` Parameters b: [FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode) The other query node. Returns [FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode) A new filter node representing the AND operation. |
| --- | --- |
| **or** ( b ) | Performs a logical OR operation with another filter node. Signature ```kotlin infix fun or(b: FilterNode): FilterNode ``` Parameters b: [FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode) The other filter node. Returns [FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode) A new filter node representing the OR operation. |