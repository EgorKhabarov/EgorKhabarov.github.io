- **`Массив (array)`** структура данных фиксированного размера
- **`Список (list)`** интерфейс в Java, который представляет динамическую структуру данных, размер которой может изменяться.


```java
int numbers[];
numbers = new int[10];

int[] nums = new int[4];
nums[0] = 1;

int[] nums2 = new int[] { 1, 2, 3, 5 };
int[] nums3 = { 1, 2, 3, 5 };

System.out.println(Arrays.toString(nums3));
System.out.println(nums3.length);

System.out.println(Arrays.toString(new int[] { 1, 2, 3, 5 }));
System.out.println(new int[] { 1, 2, 3, 5 }.length);
```

# Вывод значений

Для вывода всех значений массива используйте метод `Arrays.toString()`, преобразующий массив в строку

```java
import java.util.Arrays;
```
```java
System.out.println(Arrays.toString(arr));
```

Или напишите цикл, выводящий последовательно элементы массива

```java
for(int i=0; i<arr.length; i++) {
    System.out.println(arr[i]);
}
// Или
for (int el : arr) {
    System.out.println(el);
}
```

# Многомерный массив

```java
int[][] x = { { 0, 1, 2 }, { 3, 4, 5 } };
```

# Стандартные коллекции

![collections.jpg](Languages/Java/collections.jpg)


## Основные коллекции
Помимо главного интерфейса Collection есть три других главных формата:

- `List` - коллекция для создания массивов данных, где индексами являются числа (0, 1, 2 и так далее)
- `Set` - тоже самое что `List`, вот только в `Set` нельзя установить повторяющиеся элементы
- `Map` - коллекция для создания массивов данных, где индексами являются ключи ("one", "2", "three" и так далее)


```java
import java.util.LinkedList;
import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {
        ArrayList<Float> numbers = new ArrayList<>(1);  // 1 (initialCapacity) можно не указывать
        LinkedList<String> names = new LinkedList<>();
    }
}
```

- `add()` - добавление элемента в конец массива
- `remove()` - удаление элемента из массива по его индексу
- `clear()` - очистка всего массива
- `size()` - получение размера массива (количество элементов)
- `addFirst()` - добавление элемента в начало массива
- `addLast()` - добавление элемента в конец
- `clone()` - выполняет клонирование массива
- `get()` - возвращает элемент по индексу
- `getFirst()` - возвращает первый элемент в массиве
- `getLast()` - возвращает последний элемент в массиве
- `set(index, element)` - меняет значение элемента по индексу


```java
List<Object> items = new ArrayList<>();
items.add("Hello");
items.add(42);
items.add(3.14);
items.add(0, 3.14);
items.add(2, 3.14);

System.out.println(items.get(0));
// System.out.println(items.get(-1)); // Index -1 out of bounds for length 5
System.out.println(items.size());
for (Object item : items) {
    System.out.println(item);
}
```
```output
5
3.14
Hello
3.14
42
3.14
```
