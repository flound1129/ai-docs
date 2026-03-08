# SceneMaterialDataType Enum

Defines the data types that can be used as attributes in custom shaders.

These types correspond to the attribute types supported by the underlying rendering system and are used when creating custom materials.

Learn more about custom shaders in Meta Spatial SDK [here](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-custom-shaders#custom-materials) .

## Signature

```kotlin
enum SceneMaterialDataType : Enum<SceneMaterialDataType>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| Vector4 | Represents a 4-component vector (x, y, z, w) that can be used for colors, positions, or any other vector data in shaders |
| Texture2D | Represents a 2D texture backed by a [SceneTexture](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenetexture) that can be sampled in shaders |

## Properties

| **id** : Int [Get][Set] | The internal ID used to identify this data type in the native code Signature ```kotlin var id: Int ``` |
| --- | --- |