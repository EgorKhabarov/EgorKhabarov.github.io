# InsertionSort (Сортировка вставками)

Каждый новый элемент заносится в выходную последовательность "индивидуально",
т. е. каждый раз для добавления нового элемента приходится сдвигать часть массива
Алгоритм медленный, для ускорения вставки можно использовать бинарный поиск

```python
def insertionsort(arr):
    for index in range(1, len(arr)):

        currentvalue = arr[index]
        position = index

        while position > 0 and arr[position - 1] > currentvalue:
            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = currentvalue


arr: list = [28, 64, 2, 1, 13, 0]
insertionsort(arr)
print(arr)
# [0, 1, 2, 13, 28, 64]
```