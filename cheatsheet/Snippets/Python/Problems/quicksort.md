```python
def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


quicksortL = lambda array: (
    array
    if len(array) < 2 else
    (
        lambda pivot, less, greater: quicksortL(less) + [pivot] + quicksortL(greater)
    )(
        **(
            lambda pivot, temp_arr: {
                "pivot": pivot,
                "less": [i for i in temp_arr if i <= pivot],
                "greater": [i for i in temp_arr if i > pivot]
            }
        )(array[0], array[1:])
    )
)

q = lambda x: x and q([i for i in x[1:] if i <= x[0]]) + [x[0]] + q([i for i in x[1:] if i > x[0]])
```
```pycon
>>> print(quicksort([10, 5, 2, 3]))
[2, 3, 5, 10]
```
