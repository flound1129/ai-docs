# ByTimeFilterOperation Class

*Modifiers:
final*

A class representing a filter operation for Time attributes. It is used to build a filter expression by specifying comparison operations on Time attribute values.

This class provides methods for creating filter nodes that represent various comparison operations on Time attributes, such as equality, greater than, less than, etc. These filter nodes can then be combined using logical operators (AND, OR) to create complex filtering conditions.

Example:

```kotlin // Find entities where timeVar equals a specific timestamp
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.timeVarData).isEqualTo(1000L) }
// Find entities where timeVar is between two timestamps
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.timeVarData).greaterThanOrEqualTo(startTime) and
               by(TestComponent.timeVarData).lessThanOrEqualTo(endTime) }
// Find entities where timeVar is after a specific timestamp
Query.where { has(TestComponent.id)}
     .filter { by(TestComponent.timeVarData).greaterThan(timestamp) } ```

## Signature

```kotlin
class ByTimeFilterOperation(val attrId: Int, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByTimeFilterOperation** ( attrId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the Time attribute for the filter operation. filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByTimeFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bytimefilteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | Signature ```kotlin val filterBuilder: FilterBuilder ``` |

## Functions

| **greaterThan** ( value ) | Creates a filter node representing a greater than condition with the given timestamp value. Signature ```kotlin fun greaterThan(value: Long): ByTimeAttributeFilterNode ``` Parameters value: Long The timestamp value to compare against. Returns [ByTimeAttributeFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bytimeattributefilternode) A filter node representing the greater than condition. |
| --- | --- |
| **greaterThanOrEqualTo** ( value ) | Creates a filter node representing a greater than or equal to condition with the given timestamp value. Signature ```kotlin fun greaterThanOrEqualTo(value: Long): ByTimeAttributeFilterNode ``` Parameters value: Long The timestamp value to compare against. Returns [ByTimeAttributeFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bytimeattributefilternode) A filter node representing the greater than or equal to condition. |
| **isEqualTo** ( value ) | Creates a filter node representing an equality condition with the given timestamp value. Signature ```kotlin fun isEqualTo(value: Long): ByTimeAttributeFilterNode ``` Parameters value: Long The timestamp value to compare against. Returns [ByTimeAttributeFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bytimeattributefilternode) A filter node representing the equality condition. |
| **lessThan** ( value ) | Creates a filter node representing a less than condition with the given timestamp value. Signature ```kotlin fun lessThan(value: Long): ByTimeAttributeFilterNode ``` Parameters value: Long The timestamp value to compare against. Returns [ByTimeAttributeFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bytimeattributefilternode) A filter node representing the less than condition. |
| **lessThanOrEqualTo** ( value ) | Creates a filter node representing a less than or equal to condition with the given timestamp value. Signature ```kotlin fun lessThanOrEqualTo(value: Long): ByTimeAttributeFilterNode ``` Parameters value: Long The timestamp value to compare against. Returns [ByTimeAttributeFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bytimeattributefilternode) A filter node representing the less than or equal to condition. |