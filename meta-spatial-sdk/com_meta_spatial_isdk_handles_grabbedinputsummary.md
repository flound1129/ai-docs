# GrabbedInputSummary Class

*Modifiers:
final*

Summary of input sources interacting with a panel's grab handles.

## Constructors

| **GrabbedInputSummary** ( emittingInputSources , grabbingSource ) | Signature ```kotlin constructor(emittingInputSources: LinkedHashMap<Entity, EmittingInputSource>, EmittingInputSource> = LinkedHashMap(), grabbingSource: Entity? = null) ``` Parameters emittingInputSources: LinkedHashMap<Entity, EmittingInputSource> LinkedHashMap of input source entities to their hover info. LinkedHashMap maintains insertion order while providing O(1) lookups. grabbingSource: [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) The input source entity currently grabbing (null if not grabbed) Returns [GrabbedInputSummary](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_handles_grabbedinputsummary) |
| --- | --- |

## Properties

| **emittingInputSources** : LinkedHashMap<Entity, EmittingInputSource> [Get] | LinkedHashMap of input source entities to their hover info. LinkedHashMap maintains insertion order while providing O(1) lookups. Signature ```kotlin val emittingInputSources: LinkedHashMap<Entity, EmittingInputSource> ``` |
| --- | --- |
| **grabbingSource** : [Entity?](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_entity) [Get][Set] | The input source entity currently grabbing (null if not grabbed) Signature ```kotlin var grabbingSource: Entity? ``` |