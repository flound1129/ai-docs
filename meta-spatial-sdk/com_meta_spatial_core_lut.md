# Lut Class

*Modifiers:
final*

Passthrough lookup tables (LUTs) transform the colors that passthrough displays. You can use them to evoke a certain style, such as tinting everything red when you are low on health, or to emulate a lighting environment, like dimming lights when a movie starts.

Passthrough LUTs are represented by a 3D color "cube" with the dimensions of 16x16x16 or 32x32x32 representing input RGB values. Each of the 16^3 or 32^3 values are mapped to a 32-bit RGBA color value (each color channel being 0-255).

See our [guide on Passthrough LUTs](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-passthrough#passthrough-luts) for more details.

Usage:

```kotlin // initialize lut
val lut = Lut()
for (r in 0..15) {
    for (g in 0..15) {
        for (b in 0..15) {
            // set a mapping color for each RGB value in the (0-15)^3 range
            lut.setMapping(r, g, b, r * 4 + r / 4, g * 4 + g / 4, b * 4 + b / 4)
        }
    }
}
// alternatively, for a simple scaling, you can use `Lut.fromScale(Vector3)`
val lut = Lut.fromScale(Vector3(0.25f))
// loading from a bitmap is possible too
val lut = Lut.fromBitmap(BitmapFactory.decodeFile("lut.png"))
// finally, apply it to the passthrough
scene.setPassthroughLUT(lut) ```

## Signature

```kotlin
class Lut(val dimension: Int = 16)
```

## Constructors

| **Lut** ( dimension ) | Signature ```kotlin constructor(dimension: Int = 16) ``` Parameters dimension: Int The dimension of the LUT (16 or 32), defaults to 16. Returns [Lut](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_lut) |
| --- | --- |

## Properties

| **dimension** : Int [Get] | The dimension of the LUT (16 or 32), defaults to 16. Signature ```kotlin val dimension: Int = 16 ``` |
| --- | --- |

## Functions

| **getTable** () | Returns a 1D array representation of the 3D color lookup table. Signature ```kotlin fun getTable(): IntArray ``` Returns IntArray The internal table pixels. |
| --- | --- |
| **setMapping** ( srcR , srcG , srcB , toR , toG , toB ) | Sets a specific RGB to be set to a different RGB value in the LUT. Signature ```kotlin fun setMapping(srcR: Int, srcG: Int, srcB: Int, toR: Int, toG: Int, toB: Int) ``` Parameters srcR: Int The red component of the source color (less than `dimensions` ). srcG: Int The green component of the source color (less than `dimensions` ). srcB: Int The blue component of the source color (less than `dimensions` ). toR: Int The red component of the destination color (8-bit). toG: Int The green component of the destination color (8-bit). toB: Int The blue component of the destination color (8-bit). Throws Exception If the source color is out of range based on the `dimensions` . |

## Companion Object

### Companion Object Functions

| **fromBitmap** ( bitmap ) | Creates a LUT object from a Bitmap loaded from disk. The bitmap is a 2D representation of the 3D LUT and must be 256x16 or 1024x32 pixels. Signature ```kotlin fun fromBitmap(bitmap: Bitmap): Lut? ``` Parameters bitmap: Bitmap The bitmap to create the LUT from. Returns [Lut?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_lut) The created LUT object or null if an error occurred. |
| --- | --- |
| **fromScale** ( scale ) | Creates a LUT where RGB are scaled component-wise by the given XYZ scale. Signature ```kotlin fun fromScale(scale: Vector3): Lut ``` Parameters scale: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The scale to apply to the RGB values. Returns [Lut](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_lut) The created LUT object. |