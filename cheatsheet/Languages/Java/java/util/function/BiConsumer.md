# `BiConsumer<T, U>`
`void accept(T t, U u)`
Просуммируем два числа и выведем результат в окно консоли
```java
import java.util.function.*;

public class MyClass {
    public static void main(String[] args) {
        MyClass.test((a, b) -> System.out.println(a + b), 10, 15); // 25
    }
    public static void test(BiConsumer<Integer, Integer> f, int x, int y) {
        f.accept(x, y);
    }
}
```
