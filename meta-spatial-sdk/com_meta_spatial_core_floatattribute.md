# FloatAttribute Class

Extends
[TypedAbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_typedabstractattribute)
*Modifiers:
final*

An attribute that stores a Float value.

XML Usage Example:

```kotlin <component name="Player">
  <FloatAttribute name="maxHealth" defaultValue="100.0" />
</component> ```

## Signature

```kotlin
class FloatAttribute(keyString: String, key: Int, component: ComponentBase, initialValue: Float) : TypedAbstractAttribute<Float>
```

## Constructors

| **FloatAttribute** ( keyString , key , component , initialValue ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase, initialValue: Float) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to initialValue: Float The initial value for this attribute Returns [FloatAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattribute) |
| --- | --- |

## Properties

| **value** : Float [Get][Set] | Signature ```kotlin var value: Float ``` |
| --- | --- |

## Functions

| **checkIfComponentIsOld** () | Signature ```kotlin fun checkIfComponentIsOld() ``` |
| --- | --- |
| **checkIfComponentIsRecycled** () | Signature ```kotlin fun checkIfComponentIsRecycled() ``` |
| **get** () | Signature ```kotlin open override fun get(): Any ``` Returns Any |
| **getValue** ( thisRef , property ) | Signature ```kotlin operator fun getValue(thisRef: Any?, property: KProperty<*>): Float ``` Parameters thisRef: Any? property: KProperty Returns Float |
| **keyName** () | Signature ```kotlin fun keyName(): String ``` Returns String |
| **set** ( value ) | Signature ```kotlin open override fun set(value: Any) ``` Parameters value: Any |
| **setValue** ( thisRef , property , value ) | Signature ```kotlin operator fun setValue(thisRef: Any?, property: KProperty<*>, value: Float) ``` Parameters thisRef: Any? property: KProperty value: Float |