# Vector4Attribute Class

Extends
[TypedAbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_typedabstractattribute)
*Modifiers:
final*

An attribute that stores a Vector4 value.

XML Usage Example:

```kotlin <component name="Velocity">
  <Vector4Attribute name="velocity" defaultValue="0.0 0.0 0.0 1.0" />
</component> ```

## Signature

```kotlin
class Vector4Attribute(keyString: String, key: Int, component: ComponentBase, initialValue: Vector4) : TypedAbstractAttribute<Vector4>
```

## Constructors

| **Vector4Attribute** ( keyString , key , component , initialValue ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase, initialValue: Vector4) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to initialValue: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The initial value for this attribute Returns [Vector4Attribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4attribute) |
| --- | --- |

## Properties

| **value** : WatchedVector4 [Get][Set] | Signature ```kotlin var value: WatchedVector4 ``` |
| --- | --- |

## Functions

| **checkIfComponentIsOld** () | Signature ```kotlin fun checkIfComponentIsOld() ``` |
| --- | --- |
| **checkIfComponentIsRecycled** () | Signature ```kotlin fun checkIfComponentIsRecycled() ``` |
| **get** () | Signature ```kotlin open override fun get(): Any ``` Returns Any |
| **getValue** ( thisRef , property ) | Signature ```kotlin operator fun getValue(thisRef: Any?, property: KProperty<*>): Vector4 ``` Parameters thisRef: Any? property: KProperty Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) |
| **keyName** () | Signature ```kotlin fun keyName(): String ``` Returns String |
| **markDirty** ( potentialValue ) | Signature ```kotlin fun markDirty(potentialValue: WatchedVector4) ``` Parameters potentialValue: WatchedVector4 |
| **set** ( value ) | Signature ```kotlin open override fun set(value: Any) ``` Parameters value: Any |
| **setValue** ( thisRef , property , value ) | Signature ```kotlin operator fun setValue(thisRef: Any?, property: KProperty<*>, value: Vector4) ``` Parameters thisRef: Any? property: KProperty value: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) |