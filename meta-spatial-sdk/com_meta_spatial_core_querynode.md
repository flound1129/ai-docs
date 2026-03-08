# QueryNode Class

*Modifiers:
final*

A class representing a node in a query tree.

## Signature

```kotlin
class QueryNode(val type: QueryNodeType, val args: Array<Int>?, val queryBuilder: QueryBuilder)
```

## Constructors

| **QueryNode** ( type , args , queryBuilder ) | Signature ```kotlin constructor(type: QueryNodeType, args: Array<Int>?, queryBuilder: QueryBuilder) ``` Parameters type: [QueryNodeType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_querynodetype) args: Array? queryBuilder: [QueryBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_querybuilder) Returns [QueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_querynode) |
| --- | --- |

## Properties

| **args** : Array? [Get] | Signature ```kotlin val args: Array<Int>? ``` |
| --- | --- |
| **left** : [QueryNode?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_querynode) [Get][Set] | Signature ```kotlin var left: QueryNode? ``` |
| **parent** : [QueryNode?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_querynode) [Get][Set] | Signature ```kotlin var parent: QueryNode? ``` |
| **queryBuilder** : [QueryBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_querybuilder) [Get] | Signature ```kotlin val queryBuilder: QueryBuilder ``` |
| **right** : [QueryNode?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_querynode) [Get][Set] | Signature ```kotlin var right: QueryNode? ``` |
| **type** : [QueryNodeType](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_querynodetype) [Get] | Signature ```kotlin val type: QueryNodeType ``` |

## Functions

| **and** ( b ) | Performs a logical AND operation on multiple queries. The resulting query will match entities that match ALL of the input queries. Example: ```kotlin // Find entities that have both a Mesh and a Transform component val query = Query.where { has(Mesh.id) and has(Transform.id) } // Find entities that have a Grabbable component and have had their Transform changed val query = Query.where { has(Grabbable.id) and changed(Transform.id) } ``` Signature ```kotlin infix fun and(b: QueryNode): QueryNode ``` Parameters b: [QueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_querynode) The other query node. Returns [QueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_querynode) A new query node representing the AND operation. |
| --- | --- |
| **or** ( b ) | Performs a logical OR operation on multiple queries. The resulting query will match entities that match ANY of the input queries. Example: ```kotlin // Find entities that have either a Mesh or a Panel component val query = Query.where { has(Mesh.id) or has(Panel.id) } ``` Signature ```kotlin infix fun or(b: QueryNode): QueryNode ``` Parameters b: [QueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_querynode) The other query node. Returns [QueryNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_querynode) A new query node representing the OR operation. |