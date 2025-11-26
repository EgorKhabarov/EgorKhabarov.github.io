Библиотека "getopt" в Python используется для разбора аргументов командной строки
Она позволяет программам легко определять и обрабатывать аргументы, передаваемые при запуске программы

Методы и подмодули библиотеки "getopt":
getopt.getopt(args, shortopts, longopts=None): Парсит аргументы командной строки, возвращает пару (opts, args), где opts - список кортежей со значением и аргументом, args - список непарсированных аргументов
getopt.gnu_getopt(args, shortopts, longopts=None): Аналогичен методу getopt.getopt(), но поддерживает нестандартный формат аргументов, включая возможность использования дефисов в значении аргумента
getopt.GetoptError: Исключение, возникающее при ошибке разбора аргументов командной строки. Оно содержит информацию об ошибке и методы для доступа к ней


getopt.getopt(args, shortopts, longopts=None): Парсит аргументы командной строки и возвращает опции и аргументы

```python
import getopt
import sys

args = sys.argv[1:]
shortopts = "ho:v"   # Опции без аргументов: -h, -o, -v
longopts = ["help", "output=", "verbose"]  # Опции с аргументами: --help, --output, --verbose

try:
    opts, args = getopt.getopt(args, shortopts, longopts)
except getopt.GetoptError:
    print("Ошибка в аргументах командной строки.")
```

getopt.gnu_getopt(args, shortopts, longopts=None): Парсит аргументы командной строки с нестандартным форматом и возвращает опции и аргументы

```python
import getopt
import sys

args = sys.argv[1:]
shortopts = "ho:v"   # Опции без аргументов: -h, -o, -v
longopts = ["help", "output=", "verbose"]  # Опции с аргументами: --help, --output, --verbose

try:
    opts, args = getopt.gnu_getopt(args, shortopts, longopts)
except getopt.GetoptError:
    print("Ошибка в аргументах командной строки.")
```
