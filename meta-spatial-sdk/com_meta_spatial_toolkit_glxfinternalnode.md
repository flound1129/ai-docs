# GLXFInternalNode Class

Extends
[GLXFNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfnode)
*Modifiers:
final*

A subclass of GLXFNode that represents a node in a GLXF file that has children.

## Signature

```kotlin
class GLXFInternalNode(val entity: Entity, transform: GLXFNodeTransform, var name: String? = null, asset: GLXFAsset = GLXFAsset.nullGLXFAsset(), children: MutableList<GLXFNode> = mutableListOf<GLXFNode>(), childrenIndices: MutableSet<Int> = mutableSetOf<Int>(), isRoot: Boolean = true) : GLXFNode
```

## Constructors

| **GLXFInternalNode** ( entity , transform , name , asset , children , childrenIndices , isRoot ) | Signature ```kotlin constructor(entity: Entity, transform: GLXFNodeTransform, name: String? = null, asset: GLXFAsset = GLXFAsset.nullGLXFAsset(), children: MutableList<GLXFNode> = mutableListOf<GLXFNode>(), childrenIndices: MutableSet<Int> = mutableSetOf<Int>(), isRoot: Boolean = true) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) transform: GLXFNodeTransform name: String? asset: GLXFAsset children: MutableList The children of the node. childrenIndices: MutableSet The indices of the children of the node. isRoot: Boolean Whether the node is the root of the GLXF file. Returns [GLXFInternalNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfinternalnode) |
| --- | --- |

## Properties

| **entity** : [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get] | The entity associated with the node. Signature ```kotlin val entity: Entity ``` |
| --- | --- |
| **name** : String? [Get][Set] | The name of the node. Signature ```kotlin var name: String? ``` |

## Functions

| **getChildren** () | gets a list of the children nodes Signature ```kotlin fun getChildren(): List<GLXFNode> ``` Returns List |
| --- | --- |