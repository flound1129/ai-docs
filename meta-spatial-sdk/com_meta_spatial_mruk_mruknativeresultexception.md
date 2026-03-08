# MRUKNativeResultException Class

Extends
Exception
*Modifiers:
final*

Exception thrown when MRUK native operations fail.

This exception is thrown by MRUK native functions when they encounter errors during execution. The errorCode contains the specific error that occurred, which can be mapped to MRUKNativeResult enum values for detailed error handling.

## See Also

## Signature

```kotlin
class MRUKNativeResultException(val errorCode: Int) : Exception
```

## Constructors

| **MRUKNativeResultException** ( errorCode ) | Signature ```kotlin constructor(errorCode: Int) ``` Parameters errorCode: Int The native error code indicating the specific failure reason Returns [MRUKNativeResultException](/reference/spatial-sdk/v0.10.1/com_meta_spatial_mruk_mruknativeresultexception) |
| --- | --- |

## Properties

| **cause** : Throwable? [Get] | Signature ```kotlin open val cause: Throwable? ``` |
| --- | --- |
| **errorCode** : Int [Get] | The native error code indicating the specific failure reason Signature ```kotlin val errorCode: Int ``` |
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