# UUIDAttribute Class

Extends
[TypedAbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_typedabstractattribute)
*Modifiers:
final*

An attribute that stores a UUID value.

XML Usage Example:

```kotlin <component name="Identifier">
 <UUIDAttribute name="id" defaultValue="-1L,1L"/>
</component> ```

## Signature

```kotlin
class UUIDAttribute(keyString: String, key: Int, component: ComponentBase, initialValue: UUID) : TypedAbstractAttribute<UUID>
```

## Constructors

| **UUIDAttribute** ( keyString , key , component , initialValue ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase, initialValue: UUID) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to initialValue: UUID The initial value for this attribute Returns [UUIDAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_uuidattribute) |
| --- | --- |

## Properties

| **value** : UUID [Get][Set] | Signature ```kotlin var value: UUID ``` |
| --- | --- |

## Functions

| **checkIfComponentIsOld** () | Signature ```kotlin fun checkIfComponentIsOld() ``` |
| --- | --- |
| **checkIfComponentIsRecycled** () | Signature ```kotlin fun checkIfComponentIsRecycled() ``` |
| **get** () | Signature ```kotlin open override fun get(): Any ``` Returns Any |
| **getValue** ( thisRef , property ) | Signature ```kotlin operator fun getValue(thisRef: Any?, property: KProperty<*>): UUID ``` Parameters thisRef: Any? property: KProperty Returns UUID |
| **keyName** () | Signature ```kotlin fun keyName(): String ``` Returns String |
| **set** ( value ) | Signature ```kotlin open override fun set(value: Any) ``` Parameters value: Any |
| **setValue** ( thisRef , property , value ) | Signature ```kotlin operator fun setValue(thisRef: Any?, property: KProperty<*>, value: UUID) ``` Parameters thisRef: Any? property: KProperty value: UUID |