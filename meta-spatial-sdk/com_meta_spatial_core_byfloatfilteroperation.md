# ByFloatFilterOperation Class

*Modifiers:
final*

A class representing a filter operation for float attributes. It is used to build a filter expression by specifying comparison operations on float attribute values.

This class provides methods for creating filter nodes that represent various comparison operations on float attributes, such as equality, greater than, less than, etc. These filter nodes can then be combined using logical operators (AND, OR) to create complex filtering conditions.

Example:

```kotlin // Find entities where floatVar equals 3.14f
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.floatVarData).isEqualTo(3.14f) }
// Find entities where floatVar is between 0.0f and 1.0f
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.floatVarData).greaterThanOrEqualTo(0.0f) and
               by(TestComponent.floatVarData).lessThanOrEqualTo(1.0f) }
// Find entities where floatVar is not equal to 0.0f
Query.where { has(TestComponent.id) }
     .filter { not(by(TestComponent.floatVarData).isEqualTo(0.0f)) } ```

## Signature

```kotlin
class ByFloatFilterOperation(val attrId: Int, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByFloatFilterOperation** ( attrId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the float attribtues for the filter operation. filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByFloatFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byfloatfilteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | The attribute id of the float attribtues for the filter operation. Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | The filter builder object used to create the filter node. Signature ```kotlin val filterBuilder: FilterBuilder ``` |

## Functions

| **greaterThan** ( value ) | Creates a filter node representing a greater than condition with the given value. Signature ```kotlin fun greaterThan(value: Float): ByFloatFilterNode ``` Parameters value: Float The float value to compare against. Returns [ByFloatFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byfloatfilternode) A filter node representing the greater than condition. |
| --- | --- |
| **greaterThanOrEqualTo** ( value , epsilon ) | Creates a filter node representing a greater than or equal to condition with the given value. The epsilon parameter allows for approximate equality comparison with floating point values when checking the equality part of the condition. Signature ```kotlin fun greaterThanOrEqualTo(value: Float, epsilon: Float = 1.0E-5f): ByFloatFilterNode ``` Parameters value: Float The float value to compare against. epsilon: Float The maximum allowed difference between values for them to be considered equal. Returns [ByFloatFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byfloatfilternode) A filter node representing the greater than or equal to condition. |
| **isEqualTo** ( value , epsilon ) | Creates a filter node representing an equality condition with the given value. The epsilon parameter allows for approximate equality comparison with floating point values. Two float values are considered equal if their absolute difference is less than epsilon. Example: ```kotlin // Find entities where floatVar equals 3.14f (with default epsilon of 1e-5f) Query.where { has(TestComponent.id) } .filter { by(TestComponent.floatVarData).isEqualTo(3.14f) } ``` Signature ```kotlin fun isEqualTo(value: Float, epsilon: Float = 1.0E-5f): ByFloatFilterNode ``` Parameters value: Float The float value to compare against. epsilon: Float The maximum allowed difference between values for them to be considered equal. Returns [ByFloatFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byfloatfilternode) A filter node representing the equality condition. |
| **lessThan** ( value ) | Creates a filter node representing a less than condition with the given value. Signature ```kotlin fun lessThan(value: Float): ByFloatFilterNode ``` Parameters value: Float The float value to compare against. Returns [ByFloatFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byfloatfilternode) A filter node representing the less than condition. |
| **lessThanOrEqualTo** ( value , epsilon ) | Creates a filter node representing a less than or equal to condition with the given value. The epsilon parameter allows for approximate equality comparison with floating point values when checking the equality part of the condition. Signature ```kotlin fun lessThanOrEqualTo(value: Float, epsilon: Float = 1.0E-5f): ByFloatFilterNode ``` Parameters value: Float The float value to compare against. epsilon: Float The maximum allowed difference between values for them to be considered equal. Returns [ByFloatFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byfloatfilternode) A filter node representing the less than or equal to condition. |