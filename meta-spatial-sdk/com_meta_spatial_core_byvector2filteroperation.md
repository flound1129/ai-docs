# ByVector2FilterOperation Class

*Modifiers:
final*

A class representing a filter operation for Vector2 attributes. It is used to build a filter expression by specifying comparison operations on Vector2 attribute values.

This class provides methods for creating filter nodes that represent various comparison operations on Vector2 attributes. It supports both:

- Comparing entire Vector2 values (both X and Y components together) - Component-wise comparisons (filtering on just the X or Y component)

The component-wise filtering is enabled through the byX() and byY() methods, which configure the filter to operate on a specific component of the Vector2.

Example:

```kotlin // Find entities where vector2Var equals Vector2(1.0f, 2.0f)
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.vector2VarData).isEqualTo(Vector2(1.0f, 2.0f)) }
// Find entities where vector2Var.x is greater than 0.5f
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.vector2VarData).byX().greaterThan(0.5f) }
// Find entities where vector2Var.y is between 0.0f and 1.0f
Query.where { has(TestComponent.id)}
     .filter { by(TestComponent.vector2VarData).byY().greaterThanOrEqualTo(0.0f) and
               by(TestComponent.vector2VarData).byY().lessThanOrEqualTo(1.0f) } ```

## Signature

```kotlin
class ByVector2FilterOperation(val attrId: Int, var propId: Int = 0, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByVector2FilterOperation** ( attrId , propId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, propId: Int = 0, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the filter operation. propId: Int The property id of the filter operation (0 for x, 1 for y). filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByVector2FilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector2filteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | The attribute id of the filter operation. Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | The filter builder object used to create the filter node. Signature ```kotlin val filterBuilder: FilterBuilder ``` |
| **propId** : Int [Get][Set] | The property id of the filter operation (0 for x, 1 for y). Signature ```kotlin var propId: Int ``` |

## Functions

| **byX** () | Sets the filter to operate on the X component of the Vector2. Signature ```kotlin fun byX(): ByVector2FilterOperation ``` Returns [ByVector2FilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector2filteroperation) This filter operation configured to filter on the X component. |
| --- | --- |
| **byY** () | Sets the filter to operate on the Y component of the Vector2. Signature ```kotlin fun byY(): ByVector2FilterOperation ``` Returns [ByVector2FilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector2filteroperation) This filter operation configured to filter on the Y component. |
| **greaterThan** ( value ) | Creates a filter node representing a greater than condition with the given float value. This compares only the component specified by propId (X or Y). By default, the filter operates on the X component. Signature ```kotlin fun greaterThan(value: Float): ByVector2FilterNode ``` Parameters value: Float The float value to compare against. Returns [ByVector2FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector2filternode) A filter node representing the greater than condition. |
| **greaterThanOrEqualTo** ( value ) | Creates a filter node representing a greater than or equal to condition with the given float value. This compares only the component specified by propId (X or Y). By default, the filter operates on the X component. Signature ```kotlin fun greaterThanOrEqualTo(value: Float): ByVector2FilterNode ``` Parameters value: Float The float value to compare against. Returns [ByVector2FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector2filternode) A filter node representing the greater than or equal to condition. |
| **isEqualTo** ( value ) | Creates a filter node representing an equality condition with the given Vector2 value. This compares both x and y components of the vector. Signature ```kotlin fun isEqualTo(value: Vector2): ByVector2FilterNode ``` Parameters value: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The Vector2 value to compare against. Returns [ByVector2FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector2filternode) A filter node representing the equality condition. |
| **isEqualTo** ( value ) | Creates a filter node representing an equality condition with the given float value. This compares only the component specified by propId (X or Y). By default, the filter operates on the X component. Signature ```kotlin fun isEqualTo(value: Float): ByVector2FilterNode ``` Parameters value: Float The float value to compare against. Returns [ByVector2FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector2filternode) A filter node representing the equality condition. |
| **lessThan** ( value ) | Creates a filter node representing a less than condition with the given float value. This compares only the component specified by propId (X or Y). By default, the filter operates on the X component. Signature ```kotlin fun lessThan(value: Float): ByVector2FilterNode ``` Parameters value: Float The float value to compare against. Returns [ByVector2FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector2filternode) A filter node representing the less than condition. |
| **lessThanOrEqualTo** ( value ) | Creates a filter node representing a less than or equal to condition with the given float value. This compares only the component specified by propId (X or Y). By default, the filter operates on the X component. Signature ```kotlin fun lessThanOrEqualTo(value: Float): ByVector2FilterNode ``` Parameters value: Float The float value to compare against. Returns [ByVector2FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector2filternode) A filter node representing the less than or equal to condition. |