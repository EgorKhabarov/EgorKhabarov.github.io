# `Supplier<T>`
`T get()`
Вернем случайное целое число от 0 до 100 включительно
```java
import java.util.Random;
import java.util.function.*;

public class MyClass {
    public static void main(String[] args) {
        MyClass.test(
            () -> {
                Random r = new Random();
                return r.nextInt(101);
            }
        );
    }
    public static void test(Supplier<Integer> f) {
        System.out.println(f.get());
    }
}
```
