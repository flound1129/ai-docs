# ByStringFilterOperation Class

*Modifiers:
final*

A class representing a filter operation for string attributes. It is used to build a filter expression by specifying comparison and pattern matching operations on string attribute values.

This class provides methods for creating filter nodes that represent various string operations, such as equality, comparison, case-insensitive matching, contains, startsWith, and endsWith. These filter nodes can then be combined using logical operators (AND, OR) to create complex filtering conditions.

Example:

```kotlin // Find entities where stringVar equals "hello"
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.stringVarData).isEqualTo("hello") }
// Find entities where stringVar contains "world"
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.stringVarData).contains("world") }
// Find entities where stringVar starts with "hello" and ends with "world"
Query.where { has(TestComponent.id) }
     .filter { by(TestComponent.stringVarData).startsWith("hello") and
               by(TestComponent.stringVarData).endsWith("world") } ```

## Signature

```kotlin
class ByStringFilterOperation(val attrId: Int, val filterBuilder: FilterBuilder)
```

## Constructors

| **ByStringFilterOperation** ( attrId , filterBuilder ) | Signature ```kotlin constructor(attrId: Int, filterBuilder: FilterBuilder) ``` Parameters attrId: Int The attribute id of the String attribute for the filter operation. filterBuilder: [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) The filter builder object used to create the filter node. Returns [ByStringFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bystringfilteroperation) |
| --- | --- |

## Properties

| **attrId** : Int [Get] | The attribute id of the String attribute for the filter operation. Signature ```kotlin val attrId: Int ``` |
| --- | --- |
| **filterBuilder** : [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) [Get] | The filter builder object used to create the filter node. Signature ```kotlin val filterBuilder: FilterBuilder ``` |

## Functions

| **contains** ( value ) | Creates a filter node representing a contains condition with the given string value. Signature ```kotlin fun contains(value: String): ByStringFilterNode ``` Parameters value: String The substring to check for within the string attribute. Returns [ByStringFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bystringfilternode) A filter node representing the contains condition. |
| --- | --- |
| **endsWith** ( value ) | Creates a filter node representing an ends with condition with the given string value. Signature ```kotlin fun endsWith(value: String): ByStringFilterNode ``` Parameters value: String The suffix to check for at the end of the string attribute. Returns [ByStringFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bystringfilternode) A filter node representing the ends with condition. |
| **greaterThan** ( value ) | Creates a filter node representing a greater than condition with the given string value. Signature ```kotlin fun greaterThan(value: String): ByStringFilterNode ``` Parameters value: String The string value to compare against. Returns [ByStringFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bystringfilternode) A filter node representing the greater than condition. |
| **greaterThanOrEqualTo** ( value ) | Creates a filter node representing a greater than or equal to condition with the given string value. Signature ```kotlin fun greaterThanOrEqualTo(value: String): ByStringFilterNode ``` Parameters value: String The string value to compare against. Returns [ByStringFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bystringfilternode) A filter node representing the greater than or equal to condition. |
| **isEqualTo** ( value ) | Creates a filter node representing an equality condition with the given string value. Signature ```kotlin fun isEqualTo(value: String): ByStringFilterNode ``` Parameters value: String The string value to compare against. Returns [ByStringFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bystringfilternode) A filter node representing the equality condition. |
| **isEqualToCaseInsensitive** ( value ) | Creates a filter node representing a case-insensitive equality condition with the given string value. Signature ```kotlin fun isEqualToCaseInsensitive(value: String): ByStringFilterNode ``` Parameters value: String The string value to compare against, ignoring case. Returns [ByStringFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bystringfilternode) A filter node representing the case-insensitive equality condition. |
| **lessThan** ( value ) | Creates a filter node representing a less than condition with the given string value. Signature ```kotlin fun lessThan(value: String): ByStringFilterNode ``` Parameters value: String The string value to compare against. Returns [ByStringFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bystringfilternode) A filter node representing the less than condition. |
| **lessThanOrEqualTo** ( value ) | Creates a filter node representing a less than or equal to condition with the given string value. Signature ```kotlin fun lessThanOrEqualTo(value: String): ByStringFilterNode ``` Parameters value: String The string value to compare against. Returns [ByStringFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bystringfilternode) A filter node representing the less than or equal to condition. |
| **startsWith** ( value ) | Creates a filter node representing a starts with condition with the given string value. Signature ```kotlin fun startsWith(value: String): ByStringFilterNode ``` Parameters value: String The prefix to check for at the beginning of the string attribute. Returns [ByStringFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bystringfilternode) A filter node representing the starts with condition. |