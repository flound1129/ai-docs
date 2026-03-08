# Vector3Attribute Class

Extends
[TypedAbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_typedabstractattribute)
*Modifiers:
final*

An attribute that stores a Vector3 value.

XML Usage Example:

```kotlin <component name="3DCoordinates">
  <Vector3Attribute name="position" defaultValue="0.0 0.0 0.0" />
</component> ```

## Signature

```kotlin
class Vector3Attribute(keyString: String, key: Int, component: ComponentBase, initialValue: Vector3) : TypedAbstractAttribute<Vector3>
```

## Constructors

| **Vector3Attribute** ( keyString , key , component , initialValue ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase, initialValue: Vector3) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to initialValue: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The initial value for this attribute Returns [Vector3Attribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3attribute) |
| --- | --- |

## Properties

| **value** : WatchedVector3 [Get][Set] | Signature ```kotlin var value: WatchedVector3 ``` |
| --- | --- |

## Functions

| **checkIfComponentIsOld** () | Signature ```kotlin fun checkIfComponentIsOld() ``` |
| --- | --- |
| **checkIfComponentIsRecycled** () | Signature ```kotlin fun checkIfComponentIsRecycled() ``` |
| **get** () | Signature ```kotlin open override fun get(): Any ``` Returns Any |
| **getValue** ( thisRef , property ) | Signature ```kotlin operator fun getValue(thisRef: Any?, property: KProperty<*>): Vector3 ``` Parameters thisRef: Any? property: KProperty Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) |
| **keyName** () | Signature ```kotlin fun keyName(): String ``` Returns String |
| **markDirty** ( potentialValue ) | Signature ```kotlin fun markDirty(potentialValue: WatchedVector3) ``` Parameters potentialValue: WatchedVector3 |
| **set** ( value ) | Signature ```kotlin open override fun set(value: Any) ``` Parameters value: Any |
| **setValue** ( thisRef , property , value ) | Signature ```kotlin operator fun setValue(thisRef: Any?, property: KProperty<*>, value: Vector3) ``` Parameters thisRef: Any? property: KProperty value: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) |