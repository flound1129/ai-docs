# Pose Class

*Modifiers:
open*

Represents a pose in 3D space, which includes a position and an orientation.

## Signature

```kotlin
open class Pose(var t: Vector3 = Vector3(0f, 0f, 0f), var q: Quaternion = Quaternion(1.0f, 0f, 0f, 0f))
```

## Constructors

| **Pose** ( t , q ) | Signature ```kotlin constructor(t: Vector3 = Vector3(0f, 0f, 0f), q: Quaternion = Quaternion(1.0f, 0f, 0f, 0f)) ``` Parameters t: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The position vector of the pose. q: [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The orientation quaternion of the pose. Returns [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) |
| --- | --- |

## Properties

| **q** : [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) [Get][Set] | The orientation quaternion of the pose. Signature ```kotlin open var q: Quaternion ``` |
| --- | --- |
| **t** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get][Set] | The position vector of the pose. Signature ```kotlin open var t: Vector3 ``` |

## Functions

| **component1** () | Signature ```kotlin operator fun component1(): Vector3 ``` Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) |
| --- | --- |
| **component2** () | Signature ```kotlin operator fun component2(): Quaternion ``` Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) |
| **copy** () | Returns a copy of this pose. Signature ```kotlin fun copy(): Pose ``` Returns [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) A copy of this pose. |
| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| **forward** () | Calculates the forward direction vector of this pose. Signature ```kotlin fun forward(): Vector3 ``` Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The forward vector. |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |
| **inverse** () | Computes the inverse of this pose. Signature ```kotlin fun inverse(): Pose ``` Returns [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The inverse pose. |
| **isWithinAngle** ( other , angleRadians ) | Checks if the rotation of this pose is within a specified angular distance of another pose's rotation. This method uses the industry-standard approach for comparing quaternion orientations: computing the angular distance between the two rotations using the dot product. It correctly handles the q vs -q equivalence (both represent the same rotation). Signature ```kotlin fun isWithinAngle(other: Pose, angleRadians: Float): Boolean ``` Parameters other: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The other pose to compare with. angleRadians: Float The maximum allowed angular difference in radians. Returns Boolean True if the angular distance between the two pose rotations is less than or equal to angleRadians. |
| **isWithinAngleDegrees** ( other , angleDegrees ) | Checks if the rotation of this pose is within a specified angular distance of another pose's rotation. This method uses the industry-standard approach for comparing quaternion orientations: computing the angular distance between the two rotations using the dot product. It correctly handles the q vs -q equivalence (both represent the same rotation). Signature ```kotlin fun isWithinAngleDegrees(other: Pose, angleDegrees: Float): Boolean ``` Parameters other: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The other pose to compare with. angleDegrees: Float The maximum allowed angular difference in degrees. Returns Boolean True if the angular distance between the two pose rotations is less than or equal to angleDegrees. |
| **isWithinDistance** ( other , distance ) | Checks if the position of this pose is within a specified Euclidean distance of another pose's position. This is the recommended approach for position-based proximity checks in VR/AR applications. Signature ```kotlin fun isWithinDistance(other: Pose, distance: Float): Boolean ``` Parameters other: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The other pose to compare with. distance: Float The maximum allowed Euclidean distance (in meters). Returns Boolean True if the Euclidean distance between the two pose positions is less than or equal to distance. |
| **lerp** ( dest , ratio ) | Interpolates between this pose and another pose. Signature ```kotlin fun lerp(dest: Pose, ratio: Float): Pose ``` Parameters dest: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The destination pose to interpolate towards. ratio: Float The interpolation ratio. Returns [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The interpolated pose. |
| **removePitchAndRoll** () | Removes the pitch and roll components from this pose, effectively aligning it with the up vector. Signature ```kotlin fun removePitchAndRoll(): Pose ``` Returns [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) A new pose with pitch and roll removed. |
| **right** () | Calculates the right direction vector of this pose. Signature ```kotlin fun right(): Vector3 ``` Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The right vector. |
| **times** ( p ) | Multiplies this pose with another pose. Signature ```kotlin inline operator fun times(p: Pose): Pose ``` Parameters p: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The other pose to multiply with. Returns [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) A new pose resulting from the multiplication. |
| **times** ( v ) | Multiplies this pose with a vector. Signature ```kotlin inline operator fun times(v: Vector3): Vector3 ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The vector to multiply with. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The transformed vector. |
| **toString** () | Provides a string representation of the pose. Signature ```kotlin open override fun toString(): String ``` Returns String A string that represents the pose. |
| **up** () | Calculates the up direction vector of this pose. Signature ```kotlin fun up(): Vector3 ``` Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The up vector. |