# Vector4 Class

*Modifiers:
open*

A 4D vector class with x, y, z, and w components.

## Signature

```kotlin
open class Vector4(var x: Float, var y: Float, var z: Float, var w: Float)
```

## Constructors

| **Vector4** ( v ) | Constructor that takes a single float value and initializes all components to that value. Signature ```kotlin constructor(v: Float) ``` Parameters v: Float The value to initialize all components with. Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) |
| --- | --- |
| **Vector4** ( x , y , z , w ) | Signature ```kotlin constructor(x: Float, y: Float, z: Float, w: Float) ``` Parameters x: Float The x component of the vector. y: Float The y component of the vector. z: Float The z component of the vector. w: Float The w component of the vector. Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) |

## Properties

| **w** : Float [Get][Set] | Signature ```kotlin open var w: Float ``` |
| --- | --- |
| **x** : Float [Get][Set] | Signature ```kotlin open var x: Float ``` |
| **y** : Float [Get][Set] | Signature ```kotlin open var y: Float ``` |
| **z** : Float [Get][Set] | Signature ```kotlin open var z: Float ``` |

## Functions

| **add** ( v ) | Performs vector addition. Signature ```kotlin fun add(v: Vector4): Vector4 ``` Parameters v: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The vector to add. Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The resulting vector. |
| --- | --- |
| **component1** () | Signature ```kotlin operator fun component1(): Float ``` Returns Float |
| **component2** () | Signature ```kotlin operator fun component2(): Float ``` Returns Float |
| **component3** () | Signature ```kotlin operator fun component3(): Float ``` Returns Float |
| **component4** () | Signature ```kotlin operator fun component4(): Float ``` Returns Float |
| **copy** () | Returns a copy of this vector. Signature ```kotlin fun copy(): Vector4 ``` Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) A copy of this vector. |
| **distanceTo** ( v ) | Calculates the distance between two vectors. Signature ```kotlin fun distanceTo(v: Vector4): Float ``` Parameters v: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The other vector to calculate the distance to. Returns Float The distance between the two vectors. |
| **div** ( v ) | Overloads the div operator to perform scalar division. Signature ```kotlin operator fun div(v: Float): Vector4 ``` Parameters v: Float The scalar to divide by. Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The resulting vector. |
| **divide** ( v ) | Performs scalar division. Signature ```kotlin fun divide(v: Float): Vector4 ``` Parameters v: Float The scalar to divide by. Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The resulting vector. |
| **dot** ( v ) | Calculates the dot product of two vectors. Signature ```kotlin fun dot(v: Vector4): Float ``` Parameters v: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The vector to calculate the dot product with. Returns Float The dot product. |
| **equals** ( other ) | Signature ```kotlin open operator override fun equals(other: Any?): Boolean ``` Parameters other: Any? Returns Boolean |
| **hashCode** () | Signature ```kotlin open override fun hashCode(): Int ``` Returns Int |
| **length** () | Calculates the length of the vector. Signature ```kotlin fun length(): Float ``` Returns Float The length of the vector. |
| **lerp** ( dest , ratio ) | Linearly interpolates between two vectors. Signature ```kotlin fun lerp(dest: Vector4, ratio: Float): Vector4 ``` Parameters dest: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The destination vector to interpolate towards. ratio: Float The interpolation ratio, where 0 means no interpolation (i.e., the current vector) and 1 means full interpolation (i.e., the destination vector). Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The interpolated vector. |
| **minus** ( v ) | Overloads the minus operator to perform vector subtraction. Signature ```kotlin operator fun minus(v: Vector4): Vector4 ``` Parameters v: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The vector to subtract. Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The resulting vector. |
| **multiply** ( v ) | Performs vector multiplication. Signature ```kotlin fun multiply(v: Vector4): Vector4 ``` Parameters v: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The vector to multiply. Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The resulting vector. |
| **multiply** ( v ) | Performs scalar multiplication. Signature ```kotlin fun multiply(v: Float): Vector4 ``` Parameters v: Float The scalar to multiply by. Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The resulting vector. |
| **negate** () | Negates the vector. Signature ```kotlin fun negate(): Vector4 ``` Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The negated vector. |
| **normalize** () | Normalizes the vector. Signature ```kotlin fun normalize(): Vector4 ``` Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) A new vector representing the normalization of this vector, or (0, 0, 0, 0) if the length of this vector is 0. |
| **plus** ( v ) | Overloads the plus operator to perform vector addition. Signature ```kotlin operator fun plus(v: Vector4): Vector4 ``` Parameters v: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The vector to add. Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The resulting vector. |
| **setW** ( w ) | Signature ```kotlin fun setW(w: Float): Vector4 ``` Parameters w: Float Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) |
| **setX** ( x ) | Signature ```kotlin fun setX(x: Float): Vector4 ``` Parameters x: Float Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) |
| **setY** ( y ) | Signature ```kotlin fun setY(y: Float): Vector4 ``` Parameters y: Float Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) |
| **setZ** ( z ) | Signature ```kotlin fun setZ(z: Float): Vector4 ``` Parameters z: Float Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) |
| **sub** ( v ) | Performs vector subtraction. Signature ```kotlin fun sub(v: Vector4): Vector4 ``` Parameters v: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The vector to subtract. Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The resulting vector. |
| **times** ( v ) | Overloads the times operator to perform component-wise multiplication. Signature ```kotlin operator fun times(v: Vector4): Vector4 ``` Parameters v: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The vector to multiply. Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The resulting vector. |
| **times** ( v ) | Overloads the times operator to perform scalar multiplication. Signature ```kotlin operator fun times(v: Float): Vector4 ``` Parameters v: Float The scalar to multiply by. Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The resulting vector. |
| **toString** () | Signature ```kotlin open override fun toString(): String ``` Returns String |
| **unaryMinus** () | Overloads the unary minus operator to negate the vector. Signature ```kotlin operator fun unaryMinus(): Vector4 ``` Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) The negated vector. |