# `Consumer<T>`
`void accept(T t)`
Выведем значение любого объекта в окно консоли
```java
import java.util.function.*;

public class MyClass {
    public static void main(String[] args) {
        MyClass.test((obj) -> System.out.println(obj), 10); // 10
        MyClass.test((obj) -> System.out.println(obj), 50); // 50
    }
    public static void test(Consumer<Object> f, Object obj) {
        f.accept(obj);
    }
}
```
