# Anchor Class

*Modifiers:
final*

Represents a spatial anchor in a mixed reality environment.

Anchors are persistent spatial references that maintain their position relative to the physical environment. They can represent detected objects, planes, or user-defined points in space. Anchors can have various components (defined by [Anchor.SpaceComponentType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_anchor#spacecomponenttype) ) that provide different capabilities and information.

## Signature

```kotlin
data class Anchor(var handle: Long, var uuid: UUID)
```

## Constructors

| **Anchor** ( handle , uuid ) | Signature ```kotlin constructor(handle: Long, uuid: UUID) ``` Parameters handle: Long Native handle to the underlying OpenXR space object uuid: UUID Unique identifier for this anchor Returns [Anchor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_anchor) |
| --- | --- |

## Properties

| **handle** : Long [Get][Set] | Native handle to the underlying OpenXR space object Signature ```kotlin var handle: Long ``` |
| --- | --- |
| **uuid** : UUID [Get][Set] | Unique identifier for this anchor Signature ```kotlin var uuid: UUID ``` |

## Inner Classes

### FetchOptions Class

*Modifiers:
final*

Options for fetching anchors from the MR subsystem.

Used with the scene.discoverSpaces method to specify which anchors to retrieve based on their UUIDs and/or component types.

Signature
```kotlin
data class FetchOptions(var uuids: Array<UUID> = arrayOf(), var componentTypes: Array<Anchor.SpaceComponentType> = arrayOf())
```

Constructors
| **FetchOptions** ( uuids , componentTypes ) | Signature ```kotlin constructor(uuids: Array<UUID> = arrayOf(), componentTypes: Array<Anchor.SpaceComponentType> = arrayOf()) ``` Parameters uuids: Array Array of UUIDs to fetch specific anchors componentTypes: Array Array of component types to filter anchors by capability Returns Anchor.FetchOptions |
| --- | --- |

Properties
| **componentTypes** : Array [Get][Set] | Array of component types to filter anchors by capability Signature ```kotlin var componentTypes: Array<Anchor.SpaceComponentType> ``` |
| --- | --- |
| **uuids** : Array [Get][Set] | Array of UUIDs to fetch specific anchors Signature ```kotlin var uuids: Array<UUID> ``` |

### RoomLayout Class

*Modifiers:
final*

Represents the layout of a room detected in the physical environment.

Contains references to the floor, ceiling, and walls as separate anchors. This information is available for anchors with the [Anchor.SpaceComponentType.RoomLayout](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_anchor#spacecomponenttype#roomlayout) component.

Signature
```kotlin
data class RoomLayout(var floor: UUID, var ceiling: UUID, var walls: Array<UUID>)
```

Constructors
| **RoomLayout** ( floor , ceiling , walls ) | Signature ```kotlin constructor(floor: UUID, ceiling: UUID, walls: Array<UUID>) ``` Parameters floor: UUID UUID of the anchor representing the floor ceiling: UUID UUID of the anchor representing the ceiling walls: Array Array of UUIDs for anchors representing the walls Returns Anchor.RoomLayout |
| --- | --- |

Properties
| **ceiling** : UUID [Get][Set] | UUID of the anchor representing the ceiling Signature ```kotlin var ceiling: UUID ``` |
| --- | --- |
| **floor** : UUID [Get][Set] | UUID of the anchor representing the floor Signature ```kotlin var floor: UUID ``` |
| **walls** : Array [Get][Set] | Array of UUIDs for anchors representing the walls Signature ```kotlin var walls: Array<UUID> ``` |

### SpaceTriangleMesh Class

*Modifiers:
final*

Represents a triangle mesh associated with an anchor.

Contains the vertex positions and triangle indices that define the mesh geometry. This information is available for anchors with the [Anchor.SpaceComponentType.TriangleMesh](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_anchor#spacecomponenttype#trianglemesh) component.

Signature
```kotlin
data class SpaceTriangleMesh(val vertices: Array<Vector3>, val indices: IntArray)
```

Constructors
| **SpaceTriangleMesh** ( vertices , indices ) | Signature ```kotlin constructor(vertices: Array<Vector3>, indices: IntArray) ``` Parameters vertices: Array Array of 3D positions defining the mesh vertices indices: IntArray Integer array defining the triangle indices (groups of 3 indices form triangles) Returns Anchor.SpaceTriangleMesh |
| --- | --- |

Properties
| **indices** : IntArray [Get] | Integer array defining the triangle indices (groups of 3 indices form triangles) Signature ```kotlin val indices: IntArray ``` |
| --- | --- |
| **vertices** : Array [Get] | Array of 3D positions defining the mesh vertices Signature ```kotlin val vertices: Array<Vector3> ``` |

## Inner Enum

### SpaceComponentType Enum

Defines the types of components that can be associated with a space/anchor.

Each component type provides different capabilities or information about the space. Components can be enabled or disabled using the scene.setSpaceComponentStatus method.

Signature
```kotlin
enum SpaceComponentType : Enum<Anchor.SpaceComponentType>
```

Enumeration Constants
| Member | Description |
| --- | --- |
| Locatable | Indicates the space can be located (positioned) in the physical environment. |
| Storable | Indicates the space can be stored persistently. |
| Sharable | Indicates the space can be shared with other devices/users. |
| Bounded2D | Indicates the space has a 2D boundary. |
| Bounded3D | Indicates the space has a 3D boundary. |
| SemanticLabels | Indicates the space has semantic labels describing what it represents. |
| RoomLayout | Indicates the space contains room layout information. |
| SpaceContainer | Indicates the space can contain other spaces. |
| TriangleMesh | Indicates the space has an associated triangle mesh. |

Properties
| **value** : Int [Get] | Integer value corresponding to the native OpenXR component type Signature ```kotlin val value: Int ``` |
| --- | --- |