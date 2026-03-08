# IsLocalFilterNode Class

Extends
[FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode)
*Modifiers:
final*

A class representing a filter node for local entities.

This class is used to create filter nodes that represent conditions checking if an entity is local to the client. This is particularly useful in networked applications to filter for entities that belong to the local user.

## Signature

```kotlin
class IsLocalFilterNode(val filterBuilder: FilterBuilder) : FilterNode
```

## Constructors

| **IsLocalFilterNode** ( filterBuilder ) | Signature ```kotlin constructor(filterBuilder: FilterBuilder) ``` Parameters filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [IsLocalFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_islocalfilternode) |
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