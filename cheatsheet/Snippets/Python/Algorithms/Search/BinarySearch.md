# BinarySearch (Бинарный поиск)

Работает только с отсортированными массивами
Берется значение из середины массива и сравнивается с искомой величиной
В зависимости от сравнения дальнейший рекурсивный поиск продолжается с середины либо левого, либо правого подмассива

```python
def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == x:
            return middle

        if arr[middle] < x:
            left = middle + 1
        elif arr[middle] > x:
            right = middle - 1

arr: list = [0, 24, 64, 222, 1300, 2048]
print(binary_search(arr, 64))
# 2
```