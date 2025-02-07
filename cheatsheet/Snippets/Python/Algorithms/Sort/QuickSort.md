# QuickSort (Быстрая сортировка)

1. Выбирается опорный элемент; это в первом приближении может быть любой из элементов,
например, значение из середины массива
2. Все элементы массива сравниваются с опорным и переставляются так, чтобы образовать новый массив,
состоящий из двух последовательных сегментов — элементы меньшие опорного, равные опорному + большие опорного
3. Если длина сегментов больше 1, то рекурсивно выполнить сортировку и для них тоже

```python
def quicksort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return arr

arr: list = [28, 64, 2, 1, 13, 0]
print(quicksort(arr))
# [0, 1, 2, 13, 28, 64]
```