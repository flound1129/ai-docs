# PoseAttribute Class

Extends
[TypedAbstractAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_typedabstractattribute)
*Modifiers:
final*

An attribute that stores a Pose value.

XML Usage Example:

```kotlin <component name="MyTransform">
  <PoseAttribute name="worldPose" defaultValue="0.0 0.0 0.0 0.0 0.0 0.0 1.0" />
</component> ```

The pose format is "tx ty tz qx qy qz qw" where:

- tx, ty, tz: Translation components (Vector3) - qx, qy, qz, qw: Rotation components as a Quaternion

## Signature

```kotlin
class PoseAttribute(keyString: String, key: Int, component: ComponentBase, initialValue: Pose) : TypedAbstractAttribute<Pose>
```

## Constructors

| **PoseAttribute** ( keyString , key , component , initialValue ) | Signature ```kotlin constructor(keyString: String, key: Int, component: ComponentBase, initialValue: Pose) ``` Parameters keyString: String The string key for this attribute key: Int The integer key for this attribute component: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) The component this attribute belongs to initialValue: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The initial value for this attribute Returns [PoseAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_poseattribute) |
| --- | --- |

## Properties

| **value** : WatchedPose [Get][Set] | Signature ```kotlin var value: WatchedPose ``` |
| --- | --- |

## Functions

| **checkIfComponentIsOld** () | Signature ```kotlin fun checkIfComponentIsOld() ``` |
| --- | --- |
| **checkIfComponentIsRecycled** () | Signature ```kotlin fun checkIfComponentIsRecycled() ``` |
| **get** () | Signature ```kotlin open override fun get(): Any ``` Returns Any |
| **getValue** ( thisRef , property ) | Signature ```kotlin operator fun getValue(thisRef: Any?, property: KProperty<*>): Pose ``` Parameters thisRef: Any? property: KProperty Returns [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) |
| **keyName** () | Signature ```kotlin fun keyName(): String ``` Returns String |
| **markDirty** ( potentialValue ) | Signature ```kotlin fun markDirty(potentialValue: WatchedPose) ``` Parameters potentialValue: WatchedPose |
| **set** ( value ) | Signature ```kotlin open override fun set(value: Any) ``` Parameters value: Any |
| **setValue** ( thisRef , property , value ) | Signature ```kotlin operator fun setValue(thisRef: Any?, property: KProperty<*>, value: Pose) ``` Parameters thisRef: Any? property: KProperty value: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) |