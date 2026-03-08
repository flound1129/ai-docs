# AttributeInfo Class

*Modifiers:
final*

Data Class that holds printable data of registered attributes. Used in ComponentManager.

## Signature

```kotlin
data class AttributeInfo(val type: RegisteredAttributeType, val name: String, val componentId: Int, val enumClass: Class<out Enum<*>>? = null)
```

## Constructors

| **AttributeInfo** ( type , name , componentId , enumClass ) | Signature ```kotlin constructor(type: RegisteredAttributeType, name: String, componentId: Int, enumClass: Class<out Enum<*>>? = null) ``` Parameters type: RegisteredAttributeType name: String componentId: Int enumClass: Class? Returns [AttributeInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_attributeinfo) |
| --- | --- |

## Properties

| **componentId** : Int [Get] | Signature ```kotlin val componentId: Int ``` |
| --- | --- |
| **enumClass** : Class? [Get] | Signature ```kotlin val enumClass: Class<out Enum<*>>? = null ``` |
| **name** : String [Get] | Signature ```kotlin val name: String ``` |
| **type** : RegisteredAttributeType [Get] | Signature ```kotlin val type: RegisteredAttributeType ``` |