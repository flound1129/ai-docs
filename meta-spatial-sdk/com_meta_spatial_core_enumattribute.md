# EnumAttribute Class

Extends
[TypedAbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_typedabstractattribute)
*Modifiers:
final*

An attribute that stores an Enum value.

XML Usage Example:

```kotlin <component name="Player">
  <EnumAttribute name="playerType" enumType="PlayerType" defaultValue="HUMAN" />
</component> ```

Enums should be defined like this:

```kotlin <Enum name="MyEnum">
  <EnumValue value="ENUM_VALUE_1" />
  <EnumValue value="ENUM_VALUE_2" />
</Enum> ```

## Signature

```kotlin
class EnumAttribute<T : Enum<T>>(keyString: String, key: Int, component: ComponentBase, enumClass: Class<T>, initialValue: T) : TypedAbstractAttribute<T>
```

## Constructors

| **EnumAttribute** ( keyString , key , component , enumClass , initialValue ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase, enumClass: Class<T>, initialValue: T) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to enumClass: Class The class object for the enum type initialValue: [EnumAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattribute) The initial value for this attribute Returns [EnumAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattribute) |
| --- | --- |

## Properties

| **value** : [EnumAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattribute) [Get][Set] | Signature ```kotlin var value: T ``` |
| --- | --- |

## Functions

| **checkIfComponentIsOld** () | Signature ```kotlin fun checkIfComponentIsOld() ``` |
| --- | --- |
| **checkIfComponentIsRecycled** () | Signature ```kotlin fun checkIfComponentIsRecycled() ``` |
| **get** () | Signature ```kotlin open override fun get(): Any ``` Returns Any |
| **getValue** ( thisRef , property ) | Signature ```kotlin operator fun getValue(thisRef: Any?, property: KProperty<*>): T ``` Parameters thisRef: Any? property: KProperty Returns [EnumAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattribute) |
| **keyName** () | Signature ```kotlin fun keyName(): String ``` Returns String |
| **set** ( value ) | Signature ```kotlin open override fun set(value: Any) ``` Parameters value: Any |
| **setValue** ( thisRef , property , value ) | Signature ```kotlin operator fun setValue(thisRef: Any?, property: KProperty<*>, value: T) ``` Parameters thisRef: Any? property: KProperty value: [EnumAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattribute) |