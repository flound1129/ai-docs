# Vector2 Class

*Modifiers:
open*

Represents a 2D vector with x and y components.

## Signature

```kotlin
open class Vector2(var x: Float = 0.0f, var y: Float = 0.0f)
```

## Constructors

| **Vector2** ( v ) | Secondary constructor to create a vector where both components are the same. Signature ```kotlin constructor(v: Float) ``` Parameters v: Float The value to use for both components. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) |
| --- | --- |
| **Vector2** ( x , y ) | Signature ```kotlin constructor(x: Float = 0.0f, y: Float = 0.0f) ``` Parameters x: Float The x component of the vector. y: Float The y component of the vector. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) |

## Properties

| **x** : Float [Get][Set] | Signature ```kotlin open var x: Float ``` |
| --- | --- |
| **y** : Float [Get][Set] | Signature ```kotlin open var y: Float ``` |

## Functions

| **add** ( v ) | Adds the specified vector to this vector. Signature ```kotlin fun add(v: Vector2): Vector2 ``` Parameters v: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The other vector to add. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the sum of this vector and the other vector. |
| --- | --- |
| **component1** () | Signature ```kotlin operator fun component1(): Float ``` Returns Float |
| **component2** () | Signature ```kotlin operator fun component2(): Float ``` Returns Float |
| **copy** () | Returns a copy of this vector. Signature ```kotlin fun copy(): Vector2 ``` Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A copy of this vector. |
| **cross** ( other ) | Calculates the cross product of this vector with another vector. Signature ```kotlin fun cross(other: Vector2): Float ``` Parameters other: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The other vector to calculate the cross product with. Returns Float The cross product of this vector and the other vector. |
| **distanceTo** ( v ) | Calculates the distance to another vector. Signature ```kotlin fun distanceTo(v: Vector2): Float ``` Parameters v: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The other vector to calculate the distance to. Returns Float The distance between this vector and the other vector. |
| **div** ( v ) | Divides each component of this vector by a scalar. Signature ```kotlin operator fun div(v: Float): Vector2 ``` Parameters v: Float The scalar to divide by. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the division of this vector by the scalar. |
| **divide** ( v ) | Divides each component of this vector by a scalar. Signature ```kotlin fun divide(v: Float): Vector2 ``` Parameters v: Float The scalar to divide by. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the division of this vector by the scalar. |
| **dot** ( v ) | Calculates the dot product of this vector with another vector. Signature ```kotlin fun dot(v: Vector2): Float ``` Parameters v: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The other vector to calculate the dot product with. Returns Float The dot product of this vector and the other vector. |
| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |
| **length** () | Returns the length (magnitude) of this vector. Signature ```kotlin fun length(): Float ``` Returns Float The length of this vector. |
| **lerp** ( dest , ratio ) | Linearly interpolates between this vector and another vector by the given ratio. Signature ```kotlin fun lerp(dest: Vector2, ratio: Float): Vector2 ``` Parameters dest: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The destination vector to interpolate towards. ratio: Float The interpolation ratio, where 0 means no interpolation (i.e., the current vector) and 1 means full interpolation (i.e., the destination vector). Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the linear interpolation between this vector and the destination vector by the given ratio. |
| **max** ( v ) | Returns a vector with the maximum components of this vector and another vector. Signature ```kotlin fun max(v: Vector2): Vector2 ``` Parameters v: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The other vector to compare with. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector with the maximum components. |
| **min** ( v ) | Returns a vector with the minimum components of this vector and another vector. Signature ```kotlin fun min(v: Vector2): Vector2 ``` Parameters v: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The other vector to compare with. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector with the minimum components. |
| **minus** ( v ) | Subtracts the other vector from this vector. Signature ```kotlin operator fun minus(v: Vector2): Vector2 ``` Parameters v: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The other vector to subtract. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the difference between this vector and the other vector. |
| **multiply** ( v ) | Multiplies this vector by another vector component-wise. Signature ```kotlin fun multiply(v: Vector2): Vector2 ``` Parameters v: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The other vector to multiply. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the product of this vector and the other vector. |
| **multiply** ( v ) | Multiplies each component of this vector by a scalar. Signature ```kotlin fun multiply(v: Float): Vector2 ``` Parameters v: Float The scalar to multiply by. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the product of this vector and the scalar. |
| **negate** () | Negates this vector. Signature ```kotlin fun negate(): Vector2 ``` Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the negation of this vector. |
| **normalize** () | Normalizes this vector. Signature ```kotlin fun normalize(): Vector2 ``` Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the normalization of this vector, or (0, 0) if the length of this vector is 0. |
| **plus** ( v ) | Adds two vectors. Signature ```kotlin operator fun plus(v: Vector2): Vector2 ``` Parameters v: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The other vector to add. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the sum of this vector and the other vector. |
| **setX** ( x ) | Sets the x component of this vector. Signature ```kotlin fun setX(x: Float): Vector2 ``` Parameters x: Float The new value for the x component. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) This vector with the updated x component. |
| **setY** ( y ) | Sets the y component of this vector. Signature ```kotlin fun setY(y: Float): Vector2 ``` Parameters y: Float The new value for the y component. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) This vector with the updated y component. |
| **sub** ( v ) | Subtracts the specified vector from this vector. Signature ```kotlin fun sub(v: Vector2): Vector2 ``` Parameters v: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The other vector to subtract. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the difference between this vector and the other vector. |
| **times** ( v ) | Multiplies two vectors component-wise. Signature ```kotlin operator fun times(v: Vector2): Vector2 ``` Parameters v: [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) The other vector to multiply. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the product of this vector and the other vector. |
| **times** ( v ) | Multiplies each component of this vector by a scalar. Signature ```kotlin operator fun times(v: Float): Vector2 ``` Parameters v: Float The scalar to multiply by. Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the product of this vector and the scalar. |
| **toString** () | Returns a string representation of the vector. Signature ```kotlin open override fun toString(): String ``` Returns String A string representation of the vector in the format "(x, y)". |
| **unaryMinus** () | Negates this vector. Signature ```kotlin operator fun unaryMinus(): Vector2 ``` Returns [Vector2](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2) A new vector representing the negation of this vector. |