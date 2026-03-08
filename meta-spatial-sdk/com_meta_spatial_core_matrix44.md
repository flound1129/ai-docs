# Matrix44 Class

*Modifiers:
final*

A 4x4 matrix class for representing transformations in 3D space.

## Signature

```kotlin
data class Matrix44(var m00: Float, var m01: Float, var m02: Float, var m03: Float, var m10: Float, var m11: Float, var m12: Float, var m13: Float, var m20: Float, var m21: Float, var m22: Float, var m23: Float, var m30: Float, var m31: Float, var m32: Float, var m33: Float)
```

## Constructors

| **Matrix44** ( values ) | Constructs a new Matrix44 from a FloatArray of 16 elements. Signature ```kotlin constructor(values: FloatArray) ``` Parameters values: FloatArray the FloatArray containing the matrix data Returns [Matrix44](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_matrix44) |
| --- | --- |
| **Matrix44** ( m00 , m01 , m02 , m03 , m10 , m11 , m12 , m13 , m20 , m21 , m22 , m23 , m30 , m31 , m32 , m33 ) | Signature ```kotlin constructor(m00: Float, m01: Float, m02: Float, m03: Float, m10: Float, m11: Float, m12: Float, m13: Float, m20: Float, m21: Float, m22: Float, m23: Float, m30: Float, m31: Float, m32: Float, m33: Float) ``` Parameters m00: Float m01: Float m02: Float m03: Float m10: Float m11: Float m12: Float m13: Float m20: Float m21: Float m22: Float m23: Float m30: Float m31: Float m32: Float m33: Float Returns [Matrix44](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_matrix44) |

## Properties

| **m00** : Float [Get][Set] | Signature ```kotlin var m00: Float ``` |
| --- | --- |
| **m01** : Float [Get][Set] | Signature ```kotlin var m01: Float ``` |
| **m02** : Float [Get][Set] | Signature ```kotlin var m02: Float ``` |
| **m03** : Float [Get][Set] | Signature ```kotlin var m03: Float ``` |
| **m10** : Float [Get][Set] | Signature ```kotlin var m10: Float ``` |
| **m11** : Float [Get][Set] | Signature ```kotlin var m11: Float ``` |
| **m12** : Float [Get][Set] | Signature ```kotlin var m12: Float ``` |
| **m13** : Float [Get][Set] | Signature ```kotlin var m13: Float ``` |
| **m20** : Float [Get][Set] | Signature ```kotlin var m20: Float ``` |
| **m21** : Float [Get][Set] | Signature ```kotlin var m21: Float ``` |
| **m22** : Float [Get][Set] | Signature ```kotlin var m22: Float ``` |
| **m23** : Float [Get][Set] | Signature ```kotlin var m23: Float ``` |
| **m30** : Float [Get][Set] | Signature ```kotlin var m30: Float ``` |
| **m31** : Float [Get][Set] | Signature ```kotlin var m31: Float ``` |
| **m32** : Float [Get][Set] | Signature ```kotlin var m32: Float ``` |
| **m33** : Float [Get][Set] | Signature ```kotlin var m33: Float ``` |

## Functions

| **decompose** () | Decomposes a 4x4 transformation matrix into its constituent parts: a Pose (translation and rotation) and a Vector3 (scale). Signature ```kotlin fun decompose(): Pair<Pose, Vector3> ``` Returns Pair<Pose, Vector3> A Pair containing the Pose object and the scale Vector3. |
| --- | --- |
| **determinant** () | Calculates the determinant of this matrix. Signature ```kotlin fun determinant(): Float ``` Returns Float the determinant of the matrix |
| **times** ( other ) | Multiplies this matrix by another matrix and returns the result. Signature ```kotlin operator fun times(other: Matrix44): Matrix44 ``` Parameters other: [Matrix44](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_matrix44) the matrix to multiply by Returns [Matrix44](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_matrix44) the resulting matrix |
| **times** ( vector ) | Multiplies this matrix by a Vector4 and returns the result. Signature ```kotlin operator fun times(vector: Vector4): Vector4 ``` Parameters vector: [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) the Vector4 to multiply by Returns [Vector4](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4) the resulting Vector4 |
| **toString** () | Signature ```kotlin open override fun toString(): String ``` Returns String |

## Companion Object

### Companion Object Functions

| **composeFromTRS** ( transform , scale ) | Composes a 4x4 transformation matrix from a Pose (translation and rotation) and a Vector3 (scale). Signature ```kotlin fun composeFromTRS(transform: Pose, scale: Vector3): Matrix44 ``` Parameters transform: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The Pose object containing the translation and rotation components. scale: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The Vector3 object containing the scale factors. Returns [Matrix44](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_matrix44) A 4x4 transformation matrix representing the composition of the translation, rotation, and scale transformations. |
| --- | --- |
| **fromFloatArray** ( values ) | Creates a new Matrix44 from a FloatArray of 16 elements. Signature ```kotlin fun fromFloatArray(values: FloatArray): Matrix44 ``` Parameters values: FloatArray The FloatArray containing the matrix data. Must have exactly 16 elements. Returns [Matrix44](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_matrix44) A new Matrix44 object constructed from the input FloatArray. |