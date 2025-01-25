```java
import java.util.HashMap;

public class HashMapExample {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<>();
        map.put("Alice", 30);
        map.put("Bob", 25);
        map.put("Charlie", 35);

        for (String name : map.keySet()) {
            System.out.println(name + ": " + map.get(name));
        }
    }
}
```
