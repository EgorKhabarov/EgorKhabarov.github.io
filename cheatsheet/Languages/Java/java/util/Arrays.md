```java
import java.util.Arrays;
```

```java
int[] nums = { 1, 2, 3, 5 };
System.out.println(Arrays.toString(nums));
```

`Arrays.copyOf` - копирует один массив в другой

```java
int[] arr = new int[] { 1, 2, 3, 5 };
int[] some_new = Arrays.copyOf(arr, arr.length);
```

`Arrays.sort` - сортировка массива

```java
int[] numbers = new int[] { 1, 7, 3, 5, 2, 6, 4 };

Arrays.sort(numbers);
```
