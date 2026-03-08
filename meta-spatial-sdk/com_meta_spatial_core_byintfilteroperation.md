# ByIntFilterOperation Class

*Modifiers:
final*

A class representing a filter operation for integer attributes. It is used to build a filter expression by specifying filter operation and its operands.

This class provides methods for creating filter nodes that represent various comparison operations on integer attributes, such as equality, greater than, less than, etc. These filter nodes can then be combined using logical operators (AND, OR) to create complex filtering conditions.

Example:

```kotlin // Find entities where intVar equals 42
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.intVarData).isEqualTo(42) }
// Find entities where intVar is between 10 and 20
Query.where { has(TestComponent.id) }
     .filter {
       by(TestComponent.intVarData).greaterThanOrEqualTo(10) and
       by(TestComponent.intVarData).lessThanOrEqualTo(20)
     }
// Find entities where intVar is not equal to 0
Query.where { has(TestComponent.id) }
     .filter { not(by(TestComponent.intVarData).isEqualTo(0)) } ```

## Signature

```kotlin
class ByIntFilterOperation(val attrId: Int, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByIntFilterOperation** ( attrId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the integer attribute for the filter operation. filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByIntFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byintfilteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | The attribute id of the integer attribute for the filter operation. Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | The filter builder object used to create the filter node. Signature ```kotlin val filterBuilder: FilterBuilder ``` |

## Functions

| **greaterThan** ( value ) | Creates a filter node representing a greater than condition with the given value. Signature ```kotlin fun greaterThan(value: Int): ByIntFilterNode ``` Parameters value: Int Returns [ByIntFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byintfilternode) |
| --- | --- |
| **greaterThanOrEqualTo** ( value ) | Creates a filter node representing a greater than or equal to condition with the given value. Signature ```kotlin fun greaterThanOrEqualTo(value: Int): ByIntFilterNode ``` Parameters value: Int Returns [ByIntFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byintfilternode) |
| **isEqualTo** ( value ) | Creates a filter node representing an equality condition with the given value. Signature ```kotlin fun isEqualTo(value: Int): ByIntFilterNode ``` Parameters value: Int Returns [ByIntFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byintfilternode) |
| **lessThan** ( value ) | Creates a filter node representing a less than condition with the given value. Signature ```kotlin fun lessThan(value: Int): ByIntFilterNode ``` Parameters value: Int Returns [ByIntFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byintfilternode) |
| **lessThanOrEqualTo** ( value ) | Creates a filter node representing a less than or equal to condition with the given value. Signature ```kotlin fun lessThanOrEqualTo(value: Int): ByIntFilterNode ``` Parameters value: Int Returns [ByIntFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byintfilternode) |