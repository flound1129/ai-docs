# Color4Attribute Class

Extends
[TypedAbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_typedabstractattribute)
*Modifiers:
final*

An attribute that stores a Color4 value.

XML Usage Example:

```kotlin <component name="Material">
  <Color4Attribute name="color" defaultValue="1.0 1.0 1.0 1.0" />
</component> ```

## Signature

```kotlin
class Color4Attribute(keyString: String, key: Int, component: ComponentBase, initialValue: Color4) : TypedAbstractAttribute<Color4>
```

## Constructors

| **Color4Attribute** ( keyString , key , component , initialValue ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase, initialValue: Color4) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to initialValue: [Color4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_color4) The initial value for this attribute Returns [Color4Attribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_color4attribute) |
| --- | --- |

## Properties

| **value** : WatchedColor4 [Get][Set] | Signature ```kotlin var value: WatchedColor4 ``` |
| --- | --- |

## Functions

| **checkIfComponentIsOld** () | Signature ```kotlin fun checkIfComponentIsOld() ``` |
| --- | --- |
| **checkIfComponentIsRecycled** () | Signature ```kotlin fun checkIfComponentIsRecycled() ``` |
| **get** () | Signature ```kotlin open override fun get(): Any ``` Returns Any |
| **getValue** ( thisRef , property ) | Signature ```kotlin operator fun getValue(thisRef: Any?, property: KProperty<*>): Color4 ``` Parameters thisRef: Any? property: KProperty Returns [Color4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_color4) |
| **keyName** () | Signature ```kotlin fun keyName(): String ``` Returns String |
| **markDirty** ( potentialValue ) | Signature ```kotlin fun markDirty(potentialValue: WatchedColor4) ``` Parameters potentialValue: WatchedColor4 |
| **set** ( value ) | Signature ```kotlin open override fun set(value: Any) ``` Parameters value: Any |
| **setValue** ( thisRef , property , value ) | Signature ```kotlin operator fun setValue(thisRef: Any?, property: KProperty<*>, value: Color4) ``` Parameters thisRef: Any? property: KProperty value: [Color4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_color4) |