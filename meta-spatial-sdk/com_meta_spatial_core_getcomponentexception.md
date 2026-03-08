# GetComponentException Class

Extends
RuntimeException
*Modifiers:
final*

Exception thrown when there's an error getting a component.

## Signature

```kotlin
class GetComponentException(message: String, val attributeId: Int? = null, val entityId: Long? = null, cause: Throwable? = null) : RuntimeException
```

## Constructors

| **GetComponentException** ( message , attributeId , entityId , cause ) | Signature ```kotlin constructor(message: String, attributeId: Int? = null, entityId: Long? = null, cause: Throwable? = null) ``` Parameters message: String attributeId: Int? The attribute ID that caused the error (if applicable) entityId: Long? The entity ID involved in the operation (if applicable) cause: Throwable? Returns [GetComponentException](/reference/spatial-sdk/v0.10.1/com_meta_spatial_core_getcomponentexception) |
| --- | --- |

## Properties

| **attributeId** : Int? [Get] | The attribute ID that caused the error (if applicable) Signature ```kotlin val attributeId: Int? = null ``` |
| --- | --- |
| **cause** : Throwable? [Get] | Signature ```kotlin open val cause: Throwable? ``` |
| **entityId** : Long? [Get] | The entity ID involved in the operation (if applicable) Signature ```kotlin val entityId: Long? = null ``` |
| **message** : String? [Get] | Signature ```kotlin open val message: String? ``` |

## Functions

| **addSuppressed** ( p0 ) | Signature ```kotlin fun addSuppressed(p0: Throwable) ``` Parameters p0: Throwable |
| --- | --- |
| **fillInStackTrace** () | Signature ```kotlin open fun fillInStackTrace(): Throwable ``` Returns Throwable |
| **getLocalizedMessage** () | Signature ```kotlin open fun getLocalizedMessage(): String ``` Returns String |
| **getStackTrace** () | Signature ```kotlin open fun getStackTrace(): Array<StackTraceElement> ``` Returns Array |
| **getSuppressed** () | Signature ```kotlin fun getSuppressed(): Array<Throwable> ``` Returns Array |
| **initCause** ( p0 ) | Signature ```kotlin open fun initCause(p0: Throwable): Throwable ``` Parameters p0: Throwable Returns Throwable |
| **printStackTrace** () | Signature ```kotlin open fun printStackTrace() ``` |
| **printStackTrace** ( p0 ) | Signature ```kotlin open fun printStackTrace(p0: PrintStream) ``` Parameters p0: PrintStream |
| **printStackTrace** ( p0 ) | Signature ```kotlin open fun printStackTrace(p0: PrintWriter) ``` Parameters p0: PrintWriter |
| **setStackTrace** ( p0 ) | Signature ```kotlin open fun setStackTrace(p0: Array<StackTraceElement>) ``` Parameters p0: Array |
| **toString** () | Signature ```kotlin open override fun toString(): String ``` Returns String |