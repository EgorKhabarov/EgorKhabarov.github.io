# LinearSearch (Линейный поиск)

Последовательный поиск элемента в неотсортированном массиве

```python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return None

arr: list = [28, 64, 2, 1, 13, 0]
print(linear_search(arr, 64))
# 1
```