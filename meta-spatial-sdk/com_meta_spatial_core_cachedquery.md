# CachedQuery Class

*Modifiers:
final*

A cached query that maintains a stable entity set and updates incrementally.

Unlike [Query.eval](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_query#eval) which re-executes the full native query each call, CachedQuery:

- Returns the same [List](/reference/spatial-sdk/v0.10.1/kotlin_collections_list) instance when no entities have been added/removed - Processes only changed entities when updates occur (no spiky performance) - Provides callbacks for entity lifecycle events with filtering capability

```kotlin class MySystem : SystemBase() {
    private val enemies = CachedQuery.create { has(Enemy.id, Health.id) }
    override fun execute() {
        // Returns same List instance if membership unchanged
        // Only does native work when entities added/removed
        for (entity in enemies.get()) {
            val health = entity.getComponent<Health>()
            // getComponent uses existing timestamp caching
        }
    }
} ```

Use filter to add native-level filtering that is applied both during initial query and incremental updates.

```kotlin private val activeEnemies = CachedQuery.create {
    where { has(Enemy.id) }.filter { by(Enemy.statusData).isEqualTo(Status.ACTIVE) }
} ```

Use [CachedQuery.onAdd](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery#onadd) and [CachedQuery.onUpdate](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery#onupdate) callbacks to filter which entities are included in the result set. Return `true` to include the entity, `false` to exclude it.

```kotlin private val activeEnemies = CachedQuery.create { has(Enemy.id) }
    .onAdd { entity ->
        // Called when entity first matches the query
        // Return true to include in result set
        entity.getComponent<Enemy>().isActive
    }
    .onUpdate { entity ->
        // Called when a tracked component changes on a matching entity
        // Return true to keep in result set, false to remove
        entity.getComponent<Enemy>().isActive
    }
    .onDelete { entity ->
        // Called when entity is removed from result set (destroyed or no longer matches)
        cleanupEnemyState(entity)
    } ```

## See Also

- [Query](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_query)

## Signature

```kotlin
class CachedQuery
```

## Functions

| **contains** ( entity ) | Check if an entity is in the result set. Signature ```kotlin fun contains(entity: Entity): Boolean ``` Parameters entity: [Entity](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The entity to check. Returns Boolean `true` if the entity is currently in the cached result set. |
| --- | --- |
| **count** () | Returns the number of entities matching the query. O(1) after first [CachedQuery.get](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery#get) call. Signature ```kotlin fun count(): Int ``` Returns Int |
| **dispose** () | Unregisters the delete listener and destroys the filter handle. Call this when the CachedQuery is no longer needed. Note: With weak reference semantics, calling dispose() is optional for the delete listener. If the CachedQuery goes out of scope without calling dispose(), the listener will automatically stop receiving notifications and be cleaned up during the next delete event. However, the filter handle holds native memory that will only be released when dispose() is called or when the CachedQuery is garbage collected with a finalizer. Signature ```kotlin fun dispose() ``` |
| **get** () | Get entities matching the query. Returns the SAME [List](/reference/spatial-sdk/v0.10.1/kotlin_collections_list) instance if membership hasn't changed since the last call. When entities are added or removed, callbacks are invoked and a new list is returned. Cost breakdown: - No changes: O(1) - single version check - With changes: O(delta) - processes only added/removed/updated entities - First call: O(n) - full query Signature ```kotlin fun get(): List<Entity> ``` Returns List List of entities matching the query (after callback filtering). |
| **invalidate** () | Force a full re-query on the next [CachedQuery.get](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery#get) call. Use this after major scene changes where incremental updates may be less efficient than a full re-query. Signature ```kotlin fun invalidate() ``` |
| **isEmpty** () | Returns `true` if no entities match the query. Signature ```kotlin fun isEmpty(): Boolean ``` Returns Boolean |
| **onAdd** ( callback ) | Register a callback invoked when an entity first matches the query. The callback receives the entity and should return: - `true` to include the entity in the result set - `false` to exclude the entity (it won't appear in [CachedQuery.get](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery#get) results) If no callback is registered, all matching entities are included. Example: ```kotlin CachedQuery.create { has(Enemy.id) } .onAdd { entity -> val enemy = entity.getComponent<Enemy>() enemy.isActive // Only include active enemies } ``` Signature ```kotlin fun onAdd(callback: (Entity) -> Boolean): CachedQuery ``` Parameters callback: Function1 Function that receives the entity and returns whether to include it. Returns [CachedQuery](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery) This CachedQuery for chaining. |
| **onDelete** ( callback ) | Register a callback invoked when an entity is removed from the result set. This is called when: - The entity is destroyed - The entity loses a required component - [CachedQuery.onUpdate](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery#onupdate) returns `false` for the entity Use this for cleanup logic like releasing resources associated with the entity. Example: ```kotlin CachedQuery.create { has(Enemy.id) } .onDelete { entity -> enemyStateMap.remove(entity) Log.d("Enemy", "Removed from tracking: ${entity.id}") } ``` Signature ```kotlin fun onDelete(callback: (Entity) -> Unit): CachedQuery ``` Parameters callback: Function1 Function that receives the entity being removed. Returns [CachedQuery](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery) This CachedQuery for chaining. |
| **onUpdate** ( callback ) | Register a callback invoked when a tracked component changes on a matching entity. The callback receives the entity and should return: - `true` to keep the entity in the result set - `false` to remove the entity from the result set If no callback is registered, entities remain in the set as long as they have the required components. Note: This is called when component data changes, not when components are added/removed. For component add/remove, see [CachedQuery.onAdd](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery#onadd) and [CachedQuery.onDelete](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery#ondelete) . Example: ```kotlin CachedQuery.create { has(Enemy.id, Health.id) } .onUpdate { entity -> val health = entity.getComponent<Health>() health.current 0 // Remove dead enemies from result set } ``` Signature ```kotlin fun onUpdate(callback: (Entity) -> Boolean): CachedQuery ``` Parameters callback: Function1 Function that receives the entity and returns whether to keep it. Returns [CachedQuery](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery) This CachedQuery for chaining. |

## Companion Object

### Companion Object Functions

| **create** ( dm , initializer ) | Creates a new CachedQuery using a restricted DSL that requires `where { ... }` . All CachedQuery usage must go through `where` , and `filter` is optional after `where` . Example: ```kotlin // Basic usage (no filter) val enemies = CachedQuery.create { where { has(Enemy.id, Health.id) } } val players = CachedQuery.create { where { has(Player.id) and has(Transform.id) } } // With filter val activeEnemies = CachedQuery.create { where { has(Enemy.id) }.filter { by(Enemy.statusData).isEqualTo(Status.ACTIVE) } } ``` Signature ```kotlin fun create(dm: DataModel = EntityContext.getDataModel()!!, initializer: CachedQueryBuilder.() -> FilteredCachedQueryNode): CachedQuery ``` Parameters dm: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The DataModel to query against. Defaults to the current EntityContext. initializer: Function1 Query DSL block using [CachedQueryBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerybuilder) syntax that returns a [FilteredCachedQueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filteredcachedquerynode) via [CachedQueryBuilder.where](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquerybuilder#where) . Returns [CachedQuery](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_cachedquery) A new CachedQuery instance. |
| --- | --- |