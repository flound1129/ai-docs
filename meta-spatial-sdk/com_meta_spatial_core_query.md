# Query Class

*Modifiers:
final*

A query system for finding and filtering entities in the Spatial SDK.

Use the DSL builder pattern with Query.where { ... } to create queries. The query DSL allows you to specify conditions on entities, such as having specific components or having changed components. You can also combine conditions with logical operators (and, or) to create complex queries.

Example - Find all entities with a specific component:

```kotlin val entities = Query.where { has(Transform.id) }.eval() ```

Example - Find entities with multiple components:

```kotlin val entities = Query.where { has(Transform.id, Mesh.id) }.eval() ```

Example - Find entities with components that have changed in the last tick:

```kotlin val entities = Query.where { changed(Transform.id) }.eval() ```

Example - Combining queries with logical operators:

```kotlin val entities = Query.where { (has(Transform.id) and has(Mesh.id)) or has(Panel.id) }.eval() ```

Example - Using filters with queries:

```kotlin val entities = Query.where { has(TestComponent.id) }
                    .filter { by(TestComponent.intVarData).isEqualTo(1) }
                    .eval() ```

Example - Using sort with queries:

```kotlin val entities = Query.where { has(TestComponent.id) }
                    .sort {
                      with {
                        by(TestComponent.intVarData)
                      }
                    }.eval() ```

## Signature

```kotlin
class Query
```

## Properties

| **prev_** : [Query?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_query) [Get][Set] | Signature ```kotlin var prev_: Query? ``` |
| --- | --- |
| **query_** : IntArray [Get][Set] | Signature ```kotlin var query_: IntArray ``` |

## Functions

| **build** () | Evaluates the query for a specific DataModel and returns the a built query. Signature ```kotlin fun build(): BuiltQuery ``` Returns BuiltQuery A BuiltQuery that can be used later. |
| --- | --- |
| **eval** () | Evaluates the query and returns a sequence of entities that match the query criteria. This method executes the query against the current DataModel and returns matching entities. The result is a lazy sequence, so operations on it are only performed as needed. Example: ```kotlin // Find all entities with a Transform component and iterate through them Query.where { has(Transform.id) } .eval() .forEach { entity -> // Process each entity val transform = entity.getComponent<Transform>() // ... } ``` Signature ```kotlin fun eval(): Sequence<Entity> ``` Returns Sequence<Entity> A sequence of entities that match the query criteria. |
| **eval** ( dm ) | Evaluates the query against a specific DataModel and returns matching entities. In a Spatial app, there is only one DataModel, so this method is rarely used. Use eval() instead to evaluate the query against the current DataModel. Example: ```kotlin // Evaluate a query against a specific DataModel val customDataModel = DataModel.create() val entities = Query.where { has(Transform.id) }.eval(customDataModel) ``` Signature ```kotlin fun eval(dm: DataModel): Sequence<Entity> ``` Parameters dm: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The DataModel to evaluate the query against. Returns Sequence<Entity> A sequence of entities that match the query criteria. |
| **filter** ( initializer ) | Specifies the filter criteria for the query. Example: ```kotlin // Find all entities with a TestComponent component and filter by the intVarData field val entities = Query.where { has(TestComponent.id) } .filter { by(TestComponent.intVarData).isEqualTo(1) } .eval() ``` Signature ```kotlin fun filter(initializer: FilterBuilder.() -> Unit): Query ``` Parameters initializer: Function1 A receiver function of the FilterBuilder. Returns [Query](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_query) The Query object. |
| **sort** ( initializer ) | Specifies the sort order for the query. Example: ```kotlin // Find all entities with a TestComponent component and sort by the intVarData field val entities = Query.where { has(TestComponent.id) } .sort { with { by(TestComponent.intVarData) } } .eval() ``` Signature ```kotlin fun sort(initializer: SortBuilder.() -> Unit): Query ``` Parameters initializer: Function1 A receiver function of the SortBuilder. Returns [Query](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_query) The Query object. |

## Companion Object

### Companion Object Functions

| **eval** ( preBuiltQuery ) | Evaluates a pre-built query and returns a sequence of entities that match the query. Signature ```kotlin fun eval(preBuiltQuery: BuiltQuery): Sequence<Entity> ``` Parameters preBuiltQuery: BuiltQuery The pre-built query to evaluate. Returns Sequence<Entity> A sequence of entities that match the query. |
| --- | --- |
| **eval** ( dm , preBuiltQuery ) | Evaluates a pre-built query on a specific DataModel and returns a sequence of entities that match the query. Signature ```kotlin fun eval(dm: DataModel, preBuiltQuery: BuiltQuery): Sequence<Entity> ``` Parameters dm: [DataModel](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_datamodel) The DataModel to evaluate the query against. preBuiltQuery: BuiltQuery The pre-built query to evaluate. Returns Sequence<Entity> A sequence of entities that match the query. |
| **where** ( initializer ) | DSL for building queries. The DSL provides an interface for building complex queries with logical operations. Example: ```kotlin // Find entities that have both Transform and Mesh components val query = Query.where { has(Transform.id) and has(Mesh.id) } // Find entities that have either changed Transform or changed Mesh components val query = Query.where { changed(Transform.id) or changed(Mesh.id) } // Find entities that have a Controller component and are local val query = Query.where { has(Controller.id) } .filter { isLocal() } .eval() // Find entities with a specific component that have changed in the last tick val query = Query.where { has(Grabbable.id) and changed(Transform.id) } ``` Signature ```kotlin fun where(initializer: QueryBuilder.() -> Unit): Query ``` Parameters initializer: Function1 DSL receiver function that builds the query Returns [Query](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_query) Query object ready for evaluation or further refinement |