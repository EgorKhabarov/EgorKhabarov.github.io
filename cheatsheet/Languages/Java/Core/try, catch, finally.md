```java
public class ExceptionExample {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;  // Это вызовет ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Ошибка деления на ноль: " + e.getMessage());
        } finally {
            System.out.println("Блок finally выполняется всегда.");
        }
    }
}
```

# try-with-resources

```java
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}
```

## Без круглых скобочек

```java
BufferedReader reader = null;
try {
    reader = new BufferedReader(new FileReader("file.txt"));
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (reader != null) {
        try {
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
