`Integer` - это класс-оболочка для типа `int` в Java, предоставляющий дополнительные методы для работы с целыми числами

**Примитив vs Объект**: `int` - примитивный тип, а `Integer` - класс-оболочка, который может быть `null` и поддерживает методы

Преобразование между `int` и `Integer` происходит автоматически
```java
Integer obj = 42; // Автоупаковка
int num = obj;    // Автораспаковка
```

|                     |                  |
|---------------------|------------------|
| `Integer.MIN_VALUE` | `-2,147,483,648` |
| `Integer.MAX_VALUE` | `2,147,483,647`  |

| Метод                                   | Описание                                                                                            | Пример использования                                            |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| `.valueOf(String s)`                    | Преобразует строку в объект `Integer`                                                               | `Integer num = Integer.valueOf("42"); // 42`                    |
| `.valueOf(int i)`                       | Возвращает объект `Integer`, представляющий указанное значение `int`                                | `Integer num = Integer.valueOf(42); // 42`                      |
| `.parseInt(String s)`                   | Преобразует строку в примитивное значение `int`                                                     | `int num = Integer.parseInt("42"); // 42`                       |
| `.parseInt`<br>(String s, int radix)    | Преобразует строку в число указанной системы счисления                                              | `int num = Integer.parseInt("2A", 16); // 42`                   |
| `.toString(int i)`                      | Преобразует число `int` в строку                                                                    | `String str = Integer.toString(42); // "42"`                    |
| `.toString`<br>(int i, int radix)       | Преобразует число в строку указанной системы счисления                                              | `String str = Integer.toString(42, 16); // "2a"`                |
| `.compare(int x, int y)`                | Сравнивает два числа<br>Возвращает `0`, если равны, < `0`,<br>если `x < y`, > `0`, если `x > y`     | `int result = Integer.compare(42, 24); // 1`                    |
| `.compareTo`<br>(Integer another)       | Сравнивает текущий объект `Integer` с другим                                                        | `Integer num = 42;`<br>`int result = num.compareTo(24); // 1`   |
| `.max(int a, int b)`                    | Возвращает большее из двух чисел                                                                    | `int max = Integer.max(42, 24); // 42`                          |
| `.min(int a, int b)`                    | Возвращает меньшее из двух чисел                                                                    | `int min = Integer.min(42, 24); // 24`                          |
| `.sum(int a, int b)`                    | Возвращает сумму двух чисел                                                                         | `int sum = Integer.sum(42, 24); // 66`                          |
| `.bitCount(int i)`                      | Возвращает количество установленных битов<br>в числе (единиц в бинарной записи числа)               | `int bits = Integer.bitCount(42); // 3`                         |
| `.highestOneBit(int i)`                 | Возвращает число, в котором установлен<br>только самый старший значащий бит исходного числа         | `int highBit = Integer.highestOneBit(42); // 32`                |
| `.lowestOneBit(int i)`                  | Возвращает число, в котором установлен<br>только младший значащий бит исходного числа               | `int lowBit = Integer.lowestOneBit(42); // 2`                   |
| `.reverse(int i)`                       | Возвращает число с битами, расположенными в обратном порядке                                        | `int reversed = Integer.reverse(42); // 1409286144`             |
| `.reverseBytes(int i)`                  | Возвращает число с байтами, расположенными в обратном порядке                                       | `int reversedBytes = Integer.reverseBytes(42); // 704643072`    |
| `.rotateLeft`<br>(int i, int distance)  | Сдвигает биты числа влево циклически на указанное количество позиций                                | `int rotated = Integer.rotateLeft(42, 2); // 168`               |
| `.rotateRight`<br>(int i, int distance) | Сдвигает биты числа вправо циклически на указанное количество позиций                               | `int rotated = Integer.rotateRight(42, 2); // -2147483638`      |
| `.signum(int i)`                        | Возвращает знак числа: `1` для положительных,<br>`-1` для отрицательных, `0` для нуля               | `int sign = Integer.signum(-42); // -1`                         |
| `.decode(String nm)`                    | Преобразует строку с числом в десятичной,<br>шестнадцатеричной или восьмеричной системе в `Integer` | `Integer num = Integer.decode("0x2A"); // 42`                   |
| `.getInteger(String nm)`                | Возвращает значение свойства системы с именем<br>`nm`, интерпретируя его как число                  |                                                                 |
| `.hashCode(int value)`                  | Хэш-код для числа                                                                                   | `int hash = Integer.hashCode(42); // 42`                        |
