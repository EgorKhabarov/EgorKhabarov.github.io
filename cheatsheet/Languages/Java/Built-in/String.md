# Особенности
- **Неизменяемость (immutable)**: После создания строка не может быть изменена.
Все операции, которые, казалось бы, изменяют строку, возвращают новый объект `String`.
- **Пул строк**: При создании строк литералами Java сохраняет их в специальный пул строк, что помогает экономить память.

```java
String s1 = "Hello";
String s2 = new String("World");
```

# Методы

| Метод                                                            | Описание                                                               | Пример использования                                                                       |
|------------------------------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `.charAt(int index)`                                             | Возвращает символ по указанному индексу                                | `char c = "Hello".charAt(1); // 'e'`                                                       |
| `.length()`                                                      | Возвращает длину строки                                                | `int len = "Hello".length(); // 5`                                                         |
| `.concat(String str)`                                            | Склеивает две строки, возвращает новую строку                          | `String s = "Hello".concat(" World"); // "Hello World"`                                    |
| `.contains(CharSequence)`                                        | Проверяет, содержит ли строка<br>указанную последовательность символов | `boolean b = "Hello".contains("ll"); // true`                                              |
| `.equals(Object obj)`                                            | Проверяет строки на равенство                                          | `boolean b = "Hello".equals("hello");// false`                                             |
| `.equalsIgnoreCase(String str)`                                  | Проверяет строки на равенство, игнорируя регистр символов              | `boolean b = "Hello".equalsIgnoreCase("hello"); // true`                                   |
| `.startsWith(String prefix)`                                     | Проверяет, начинается ли строка с указанного префикса                  | `boolean b = "Hello".startsWith("He"); // true`                                            |
| `.endsWith(String suffix)`                                       | Проверяет, заканчивается ли строка указанным суффиксом                 | `boolean b = "Hello".endsWith("lo"); // true`                                              |
| `.indexOf(String str)`                                           | Возвращает индекс первого вхождения подстроки                          | `int idx = "Hello".indexOf("l"); // 2`                                                     |
| `.lastIndexOf(String str)`                                       | Возвращает индекс последнего вхождения подстроки                       | `int idx = "Hello".lastIndexOf("l"); // 3`                                                 |
| `.substring`<br>(int beginIndex)                                 | Возвращает подстроку, начиная с указанного индекса                     | `String sub = "Hello".substring(2); // "llo"`                                              |
| `.substring`<br>(int beginIndex, int endIndex)                   | Возвращает подстроку с указанного<br>начала до конца (не включая)      | `String sub = "Hello".substring(1, 4); // "ell"`                                           |
| `.toLowerCase()`                                                 | Возвращает новую строку, переведенную в нижний регистр                 | `String s = "HELLO".toLowerCase(); // "hello"`                                             |
| `.toUpperCase()`                                                 | Возвращает новую строку, переведенную в верхний регистр                | `String s = "hello".toUpperCase(); // "HELLO"`                                             |
| `.trim()`                                                        | Удаляет начальные и конечные пробелы                                   | `String s = "  Hello  ".trim(); // "Hello"`                                                |
| `.replace`<br>(char oldChar, char newChar)                       | Заменяет все вхождения одного символа на другой                        | `String s = "Hello".replace('l', 'p'); // "Heppo"`                                         |
| `.replace`<br>(CharSequence target,<br>CharSequence replacement) | Заменяет все вхождения одной<br>последовательности символов на другую  | `String s = "Hello".replace("ll", "yy"); // "Heyyo"`                                       |
| `.split(String regex)`                                           | Разделяет строку по указанному регулярному выражению                   | `String[] arr = "a,b,c".split(",");`<br>`Arrays.toString("a,b,c".split(",")) // [a, b, c]` |
| `.matches(String regex)`                                         | Проверяет, соответствует ли строка регулярному выражению               | `boolean b = "abc".matches("[a-z]+"); // true`                                             |
| `.isEmpty()`                                                     | Проверяет, пуста ли строка (имеет длину 0)                             | `boolean b = "".isEmpty(); // true`                                                        |
| `.intern()`                                                      | Возвращает строку из пула строк или добавляет её туда                  | `String s = "Hello".intern(); // "Hello"`                                                  |
| `.toCharArray()`                                                 | Преобразует строку в массив символов                                   | `char[] arr = "Hello".toCharArray(); // "Hello"`                                           |
| `.compareTo(String anotherString)`                               | Сравнивает строки лексикографически                                    | `int cmp = "abc".compareTo("abd"); // -1`                                                  |
| `.compareToIgnoreCase(String str)`                               | Лексикографическое сравнение<br>строк без учета регистра               | `int cmp = "abc".compareToIgnoreCase("ABC"); // 0`                                         |
| `.format(String format, Object... args)`                         | Возвращает отформатированную<br>строку на основе переданных аргументов | `String s = String.format("Hello %s", "World"); // "Hello World"`                          |
| `.join`<br>(CharSequence delimiter,<br>CharSequence... elements) | Объединяет элементы в строку с указанным разделителем                  | `String s = String.join(", ", "a", "b", "c"); // "a, b, c"`                                |

# Примеры использования

1. **Склеивание строк:**
```java
String s1 = "Hello";
String s2 = "World";
String result = s1.concat(" ").concat(s2);  // "Hello World"
```

2. **Получение подстроки:**
```java
String s = "Hello World";
String sub = s.substring(6);  // "World"
```

3. **Замена символов:**
```java
String s = "apple";
String replaced = s.replace('p', 'b');  // "abble"
```

4. **Разделение строки:**
```java
String s = "a,b,c";
String[] parts = s.split(",");  // ["a", "b", "c"]
```

5. **Проверка содержания строки:**
```java
String s = "Hello";
boolean contains = s.contains("ell");  // true
```

6. **Форматирование строки:**
```java
String formatted = String.format("Name: %s, Age: %d", "Alice", 30);
System.out.println(formatted);  // "Name: Alice, Age: 30"
```
