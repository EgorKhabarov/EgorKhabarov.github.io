Библиотека `fnmatch` в Python используется для работы с шаблонами файловых имен, основанными на Unix shell-подобном синтаксисе
Она позволяет легко сопоставлять строки с шаблонами, которые включают такие символы, как `*`, `?`, и `[]`

# Основные функции и их описание

| Функция                 | Описание                                                                                                        | Пример использования                             |
|-------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| `fnmatch.fnmatch()`     | Сопоставляет строку с шаблоном<br>Регистро**зависимо** на Unix и регистро**независимо** на Windows              | `fnmatch.fnmatch("foo.txt", "*.txt")`            |
| `fnmatch.fnmatchcase()` | Сопоставляет строку с шаблоном с учетом регистра на всех платформах                                             | `fnmatch.fnmatchcase("Foo.txt", "*.TXT")`        |
| `fnmatch.filter()`      | Фильтрует список строк, оставляя только те, которые соответствуют шаблону                                       | `fnmatch.filter(["foo.txt", "bar.py"], "*.txt")` |
| `fnmatch.translate()`   | Преобразует шаблон в регулярное выражение,<br>которое можно использовать с `re` для более сложных сопоставлений | `pattern = fnmatch.translate("*.txt")`           |

# Специальные символы в шаблонах

| Символ    | Описание                                                                                                                                | Пример                                                              |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| `*`       | Соответствует любой строке (включая пустую)                                                                                             | `"*.txt"` соответствует `"file.txt"` и `"a.txt"`                    |
| `?`       | Соответствует любому одному символу                                                                                                     | `"file?.txt"` соответствует `"file1.txt"`, но не `"file12.txt"`     |
| `[seq]`   | Соответствует любому символу из `seq`<br>Например, `[abc]` соответствует `a`, `b`, или `c`                                              | `"file[0-9].txt"` соответствует `"file1.txt"`, но не `"file12.txt"` |
| `[!seq]`  | Соответствует любому символу, который **не** входит в `seq`<br>Например, `[!abc]` соответствует любому символу, кроме `a`, `b`, или `c` | `"file[!0-9].txt"` соответствует `"fileA.txt"`, но не `"file1.txt"` |

# Примеры использования

### Сопоставление строки с шаблоном
```python
import fnmatch

print(fnmatch.fnmatch("data.csv", "*.csv"))  # True
print(fnmatch.fnmatch("data.txt", "*.csv"))  # False
```

### Сопоставление с учетом регистра
```python
import fnmatch

print(fnmatch.fnmatchcase("Data.CSV", "*.csv"))  # False
print(fnmatch.fnmatchcase("Data.CSV", "*.CSV"))  # True
```

### Фильтрация списка файлов
```python
import fnmatch

files = ["data1.csv", "data2.txt", "data3.csv"]
csv_files = fnmatch.filter(files, "*.csv")
print(csv_files)  # ["data1.csv", "data3.csv"]
```

### Использование с регулярными выражениями
```python
import fnmatch
import re

pattern = fnmatch.translate("*.txt")
print(pattern)  # (?s:.*\.txt)\Z

regex = re.compile(pattern)
print(regex.match("file.txt"))  # <re.Match object; span=(0, 8), match='file.txt'>
print(regex.match("file.csv"))  # None
```

## Примечания

- На Unix-системах функции `fnmatch()` и `fnmatchcase()` работают **с учетом регистра**, а на Windows они **регистронезависимы**
Однако `fnmatchcase()` **всегда учитывает регистр**, независимо от платформы
- Используйте `fnmatch.translate()` для сложных сопоставлений, которые требуют регулярных выражений

# Полезные примеры

### Сопоставление с шаблоном для нескольких расширений
```python
import fnmatch

files = ["report.doc", "data.csv", "image.png", "script.py"]
docs = fnmatch.filter(files, "*.[dc][so][cv]")
print(docs)  # ["report.doc", "data.csv"]
```

### Фильтрация скрытых файлов (начинающихся с точки)
```python
import fnmatch

files = [".bashrc", "data.csv", ".gitignore", "script.py"]
hidden_files = fnmatch.filter(files, ".*")
print(hidden_files)  # [".bashrc", ".gitignore"]
```

# Полезные ссылки

- [Официальная документация](https://docs.python.org/3/library/fnmatch.html)
- [Real Python - Guide to Filename Matching](https://realpython.com/lessons/filename-matching/)
