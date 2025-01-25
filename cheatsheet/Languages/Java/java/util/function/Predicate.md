# `Predicate<T>`
`boolean test(T t)`
Напишем проверку неравенства целого числа нулю
```java
import java.util.function.*;

public class MyClass {
    public static void main(String[] args) {
        MyClass.test( n -> n != 0, 10 ); // true
        MyClass.test( n -> n != 0, 0 ); // false
    }
    public static void test(Predicate<Integer> f, int x) {
        System.out.println(f.test(x));
    }
}
```
