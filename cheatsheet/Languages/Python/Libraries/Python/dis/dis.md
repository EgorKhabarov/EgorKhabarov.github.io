Библиотека `dis` в Python предоставляет функции для дизассемблирования байт-кода
Она используется для анализа низкоуровневого байт-кода Python
и может быть полезна для отладки, оптимизации производительности и исследования внутренней работы интерпретатора

Вот шпаргалка по библиотеке **`dis`**, включающая ключевые функции и классы

### Основные функции `dis`
| Функция                     | Описание                                                                                                                                        | Пример использования                                                                                   |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `dis.dis(obj)`              | Дизассемблирует функцию, метод, класс,<br>модуль или объект и выводит байт-код в читабельном виде                                               | `import dis; dis.dis(some_function)`                                                                   |
| `dis.code_info(obj)`        | Выводит подробную информацию о коде функции,<br>метода или объекта в виде строки<br>(имя, аргументы, количество инструкций и т.д.)              | `import dis; print(dis.code_info(some_function))`                                                      |
| `dis.show_code(obj)`        | Показывает информацию о коде объекта,<br>включая аргументы и размеры                                                                            | `dis.show_code(some_function)`                                                                         |
| `dis.get_instructions(obj)` | Возвращает итератор инструкций байт-кода для объекта<br>(функции, метода или класса)                                                            | `instructions = list(dis.get_instructions(some_function))`                                             |
| `dis.Bytecode(obj)`         | Возвращает объект `Bytecode`, представляющий<br>инструкции байт-кода для объекта.<br>Можно использовать для итерации по инструкциям             | `bytecode = dis.Bytecode(some_function)`<br>`for instr in bytecode: print(instr.opname, instr.argval)` |
| `dis.distb([tb])`           | Дизассемблирует байт-код последней трассировки (traceback)<br>или переданного объекта трассировки,<br>полезно для анализа ошибок в стек-трейсах | `try: 1/0; except ZeroDivisionError: dis.distb()`                                                      |
| `dis.disassemble(code)`     | Дизассемблирует объект кода (code object) и возвращает его инструкции                                                                           | `code = some_function.__code__`<br>`dis.disassemble(code)`                                             |

### Классы в библиотеке `dis`

| Класс             | Описание                                                                                                                              | Пример использования                                                                                            |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `dis.Bytecode`    | Представляет последовательность инструкций байт-кода для объекта.<br>Можно итерировать по объектам этого класса для анализа байт-кода | `bytecode = dis.Bytecode(some_function)`<br>`for instr in bytecode:`<br>`    print(instr.opname, instr.argval)` |
| `dis.Instruction` | Описывает одну инструкцию байт-кода, содержит такие поля как<br>`opcode`, `opname`, `arg`, `argval`, `starts_line` и т.д              | `for instr in dis.get_instructions(some_function):`<br>`    print(instr.opname, instr.argval)`                  |

### Поля класса `dis.Instruction`

| Поле             | Описание                                                                                                                      |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `opcode`         | Числовое значение кода операции (инструкции байт-кода)                                                                        |
| `opname`         | Имя инструкции (например, `LOAD_CONST`, `RETURN_VALUE`)                                                                       |
| `arg`            | Аргумент инструкции (может быть None, если у инструкции нет аргументов)                                                       |
| `argval`         | Значение аргумента инструкции (например, константа, которая загружается инструкцией `LOAD_CONST`)                             |
| `argrepr`        | Представление аргумента в виде строки (удобное для чтения описание)                                                           |
| `offset`         | Смещение инструкции относительно начала байт-кода (в байтах)                                                                  |
| `starts_line`    | Номер строки Python-кода, с которой начинается выполнение инструкции (или None, если инструкция не начинается с новой строки) |
| `is_jump_target` | Булево значение, указывающее, является ли инструкция целью перехода                                                           |

### Дизассемблирование кода

Пример дизассемблирования функции
```python
import dis

def example(a, b):
    return a + b

dis.dis(example)
```

```
  2           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
```

### Разбор объектов с помощью `dis.get_instructions`

```python
import dis

def example(a, b):
    return a + b

for instr in dis.get_instructions(example):
    print(instr.opname, instr.argval)
```

```
LOAD_FAST a
LOAD_FAST b
BINARY_ADD None
RETURN_VALUE None
```

### Примеры других функций

**`dis.code_info()`** для получения информации о функции
```python
import dis

def example(a, b):
  return a + b

print(dis.code_info(example))
```

```
Name:              example
Argument count:    2
Positional-only arguments: 0
Kw-only arguments: 0
Number of locals:  2
Stack size:        2
Flags:             OPTIMIZED, NEWLOCALS, NOFREE
```

### `dis.Bytecode`

Использование `Bytecode` для итерации по инструкциям
```python
import dis

def example(a, b):
    return a + b

bytecode = dis.Bytecode(example)

for instr in bytecode:
    print(instr.opname, instr.argval)
```

### Полезные функции для анализа исключений

**`dis.distb()`**: используется для дизассемблирования байт-кода по последней трассировке (traceback)
```python
try:
  1 / 0
except ZeroDivisionError:
  import dis
  dis.distb()
```

### Использование с модулями и классами

Можно дизассемблировать не только функции, но и модули целиком
```python
import dis

module_code = compile("a = 10\nb = 20\nc = a + b", "<string>", "exec")
dis.dis(module_code)
```

Это покажет инструкции для выполнения кода всего модуля.
