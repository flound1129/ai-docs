# Vector3 Class

*Modifiers:
open*

A 3D vector class.

## Signature

```kotlin
open class Vector3(var x: Float, var y: Float, var z: Float)
```

## Constructors

| **Vector3** ( v ) | Constructor for creating a Vector3 with all components set to the same value. Signature ```kotlin constructor(v: Float) ``` Parameters v: Float The value to set for all components. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) |
| --- | --- |
| **Vector3** ( c ) | Constructor for creating a Vector3 from a Color object. Signature ```kotlin constructor(c: Color) ``` Parameters c: Color The Color object to create the Vector3 from. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) |
| **Vector3** ( x , y , z ) | Signature ```kotlin constructor(x: Float, y: Float, z: Float) ``` Parameters x: Float y: Float z: Float Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) |

## Properties

| **x** : Float [Get][Set] | Signature ```kotlin open var x: Float ``` |
| --- | --- |
| **y** : Float [Get][Set] | Signature ```kotlin open var y: Float ``` |
| **z** : Float [Get][Set] | Signature ```kotlin open var z: Float ``` |

## Functions

| **add** ( v ) | Adds two vectors component-wise. Signature ```kotlin inline fun add(v: Vector3): Vector3 ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The vector to add. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The resulting vector. |
| --- | --- |
| **angleBetweenDegrees** ( v ) | Calculates the angle between two vectors in degrees. Signature ```kotlin fun angleBetweenDegrees(v: Vector3): Float ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The other vector to calculate the angle with. Returns Float The angle between the two vectors in degrees. |
| **component1** () | Signature ```kotlin operator fun component1(): Float ``` Returns Float |
| **component2** () | Signature ```kotlin operator fun component2(): Float ``` Returns Float |
| **component3** () | Signature ```kotlin operator fun component3(): Float ``` Returns Float |
| **copy** () | Returns a copy of this vector. Signature ```kotlin fun copy(): Vector3 ``` Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) A copy of this vector. |
| **cross** ( other ) | Calculates the cross product of two vectors. Signature ```kotlin fun cross(other: Vector3): Vector3 ``` Parameters other: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The vector to calculate the cross product with. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The cross product. |
| **distanceTo** ( v ) | Calculates the distance between two vectors. Signature ```kotlin fun distanceTo(v: Vector3): Float ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The other vector to calculate the distance to. Returns Float The distance between the two vectors. |
| **div** ( v ) | Divides a vector by a scalar. Signature ```kotlin inline operator fun div(v: Float): Vector3 ``` Parameters v: Float The scalar to divide by. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The resulting vector. |
| **divide** ( v ) | Divides a vector by a scalar. Signature ```kotlin inline fun divide(v: Float): Vector3 ``` Parameters v: Float The scalar to divide by. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The resulting vector. |
| **dot** ( v ) | Calculates the dot product of two vectors. Signature ```kotlin inline fun dot(v: Vector3): Float ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The vector to calculate the dot product with. Returns Float The dot product. |
| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |
| **isWithinDistance** ( other , distance ) | Checks if this position vector is within a specified Euclidean distance of another position vector. This method uses squared distance internally for performance, avoiding a square root calculation. This is the recommended approach for position-based proximity checks in VR/AR applications. Signature ```kotlin fun isWithinDistance(other: Vector3, distance: Float): Boolean ``` Parameters other: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The other position vector to compare with. distance: Float The maximum allowed Euclidean distance (in meters for world-space positions). Returns Boolean True if the Euclidean distance between the two vectors is less than or equal to distance. |
| **length** () | Calculates the length (magnitude) of a vector. Signature ```kotlin fun length(): Float ``` Returns Float The length of the vector. |
| **lerp** ( dest , ratio ) | Linearly interpolates between two vectors. Signature ```kotlin fun lerp(dest: Vector3, ratio: Float): Vector3 ``` Parameters dest: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The destination vector to interpolate towards. ratio: Float The interpolation ratio, where 0 means no interpolation (i.e., the current vector) and 1 means full interpolation (i.e., the destination vector). Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The interpolated vector. |
| **max** ( v ) | Returns a vector with the maximum components of this vector and another vector. Signature ```kotlin fun max(v: Vector3): Vector3 ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The other vector to compare with. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) A new vector with the maximum components. |
| **min** ( v ) | Returns a vector with the minimum components of this vector and another vector. Signature ```kotlin fun min(v: Vector3): Vector3 ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The other vector to compare with. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) A new vector with the minimum components. |
| **minus** ( v ) | Subtracts two vectors component-wise. Signature ```kotlin inline operator fun minus(v: Vector3): Vector3 ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The vector to subtract. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The resulting vector. |
| **multiply** ( v ) | Multiplies two vectors component-wise. Signature ```kotlin inline fun multiply(v: Vector3): Vector3 ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The vector to multiply. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The resulting vector. |
| **multiply** ( v ) | Multiplies a vector by a scalar. Signature ```kotlin inline fun multiply(v: Float): Vector3 ``` Parameters v: Float The scalar to multiply. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The resulting vector. |
| **negate** () | Negates a vector. Signature ```kotlin inline fun negate(): Vector3 ``` Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The negated vector. |
| **normalize** () | Normalizes a vector to have a length of 1 Signature ```kotlin fun normalize(): Vector3 ``` Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) A new vector representing the normalization of this vector, or (0, 0, 0) if the length of this vector is 0. |
| **plus** ( v ) | Adds two vectors component-wise. Signature ```kotlin inline operator fun plus(v: Vector3): Vector3 ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The vector to add. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The resulting vector. |
| **setX** ( x ) | Signature ```kotlin fun setX(x: Float): Vector3 ``` Parameters x: Float Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) |
| **setY** ( y ) | Signature ```kotlin fun setY(y: Float): Vector3 ``` Parameters y: Float Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) |
| **setZ** ( z ) | Signature ```kotlin fun setZ(z: Float): Vector3 ``` Parameters z: Float Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) |
| **sub** ( v ) | Subtracts two vectors component-wise. Signature ```kotlin inline fun sub(v: Vector3): Vector3 ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The vector to subtract. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The resulting vector. |
| **times** ( v ) | Multiplies two vectors component-wise. Signature ```kotlin inline operator fun times(v: Vector3): Vector3 ``` Parameters v: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The vector to multiply. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The resulting vector. |
| **times** ( v ) | Multiplies a vector by a scalar. Signature ```kotlin inline operator fun times(v: Float): Vector3 ``` Parameters v: Float The scalar to multiply. Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The resulting vector. |
| **toString** () | Returns a string representation of the vector. Signature ```kotlin open override fun toString(): String ``` Returns String A string representation of the vector in the format "(x, y, z)". |
| **unaryMinus** () | Negates a vector. Signature ```kotlin inline operator fun unaryMinus(): Vector3 ``` Returns [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The negated vector. |

## Companion Object

### Companion Object Properties

| **Forward** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | Signature ```kotlin val Forward: Vector3 ``` |
| --- | --- |
| **Right** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | Signature ```kotlin val Right: Vector3 ``` |
| **Up** : [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) [Get] | Signature ```kotlin val Up: Vector3 ``` |