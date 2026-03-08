# Quaternion Class

*Modifiers:
open*

Quaternion class for representing 3D rotations.

This class provides methods for creating quaternions from various sources, such as pitch, yaw, and roll angles, rotation matrices, and random values. Provides operator overloading for unary minus and multiplication with other quaternions and vectors. Example Usage:

Creating a quaternion from pitch, yaw, and roll: ---

val quaternion = Quaternion(pitch = 30f, yaw = 45f, roll = 60f) println(quaternion) // Outputs the quaternion representation

Multiplying two quaternions: ---

val q1 = Quaternion(1f, 0f, 0f, 0f) val q2 = Quaternion(0f, 1f, 0f, 0f) val result = q1 * q2 println(result) // Outputs the resulting quaternion

Converting a quaternion to Euler angles: ---

val eulerAngles = quaternion.toEuler() println(eulerAngles) // Outputs the Euler angles (pitch, yaw, roll)

Normalizing a quaternion: ---

val normalizedQuaternion = quaternion.normalize() println(normalizedQuaternion) // Outputs the normalized quaternion

## Signature

```kotlin
open class Quaternion(var w: Float = 1.0f, var x: Float = 0.0f, var y: Float = 0.0f, var z: Float = 0.0f)
```

## Constructors

| **Quaternion** ( pitch , yaw , roll ) | Constructor for creating a quaternion from pitch, yaw, and roll angles. Signature ```kotlin constructor(pitch: Float, yaw: Float, roll: Float) ``` Parameters pitch: Float The pitch angle in degrees. yaw: Float The yaw angle in degrees. roll: Float The roll angle in degrees. Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) |
| --- | --- |
| **Quaternion** ( w , x , y , z ) | Signature ```kotlin constructor(w: Float = 1.0f, x: Float = 0.0f, y: Float = 0.0f, z: Float = 0.0f) ``` Parameters w: Float w component of the quaternion. x: Float x component of the quaternion. y: Float y component of the quaternion. z: Float z component of the quaternion. Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) |

## Properties

| **w** : Float [Get][Set] | w component of the quaternion. Signature ```kotlin open var w: Float ``` |
| --- | --- |
| **x** : Float [Get][Set] | x component of the quaternion. Signature ```kotlin open var x: Float ``` |
| **y** : Float [Get][Set] | y component of the quaternion. Signature ```kotlin open var y: Float ``` |
| **z** : Float [Get][Set] | z component of the quaternion. Signature ```kotlin open var z: Float ``` |

## Functions

