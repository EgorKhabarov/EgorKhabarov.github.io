# ast
**Abstract Syntax Tree** абстрактное синтаксическое дерево
Позволяет анализировать и изменять исходный код Python программ.
Она предоставляет инструменты для разбора (парсинга) Python-кода в дерево синтаксических структур,
а также для создания, модификации и компиляции этих деревьев обратно в исполняемый код.

# Основные функции и классы

### parse
Разбирает Python-код, представленный в виде строки, и возвращает его в виде абстрактного синтаксического дерева (AST).

```python
import ast

code = "x = 42"
tree = ast.parse(code)
print(ast.dump(tree, indent=4))
"""
Module(
   body=[
       Assign(
           targets=[Name(id="x", ctx=Store())],
           value=Constant(value=42))
   ],
   type_ignores=[])
"""
```

### dump
```python
ast.dump(node, annotate_fields=True, include_attributes=False, indent=None)
```
Возвращает строковое представление AST-дерева. Если `annotate_fields=True`,
добавляет аннотации полей, если `include_attributes=True`, включает информацию об атрибутах.

```python
code = "y = x + 2"
tree = ast.parse(code)
print(ast.dump(tree, indent=4))
"""
Module(
    body=[
        Assign(
            targets=[
                Name(id="y", ctx=Store())],
            value=BinOp(
                left=Name(id="x", ctx=Load()),
                op=Add(),
                right=Constant(value=2)))],
    type_ignores=[])
"""
```

### NodeVisitor
Класс, предназначенный для обхода узлов дерева.
Переопределяя методы этого класса, можно обрабатывать определённые типы узлов (например, выражения, переменные, функции).

```python
class MyVisitor(ast.NodeVisitor):
    def visit_Assign(self, node):
        print(f"Присваивание найдено: {ast.dump(node)}")
        self.generic_visit(node)

tree = ast.parse("x = 5")
visitor = MyVisitor()
visitor.visit(tree)
# Присваивание найдено: Assign(targets=[Name(id="x", ctx=Store())], value=Constant(value=5))
```

### NodeTransformer
Этот класс позволяет изменять дерево `AST`.
Переопределяя методы, можно модифицировать узлы.
Методы, возвращающие новые узлы, заменяют существующие.

```python
class Transformer(ast.NodeTransformer):
   def visit_BinOp(self, node):
       if isinstance(node.op, ast.Add):
           node.op = ast.Sub()
       return node

code = "x = 1 + 2"
tree = ast.parse(code)
transformer = Transformer()
new_tree = transformer.visit(tree)

# Скомпилируем и выполним новый код
exec(compile(new_tree, filename="<ast>", mode="exec"))
print(x)  # 1 - 2, то есть -1
```

### Expression & Module
Узлы верхнего уровня. `ast.Module` - это представление программы или модуля, состоящего из списка операторов.
`ast.Expression` - выражение, которое можно выполнить и получить значение.

```python
tree = ast.parse("x = 5", mode="exec")  # Режим модуля
expr_tree = ast.parse("x + 2", mode="eval")  # Режим выражения
```

### literal_eval
Безопасная функция для вычисления литеральных выражений из строки или узла `AST`.
Поддерживает только простые типы, такие как строки, числа, списки и словари.

```python
print(ast.literal_eval("[1, 2, 3]"))  # [1, 2, 3]
```

# Важные узлы AST

- `Module`: Главный узел для кода, представляющий модуль.
- `Expr`: Узел для выражений.
- `Assign`: Операция присваивания.
- `BinOp`: Бинарные операции (например, `+`, `-`, `*`).
- `FunctionDef`: Определение функции.
- `If`: Оператор `if`.
- `For`: Цикл `for`.
- `While`: Цикл `while`.
- `Call`: Вызов функции.

### Пример сложного AST-дерева

Рассмотрим более сложный пример с условием и циклом.

```python
import ast

code = """
def foo(x):
    if x > 10:
        return x * 2
    else:
        return x + 2
"""

tree = ast.parse(code)
print(ast.dump(tree, indent=4))
"""
Module(
    body=[
        FunctionDef(
            name="foo",
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg="x")],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]),
            body=[
                If(
                    test=Compare(
                        left=Name(id="x", ctx=Load()),
                        ops=[
                            Gt()],
                        comparators=[
                            Constant(value=10)]),
                    body=[
                        Return(
                            value=BinOp(
                                left=Name(id="x", ctx=Load()),
                                op=Mult(),
                                right=Constant(value=2)))],
                    orelse=[
                        Return(
                            value=BinOp(
                                left=Name(id="x", ctx=Load()),
                                op=Add(),
                                right=Constant(value=2)))])],
            decorator_list=[])],
    type_ignores=[])
"""
```

Вывод будет содержать структуру дерева, описывающую определение функции, условие `if` и возврат значений.

### Обработка и трансформация кода

`ast` позволяет писать программы, которые автоматически модифицируют Python-код.
Например, можно автоматически заменять одну операцию на другую, добавлять или изменять функции и так далее.

### Пример: замена оператора сложения на вычитание

```python
import ast

class SubtractTransformer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            node.op = ast.Sub()
        return self.generic_visit(node)

code = "result = 1 + 2 + 3"
tree = ast.parse(code)
transformed_tree = SubtractTransformer().visit(tree)

# Компилируем и выполняем новый код
exec(compile(transformed_tree, filename="<ast>", mode="exec"))
print(result)  # -4 (1 - 2 - 3)
```
