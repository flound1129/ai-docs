# ByVector4FilterOperation Class

*Modifiers:
final*

A class representing a filter operation for Vector4 attributes. It is used to build a filter expression by specifying comparison operations on Vector4 attribute values.

This class provides methods for creating filter nodes that represent various comparison operations on Vector4 attributes. It supports both:

- Comparing entire Vector4 values (all X, Y, Z, and W components together) - Component-wise comparisons (filtering on just the X, Y, Z, or W component)

The component-wise filtering is enabled through the byX(), byY(), byZ(), and byW() methods, which configure the filter to operate on a specific component of the Vector4.

Example:

```kotlin // Find entities where vector4Var equals Vector4(1.0f, 2.0f, 3.0f, 4.0f)
Query.where { has(TestComponent.id) }
    .filter { by(TestComponent.vector4VarData).isEqualTo(Vector4(1.0f, 2.0f, 3.0f, 4.0f)) }
// Find entities where vector4Var.w is greater than 0.5f
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.vector4VarData).byW().greaterThan(0.5f) }
// Find entities where vector4Var.z is between 0.0f and 1.0f
Query.where { has(TestComponent.id)}
     .filter { by(TestComponent.vector4VarData).byZ().greaterThanOrEqualTo(0.0f) and
               by(TestComponent.vector4VarData).byZ().lessThanOrEqualTo(1.0f) } ```

## Signature

```kotlin
class ByVector4FilterOperation(val attrId: Int, var propId: Int = 0, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByVector4FilterOperation** ( attrId , propId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, propId: Int = 0, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the filter operation. propId: Int The property id of the filter operation (0 for x, 1 for y, 2 for z, 3 for w). filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByVector4FilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector4filteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | Signature ```kotlin val filterBuilder: FilterBuilder ``` |
| **propId** : Int [Get][Set] | Signature ```kotlin var propId: Int ``` |

## Functions

| **byW** () | Sets the filter to operate on the W component of the Vector4. Signature ```kotlin fun byW(): ByVector4FilterOperation ``` Returns [ByVector4FilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector4filteroperation) This filter operation configured to filter on the W component. |
| --- | --- |
| **byX** () | Sets the filter to operate on the X component of the Vector4. Signature ```kotlin fun byX(): ByVector4FilterOperation ``` Returns [ByVector4FilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector4filteroperation) This filter operation configured to filter on the X component. |
| **byY** () | Sets the filter to operate on the Y component of the Vector4. Signature ```kotlin fun byY(): ByVector4FilterOperation ``` Returns [ByVector4FilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector4filteroperation) This filter operation configured to filter on the Y component. |
| **byZ** () | Sets the filter to operate on the Z component of the Vector4. Signature ```kotlin fun byZ(): ByVector4FilterOperation ``` Returns [ByVector4FilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector4filteroperation) This filter operation configured to filter on the Z component. |
| **greaterThan** ( value ) | Creates a filter node representing a greater than condition with the given float value. This compares only the component specified by propId (X, Y, Z, or W). By default, the filter operates on the X component. Signature ```kotlin fun greaterThan(value: Float): ByVector4FilterNode ``` Parameters value: Float The float value to compare against. Returns [ByVector4FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector4filternode) A filter node representing the greater than condition. |
| **greaterThanOrEqualTo** ( value ) | Creates a filter node representing a greater than or equal to condition with the given float value. This compares only the component specified by propId (X, Y, Z, or W). By default, the filter operates on the X component. Signature ```kotlin fun greaterThanOrEqualTo(value: Float): ByVector4FilterNode ``` Parameters value: Float The float value to compare against. Returns [ByVector4FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector4filternode) A filter node representing the greater than or equal to condition. |
| **isEqualTo** ( value ) | Creates a filter node representing an equality condition with the given Vector4 value. This compares all x, y, z, and w components of the vector. Signature ```kotlin fun isEqualTo(value: Vector4): ByVector4FilterNode ``` Parameters value: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The Vector4 value to compare against. Returns [ByVector4FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector4filternode) A filter node representing the equality condition. |
| **isEqualTo** ( value ) | Creates a filter node representing an equality condition with the given float value. This compares only the component specified by propId (X, Y, Z, or W). By default, the filter operates on the X component. Signature ```kotlin fun isEqualTo(value: Float): ByVector4FilterNode ``` Parameters value: Float The float value to compare against. Returns [ByVector4FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector4filternode) A filter node representing the equality condition. |
| **lessThan** ( value ) | Creates a filter node representing a less than condition with the given float value. This compares only the component specified by propId (X, Y, Z, or W). By default, the filter operates on the X component. Signature ```kotlin fun lessThan(value: Float): ByVector4FilterNode ``` Parameters value: Float The float value to compare against. Returns [ByVector4FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector4filternode) A filter node representing the less than condition. |
| **lessThanOrEqualTo** ( value ) | Creates a filter node representing a less than or equal to condition with the given float value. This compares only the component specified by propId (X, Y, Z, or W). By default, the filter operates on the X component. Signature ```kotlin fun lessThanOrEqualTo(value: Float): ByVector4FilterNode ``` Parameters value: Float The float value to compare against. Returns [ByVector4FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector4filternode) A filter node representing the less than or equal to condition. |