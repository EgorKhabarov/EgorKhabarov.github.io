Библиотека `argparse` в Python позволяет легко создавать интерфейсы командной строки для ваших скриптов
Эта библиотека предоставляет механизмы для определения аргументов командной строки и автоматического
генерирования справочной информации и сообщений об ошибках

# Простой скрипт

```python@script.py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")

args = parser.parse_args()
print(args.echo)
```

> ```bash
python script.py hello
```
> hello

> ```bash
python script.py -h
```
> usage: script.py \[-h] echo
> 
> positional arguments:
>   echo        echo the string you use here
> 
> options:
>   -h, --help  show this help message and exit

# Аргументы с флагами

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")

args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
```

Для запуска скрипта нужно использовать команду

```bash
python script.py --verbosity
```

# Опциональный аргумент

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--number", help="enter a number", type=int)

args = parser.parse_args()
if args.number:
    print(args.number * 2)
```

Для запуска скрипта нужно использовать команду

```bash
python script.py --number 5
```

# Обязательный аргумент

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the name of the file to read")

args = parser.parse_args()
print(args.filename)
```

Для запуска скрипта нужно использовать команду

```bash
python script.py filename.txt
```

# Группировка аргументов

```python
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--verbose", help="increase output verbosity", action="store_true")
group.add_argument("--quiet", help="decrease output verbosity", action="store_true")

args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
elif args.quiet:
    print("verbosity turned off")
```

Для запуска скрипта нужно использовать команду

```bash
python script.py --verbose или python script.py --quiet
```




# Позиционные аргументы с выбором

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("operation", help="operation to perform", choices=["add", "sub", "mul", "div"])
parser.add_argument("num1", help="first number", type=int)
parser.add_argument("num2", help="second number", type=int)

args = parser.parse_args()
if args.operation == "add":
    print(args.num1 + args.num2)
elif args.operation == "sub":
    print(args.num1 - args.num2)
elif args.operation == "mul":
    print(args.num1 * args.num2)
else:
    print(args.num1 / args.num2)
```

Для запуска скрипта нужно использовать команду

```bash
python script.py add 5 3
```

# Описание программы и аргументов

```python
import argparse

parser = argparse.ArgumentParser(description="A simple calculator program")
parser.add_argument("operation", help="operation to perform", choices=["add", "sub", "mul", "div"])
parser.add_argument("num1", help="first number", type=int)
parser.add_argument("num2", help="second number", type=int)

args = parser.parse_args()
if args.operation == "add":
    print(args.num1 + args.num2)
elif args.operation == "sub":
    print(args.num1 - args.num2)
elif args.operation == "mul":
    print(args.num1 * args.num2)
else:
    print(args.num1 / args.num2)
```

Для запуска скрипта нужно использовать команду:

```bash
python script.py --help
```




# Парсинг аргументов из файла

```python
import argparse

parser = argparse.ArgumentParser(fromfile_prefix_chars="@")
parser.add_argument("operation", help="operation to perform", choices=["add", "sub", "mul", "div"])
parser.add_argument("num1", help="first number", type=int)
parser.add_argument("num2", help="second number", type=int)

args = parser.parse_args(["@args.txt"])
if args.operation == "add":
    print(args.num1 + args.num2)
elif args.operation == "sub":
    print(args.num1 - args.num2)
elif args.operation == "mul":
    print(args.num1 * args.num2)
else:
    print(args.num1 / args.num2)
```

Для использования данного примера нужно создать файл "args.txt" со следующим содержимым

```text
add 5 3
```

Затем, чтобы запустить скрипт, нужно использовать команду

```bash
python script.py @args.txt
```

# Аргумент со значением по умолчанию

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")
parser.add_argument("--num", help="a number", type=int, default=5)

args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
print(args.num * 2)
```

Для запуска скрипта нужно использовать команду

```bash
python script.py --verbosity --num 3
```

# Поддержка субкоманд

```python
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

parser_a = subparsers.add_parser("command_a", help="command a help")
parser_a.add_argument("foo", type=int, help="foo help")

parser_b = subparsers.add_parser("command_b", help="command b help")
parser_b.add_argument("--bar", type=str, help="bar help")

args = parser.parse_args()
if args.subcommand == "command_a":
    print(args.foo)
else:
    print(args.bar)
```

Для запуска скрипта нужно использовать команду:

```bash
python script.py command_a 5
```

или

```bash
python script.py command_b --bar test
```
