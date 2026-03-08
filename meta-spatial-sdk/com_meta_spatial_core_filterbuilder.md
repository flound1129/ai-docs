# FilterBuilder Class

*Modifiers:
final*

A filtering system for refining entity queries in the Spatial SDK.

The FilterBuilder class provides an API for constructing complex filter conditions that can be applied to Query results. Filters allow you to narrow down query results based on component attribute values, using various comparison operations and logical operators.

Filters are typically used in conjunction with the Query class to find entities that not only have specific components but also have specific values for those components' attributes.

Example - Basic filtering by attribute value:

```kotlin // Find entities with TestComponent where intVar equals 1
val entities = Query.where { has(TestComponent.id) }
                    .filter { by(TestComponent.intVarData).isEqualTo(1) }
                    .eval() ```

Example - Combining multiple filters with logical operators:

```kotlin // Find entities with TestComponent where intVar 0 AND floatVar < 0.5
val entities = Query.where { has(TestComponent.id) }
                    .filter { by(TestComponent.intVarData).greaterThan(0) and
                              by(TestComponent.floatVarData).lessThan(0.5f) }
                    .eval() ```

Example - Using the NOT operator:

```kotlin // Find entities with TestComponent where intVar is NOT equal to 1
val entities = Query.where { has(TestComponent.id) }
                    .filter {  not(by(TestComponent.intVarData).isEqualTo(1)) }
                    .eval() ```

Example - Filtering local entities:

```kotlin // Find local entities with Controller component
val entities = Query.where { has(Controller.id) } .filter { isLocal() } .eval() ```

## Signature

```kotlin
class FilterBuilder
```

## Constructors

| **FilterBuilder** () | Signature ```kotlin constructor() ``` Returns [FilterBuilder](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filterbuilder) |
| --- | --- |

## Functions

