# FilterNode Class

*Modifiers:
open*

A class representing a node in a filter tree.

Filter nodes are the building blocks of filter expressions. They can be combined using logical operators (AND, OR) to create complex filtering conditions. Each filter node represents either a basic filter condition or a logical operation between other filter nodes.

## Signature

```kotlin
open class FilterNode(val type: FilterNodeType, val filterFunctionInfo: FilterFunctionInfo? = null, val filterBuilder: FilterBuilder)
```

## Constructors

| **FilterNode** ( type , filterFunctionInfo , filterBuilder ) | Signature ```kotlin constructor(type: FilterNodeType, filterFunctionInfo: FilterFunctionInfo? = null, filterBuilder: FilterBuilder) ``` Parameters type: [FilterNodeType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternodetype) filterFunctionInfo: FilterFunctionInfo? filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) Returns [FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode) |
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