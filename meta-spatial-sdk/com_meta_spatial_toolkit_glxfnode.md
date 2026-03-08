# GLXFNode Class

*Modifiers:
open*

An open class representing a node in a GLXF file. You can use it to access the entity that has been inflated to represent the node.

Example:

```kotlin val myNode = myGLXFInfo.getNodeByName("myNodeName")
val myEntity = myNode.entity ```

## Signature

```kotlin
open class GLXFNode(val entity: Entity, transform: GLXFNodeTransform, var name: String? = null, asset: GLXFAsset = GLXFAsset.nullGLXFAsset())
```

## Constructors

| **GLXFNode** ( entity , transform , name , asset ) | Signature ```kotlin constructor(entity: Entity, transform: GLXFNodeTransform, name: String? = null, asset: GLXFAsset = GLXFAsset.nullGLXFAsset()) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity associated with the node. transform: GLXFNodeTransform The transformation of the node. name: String? The name of the node. asset: GLXFAsset The asset associated with the node. Returns [GLXFNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfnode) |
| --- | --- |

## Properties

| **entity** : [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get] | The entity associated with the node. Signature ```kotlin val entity: Entity ``` |
| --- | --- |
| **name** : String? [Get][Set] | The name of the node. Signature ```kotlin var name: String? ``` |