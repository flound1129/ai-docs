# ByUUIDFilterNode Class

Extends
[FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode)
*Modifiers:
final*

A class representing a filter node for UUID values.

## Signature

```kotlin
class ByUUIDFilterNode(attrId: Int, filterNodeType: FilterNodeType = FilterNodeType.FILTER, val filterBuilder: FilterBuilder) : FilterNode
```

## Constructors

| **ByUUIDFilterNode** ( attrId , filterNodeType , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, filterNodeType: FilterNodeType = FilterNodeType.FILTER, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the filter node. filterNodeType: [FilterNodeType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternodetype) filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByUUIDFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byuuidfilternode) |
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