```java
import java.util.function.*;
```

```java
import java.util.function.*;

public class MyClass {
    public static void main(String[] args) {
        MyClass.test( n -> n * 2, 10 );
    }
    public static void test(
        Function<Integer, Integer> f, int x) {
        System.out.println(f.apply(x));
    }
}
```

- `Function<T, R>` `R apply(T t)`
    - `UnaryOperator<T>` `T apply(T t)`
    - `IntUnaryOperator` `int applyAsInt(int x)`
    - `LongUnaryOperator` `long applyAsLong(long x)`
    - `DoubleUnaryOperator` `double applyAsDouble(double x)`
    - `IntFunction<R>` `R apply(int x)`
    - `LongFunction<R>` `R apply(long x)`
    - `DoubleFunction<R>` `R apply(double x)`
    - `ToIntFunction<T>` `int applyAsInt(T x)`
        - `LongToIntFunction` `int applyAsInt(long x)`
        - `DoubleToIntFunction` `int applyAsInt(double x)`
    - `ToLongFunction<T>` `long applyAsLong(T x)`
        - `IntToLongFunction` `long applyAsLong(int x)`
        - `DoubleToLongFunction` `long applyAsLong(double x)`
    - `ToDoubleFunction<T>` `double applyAsDouble(T x)`
        - `IntToDoubleFunction` `double applyAsDouble(int x)`
        - `LongToDoubleFunction` `double applyAsDouble(long x)`
    - `BiFunction<T, U, R>` `R apply(T t, U u)`
        - `ToIntBiFunction<T, U>` `int applyAsInt(T t, U u)`
        - `ToLongBiFunction<T, U>` `long applyAsLong(T t, U u)`
        - `ToDoubleBiFunction<T, U>` `double applyAsDouble(T t, U u)`
        - `BinaryOperator<T>` `T apply(T t, T u)`
            - `IntBinaryOperator` `int applyAsInt(int x, int y)`
            - `LongBinaryOperator` `long applyAsLong(long x, long y)`
            - `DoubleBinaryOperator` `double applyAsDouble(double x, double y)`
- `Predicate<T>` `boolean test(T t)`
    - `IntPredicate` `boolean test(int x)`
    - `LongPredicate` `boolean test(long x)`
    - `DoublePredicate` `boolean test(double x)`
- `BiPredicate<T, U>` `boolean test(T t, U u)`
- `Consumer<T>` `void accept(T t)`
    - `IntConsumer` `void accept(int x)`
    - `LongConsumer` `void accept(long x)`
    - `DoubleConsumer` `void accept(double x)`
- `BiConsumer<T, U>` `void accept(T t, U u)`
    - `ObjIntConsumer<T>` `void accept(T t, int y)`
    - `ObjLongConsumer<T>` `void accept(T t, long y)`
    - `ObjDoubleConsumer<T>` `void accept(T t, double y)`
- `Supplier<T>` `T get()`
    - `BooleanSupplier` `boolean getAsBoolean()`
    - `IntSupplier` `int getAsInt()`
    - `LongSupplier` `long getAsLong()`
    - `DoubleSupplier` `double getAsDouble()`
