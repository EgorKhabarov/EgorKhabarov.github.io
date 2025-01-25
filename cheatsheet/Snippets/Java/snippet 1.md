```java
import java.util.function.Consumer;

class Example {
    int print = 1;
    // String print = "qwe"; // Variable 'print' is already defined in the scope

    public void print(int x) {
        System.out.println(x);
    }
    public void print(String x) {
        System.out.println(x);
    }
}

public class Main {
    public static void main(String[] args) {
        Example example = new Example();
        System.out.println(example.print);
        example.print(23);
        example.print("qwerty");

        int Int = example.print;
        System.out.println(Int);

        Consumer<Integer> printInt = example::print;
        printInt.accept(23);

        Consumer<String> printString = example::print;
        printString.accept("qwerty");
    }
}
```
