# GLXFLeafNode Class

Extends
[GLXFNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfnode)
*Modifiers:
final*

A subclass of GLXFNode that represents a leaf node in a GLXF file.

## Signature

```kotlin
class GLXFLeafNode(val entity: Entity, transform: GLXFNodeTransform, var name: String? = null, asset: GLXFAsset) : GLXFNode
```

## Constructors

| **GLXFLeafNode** ( entity , transform , name , asset ) | Signature ```kotlin constructor(entity: Entity, transform: GLXFNodeTransform, name: String? = null, asset: GLXFAsset) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) transform: GLXFNodeTransform name: String? asset: GLXFAsset Returns [GLXFLeafNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfleafnode) |
| --- | --- |

## Properties

| **entity** : [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get] | The entity associated with the node. Signature ```kotlin val entity: Entity ``` |
| --- | --- |
| **name** : String? [Get][Set] | The name of the node. Signature ```kotlin var name: String? ``` |