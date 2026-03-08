# FeatureManager Class

*Modifiers:
final*

Manages a collection of [SpatialFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature) instances for your Spatial SDK activity.

The FeatureManager is responsible for:

- Storing and providing access to registered features - Managing feature lifecycle events - Checking feature dependencies - Registering components and systems from features

Example usage of registering features:

```kotlin // ImmersiveActivity.kt (your immersive Spatial SDK activity)
override fun registerFeatures(): List<SpatialFeature> {
  return listOf(
    VRFeature(),
    IsdkFeature(),
    PhysicsFeature())
} ```

Example usage of accessing features:

```kotlin // ImmersiveActivity.kt (your immersive Spatial SDK activity)
fun myHelperFunction() {
  val toolkitFeature = featureManager.tryFindFeature<ToolkitFeature>()
  ...
} ```

## Signature

```kotlin
class FeatureManager(val features: List<SpatialFeature>)
```

## Constructors

| **FeatureManager** ( features ) | Signature ```kotlin constructor(features: List<SpatialFeature>) ``` Parameters features: List The list of SpatialFeature instances managed by this FeatureManager Returns [FeatureManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_featuremanager) |
| --- | --- |

## Properties

| **features** : List [Get] | The list of SpatialFeature instances managed by this FeatureManager Signature ```kotlin val features: List<SpatialFeature> ``` |
| --- | --- |

## Functions

| **findFeature** ( clazz ) | Finds a [SpatialFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature) of the specified type or throws an exception if not found. Signature ```kotlin fun <T : SpatialFeature> findFeature(clazz: KClass<T>): T ``` Parameters clazz: KClass The KClass of the feature to find Returns [FeatureManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_featuremanager) The found feature instance Throws Exception if the feature is not found |
| --- | --- |
| **findFeature** () | Finds a feature of the specified [SpatialFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature) class or throws an exception if not found. Signature ```kotlin inline fun <T : SpatialFeature> findFeature(): T ``` Returns [FeatureManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_featuremanager) The found feature instance Throws Exception if the feature is not found |
| **tryFindFeature** ( clazz ) | Attempts to find a [SpatialFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature) of the specified type, or null if no matching feature is found. Signature ```kotlin fun <T : SpatialFeature> tryFindFeature(clazz: KClass<T>): T? ``` Parameters clazz: KClass The KClass of the feature to find Returns [FeatureManager?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_featuremanager) The found feature instance, or null if not found |
| **tryFindFeature** () | Attempts to find a feature of the specified [SpatialFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialfeature) class. Signature ```kotlin inline fun <T : SpatialFeature> tryFindFeature(): T? ``` Returns [FeatureManager?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_featuremanager) The found feature instance, or null if not found |