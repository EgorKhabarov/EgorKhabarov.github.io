# `BiFunction<T, U, R>`
`R apply(T t, U u)`
Просуммируем два числа и вернем результат
```java
import java.util.function.*;

public class MyClass {
    public static void main(String[] args) {
        MyClass.test( (a, b) -> a + b, 10, 20 ); // 30
    }
    public static void test(
        BiFunction<Integer, Integer, Integer> f, int x, int y) {
        System.out.println(f.apply(x, y));
    }
}
```
В этом случае метод принимает два параметра, поэтому круглые скобки нужно указать обязательно, как и в случае отсутствия параметров
`(a, b) -> a + b`
