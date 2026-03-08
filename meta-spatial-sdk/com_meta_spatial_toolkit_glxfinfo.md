# GLXFInfo Class

*Modifiers:
final*

GLXFInfo is a class that represents a GLXF file. Refer to [readme](https://github.com/KhronosGroup/glTF-External-Reference/blob/main/specification/2.0/README.md) for detailed specification.

A GLXFInfo is made whenever you use [GLXFManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfmanager) to inflate a glXF file. Here is an example of creating a GLXFInfo:

```kotlin val myGLXFInfo = glXFManager.inflateGLXF(Uri.parse("apk:///scenes/Composition.glxf")) ```

## Constructors

| **GLXFInfo** ( glxfManager , version , experience , assets , nodes , rootEntity , uri , context , nodeMap , nodesByName , keyName , entityIdToEntityMap , overrideCreateEntity ) | Parameters glxfManager: [GLXFManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfmanager) version: String : the version of the GLXF file, e.g., "2.0" experience: Boolean : The experience property set to true indicates that this file is intended to be directly viewed as an experience and MUST NOT be imported into other scenes. assets: MutableList : a list of assets in the GLXF file nodes: MutableList : a list of nodes in the GLXF file rootEntity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) : the root entity of the GLXF file uri: Uri : the URI of the GLXF file context: Context : the context of the GLXF file, a.k.a. the Spatial Activity object. nodeMap: NodeMap : a map of entities to GLXFNodes nodesByName: MutableMap : a map of node names to GLXFNodes keyName: String? : the key name of the GLXF file. This optional value is used to uniquely identify the GLXF file. entityIdToEntityMap: MutableMap overrideCreateEntity: Function1 Returns [GLXFInfo](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfinfo) |
| --- | --- |

## Properties

| **experience** : Boolean [Get] | : The experience property set to true indicates that this file is intended to be directly viewed as an experience and MUST NOT be imported into other scenes. Signature ```kotlin val experience: Boolean ``` |
| --- | --- |
| **glxfManager** : [GLXFManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfmanager) [Get] | Signature ```kotlin val glxfManager: GLXFManager ``` |
| **keyName** : String? [Get] | : the key name of the GLXF file. This optional value is used to uniquely identify the GLXF file. Signature ```kotlin val keyName: String? = null ``` |
| **nodes** : MutableList [Get][Set] | : a list of nodes in the GLXF file Signature ```kotlin var nodes: MutableList<GLXFNode> ``` |
| **rootEntity** : [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get] | : the root entity of the GLXF file Signature ```kotlin val rootEntity: Entity ``` |
| **uri** : Uri [Get] | : the URI of the GLXF file Signature ```kotlin val uri: Uri ``` |
| **version** : String [Get] | : the version of the GLXF file, e.g., "2.0" Signature ```kotlin val version: String ``` |

## Functions

| **destroy** () | Immediately destroys GLXFInfo and all its child resources including all entities inflated as part of the GLXFInfo. Signature ```kotlin fun destroy() ``` |
| --- | --- |
| **getNestedGLXFInfo** ( childName ) | Gets the nested GLXFInfo for a given child name. Example: ```kotlin val myNestedGLXFInfo = myGLXFInfo.getNestedGLXFInfo("childWithNestedGLXFName") ``` Signature ```kotlin fun getNestedGLXFInfo(childName: String): GLXFInfo? ``` Parameters childName: String The name of the child node. Returns [GLXFInfo?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfinfo) The nested GLXFInfo object, or null if not found. |
| **getNestedGLXFInfo** ( childNamePathList ) | Gets the nested GLXFInfo for a given list of child names. The first name should be the highest level child name, with each subsequent name being a child of that nested GLXFInfo Example: ```kotlin val myNestedGLXFInfo = myGLXFInfo.getNestedGLXFInfo(listOf("childOfMyGLXFInfo", "childOf_childOfMyGLXFInfo")) ``` Signature ```kotlin fun getNestedGLXFInfo(childNamePathList: List<String>): GLXFInfo? ``` Parameters childNamePathList: List The list of child names. Returns [GLXFInfo?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfinfo) The nested GLXFInfo object, or null if not found. |
| **getNodeByName** ( name ) | Returns the GLXFNode object for the given name. This gives you access to the node's properties, including the entity inf;ated to represent this node Example: ```kotlin val myPanelEntity = myGLXFInfo.getNodeByName("panel").entity ``` Signature ```kotlin fun getNodeByName(name: String): GLXFNode ``` Parameters name: String The name of the node to retrieve. Returns [GLXFNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfnode) The GLXFNode object associated with the given name. |
| **getNodeByName** ( resId ) | Returns the GLXFNode object for the string value represented by the resource ID. Example: ```kotlin val myPanelEntity = myGLXFInfo.getNodeByName(R.string.panel).entity ``` Signature ```kotlin fun getNodeByName(resId: Int): GLXFNode ``` Parameters resId: Int The resource ID of the node to retrieve. Returns [GLXFNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfnode) The GLXFNode object associated with the given resource ID. |
| **getNodeEntitiesWithNames** () | Gets map of all entities in the GLXFInfo, keyed by their names. Nodes without names will not be included. Signature ```kotlin fun getNodeEntitiesWithNames(): Map<String, Entity> ``` Returns Map |
| **tryGetNodeByName** ( name ) | Returns the GLXFNode object for the given name, or null if it doesn't exist. Example: ```kotlin val myPanelEntity = myGLXFInfo.tryGetNodeByName("panel").entity ?: return ``` Signature ```kotlin fun tryGetNodeByName(name: String): GLXFNode? ``` Parameters name: String The name of the node to retrieve. Returns [GLXFNode?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfnode) The GLXFNode object associated with the given name, or null if it doesn't exist. |
| **tryGetNodeByName** ( resId ) | Returns the GLXFNode object for the given resource ID, or null if it doesn't exist. Example: ```kotlin val myPanelEntity = myGLXFInfo.tryGetNodeByName(R.string.panel).entity ?: return ``` Signature ```kotlin fun tryGetNodeByName(resId: Int): GLXFNode? ``` Parameters resId: Int The resource ID of the node to retrieve. Returns [GLXFNode?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_toolkit_glxfnode) The GLXFNode object associated with the given resource ID, or null if it doesn't exist. |