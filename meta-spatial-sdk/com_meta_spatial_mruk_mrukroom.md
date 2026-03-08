# MRUKRoom Class

*Modifiers:
final*

Represents a spatial room containing anchors and surfaces detected by the Mixed Reality Utility Kit.

MRUKRoom manages room data including walls, floors, ceilings, and spatial anchors within a physical space. It provides functionality to access room surfaces, check if positions are contained within the room boundaries, and manage the room's lifecycle.

## Signature

```kotlin
class MRUKRoom(var anchor: Anchor)
```

## Constructors

| **MRUKRoom** ( anchor ) | Signature ```kotlin constructor(anchor: Anchor) ``` Parameters anchor: [Anchor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_anchor) The primary anchor that represents this room's coordinate system Returns [MRUKRoom](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroom) |
| --- | --- |

## Properties

| **anchor** : [Anchor](/reference/spatial-sdk/v0.10.1/com_meta_spatial_runtime_anchor) [Get][Set] | The primary anchor that represents this room's coordinate system Signature ```kotlin var anchor: Anchor ``` |
| --- | --- |
| **anchors** : MutableList [Get] | List of all anchor entities in this room. This includes all spatial anchors detected in the room such as walls, floors, ceilings, and furniture. Each entity contains components like MRUKAnchor, MRUKPlane, or MRUKVolume that describe its properties. Signature ```kotlin var anchors: MutableList<Entity> ``` |
| **ceilings** : MutableList [Get] | List of all ceiling anchor entities in this room. Contains entities representing the horizontal surfaces at the top of the room. Signature ```kotlin var ceilings: MutableList<Entity> ``` |
| **entity** : [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get][Set] | The entity representing this room in the scene graph. This entity is created when [MRUKRoom.create](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroom#create) is called and serves as the root for room-related components and transforms. May be null if [MRUKRoom.create](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroom#create) has not been called yet. Signature ```kotlin var entity: Entity? ``` |
| **floors** : MutableList [Get] | List of all floor anchor entities in this room. Contains entities representing the horizontal surfaces at the bottom of the room. Signature ```kotlin var floors: MutableList<Entity> ``` |
| **globalMesh** : [MRUKMesh?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukmesh) [Get][Set] | The global mesh representation of the room, if available. Provides a unified mesh that combines all surfaces in the room. May be null if mesh data is not available or has not been generated. Signature ```kotlin var globalMesh: MRUKMesh? ``` |
| **roomBounds** : [Bound3D](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bound3d) [Get][Set] | The 3D bounding box that encompasses the entire room. Defines the spatial extents of the room in all three dimensions, useful for spatial queries and collision detection. Signature ```kotlin var roomBounds: Bound3D ``` |
| **roomMesh** : [MRUKRoomMesh?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mrukroommesh) [Get][Set] | The high-fidelity room mesh data, if available. Contains detailed mesh geometry including vertex positions and semantic face definitions. Only available when using High Fidelity Scene (Scene V2). May be null for standard scenes. Signature ```kotlin var roomMesh: MRUKRoomMesh? ``` |
| **walls** : MutableList [Get] | List of all wall anchor entities in this room. Contains entities representing the vertical surfaces that form the room's boundaries. Signature ```kotlin var walls: MutableList<Entity> ``` |

## Functions

| **create** () | Creates and initializes the room entity. This method must be called before using the room to ensure the entity is properly initialized. Signature ```kotlin fun create() ``` |
| --- | --- |
| **destroy** () | Destroys this room and all associated entities and anchors. This method cleans up all resources associated with the room, including destroying all anchor entities and the room entity itself. After calling this method, the room should not be used. Signature ```kotlin fun destroy() ``` |
| **getKeyWall** () | Returns the wall entity with the largest width in the room. The width is determined by measuring the x-axis extent of each wall's plane component. This is typically used to identify the most prominent wall for content placement or alignment. Signature ```kotlin fun getKeyWall(): Entity? ``` Returns [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The widest wall entity, or null if no walls exist or no walls have a MRUKPlane component |
| **isPositionInRoom** ( position , testVerticalBounds ) | Checks if a given position is contained within the room's boundaries. This method determines whether a 3D position falls within the spatial bounds of the room. It can optionally test vertical bounds to check if the position is between the floor and ceiling. Signature ```kotlin fun isPositionInRoom(position: Vector3, testVerticalBounds: Boolean = true): Boolean ``` Parameters position: [Vector3](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3) The 3D position to test in world coordinates testVerticalBounds: Boolean If true, checks if the position is between floor and ceiling; if false, only checks horizontal (XZ plane) containment Returns Boolean True if the position is within the room boundaries, false otherwise |
| **setPose** ( pose ) | Sets the pose (position and orientation) of the room entity. Updates the room's transform component with the specified pose, affecting the spatial positioning of the room and all its child anchors. Signature ```kotlin fun setPose(pose: Pose) ``` Parameters pose: [Pose](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_pose) The new pose to apply to the room entity |