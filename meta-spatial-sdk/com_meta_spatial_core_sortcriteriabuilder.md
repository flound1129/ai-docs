# SortCriteriaBuilder Class

*Modifiers:
final*

Builder class for creating sort criteria. All sort criteria are created using the "by" function.

This builder provides an API for defining multiple sort criteria that can be combined to create complex sorting logic. Example:

```kotlin val entities = Query.where{ has(TestComponent.id) }
                    .sort {
                      with {
                        by(TestComponent.intVarData).desc()
                       }
                     }.eval() ```

## Signature

```kotlin
class SortCriteriaBuilder
```

## Constructors

| **SortCriteriaBuilder** () | Signature ```kotlin constructor() ``` Returns [SortCriteriaBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_sortcriteriabuilder) |
| --- | --- |

## Functions

| **build** () | Signature ```kotlin fun build(): List<SortCriterion> ``` Returns List |
| --- | --- |
| **by** ( intData ) | Create a sorting criterion for a given int attribute data. Signature ```kotlin fun by(intData: IntAttributeData): IntSortCriterion ``` Parameters intData: [IntAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattributedata) The int attribute data to sort by. Returns [IntSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intsortcriterion) An IntSortCriterion instance that can be further configured with sort options. Example: ```kotlin with { by(TestComponent.intVarData) } // Sort by integer values in ascending order ``` |
| **by** ( longData ) | Create a sorting criterion for a given long attribute data. Signature ```kotlin fun by(longData: LongAttributeData): LongSortCriterion ``` Parameters longData: [LongAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_longattributedata) The long attribute data to sort by. Returns [LongSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_longsortcriterion) A LongSortCriterion instance that can be further configured with sort options. Example: ```kotlin with { by(TestComponent.longVarData).desc() } // Sort by long values in descending order ``` |
| **by** ( floatData ) | Create a sorting criterion for a given float attribute data. Signature ```kotlin fun by(floatData: FloatAttributeData): FloatSortCriterion ``` Parameters floatData: [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) The float attribute data to sort by. Returns [FloatSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatsortcriterion) A FloatSortCriterion instance that can be further configured with sort options. Example: ```kotlin with { by(TestComponent.floatVarData) } // Sort by float values in ascending order ``` |
| **by** ( stringData ) | Create a sorting criterion for a given string attribute data. Signature ```kotlin fun by(stringData: StringAttributeData): StringSortCriterion ``` Parameters stringData: [StringAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_stringattributedata) The string attribute data to sort by. Returns [StringSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_stringsortcriterion) A StringSortCriterion instance that can be further configured with sort options, including case sensitivity options. Example: ```kotlin with { by(TestComponent.stringVarData).descCaseInsensitive() } // Sort strings in descending order, ignoring case ``` |
| **by** ( vec2Data ) | Create a sorting criterion for a given vector2 attribute data. Signature ```kotlin fun by(vec2Data: Vector2AttributeData): Vector2SortCriterion ``` Parameters vec2Data: [Vector2AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2attributedata) The vector2 attribute data to sort by. Returns [Vector2SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2sortcriterion) A Vector2SortCriterion instance that can be further configured to sort by specific components (X or Y) and sort direction. Example: ```kotlin with { by(TestComponent.vector2VarData).byX() } // Sort by X component in ascending order with { by(TestComponent.vector2VarData).byY().desc() } // Sort by Y component in descending order ``` |
| **by** ( vec3Data ) | Create a sorting criterion for a given vector3 attribute data. Signature ```kotlin fun by(vec3Data: Vector3AttributeData): Vector3SortCriterion ``` Parameters vec3Data: [Vector3AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3attributedata) The vector3 attribute data to sort by. Returns [Vector3SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3sortcriterion) A Vector3SortCriterion instance that can be further configured to sort by specific components (X, Y, or Z) and sort direction. Example: ```kotlin with { by(TestComponent.vector3VarData).byX() } // Sort by X component in ascending order with { by(TestComponent.vector3VarData).byY().desc() } // Sort by Y component in descending order with { by(TestComponent.vector3VarData).byZ() } // Sort by Z component in ascending order ``` |
| **by** ( vec4Data ) | Create a sorting criterion for a given vector4 attribute data. Signature ```kotlin fun by(vec4Data: Vector4AttributeData): Vector4SortCriterion ``` Parameters vec4Data: [Vector4AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4attributedata) The vector4 attribute data to sort by. Returns [Vector4SortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4sortcriterion) A Vector4SortCriterion instance that can be further configured to sort by specific components (X, Y, Z, or W) and sort direction. Example: ```kotlin with { by(TestComponent.vector4VarData).byX().desc() } // Sort by X component in descending order with { by(TestComponent.vector4VarData).byY() } // Sort by Y component in ascending order with { by(TestComponent.vector4VarData).byZ().desc() } // Sort by Z component in descending order with { by(TestComponent.vector4VarData).byW() } // Sort by W component in ascending order ``` |
| **by** ( poseData ) | Create a sorting criterion for a given pose attribute data. Signature ```kotlin fun by(poseData: PoseAttributeData): PoseSortCriterion ``` Parameters poseData: [PoseAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_poseattributedata) The pose attribute data to sort by. Returns [PoseSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_posesortcriterion) A PoseSortCriterion instance that can be further configured to sort by specific position components (X, Y, Z) or orientation components (W, X, Y, Z) and sort direction. Example: ```kotlin with { by(TestComponent.poseVarData).byPositionX().desc() } // Sort by position X in descending order with { by(TestComponent.poseVarData).byPositionY() } // Sort by position Y in ascending order with { by(TestComponent.poseVarData).byOrientationW().desc() } // Sort by orientation W in descending order ``` |
| **by** ( timeData ) | Create a sorting criterion for a given time attribute data. Signature ```kotlin fun by(timeData: TimeAttributeData): TimeSortCriterion ``` Parameters timeData: [TimeAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_timeattributedata) The time attribute data to sort by. Returns [TimeSortCriterion](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_timesortcriterion) A TimeSortCriterion instance that can be further configured with sort options. Example: ```kotlin with { by(TestComponent.timeVarData).desc() } // Sort by time values in descending order ``` |