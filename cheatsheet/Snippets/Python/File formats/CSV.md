# CSV - Comma Separated Values

Текстовый формат файла, который используется для хранения табличных данных
Каждая строка файла содержит одну запись, а значения в этой записи разделены запятыми

```csv
Name,Age,City
John Smith,30,New York
Jane Doe,25,Chicago
```

```python
import csv


data = [
    ("Name", "Age"),
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35),
]

with open("data.csv", "w", newline="", encoding="UTF-8") as file:
    csv.writer(file).writerows(data)

with open("data.csv", "r", encoding="UTF-8") as file:
    print(list(csv.reader(file)))
```
