# SortBuilder Class

*Modifiers:
final*

A builder class for constructing sorting criteria and configurations.

This builder provides an API for defining complex sorting operations, including:

- Multiple sort criteria with different attribute types - Pagination through the take method - Building the final sort configuration

Example usage -- Sort by the intVar attribute of the TestComponent; if there's a tie, sort by the stringVar attribute, ignoring case. Take the first 10 items:

```kotlin val sortConfig = Query.where{ has(TestComponent.id) }
                      .with {
                        by(TestComponent.intVarData)
                        by(TestComponent.stringVarData).descCaseInsensitive()
                       }.take(0, 10) ```

## Signature

```kotlin
class SortBuilder
```

## Constructors

| **SortBuilder** () | Signature ```kotlin constructor() ``` Returns [SortBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortbuilder) |
| --- | --- |

## Functions

| **take** ( offset , count ) | Defines the range of sorting results by specifying the starting index and the number of items to include. Signature ```kotlin fun take(offset: Int, count: Int): SortBuilder ``` Parameters offset: Int The starting index for the results (0-based). count: Int The number of items to include in the results. Returns [SortBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortbuilder) The current instance of SortBuilder, allowing for method chaining. Example: ```kotlin // Get the first 10 items (items 0-9) { with { by(TestComponent.intVarData) } take(0, 10) } // Get the next 10 items (items 10-19) { with { by(TestComponent.intVarData) } take(10, 10) } ``` |
| --- | --- |
| **with** ( init ) | Configures the sorting criteria using a lambda function. Signature ```kotlin fun with(init: SortCriteriaBuilder.() -> Unit): SortBuilder ``` Parameters init: Function1 A lambda function with a receiver of type SortCriteriaBuilder that defines the sort criteria. The SortCriteriaBuilder instance is the implicit `this` within the lambda, allowing you to call its methods directly. Returns [SortBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortbuilder) The current instance of SortBuilder for method chaining. Example -- Sort by the intVar attribute of the TestComponent; if there's a tie, sort by the stringVar attribute, ignoring case; if there's still a tie, sort by the Z component of the vector3Var attribute: ```kotlin with { by(TestComponent.intVarData) by(TestComponent.stringVarData).descCaseInsensitive() by(TestComponent.vector3VarData).byZ() } ``` |