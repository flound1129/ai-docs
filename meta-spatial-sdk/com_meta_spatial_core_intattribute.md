# IntAttribute Class

Extends
[TypedAbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_typedabstractattribute)
*Modifiers:
final*

An attribute that stores an Int value.

XML Usage Example:

```kotlin <component name="Counter">
  <IntAttribute name="score" defaultValue="0" />
</component> ```

## Signature

```kotlin
class IntAttribute(keyString: String, key: Int, component: ComponentBase, initialValue: Int) : TypedAbstractAttribute<Int>
```

## Constructors

| **IntAttribute** ( keyString , key , component , initialValue ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase, initialValue: Int) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to initialValue: Int The initial value for this attribute Returns [IntAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattribute) |
| --- | --- |

## Properties

| **value** : Int [Get][Set] | Signature ```kotlin var value: Int ``` |
| --- | --- |

## Functions

| **checkIfComponentIsOld** () | Signature ```kotlin fun checkIfComponentIsOld() ``` |
| --- | --- |
| **checkIfComponentIsRecycled** () | Signature ```kotlin fun checkIfComponentIsRecycled() ``` |
| **get** () | Signature ```kotlin open override fun get(): Any ``` Returns Any |
| **getValue** ( thisRef , property ) | Signature ```kotlin operator fun getValue(thisRef: Any?, property: KProperty<*>): Int ``` Parameters thisRef: Any? property: KProperty Returns Int |
| **keyName** () | Signature ```kotlin fun keyName(): String ``` Returns String |
| **set** ( value ) | Signature ```kotlin open override fun set(value: Any) ``` Parameters value: Any |
| **setValue** ( thisRef , property , value ) | Signature ```kotlin operator fun setValue(thisRef: Any?, property: KProperty<*>, value: Int) ``` Parameters thisRef: Any? property: KProperty value: Int |