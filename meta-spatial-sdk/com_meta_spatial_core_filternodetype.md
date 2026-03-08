# FilterNodeType Enum

An enumeration representing the node type of a filter.

Filter nodes are used to build a tree structure that represents complex filtering conditions. Each node type serves a specific purpose in the filter expression.

## Signature

```kotlin
enum FilterNodeType : Enum<FilterNodeType>
```

## Enumeration Constants

| Member | Description |
| --- | --- |
| NOT | A filter node that represents a logical NOT operation. |
| AND | A filter node that represents a logical AND operation. |
| OR | A filter node that represents a logical OR operation. |
| FILTER | A filter node that represents a filter operation. |