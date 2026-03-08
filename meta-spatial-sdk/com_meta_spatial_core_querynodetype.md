# QueryNodeType Enum

An enumeration representing the node type of a query.

## Signature

```kotlin
enum QueryNodeType : Enum<QueryNodeType>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| CHILDREN_OF | A query node that represents a query that returns all child entities of an entity |
| CHANGED | A query node that represents a query that checks if a component has changed in the last tick. |
| CHANGED_SINCE | A query node that represents a query that checks if a component has changed since a datamodel version number. |
| HAS_CHANGED_SINCE | A query node that represents a query that checks if an entity has ALL specified components AND at least one of them has changed since a datamodel version number. |
| AND | A query node that represents a logical AND operation. |
| HAS | A query node that represents a query that checks if an entity has a specific component. |
| OR | A query node that represents a logical OR operation. |