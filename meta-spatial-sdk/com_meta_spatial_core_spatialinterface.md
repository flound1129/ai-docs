# SpatialInterface Class

*Modifiers:
open*

Core interface between the Spatial SDK's Kotlin layer and the native C++ implementation.

SpatialInterface provides access to the underlying native functionality through JNI. It handles initialization, destruction, and the execution of various subsystems including:

- Physics simulation - Animation - Input (controllers and hands) - Transformation systems - Data model synchronization

This class is typically instantiated and managed by VrActivity or its subclasses, which handle the proper sequencing of method calls throughout the application lifecycle.

## Signature

```kotlin
open class SpatialInterface
```

## Constructors

| **SpatialInterface** () | Signature ```kotlin constructor() ``` Returns [SpatialInterface](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_spatialinterface) |
| --- | --- |

## Properties

| **appPtr_** : Long [Get] | Pointer to the native application instance. This is set during initialization and used for all native method calls. Signature ```kotlin var appPtr_: Long ``` |
| --- | --- |
| **dataModel** : [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) [Get] | The data model associated with this spatial interface. Contains the entity-component data for the application. Signature ```kotlin lateinit var dataModel: DataModel ``` |

## Functions

| **applyHapticFeedback** ( hand , amplitude , duration , frequency ) | Applies the given haptic feedback to both controllers. This method triggers haptic feedback (vibration) on the specified controller, allowing for tactile feedback in response to user interactions. Signature ```kotlin fun applyHapticFeedback(hand: Hand, amplitude: Float, duration: Long, frequency: Float) ``` Parameters hand: [Hand](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_hand) Apply haptics to the specified controller hand. amplitude: Float Value between 0 - 1 for strength of haptics. duration: Long Time in nanoseconds for how long the haptic feedback should be applied. frequency: Float Frequency of vibration (in hz). |
| --- | --- |
| **enableAABBDebugLines** ( enabled ) | Toggles debug lines for AABB(Axis Aligned Bounding Boxes) around each scene object. This is useful for visualizing the spatial extents of objects in the scene and understanding collision boundaries. Signature ```kotlin fun enableAABBDebugLines(enabled: Boolean) ``` Parameters enabled: Boolean Whether to enable or disable AABB debug lines. |
| **enableInput** ( enabled ) | Controls whether input (controllers and hands) are enabled. This method can be used to temporarily disable input processing. Signature ```kotlin fun enableInput(enabled: Boolean) ``` Parameters enabled: Boolean Whether input should be enabled or disabled. |
| **setPerformanceLevel** ( level ) | Set the performance level for both CPU and GPU. This allows developers to control the performance level of the device. Higher performance levels provide better performance but consume more power. Example usage: ```kotlin // Set to boost mode during intensive operations spatial.setPerformanceLevel(PerformanceLevel.BOOST_HINT) // Disable boost by setting back to default (SUSTAIN_HIGH) spatial.setPerformanceLevel(PerformanceLevel.SUSTAIN_HIGH) // Set to sustained low mode to preserve battery life spatial.setPerformanceLevel(PerformanceLevel.SUSTAINED_LOW) ``` Signature ```kotlin fun setPerformanceLevel(level: PerformanceLevel): Boolean ``` Parameters level: [PerformanceLevel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_performancelevel) The performance level to set for both CPU and GPU. Returns Boolean true if the operation was successful, false otherwise. |