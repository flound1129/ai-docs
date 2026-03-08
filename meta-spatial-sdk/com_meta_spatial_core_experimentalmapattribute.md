# ExperimentalMapAttribute Class

Implements
[AbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_abstractattribute)
*Modifiers:
final*

An attribute that stores a map of key-value pairs.

XML Usage Example:

```kotlin <component name="Properties">
  <ExperimentalMapAttribute name="settings" keyType="String" valueType="Int" />
</component> ```

## Signature

```kotlin
class ExperimentalMapAttribute<KeyT, ValT>(keyString: String, key: Int, component: ComponentBase) : AbstractAttribute
```

## Constructors

| **ExperimentalMapAttribute** ( keyString , key , component ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to Returns [ExperimentalMapAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_experimentalmapattribute) |
| --- | --- |

## Properties

| **map** : mutableMapOf<KeyT, ValT>() [Get][Set] | Signature ```kotlin var map: mutableMapOf<KeyT, ValT>() ``` |
| --- | --- |
| **mapDelegate** : MapDelegate [Get][Set] | Signature ```kotlin var mapDelegate: MapDelegate<KeyT, ValT> ``` |

## Functions

| **get** () | Signature ```kotlin open override fun get(): Any ``` Returns Any |
| --- | --- |
| **getValue** ( thisRef , property ) | Signature ```kotlin operator fun getValue(thisRef: Any?, property: KProperty<*>): MapDelegate<KeyT, ValT> ``` Parameters thisRef: Any? property: KProperty Returns MapDelegate |
| **set** ( value ) | Signature ```kotlin open override fun set(value: Any) ``` Parameters value: Any |
| **setValue** ( thisRef , property , value ) | Signature ```kotlin operator fun setValue(thisRef: Any?, property: KProperty<*>, value: MapDelegate<KeyT, ValT>) ``` Parameters thisRef: Any? property: KProperty value: MapDelegate |