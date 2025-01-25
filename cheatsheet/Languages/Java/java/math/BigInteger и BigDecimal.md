Предназначены для работы с большими числами, которые выходят за пределы типа `int` или `double`
а также для работы с высокой точностью

# BigInteger

Класс для работы с целыми числами произвольной длины

| Метод                                | Описание                                                             | Пример использования                                       |
|--------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------|
| `BigInteger(String val)`             | Создает объект из строки                                             | `BigInteger num = new BigInteger("12345678901234567890");` |
| `BigInteger.valueOf(long val)`       | Создает объект из `long`                                             | `BigInteger num = BigInteger.valueOf(42);`                 |
| `add(BigInteger val)`                | Складывает два числа                                                 | `BigInteger sum = a.add(b);`                               |
| `subtract(BigInteger val)`           | Вычитает одно число из другого                                       | `BigInteger diff = a.subtract(b);`                         |
| `multiply(BigInteger val)`           | Умножает два числа                                                   | `BigInteger product = a.multiply(b);`                      |
| `divide(BigInteger val)`             | Делит одно число на другое (целочисленное деление)                   | `BigInteger quotient = a.divide(b);`                       |
| `remainder(BigInteger val)`          | Остаток от деления                                                   | `BigInteger rem = a.remainder(b);`                         |
| `divideAndRemainder(BigInteger val)` | Возвращает массив с результатом<br>целочисленного деления и остатком | `BigInteger[] result = a.divideAndRemainder(b);`           |
| `pow(int exponent)`                  | Возводит число в степень                                             | `BigInteger power = a.pow(3);`                             |
| `mod(BigInteger val)`                | Остаток от деления для положительных чисел (модуль)                  | `BigInteger mod = a.mod(b);`                               |
| `gcd(BigInteger val)`                | НОД двух чисел                                                       | `BigInteger gcd = a.gcd(b);`                               |
| `abs()`                              | Возвращает абсолютное значение числа                                 | `BigInteger absVal = a.abs();`                             |
| `negate()`                           | Возвращает отрицательное значение числа                              | `BigInteger neg = a.negate();`                             |
| `compareTo(BigInteger val)`          | Сравнивает числа: `-1` (меньше),<br>`0` (равны), `1` (больше)        | `int cmp = a.compareTo(b);`                                |
| `toString()`                         | Преобразует число в строку                                           | `String str = a.toString();`                               |
| `isProbablePrime(int certainty)`     | Проверяет, является ли число<br>простым с заданной вероятностью      | `boolean isPrime = a.isProbablePrime(10);`                 |

### Пример использования `BigInteger`

```java
import java.math.BigInteger;

public class BigIntegerExample {
    public static void main(String[] args) {
        BigInteger a = new BigInteger("123456789012345678901234567890");
        BigInteger b = new BigInteger("987654321098765432109876543210");

        BigInteger sum = a.add(b);
        BigInteger product = a.multiply(b);
        BigInteger power = a.pow(2);

        System.out.println("Сумма: " + sum);
        System.out.println("Произведение: " + product);
        System.out.println("Квадрат: " + power);
    }
}
// Сумма: 1111111110111111111011111111100
// Произведение: 121932631137021795226185032733622923332237463801111263526900
// Квадрат: 15241578753238836750495351562536198787501905199875019052100
```

# BigDecimal

Класс для работы с числами с плавающей точкой произвольной точности

| Метод                                                               | Описание                                                      | Пример использования                                          |
|---------------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| `BigDecimal(String val)`                                            | Создает объект из строки                                      | `BigDecimal num = new BigDecimal("12345.6789");`              |
| `BigDecimal.valueOf(double val)`                                    | Создает объект из `double`                                    | `BigDecimal num = BigDecimal.valueOf(12345.6789);`            |
| `add(BigDecimal val)`                                               | Складывает два числа                                          | `BigDecimal sum = a.add(b);`                                  |
| `subtract(BigDecimal val)`                                          | Вычитает одно число из другого                                | `BigDecimal diff = a.subtract(b);`                            |
| `multiply(BigDecimal val)`                                          | Умножает два числа                                            | `BigDecimal product = a.multiply(b);`                         |
| `divide(BigDecimal val, int scale,`<br>`RoundingMode roundingMode)` | Делит числа с указанием<br>точности и метода округления       | `BigDecimal quotient = a.divide(b, 2, RoundingMode.HALF_UP);` |
| `remainder(BigDecimal val)`                                         | Остаток от деления                                            | `BigDecimal rem = a.remainder(b);`                            |
| `setScale(int newScale,`<br>`RoundingMode roundingMode)`            | Изменяет точность числа с указанием метода округления         | `BigDecimal scaled = a.setScale(2, RoundingMode.HALF_UP);`    |
| `compareTo(BigDecimal val)`                                         | Сравнивает числа: `-1` (меньше),<br>`0` (равны), `1` (больше) | `int cmp = a.compareTo(b);`                                   |
| `toString()`                                                        | Преобразует число в строку                                    | `String str = a.toString();`                                  |
| `scale()`                                                           | Возвращает текущую точность числа                             | `int scale = a.scale();`                                      |
| `precision()`                                                       | Возвращает общее количество значащих цифр                     | `int precision = a.precision();`                              |
| `stripTrailingZeros()`                                              | Убирает незначащие нули после запятой                         | `BigDecimal stripped = a.stripTrailingZeros();`               |

### Пример использования `BigDecimal`
```java
import java.math.BigDecimal;
import java.math.RoundingMode;

public class BigDecimalExample {
    public static void main(String[] args) {
        BigDecimal a = new BigDecimal("12345.6789");
        BigDecimal b = new BigDecimal("0.001");

        BigDecimal sum = a.add(b);
        BigDecimal diff = a.subtract(b);
        BigDecimal scaled = a.setScale(2, RoundingMode.HALF_UP);

        System.out.println("Сумма: " + sum);
        System.out.println("Разность: " + diff);
        System.out.println("С округлением: " + scaled);
    }
}
```

### Заметки

1. Не использовать `double` или `float` в конструкторе `BigDecimal` ```java
BigDecimal a = new BigDecimal(0.1); // Неточно!
BigDecimal b = new BigDecimal("0.1"); // Точно
```
2. Методы округления (`RoundingMode`)
    - `RoundingMode.HALF_UP` — округление "по математическим правилам"
    - `RoundingMode.FLOOR` — округление вниз
    - `RoundingMode.CEILING` — округление вверх
