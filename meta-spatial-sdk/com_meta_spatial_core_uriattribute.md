# URIAttribute Class

Extends
[TypedAbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_typedabstractattribute)
*Modifiers:
final*

An attribute that stores a URI value.

XML Usage Example:

```kotlin <component name="Asset">
<URIAttribute name="assetUri" defaultValue="apk:///models/cube.glb" />
</component> ```

## Constructors

| **URIAttribute** ( keyString , key , component , initialValue ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase, initialValue: Uri) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to initialValue: Uri The initial value for this attribute Returns [URIAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_uriattribute) |
| --- | --- |

## Properties

| **value** : Uri [Get][Set] | Signature ```kotlin var value: Uri ``` |
| --- | --- |

## Functions

| **checkIfComponentIsOld** () | Signature ```kotlin fun checkIfComponentIsOld() ``` |
| --- | --- |
| **checkIfComponentIsRecycled** () | Signature ```kotlin fun checkIfComponentIsRecycled() ``` |
| **get** () | Signature ```kotlin open override fun get(): Any ``` Returns Any |
| **getValue** ( thisRef , property ) | Signature ```kotlin operator fun getValue(thisRef: Any?, property: KProperty<*>): Uri ``` Parameters thisRef: Any? property: KProperty Returns Uri |
| **keyName** () | Signature ```kotlin fun keyName(): String ``` Returns String |
| **set** ( value ) | Signature ```kotlin open override fun set(value: Any) ``` Parameters value: Any |
| **setValue** ( thisRef , property , value ) | Signature ```kotlin operator fun setValue(thisRef: Any?, property: KProperty<*>, value: Uri) ``` Parameters thisRef: Any? property: KProperty value: Uri |