| **by** ( intData ) | Creates a new filter operation for an integer attribute. This method is the entry point for filtering entities based on integer attribute values. It returns a ByIntFilterOperation object that provides methods for various comparison operations. Signature ```kotlin fun by(intData: IntAttributeData): ByIntFilterOperation ``` Parameters intData: [IntAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_intattributedata) Returns [ByIntFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byintfilteroperation) |
| --- | --- |
| **by** ( longData ) | Creates a new filter operation for a long integer attribute. This method is the entry point for filtering entities based on long integer attribute values. It returns a ByLongFilterOperation object that provides methods for various comparison operations. Signature ```kotlin fun by(longData: LongAttributeData): ByLongFilterOperation ``` Parameters longData: [LongAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_longattributedata) Returns [ByLongFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bylongfilteroperation) |
| **by** ( floatData ) | Creates a new filter operation for a float attribute. This method is the entry point for filtering entities based on float attribute values. It returns a ByFloatFilterOperation object that provides methods for various comparison operations. Signature ```kotlin fun by(floatData: FloatAttributeData): ByFloatFilterOperation ``` Parameters floatData: [FloatAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_floatattributedata) Returns [ByFloatFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byfloatfilteroperation) |
| **by** ( boolData ) | Creates a new filter operation for a boolean attribute. This method is the entry point for filtering entities based on boolean attribute values. It returns a ByBooleanFilterOperation object that provides methods for equality comparison. Signature ```kotlin fun by(boolData: BooleanAttributeData): ByBooleanFilterOperation ``` Parameters boolData: [BooleanAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_booleanattributedata) Returns [ByBooleanFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bybooleanfilteroperation) |
| **by** ( stringData ) | Creates a new filter operation for a string attribute. This method is the entry point for filtering entities based on string attribute values. It returns a ByStringFilterOperation object that provides methods for various string comparison operations. Signature ```kotlin fun by(stringData: StringAttributeData): ByStringFilterOperation ``` Parameters stringData: [StringAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_stringattributedata) Returns [ByStringFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bystringfilteroperation) |
| **by** ( enumData ) | Creates a new filter operation for an enum attribute. This method is the entry point for filtering entities based on enum attribute values. It returns a ByEnumFilterOperation object that provides methods for equality comparison. Signature ```kotlin fun by(enumData: EnumAttributeData): ByEnumFilterOperation ``` Parameters enumData: [EnumAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_enumattributedata) Returns [ByEnumFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byenumfilteroperation) |
| **by** ( uuidData ) | Creates a new filter operation for a UUID attribute. This method is the entry point for filtering entities based on UUID attribute values. It returns a ByUUIDFilterOperation object that provides methods for equality comparison. Signature ```kotlin fun by(uuidData: UUIDAttributeData): ByUUIDFilterOperation ``` Parameters uuidData: [UUIDAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_uuidattributedata) Returns [ByUUIDFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byuuidfilteroperation) |
| **by** ( vector2Data ) | Creates a new filter operation for a Vector2 attribute. This method is the entry point for filtering entities based on Vector2 attribute values. It returns a ByVector2FilterOperation object that provides methods for comparing the entire vector or its individual components (x, y). Signature ```kotlin fun by(vector2Data: Vector2AttributeData): ByVector2FilterOperation ``` Parameters vector2Data: [Vector2AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector2attributedata) Returns [ByVector2FilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector2filteroperation) |
| **by** ( vector3Data ) | Creates a new filter operation for a Vector3 attribute. This method is the entry point for filtering entities based on Vector3 attribute values. It returns a ByVector3FilterOperation object that provides methods for comparing the entire vector or its individual components (x, y, z). Signature ```kotlin fun by(vector3Data: Vector3AttributeData): ByVector3FilterOperation ``` Parameters vector3Data: [Vector3AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector3attributedata) Returns [ByVector3FilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector3filteroperation) |
| **by** ( vector4Data ) | Creates a new filter operation for a Vector4 attribute. This method is the entry point for filtering entities based on Vector4 attribute values. It returns a ByVector4FilterOperation object that provides methods for comparing the entire vector or its individual components (x, y, z, w). Signature ```kotlin fun by(vector4Data: Vector4AttributeData): ByVector4FilterOperation ``` Parameters vector4Data: [Vector4AttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_vector4attributedata) Returns [ByVector4FilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byvector4filteroperation) |
| **by** ( poseData ) | Creates a new filter operation for a Pose attribute. This method is the entry point for filtering entities based on Pose attribute values. It returns a ByPoseFilterOperation object that provides methods for comparing the entire pose or its individual components (position x/y/z, orientation w/x/y/z). Signature ```kotlin fun by(poseData: PoseAttributeData): ByPoseFilterOperation ``` Parameters poseData: [PoseAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_poseattributedata) Returns [ByPoseFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byposefilteroperation) |
| **by** ( mapData ) | Creates a new filter operation for a Map attribute. This method is the entry point for filtering entities based on Map attribute values. It returns a ByMapFilterOperation object that provides methods for checking map properties. Signature ```kotlin fun <KeyType, ValueType> by(mapData: ExperimentalMapAttributeData<KeyType, ValueType>): ByMapFilterOperation<KeyType, ValueType> ``` Parameters mapData: [ExperimentalMapAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_experimentalmapattributedata) Returns [ByMapFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bymapfilteroperation) |
| **by** ( entityData ) | Creates a new filter operation for an Entity attribute. This method is the entry point for filtering entities based on Entity attribute values. It returns a ByEntityFilterOperation object that provides methods for equality comparison. Signature ```kotlin fun by(entityData: EntityAttributeData): ByEntityFilterOperation ``` Parameters entityData: [EntityAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entityattributedata) Returns [ByEntityFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_byentityfilteroperation) |
| **by** ( timeData ) | Creates a new filter operation for a Time attribute. This method is the entry point for filtering entities based on Time attribute values. It returns a ByTimeFilterOperation object that provides methods for various comparison operations. Signature ```kotlin fun by(timeData: TimeAttributeData): ByTimeFilterOperation ``` Parameters timeData: [TimeAttributeData](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_timeattributedata) Returns [ByTimeFilterOperation](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_bytimefilteroperation) |
| **getFloatArray** () | Returns the float filter values as an array, or null if none were added. Signature ```kotlin fun getFloatArray(): FloatArray? ``` Returns FloatArray? |
| **getIntArray** () | Returns the int filter values as an array, or null if none were added. Signature ```kotlin fun getIntArray(): IntArray? ``` Returns IntArray? |
| **getLongArray** () | Returns the long filter values as an array, or null if none were added. Signature ```kotlin fun getLongArray(): LongArray? ``` Returns LongArray? |
| **getStringArray** () | Returns the string filter values as an array, or null if none were added. Signature ```kotlin fun getStringArray(): Array<String>? ``` Returns Array? |
| **isLocal** () | Creates a filter that matches only entities that are local to the client. This is particularly useful in networked applications to filter for entities that belong to the local user. Signature ```kotlin fun isLocal(): IsLocalFilterNode ``` Returns [IsLocalFilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_islocalfilternode) A filter node that matches only local entities |
| **not** ( filterNode ) | Creates a filter that negates another filter condition. This method applies a logical NOT operation to the provided filter node, returning entities that do NOT match the specified condition. Signature ```kotlin fun not(filterNode: FilterNode): FilterNode ``` Parameters filterNode: [FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode) The filter node to negate Returns [FilterNode](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_filternode) A new filter node representing the logical NOT of the input filter |