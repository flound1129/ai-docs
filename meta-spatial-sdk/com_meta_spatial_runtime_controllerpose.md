# ControllerPose Class

*Modifiers:
final*

Experimental api that represents a controller's pose with additional tracking state information.

The tracking state is represented as bit flags in the [ControllerPose.flags](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_controllerpose#flags) property, which can be checked using the bit constants defined in the companion object.

Example usage:

```kotlin // Get the controller pose
val controllerPose = scene.getControllerPoseAtTime(isLeftHand, timestamp)
// Check if position data is valid and tracked
val isPositionValid = (controllerPose.flags and ControllerPose.LocationValidBit) != 0
val isPositionTracked = (controllerPose.flags and ControllerPose.LocationTrackedBit) != 0
// Check if orientation data is valid and tracked
val isOrientationValid = (controllerPose.flags and ControllerPose.OrientationValidBit) != 0
val isOrientationTracked = (controllerPose.flags and ControllerPose.OrientationTrackedBit) != 0
// Check if both position and orientation are valid
val isPoseValid = (controllerPose.flags and ControllerPose.ValidBits) == ControllerPose.ValidBits
// Check if both position and orientation are tracked
val isPoseTracked = (controllerPose.flags and ControllerPose.TrackedBits) == ControllerPose.TrackedBits ```

## Signature

```kotlin
data class ControllerPose(val pose: Pose, val flags: Int)
```

## Constructors

| **ControllerPose** ( pose , flags ) | Signature ```kotlin constructor(pose: Pose, flags: Int) ``` Parameters pose: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The position and orientation of the controller flags: Int Bit flags indicating the tracking state of the controller Returns [ControllerPose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_controllerpose) |
| --- | --- |

## Properties

| **flags** : Int [Get] | Bit flags indicating the tracking state of the controller Signature ```kotlin val flags: Int ``` |
| --- | --- |
| **pose** : [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) [Get] | The position and orientation of the controller Signature ```kotlin val pose: Pose ``` |

## Companion Object

### Companion Object Properties

| **LocationTrackedBit** : Int [Get] | Bit flag indicating that the controller's position (location) is actively tracked. When this bit is set, the position is being updated in real-time by the tracking system. Signature ```kotlin const val LocationTrackedBit: Int = 2 ``` |
| --- | --- |
| **LocationValidBit** : Int [Get] | Bit flag indicating that the controller's position (location) is valid. When this bit is set, the position data in the pose can be considered reliable. Signature ```kotlin const val LocationValidBit: Int = 1 ``` |
| **OrientationTrackedBit** : Int [Get] | Bit flag indicating that the controller's orientation is actively tracked. When this bit is set, the orientation is being updated in real-time by the tracking system. Signature ```kotlin const val OrientationTrackedBit: Int = 8 ``` |
| **OrientationValidBit** : Int [Get] | Bit flag indicating that the controller's orientation is valid. When this bit is set, the orientation data in the pose can be considered reliable. Signature ```kotlin const val OrientationValidBit: Int = 4 ``` |
| **TrackedBits** : Int [Get] | Combined bit mask for checking if both position and orientation are actively tracked. Use this to check if the entire pose (position and orientation) is being tracked in real-time. Signature ```kotlin const val TrackedBits: Int ``` |
| **ValidBits** : Int [Get] | Combined bit mask for checking if both position and orientation are valid. Use this to check if the entire pose (position and orientation) is valid. Signature ```kotlin const val ValidBits: Int ``` |