| **component1** () | Signature ```kotlin operator fun component1(): Float ``` Returns Float |
| --- | --- |
| **component2** () | Signature ```kotlin operator fun component2(): Float ``` Returns Float |
| **component3** () | Signature ```kotlin operator fun component3(): Float ``` Returns Float |
| **component4** () | Signature ```kotlin operator fun component4(): Float ``` Returns Float |
| **conjugate** () | Calculates the conjugate of the quaternion. Signature ```kotlin fun conjugate(): Quaternion ``` Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The conjugate of the quaternion. |
| **copy** () | Returns a copy of this Quaternion. Signature ```kotlin fun copy(): Quaternion ``` Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A copy of this Quaternion. |
| **dot** ( other ) | Calculates the dot product of two quaternions. Signature ```kotlin fun dot(other: Quaternion): Float ``` Parameters other: [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The other quaternion to calculate the dot product with. Returns Float The dot product of the two quaternions. |
| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |
| **inverse** () | Calculates the inverse of the quaternion. Signature ```kotlin fun inverse(): Quaternion ``` Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The inverse of the quaternion. |
| **isWithinAngle** ( other , angleRadians ) | Checks if the angular distance between this quaternion and another quaternion is within a specified tolerance in radians. This method uses the industry-standard approach for comparing quaternion orientations: computing the angular distance between the two rotations using the dot product. It correctly handles the q vs -q equivalence (both represent the same rotation). Note: This assumes both quaternions are normalized. For best results, normalize quaternions before comparison. Signature ```kotlin fun isWithinAngle(other: Quaternion, angleRadians: Float): Boolean ``` Parameters other: [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The other quaternion to compare with. angleRadians: Float The maximum allowed angular difference in radians. Returns Boolean True if the angular distance between the two quaternions is less than or equal to angleRadians. |
| **isWithinAngleDegrees** ( other , angleDegrees ) | Checks if the angular distance between this quaternion and another quaternion is within a specified tolerance in degrees. This method uses the industry-standard approach for comparing quaternion orientations: computing the angular distance between the two rotations using the dot product. It correctly handles the q vs -q equivalence (both represent the same rotation). Note: This assumes both quaternions are normalized. For best results, normalize quaternions before comparison. Signature ```kotlin fun isWithinAngleDegrees(other: Quaternion, angleDegrees: Float): Boolean ``` Parameters other: [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The other quaternion to compare with. angleDegrees: Float The maximum allowed angular difference in degrees. Returns Boolean True if the angular distance between the two quaternions is less than or equal to angleDegrees. |
| **nlerp** ( dest , ratio ) | Performs normalized linear interpolation between the current quaternion and the destination quaternion. Signature ```kotlin fun nlerp(dest: Quaternion, ratio: Float): Quaternion ``` Parameters dest: [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The destination quaternion to interpolate towards. ratio: Float The interpolation ratio, where 0 means no interpolation (i.e., the current quaternion) and 1 means full interpolation (i.e., the destination quaternion). Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A new quaternion that is the result of interpolating between the current quaternion and the destination quaternion by the given ratio. |
| **norm** () | Calculates the squared magnitude (length) of the quaternion. Signature ```kotlin fun norm(): Float ``` Returns Float The squared magnitude of the quaternion. |
| **normalize** () | Normalizes the quaternion to have a magnitude of 1. Signature ```kotlin fun normalize(): Quaternion ``` Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The normalized quaternion. |
| **removePitchAndRoll** () | Removes the pitch and roll components from the quaternion, leaving only the yaw component. Signature ```kotlin fun removePitchAndRoll(): Quaternion ``` Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A new quaternion with the pitch and roll components removed. |
| **slerp** ( dest , ratio ) | Performs spherical linear interpolation between the current quaternion and the destination quaternion. Signature ```kotlin fun slerp(dest: Quaternion, ratio: Float): Quaternion ``` Parameters dest: [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The destination quaternion to interpolate towards. ratio: Float The interpolation ratio, where 0 means no interpolation (i.e., the current quaternion) and 1 means full interpolation (i.e., the destination quaternion). Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A new quaternion that is the result of interpolating between the current quaternion and the destination quaternion by the given ratio. |
| **times** ( q ) | Multiplies this quaternion with another quaternion. Signature ```kotlin inline operator fun times(q: Quaternion): Quaternion ``` Parameters q: [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The other quaternion to multiply with. Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The resulting quaternion. |
| **times** ( v ) | Multiplies this quaternion with a vector. Signature ```kotlin inline operator fun times(v: Vector3): Vector3 ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The vector to multiply with. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The resulting vector. |
| **toEuler** () | Converts the quaternion to Euler angles (pitch, yaw, roll). Signature ```kotlin fun toEuler(): Vector3 ``` Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) A 3D vector representing the Euler angles. |
| **toRotationMatrix44** () | Converts the quaternion to a 4x4 rotation matrix. Signature ```kotlin fun toRotationMatrix44(): Matrix44 ``` Returns [Matrix44](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_matrix44) A 4x4 rotation matrix representing the quaternion. |
| **toString** () | Signature ```kotlin open override fun toString(): String ``` Returns String |
| **toVector4** () | Converts the quaternion to a 4D vector. Signature ```kotlin fun toVector4(): Vector4 ``` Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) A 4D vector representing the quaternion. |
| **unaryMinus** () | Negates the quaternion. Signature ```kotlin inline operator fun unaryMinus(): Quaternion ``` Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) |

## Companion Object

### Companion Object Functions

| **fromAxisAngle** ( axis , angleDegrees ) | Creates a quaternion representing a rotation around an axis by a specified angle. Signature ```kotlin fun fromAxisAngle(axis: Vector3, angleDegrees: Float): Quaternion ``` Parameters axis: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The axis of rotation (will be normalized internally). angleDegrees: Float The angle of rotation in degrees. Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A quaternion representing the rotation. |
| --- | --- |
| **fromAxisAngleRadians** ( axis , angleRadians ) | Creates a quaternion representing a rotation around an axis by a specified angle in radians. Signature ```kotlin fun fromAxisAngleRadians(axis: Vector3, angleRadians: Float): Quaternion ``` Parameters axis: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The axis of rotation (will be normalized internally). angleRadians: Float The angle of rotation in radians. Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A quaternion representing the rotation. |
| **fromDirection** ( dirX , dirY , dirZ , upX , upY , upZ ) | Creates a quaternion that rotates the +Z axis to point in the given direction. Uses a lookAt-style approach consistent with GLM's quatLookAtLH. The resulting quaternion, when applied to a vector pointing in the +Z direction, will rotate it to align with the specified direction. Signature ```kotlin fun fromDirection(dirX: Float, dirY: Float, dirZ: Float, upX: Float = 0.0f, upY: Float = 1.0f, upZ: Float = 0.0f): Quaternion ``` Parameters dirX: Float The x component of the target direction. dirY: Float The y component of the target direction. dirZ: Float The z component of the target direction. upX: Float The x component of the up vector (default: 0). upY: Float The y component of the up vector (default: 1). upZ: Float The z component of the up vector (default: 0). Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A quaternion that rotates +Z to the given direction. |
| **fromDirection** ( direction , up ) | Creates a quaternion that rotates the +Z axis to point in the given direction. Signature ```kotlin fun fromDirection(direction: Vector3, up: Vector3 = Vector3.Up): Quaternion ``` Parameters direction: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The target direction vector. up: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The up vector (default: Vector3.Up). Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A quaternion that rotates +Z to the given direction. |
| **fromEuler** ( pitch , yaw , roll ) | Creates a quaternion from Euler angles (pitch, yaw, roll). Signature ```kotlin fun fromEuler(pitch: Float, yaw: Float, roll: Float): Quaternion ``` Parameters pitch: Float The pitch angle in degrees (rotation around X-axis). yaw: Float The yaw angle in degrees (rotation around Y-axis). roll: Float The roll angle in degrees (rotation around Z-axis). Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A quaternion representing the combined rotation. |
| **fromEuler** ( euler ) | Creates a quaternion from a Vector3 containing Euler angles (pitch, yaw, roll). Signature ```kotlin fun fromEuler(euler: Vector3): Quaternion ``` Parameters euler: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) A Vector3 where x=pitch, y=yaw, z=roll (all in degrees). Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A quaternion representing the combined rotation. |
| **fromRotationMatrix** ( matrix ) | Creates a quaternion from a rotation matrix. Signature ```kotlin fun fromRotationMatrix(matrix: Array<FloatArray>): Quaternion ``` Parameters matrix: Array The rotation matrix to create the quaternion from. Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) The resulting quaternion. |
| **fromTwoVectors** ( from , to ) | Creates a quaternion that rotates one vector to another. Signature ```kotlin fun fromTwoVectors(from: Vector3, to: Vector3): Quaternion ``` Parameters from: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The starting direction vector (will be normalized internally). to: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The target direction vector (will be normalized internally). Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A quaternion representing the rotation from 'from' to 'to'. |
| **getRandomQuat** () | Formula using "Choosing a Point from the Surface of a Sphere" authored by George Marsaglia Generates uniform random quaternion. Signature ```kotlin fun getRandomQuat(): Quaternion ``` Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A random quaternion. |
| **lookRotation** ( forward , lookUp ) | Creates a quaternion that represents a rotation from the forward vector to the look-up vector. Signature ```kotlin fun lookRotation(forward: Vector3, lookUp: Vector3 = Vector3.Up): Quaternion ``` Parameters forward: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The forward vector. lookUp: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The look-up vector. Defaults to Vector3.Up. Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A quaternion representing the rotation from the forward vector to the look-up vector. |
| **lookRotationAroundY** ( forward ) | Creates a quaternion that represents a rotation around the Y-axis from the forward vector to the look-up vector. Signature ```kotlin fun lookRotationAroundY(forward: Vector3): Quaternion ``` Parameters forward: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The forward vector. Returns [Quaternion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_quaternion) A quaternion representing the rotation around the Y-axis from the forward vector to the look-up vector. |