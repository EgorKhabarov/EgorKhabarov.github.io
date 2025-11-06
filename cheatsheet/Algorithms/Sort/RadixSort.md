# RadixSort (Поразрядная сортировка)

Сортирует только сущности, которые можно разбить на "разряды", имеющие разный вес
Это могут быть, например, целые числа или строки
Соответственно, элементы сортируются поразрядно, начиная с разряда, имеющего максимальный вес

```python
def radixsort(arr: list):
    n = len(str(max(arr)))

    for k in range(n):
        bucket_list=[[] for i in range(10)]
        for i in arr:
            bucket_list[i // (10**k) % 10].append(i)
        arr = sum(bucket_list, [])  # Flattening a list of lists to a list
    return arr

arr: list = [28, 64, 2, 1, 13, 0]
print(radixsort(arr))
# [0, 1, 2, 13, 28, 64]
```