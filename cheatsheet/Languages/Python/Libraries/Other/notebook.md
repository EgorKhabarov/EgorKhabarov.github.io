Библиотека "notebook" используется для создания интерактивных блокнотов в среде Jupyter Notebook.
Она предоставляет возможность комбинировать код, текст, графики и другие элементы в одном документе,
что делает его удобным инструментом для исследования данных, прототипирования и обучения.

Методы модуля "notebook" и его подмодулей:

Модуль "notebook":
`list_notebooks()`: возвращает список всех блокнотов в текущем рабочем каталоге.
`open_notebook(path)`: открывает блокнот по указанному пути.
`create_notebook()`: создает новый блокнот.
`save_notebook(path)`: сохраняет текущий блокнот по указанному пути.
`export_notebook(path, format)`: экспортирует блокнот в указанный формат (например, HTML, PDF).

Подмодуль "cells":
`list_cells()`: возвращает список всех ячеек в текущем блокноте.
`add_code_cell()`: добавляет новую ячейку с кодом.
`add_markdown_cell()`: добавляет новую ячейку с текстом в формате Markdown.
`delete_cell(index)`: удаляет ячейку по указанному индексу.

Самые часто используемые методы:

`list_notebooks()`: возвращает список всех блокнотов в текущем рабочем каталоге.

```python
from notebook import list_notebooks

notebooks = list_notebooks()
print(notebooks)
```

`open_notebook(path)`: открывает блокнот по указанному пути.

```python
from notebook import open_notebook

notebook = open_notebook("path/to/notebook.ipynb")
print(notebook)
```

`create_notebook()`: создает новый блокнот.

```python
from notebook import create_notebook

notebook = create_notebook()
print(notebook)
```

`save_notebook(path)`: сохраняет текущий блокнот по указанному пути.

```python
from notebook import save_notebook

save_notebook("path/to/save.ipynb")
```

`list_cells()`: возвращает список всех ячеек в текущем блокноте.

```python
from notebook.cells import list_cells

cells = list_cells()
print(cells)
```

`add_code_cell()`: добавляет новую ячейку с кодом.

```python
from notebook.cells import add_code_cell

cell = add_code_cell()
print(cell)
```

`add_markdown_cell()`: добавляет новую ячейку с текстом в формате Markdown.

```python
from notebook.cells import add_markdown_cell

cell = add_markdown_cell()
print(cell)
```

`delete_cell(index)`: удаляет ячейку по указанному индексу.

```python
from notebook.cells import delete_cell

delete_cell(0)
```
