# SceneTexture Class

*Modifiers:
final*

The SceneTexture class represents a texture resource. SceneTextures are used to construct [SceneMaterial](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenematerial) s and can be used as inputs for shaders also in the construction of [SceneMaterial](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenematerial) s.

Example ways to create a SceneTexture:

```kotlin SceneTexture(getDrawable(R.drawable.myDrawable)) // Creating a SceneTexture from drawable in resources
SceneTexture(Color.valueOf(Color.BLACK)) // Creating a plain black SceneTexture ```

SceneTextures are also generated as part of the Panel rendering process and are used to render Panels by populating their [SceneMaterial](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenematerial) . This is not necessary for Layer panels, but can be enabled with [PanelConfigOptions](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_panelconfigoptions) "forceSceneTexture" parameter.

## Signature

```kotlin
class SceneTexture
```

## Constructors

| **SceneTexture** ( width , height , numberOfMips , samplerConfig , color ) | Signature ```kotlin constructor(width: Int, height: Int, numberOfMips: Int, samplerConfig: SamplerConfig = SamplerConfig(), color: Color?) ``` Parameters width: Int height: Int numberOfMips: Int samplerConfig: [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) color: Color? Returns [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) |
| --- | --- |
| **SceneTexture** ( image , samplerConfig ) | Signature ```kotlin constructor(image: Image, samplerConfig: SamplerConfig = SamplerConfig()) ``` Parameters image: Image samplerConfig: [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) Returns [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) |
| **SceneTexture** ( bitmap , samplerConfig ) | Signature ```kotlin constructor(bitmap: Bitmap, samplerConfig: SamplerConfig = SamplerConfig()) ``` Parameters bitmap: Bitmap samplerConfig: [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) Returns [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) |
| **SceneTexture** ( drawable ) | Signature ```kotlin constructor(drawable: Drawable?) ``` Parameters drawable: Drawable? Returns [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) |
| **SceneTexture** ( color , samplerConfig ) | Signature ```kotlin constructor(color: Color, samplerConfig: SamplerConfig = SamplerConfig()) ``` Parameters color: Color samplerConfig: [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) Returns [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) |

## Properties

| **handle** : Long [Get] | Signature ```kotlin var handle: Long ``` |
| --- | --- |

## Functions

| **clear** ( r , g , b , a ) | Clears the texture with a solid color specified by RGBA float values. Signature ```kotlin fun clear(r: Float, g: Float, b: Float, a: Float) ``` Parameters r: Float Red component (0.0 to 1.0) g: Float Green component (0.0 to 1.0) b: Float Blue component (0.0 to 1.0) a: Float Alpha component (0.0 to 1.0) |
| --- | --- |
| **destroy** () | Signature ```kotlin fun destroy() ``` |
| **nativeHandle** () | Signature ```kotlin fun nativeHandle(): Long ``` Returns Long |
| **update** ( buffer , width , height , strideInBytes ) | Updates the texture with new data. Signature ```kotlin fun update(buffer: ByteBuffer, width: Int, height: Int, strideInBytes: Int) ``` Parameters buffer: ByteBuffer ByteBuffer containing the pixel data width: Int Width of the image data in pixels height: Int Height of the image data in pixels strideInBytes: Int Number of bytes per row in the buffer |

## Companion Object

### Companion Object Properties

| **DEFAULT_TEXTURE_SIZE** : Int [Get] | Default texture size for non-bitmap resources (e.g., vector drawables). Signature ```kotlin const val DEFAULT_TEXTURE_SIZE: Int = 256 ``` |
| --- | --- |

### Companion Object Functions

| **calculateMips** ( w , h ) | Calculates the number of mipmap levels for a texture of the given dimensions. Mipmaps are smaller versions of a texture used for rendering at different distances, which improves rendering quality and performance. Signature ```kotlin fun calculateMips(w: Int, h: Int): Int ``` Parameters w: Int Width of the texture in pixels h: Int Height of the texture in pixels Returns Int The number of mipmap levels |
| --- | --- |
| **createFromPlatformImage** ( w , h , mips , platformImage , samplerConfig ) | Signature ```kotlin fun createFromPlatformImage(w: Int, h: Int, mips: Int, platformImage: Long, samplerConfig: SamplerConfig = SamplerConfig()): SceneTexture ``` Parameters w: Int h: Int mips: Int platformImage: Long samplerConfig: [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) Returns [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) |
| **fromBitmapWithScaling** ( originalBitmap , targetWidth , targetHeight , scale , samplerConfig ) | Helper to create a SceneTexture from a bitmap with optional scaling. Signature ```kotlin fun fromBitmapWithScaling(originalBitmap: Bitmap, targetWidth: Int?, targetHeight: Int?, scale: Float?, samplerConfig: SamplerConfig): SceneTexture ``` Parameters originalBitmap: Bitmap targetWidth: Int? targetHeight: Int? scale: Float? samplerConfig: [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) Returns [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) |
| **fromResource** ( context , resourceId , targetWidth , targetHeight , scale , samplerConfig ) | Creates a SceneTexture from an Android drawable resource, automatically converting it to a bitmap and optionally scaling it. This is a convenience method that handles the common pattern of loading a drawable resource, decoding it to a bitmap, optionally scaling it, and creating a texture. **Size behavior:** - If the resource is a bitmap drawable: uses the original bitmap dimensions by default - If the resource is a vector/shape drawable with intrinsic dimensions: uses those dimensions - If the resource has no intrinsic dimensions (e.g., some shape drawables): uses 256x256 - If `targetWidth` and `targetHeight` are specified: uses those dimensions - If `scale` is specified: scales from the base size (original or default) **Supported resource types:** - Bitmap drawables (PNG, JPG, WebP, etc.) - Vector drawables (XML vector graphics) - Shape drawables (XML shapes like oval, rectangle, etc.) - Nine-patch drawables - Layer-list and other compound drawables Example usage: ```kotlin // Use original bitmap size or intrinsic drawable size val texture = SceneTexture.fromResource(context, R.drawable.my_bitmap) // Scale to 50% of original size val halfSize = SceneTexture.fromResource(context, R.drawable.my_bitmap, scale = 0.5f) // Force specific dimensions (good for vector/shape drawables) val fixedSize = SceneTexture.fromResource(context, R.drawable.my_shape, 512, 512) ``` Signature ```kotlin fun fromResource(context: Context, resourceId: Int, targetWidth: Int? = null, targetHeight: Int? = null, scale: Float? = null, samplerConfig: SamplerConfig = SamplerConfig()): SceneTexture ``` Parameters context: Context Android context used to access resources resourceId: Int The drawable resource ID (e.g., R.drawable.my_image) targetWidth: Int? Optional target width in pixels. If null, uses intrinsic/original size or default. targetHeight: Int? Optional target height in pixels. If null, uses intrinsic/original size or default. scale: Float? Optional scale factor applied to the base size (1.0 = no scaling). Ignored if targetWidth/targetHeight are specified. samplerConfig: [SamplerConfig](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_samplerconfig) Optional sampler configuration for texture filtering and addressing Returns [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) A new SceneTexture containing the resource image Throws IllegalArgumentException if the resource cannot be loaded |