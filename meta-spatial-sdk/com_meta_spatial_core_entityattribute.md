# EntityAttribute Class

Extends
[TypedAbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_typedabstractattribute)
*Modifiers:
final*

An attribute that stores an Entity reference.

XML Usage Example (Entity references are typically set programmatically rather than through XML default values):

```kotlin <component name="Relationship">
  <EntityAttribute name="target" />
</component> ```

## Signature

```kotlin
class EntityAttribute(keyString: String, key: Int, component: ComponentBase, initialValue: Entity) : TypedAbstractAttribute<Entity>
```

## Constructors

| **EntityAttribute** ( keyString , key , component , initialValue ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase, initialValue: Entity) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to initialValue: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The initial value for this attribute Returns [EntityAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entityattribute) |
| --- | --- |

## Properties

| **value** : [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get][Set] | Signature ```kotlin var value: Entity ``` |
| --- | --- |

## Functions

| **checkIfComponentIsOld** () | Signature ```kotlin fun checkIfComponentIsOld() ``` |
| --- | --- |
| **checkIfComponentIsRecycled** () | Signature ```kotlin fun checkIfComponentIsRecycled() ``` |
| **get** () | Signature ```kotlin open override fun get(): Any ``` Returns Any |
| **getValue** ( thisRef , property ) | Signature ```kotlin operator fun getValue(thisRef: Any?, property: KProperty<*>): Entity ``` Parameters thisRef: Any? property: KProperty Returns [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **keyName** () | Signature ```kotlin fun keyName(): String ``` Returns String |
| **set** ( value ) | Signature ```kotlin open override fun set(value: Any) ``` Parameters value: Any |
| **setValue** ( thisRef , property , value ) | Signature ```kotlin operator fun setValue(thisRef: Any?, property: KProperty<*>, value: Entity) ``` Parameters thisRef: Any? property: KProperty value: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |