# IsdkSystems Class

*Modifiers:
final*

Isdk adds support for more generic device agnostic input handling. It fully supports hand and controller based interactions, such as near-field surface touch, distance grabbing, ray selecting. When this feature is present, it will disable the default SpatialSDK input system.

## Constructors

| **IsdkSystems** ( ctx ) | Signature ```kotlin constructor(ctx: Context) ``` Parameters ctx: Context The Android context. Returns [IsdkSystems](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_isdksystems) |
| --- | --- |

## Properties

| **ctx** : Context [Get] | The Android context. Signature ```kotlin val ctx: Context ``` |
| --- | --- |

## Functions

| **componentsToRegister** () | Signature ```kotlin fun componentsToRegister(): List<ComponentRegistration> ``` Returns List |
| --- | --- |
| **earlySystemsToRegister** ( externalControllerInputHandler ) | Signature ```kotlin fun earlySystemsToRegister(externalControllerInputHandler: ExternalControllerInputHandler): List<SystemBase> ``` Parameters externalControllerInputHandler: [ExternalControllerInputHandler](/reference/spatial-sdk/v0.10.1/com_meta_spatial_isdk_externalcontrollerinputhandler) Returns List |
| **systemsToRegister** () | Signature ```kotlin fun systemsToRegister(): List<SystemBase> ``` Returns List |