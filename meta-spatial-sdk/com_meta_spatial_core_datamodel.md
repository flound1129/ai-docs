# DataModel Class

*Modifiers:
final*

DataModel is a class that manages data for Entities, Components, and Attributes in the Spatial SDK ECS architecture.

For debugging and introspecting into the live state of your datamodel, register the [DataModelInspectorFeature](/reference/spatial-sdk/v0.10.1/com_meta_spatial_datamodelinspector_datamodelinspectorfeature) .

The DataModel is also responsible for passing custom events to listeners. Example:

```kotlin val dataModel = EntityContext.getDataModel()
// setup button event listener
button.entity.registerEventListener<EventArgs>("button") { _, _ ->
  // handle event
}
dataModel?.sendEvent(entity, "button", EventArgs("click", dataModel)) ```

Also see [PhysicsSample](https://github.com/meta-quest/Meta-Spatial-SDK-Samples/tree/901965d952d89aef5c5d81d93e5a2b88d275799d/PhysicsSample) sample project for a more in depth example of registering custom event listeners.

## Signature

```kotlin
class DataModel(dataModel_: Long)
```

## Constructors

| **DataModel** ( dataModel_ ) | Signature ```kotlin constructor(dataModel_: Long) ``` Parameters dataModel_: Long Returns [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) |
| --- | --- |

## Functions

| **bumpComponentVersion** ( entityId , componentId ) | Bumps the component version, marking it as "changed" without modifying data. This forces a component to be considered changed for change detection purposes, even when the actual component data hasn't been modified. This will trigger component change listeners and queries that look for changed components. Signature ```kotlin fun bumpComponentVersion(entityId: Long, componentId: Int) ``` Parameters entityId: Long The ID of the entity. componentId: Int The ID of the component to mark as changed. |
| --- | --- |
| **createEntity** () | Creates a new entity in the data model. Signature ```kotlin fun createEntity(): Entity ``` Returns [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The Entity. |
| **createEntity** ( components ) | Creates a new entity in the data model with components. Signature ```kotlin fun createEntity(components: List<ComponentBase>): Entity ``` Parameters components: List Returns [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The Entity. |
| **createEntity** ( components ) | Creates a new entity in the data model with components. Signature ```kotlin fun createEntity(vararg components: ComponentBase): Entity ``` Parameters components: [ComponentBase](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentbase) Returns [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The Entity. |
| **createFilterHandle** ( filterCode , filterIntCode , filterLongCode , filterFloatCode , filterStringCode ) | Creates a pre-compiled filter handle for efficient reuse in CachedQuery. The filter handle compiles the filter bytecode into a std::function once, avoiding the overhead of rebuilding the filter on every query evaluation. The handle is owned by the caller and must be destroyed with [DataModel.Companion.destroyFilterHandle](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel#destroyfilterhandle) when no longer needed. Signature ```kotlin fun createFilterHandle(filterCode: IntArray?, filterIntCode: IntArray?, filterLongCode: LongArray?, filterFloatCode: FloatArray?, filterStringCode: Array<String>?): Long ``` Parameters filterCode: IntArray? The filter bytecode. filterIntCode: IntArray? Integer values used in the filter. filterLongCode: LongArray? Long values used in the filter. filterFloatCode: FloatArray? Float values used in the filter. filterStringCode: Array? String values used in the filter. Returns Long A handle (as Long pointer), or 0L if no filter code was provided. |
| **deleteEntity** ( eid ) | Deletes an entity from the data model. The entity will be included in deleted queries next tick. We recommend using Entity.destroy() instead of this function. Signature ```kotlin fun deleteEntity(eid: Long) ``` Parameters eid: Long The ID of the entity to delete. |
| **getChangedEntitiesSinceWithFilterAndRemoval** ( sinceVersion , componentIds , filterHandle ) | Get all entity IDs that have changed since a given version using a pre-compiled filter handle. Returns packed array: matchingCount, ...matchingIds, ...removedIds Signature ```kotlin fun getChangedEntitiesSinceWithFilterAndRemoval(sinceVersion: ULong, componentIds: IntArray, filterHandle: Long): LongArray? ``` Parameters sinceVersion: ULong The version to check against (exclusive - returns changes after this version). componentIds: IntArray Array of component/attribute IDs to check for. filterHandle: Long The pre-compiled filter handle from [DataModel.createFilterHandle](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel#createfilterhandle) , or 0L for no filter. Returns LongArray? Packed array as described above, or null if no changes. |
| **getChangedEntitiesSinceWithRemoval** ( sinceVersion , componentIds ) | Get all entity IDs that have changed since a given version, packed as: matchingCount, ...matchingIds, ...removedIds Where: - matchingCount: number of entities that have ALL specified components - matchingIds: entity IDs that match (indices 1 to matchingCount) - removedIds: entity IDs that no longer match (indices matchingCount+1 to end) This is used by CachedQuery for incremental updates with component removal support. Signature ```kotlin fun getChangedEntitiesSinceWithRemoval(sinceVersion: ULong, componentIds: IntArray): LongArray? ``` Parameters sinceVersion: ULong The version to check against (exclusive - returns changes after this version). componentIds: IntArray Array of component/attribute IDs to check for. Returns LongArray? Packed array as described above, or null if no changes. |
| **getComponentIdsForEntity** ( entityId , componentManager ) | Gets all component IDs associated with a given entity. This function iterates through all registered component IDs (where componentId == attrId in attributeInfoMap) and checks if the entity has data for each component using a single batch JNI call to minimize JNI boundary crossings. Signature ```kotlin fun getComponentIdsForEntity(entityId: Long, componentManager: ComponentManager): IntArray ``` Parameters entityId: Long The entity ID to query components for. componentManager: [ComponentManager](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentmanager) The ComponentManager containing the attributeInfoMap. Returns IntArray An IntArray of component IDs that the entity has. |
| **getEventListenerForEvent** ( eventType ) | Gets all listeners registered for a specific event type. Parameters eventType: String The type of event to get listeners for. Returns Set A set of entity-listener pairs for the specified event type. |
| **getKeyValueMap** ( id , attribute ) | Signature ```kotlin inline fun <T, V> getKeyValueMap(id: Long, attribute: Int): HashMap<T, V> ``` Parameters id: Long attribute: Int Returns HashMap |
| **getLastUpdateVersion** () | Experimental API. This gets a long that represents the last updated version of the data model. This is important for making updates the same tick as other component changes. Example: ```kotlin class MyComponentSystem() : SystemBase() { private var lastUpdateVersion = 0UL @OptIn(SpatialSDKExperimentalAPI::class) override fun execute() { for (entity in Query.where { changedSince(MyComponent.id, lastUpdateVersion) }.eval()) { // handle changing entity } lastUpdateVersion = EntityContext.getDataModel()!!.getLastUpdateVersion() } } ``` Signature ```kotlin fun getLastUpdateVersion(): ULong ``` Returns ULong |
| **hasAllKeys** ( id , componentIds ) | Batch check if an entity has all specified component attributes. This is more efficient than calling hasKey() multiple times as it reduces JNI overhead. Signature ```kotlin fun hasAllKeys(id: Long, componentIds: IntArray): Boolean ``` Parameters id: Long The ID of the entity. componentIds: IntArray Array of component/attribute IDs to check for. Returns Boolean True if the entity has all specified components, false otherwise. |
| **hasKey** ( id , attribute ) | Checks if an entity has a specific attribute. Signature ```kotlin fun hasKey(id: Long, attribute: Int): Boolean ``` Parameters id: Long The ID of the entity. attribute: Int The attribute ID to check for. Returns Boolean True if the entity has the attribute, false otherwise. |
| **nativeGetKeyValueMap** ( dataModel , id , attribute ) | Signature ```kotlin external fun nativeGetKeyValueMap(dataModel: Long, id: Long, attribute: Int): Array<Any> ``` Parameters dataModel: Long id: Long attribute: Int Returns Array |
| **registerAttributeListener** ( attribute , listener ) | Registers a listener for changes to a specific attribute. Signature ```kotlin fun registerAttributeListener(attribute: Int, listener: AttributeListener) ``` Parameters attribute: Int The ID of the attribute to listen for changes on. listener: [AttributeListener](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_attributelistener) The callback to invoke when the attribute changes. |
| **registerComponentListener** ( componentID , componentClass , listener ) | Registers a listener for changes to a specific component. Signature ```kotlin fun registerComponentListener(componentID: Int, componentClass: KClass<*>, listener: ComponentListener) ``` Parameters componentID: Int The ID of the component to listen for changes on. componentClass: KClass The class of the component. listener: [ComponentListener](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_componentlistener) The callback to invoke when the component changes. |
| **registerDeleteListener** ( listener ) | Registers a listener to be notified when any entity is deleted. The listener is held via a weak reference, allowing the owning object (e.g., CachedQuery) to be garbage collected even without explicitly calling [DataModel.removeDeleteListener](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel#removedeletelistener) . Stale references are automatically cleaned up during delete notifications. For proper cleanup semantics, callers should retain a strong reference to the returned [DeleteListenerHolder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_deletelistenerholder) for as long as they want to receive notifications. Signature ```kotlin fun registerDeleteListener(listener: (Long) -> Unit): DeleteListenerHolder ``` Parameters listener: Function1 The callback to invoke with the entity ID when an entity is deleted. Returns [DeleteListenerHolder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_deletelistenerholder) A [DeleteListenerHolder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_deletelistenerholder) that the caller should retain. When this holder is garbage collected, the listener will automatically stop receiving notifications. |
| **registerEventListener** ( entity , eventType , listener ) | Registers a listener for events on a specific entity. Signature ```kotlin fun registerEventListener(entity: Entity, eventType: String, listener: EventListener<EventArgs>) ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity to listen for events on. eventType: String The type of event to listen for. listener: [EventListener](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_eventlistener) The callback to invoke when the event occurs. |
| **registerLinkedEntityAttribute** ( attributeID ) | This method is experimental and is subject to change in the future. Registering a linked entity attribute makes it so that the DataModel will build a hierarchy based on the given entity attribute. This means that you can query for children of a given entity based on the registered linked entity attribute. Example: In Your Activity's OnCreate: ```kotlin EntityContext.getDataModel()?.registerLinkedEntityAttribute(MyComponent.myEntityAttributeData) ``` Then you can query for children of a certain entity (Where their MyComponent.myEntityAttribute is myEntity) in a System Query: ```kotlin val query = Query.where { childrenOf(myEntity, MyComponent.myEntityAttributeData) } ``` Signature ```kotlin fun registerLinkedEntityAttribute(attributeID: Int) ``` Parameters attributeID: Int |
| **removeComponentListener** ( componentID ) | Removes a previously registered component listener. Signature ```kotlin fun removeComponentListener(componentID: Int) ``` Parameters componentID: Int The ID of the component to stop listening for changes on. |
| **removeDeleteListener** ( holder ) | Removes a previously registered delete listener. Note: With weak reference semantics, explicit removal is optional. If the [DeleteListenerHolder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_deletelistenerholder) goes out of scope, the listener will automatically stop receiving notifications and be cleaned up during the next delete event. Signature ```kotlin fun removeDeleteListener(holder: DeleteListenerHolder) ``` Parameters holder: [DeleteListenerHolder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_deletelistenerholder) The holder returned from [DataModel.registerDeleteListener](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel#registerdeletelistener) . |
| **willBeDeleted** ( eid ) | Checks if an entity will be deleted in the next frame. Returns true if deleteEntity() has been called on this entity in the current frame, but the entity hasn't been fully removed yet. The entity will be inaccessible starting in the next frame. Signature ```kotlin fun willBeDeleted(eid: Long): Boolean ``` Parameters eid: Long The ID of the entity to check. Returns Boolean True if the entity is scheduled for deletion, false otherwise. |

## Companion Object

### Companion Object Functions

| **destroyFilterHandle** ( filterHandle ) | Destroys a filter handle created by [DataModel.createFilterHandle](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel#createfilterhandle) . This is a static method that doesn't require a DataModel instance, allowing filter handles to be cleaned up even if the DataModel has been destroyed. Signature ```kotlin fun destroyFilterHandle(filterHandle: Long) ``` Parameters filterHandle: Long The handle to destroy. |
| --- | --- |
| **getLocalDataModelTime** () | Gets the local time based on the data model. Signature ```kotlin fun getLocalDataModelTime(): Long ``` Returns Long |

## Inner Class

### KeyIterator Class

*Modifiers:
final*

Signature
```kotlin
inner class KeyIterator(dm_: DataModel, it_: Long)
```

Constructors
| **KeyIterator** ( dm_ , it_ ) | Signature ```kotlin constructor(dm_: DataModel, it_: Long) ``` Parameters dm_: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) it_: Long Returns DataModel.KeyIterator |
| --- | --- |

Functions
| **close** () | Signature ```kotlin fun close() ``` |
| --- | --- |
| **end** () | Signature ```kotlin fun end(): Boolean ``` Returns Boolean |
| **entity** () | Signature ```kotlin fun entity(): Entity ``` Returns [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) |
| **finalize** () | Signature ```kotlin fun finalize() ``` |
| **next** () | Signature ```kotlin operator fun next() ``` |