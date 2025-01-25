# `BiPredicate<T, U>`
`boolean test(T t, U u)`
Проверим числа на равенство
```java
import java.util.function.*;

public class MyClass {
    public static void main(String[] args) {
        MyClass.test( (a, b) -> a == b, 10, 10 ); // true
        MyClass.test( (a, b) -> a == b, 10, 20 ); // false
    }
    public static void test(BiPredicate<Integer, Integer> f, int x, int y) {
        System.out.println(f.test(x, y));
    }
}
```
