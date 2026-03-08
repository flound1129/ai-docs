# AttributePrimitive Enum

Enum class representing different types of attribute implementations in the native layer.

## Signature

```kotlin
enum AttributePrimitive : Enum<AttributePrimitive>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| DEFAULT | Default attribute type. |
| INT | Attribute type representing an integer value. |
| LONG | Attribute type representing a long value. |
| FLOAT | Attribute type representing a floating-point value. |
| STRING | Attribute type representing a string value. |
| UUID | Attribute type representing a universally unique identifier (UUID). |
| VECTOR2 | Attribute type representing a 2D vector. |
| VECTOR3 | Attribute type representing a 3D vector. |
| VECTOR4 | Attribute type representing a 4D vector. |
| POSE | Attribute type representing a pose (position and orientation). |
| TUPLE | Attribute type representing a tuple of values. |
| MAP | Attribute type representing a map of key-value pairs. |
| ENTITY | Attribute type representing an entity. |
| TIME | Attribute type representing a time value. |
| URI | Attribute type representing a Uri. |

## Companion Object

### Companion Object Functions

| **fromIndex** ( index ) | Returns the attribute type corresponding to the given index. Signature ```kotlin fun fromIndex(index: Int): AttributePrimitive ``` Parameters index: Int Returns [AttributePrimitive](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_attributeprimitive) |
| --- | --- |