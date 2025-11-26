Библиотека `Rich` - это мощный инструмент для форматирования текста, вывода в терминал с использованием стилей,
цветов, таблиц, прогресс-баров и других элементов пользовательского интерфейса
Она облегчает создание красивого и информативного вывода в консоли
Библиотека также поддерживает рендеринг логов и трассировок ошибок

# Основные возможности

1. **Цветной и стилизованный текст**
2. **Отображение таблиц**
3. **Прогресс-бары**
4. **Логи и трассировки ошибок**
5. **Отображение деревьев**
6. **Поддержка разметки Markdown**

# Установка

```bash
pip install rich
```

### Пример простого форматированного текста

```python
rich.print("[bold magenta]Hello, [italic]Rich[/italic]!")
```
> <span style="color:magenta"><span style="font-weight:700">Hello, <span style="font-style:italic">Rich</span>!</span></span>


## Основные функции и примеры

### Форматирование текста
В `Rich` используется синтаксис разметки для стилизации текста
Стили можно комбинировать
```python
rich.print("[bold red]Ошибка:[/] неверный ввод!")
```
> <span style="font-weight:700;color:red">Ошибка:</span> неверный ввод!

Возможные стили: `bold`, `italic`, `underline`, `strikethrough`,
а также цветовые схемы (`red`, `green`, `blue` и другие)

## Таблицы
Вы можете создавать и выводить таблицы с помощью класса `Table`
```python
from rich.table import Table
from rich.console import Console


console = Console()

table = Table(title="Таблица Пользователей")

table.add_column("Имя", justify="right", style="cyan", no_wrap=True)
table.add_column("Возраст", style="magenta")
table.add_column("Профессия", justify="right", style="green")

table.add_row("Иван", "32", "Инженер")
table.add_row("Анна", "28", "Дизайнер")
table.add_row("Петр", "40", "Менеджер")

console.print(table)
```
> &nbsp;&nbsp;&nbsp;&nbsp;<span style="font-style:italic">Таблица Пользователей</span>
> ┏━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━┓
> ┃  Имя ┃ Возраст ┃ Профессия ┃
> ┡━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━┩
> │ <span style="color:cyan">Иван</span> │ <span style="color:magenta">32</span>      │   <span style="color:green">Инженер</span> │
> │ <span style="color:cyan">Анна</span> │ <span style="color:magenta">28</span>      │  <span style="color:green">Дизайнер</span> │
> │ <span style="color:cyan">Петр</span> │ <span style="color:magenta">40</span>      │  <span style="color:green">Менеджер</span> │
> └──────┴─────────┴───────────┘


Этот код создаст таблицу с тремя столбцами, которая будет выведена в консоль с цветами и выравниванием

### Прогресс-бары
```python
import time
from rich.progress import Progress


with Progress() as progress:
    task = progress.add_task("Обработка...", total=100)
    while not progress.finished:
        progress.update(task, advance=1)
        time.sleep(0.1)
```

Прогресс-бар будет обновляться в реальном времени, показывая прогресс задачи

### Логи

`Rich` интегрируется с модулем `logging`, позволяя выводить цветные и более информативные логи

```python
import logging
from rich.logging import RichHandler


logging.basicConfig(level="NOTSET", handlers=[RichHandler()])
log = logging.getLogger("rich")

log.info("Это информационное сообщение")
log.error("Это ошибка")
```

### Трассировки ошибок

`Rich` может красиво отображать трассировки ошибок, улучшая их читаемость

```python
from rich.console import Console


console = Console()

try:
    1 / 0
except ZeroDivisionError:
    console.print_exception()
```

### Деревья

С помощью `Tree` можно отображать данные в виде иерархических деревьев

```python
from rich.tree import Tree
from rich.console import Console


console = Console()

tree = Tree("Файловая система")
tree.add("Папка 1")
tree.add("Папка 2").add("Файл 1")

console.print(tree)
"""
Файловая система
├── Папка 1
└── Папка 2
    └── Файл 1
"""
```

### Markdown

`Rich` поддерживает рендеринг разметки Markdown

```python
from rich.console import Console
from rich.markdown import Markdown


console = Console()
md = Markdown(
    """
# Заголовок

* Пункт 1
* Пункт 2
"""
)
console.print(md)
"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                Заголовок                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

 • Пункт 1
 • Пункт 2
"""
```

# Дополнительные возможности

- **Списки**: Создание стилизованных списков
- **JSON**: Вывод `JSON` данных в цвете
- **Ограничение по ширине**: Вывод данных с ограничением по ширине консоли
