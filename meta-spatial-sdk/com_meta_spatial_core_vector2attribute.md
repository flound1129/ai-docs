# Vector2Attribute Class

Extends
[TypedAbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_typedabstractattribute)
*Modifiers:
final*

An attribute that stores a Vector2 value.

XML Usage Example:

```kotlin <component name="2DCoordinates">
<Vector2Attribute name="coords" defaultValue="0.0 0.0" />
</component> ```

## Signature

```kotlin
class Vector2Attribute(keyString: String, key: Int, component: ComponentBase, initialValue: Vector2) : TypedAbstractAttribute<Vector2>
```

## Constructors

| **Vector2Attribute** ( keyString , key , component , initialValue ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase, initialValue: Vector2) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to initialValue: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The initial value for this attribute Returns [Vector2Attribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2attribute) |
| --- | --- |

## Properties

| **value** : WatchedVector2 [Get][Set] | Signature ```kotlin var value: WatchedVector2 ``` |
| --- | --- |

## Functions

| **checkIfComponentIsOld** () | Signature ```kotlin fun checkIfComponentIsOld() ``` |
| --- | --- |
| **checkIfComponentIsRecycled** () | Signature ```kotlin fun checkIfComponentIsRecycled() ``` |
| **get** () | Signature ```kotlin open override fun get(): Any ``` Returns Any |
| **getValue** ( thisRef , property ) | Signature ```kotlin operator fun getValue(thisRef: Any?, property: KProperty<*>): Vector2 ``` Parameters thisRef: Any? property: KProperty Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) |
| **keyName** () | Signature ```kotlin fun keyName(): String ``` Returns String |
| **markDirty** ( potentialValue ) | Signature ```kotlin fun markDirty(potentialValue: WatchedVector2) ``` Parameters potentialValue: WatchedVector2 |
| **set** ( value ) | Signature ```kotlin open override fun set(value: Any) ``` Parameters value: Any |
| **setValue** ( thisRef , property , value ) | Signature ```kotlin operator fun setValue(thisRef: Any?, property: KProperty<*>, value: Vector2) ``` Parameters thisRef: Any? property: KProperty value: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) |