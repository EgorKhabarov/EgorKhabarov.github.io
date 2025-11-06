# HeapSort (Пирамидальная сортировка)

Превращаем массив в двоичное дерево за `О(n)` операций
Раз за разом преобразуя дерево, получим отсортированный массив

```python
def heap_sort():
    end = len(arr)
    start = end // 2 - 1
    for i in range(start, -1, -1):
        heapify(end, i)
    for i in range(end-1, 0, -1):
        swap(i, 0)
        heapify(i, 0)

def heapify(end,i):
    l = 2 * i + 1
    r = 2 * (i + 1)
    max = i
    if l < end and arr[i] < arr[l]:
        max = l
    if r < end and arr[max] < arr[r]:
        max = r
    if max != i:
        swap(i, max)
        heapify(end, max)

def swap(i, j):
    arr[i], arr[j] = arr[j], arr[i]

arr: list = [28, 64, 2, 1, 13, 0]
heap_sort()
print(arr)
# [0, 1, 2, 13, 28, 64]
```