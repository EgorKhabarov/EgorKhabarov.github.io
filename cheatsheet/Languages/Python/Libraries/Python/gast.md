Библиотека "gast" используется для анализа и модификации абстрактного синтаксического дерева (AST) в Python.
Она предоставляет инструменты для работы с AST, такие как обход узлов дерева, замена узлов, добавление новых узлов и т.д.

Методы модуля "gast" и его подмодулей:

Модуль "gast":
NodeVisitor: Класс для обхода узлов AST.
NodeTransformer: Класс для модификации узлов AST.
parse: Функция для преобразования исходного кода в AST.


NodeVisitor: Класс, который позволяет обойти все узлы AST и выполнить определенные действия для каждого узла.

```python
from gast import NodeVisitor

class MyVisitor(NodeVisitor):
    def visit_FunctionDef(self, node):
        print("Found a function definition:", node.name)

# Создание экземпляра класса и обход AST
visitor = MyVisitor()
visitor.visit(ast_tree)
```

NodeTransformer: Класс, который позволяет модифицировать узлы AST путем замены, добавления или удаления узлов.

```python
from gast import NodeTransformer

class MyTransformer(NodeTransformer):
    def visit_FunctionDef(self, node):
        # Изменение имени функции
        node.name = "new_function_name"
        return node

# Создание экземпляра класса и модификация AST
transformer = MyTransformer()
new_ast_tree = transformer.visit(ast_tree)
```

parse: Функция, которая преобразует исходный код в AST.

```python
from gast import parse

source_code = "print('Hello, World!')"
ast_tree = parse(source_code)
```
