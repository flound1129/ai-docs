# SceneMaterialAttribute Class

*Modifiers:
final*

Defines a named attribute for use with custom shaders.

## Signature

```kotlin
class SceneMaterialAttribute(val name: String, val type: SceneMaterialDataType)
```

## Constructors

| **SceneMaterialAttribute** ( name , type ) | Signature ```kotlin constructor(name: String, type: SceneMaterialDataType) ``` Parameters name: String The name of the attribute as it appears in the shader type: [SceneMaterialDataType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenematerialdatatype) The data type of the attribute Returns [SceneMaterialAttribute](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenematerialattribute) |
| --- | --- |

## Properties

| **name** : String [Get] | The name of the attribute as it appears in the shader Signature ```kotlin val name: String ``` |
| --- | --- |
| **type** : [SceneMaterialDataType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_scenematerialdatatype) [Get] | The data type of the attribute Signature ```kotlin val type: SceneMaterialDataType ``` |