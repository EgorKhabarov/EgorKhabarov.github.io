<p>Библиотека "gast" используется для анализа и модификации абстрактного синтаксического дерева (AST) в Python.
Она предоставляет инструменты для работы с AST, такие как обход узлов дерева, замена узлов, добавление новых узлов и т.д.</p>
<p>Методы модуля "gast" и его подмодулей:</p>
<p>Модуль "gast":
NodeVisitor: Класс для обхода узлов AST.
NodeTransformer: Класс для модификации узлов AST.
parse: Функция для преобразования исходного кода в AST.</p>
<p>NodeVisitor: Класс, который позволяет обойти все узлы AST и выполнить определенные действия для каждого узла.</p>
<pre><code class="language-python">from gast import NodeVisitor

class MyVisitor(NodeVisitor):
    def visit_FunctionDef(self, node):
        print(&quot;Found a function definition:&quot;, node.name)

# Создание экземпляра класса и обход AST
visitor = MyVisitor()
visitor.visit(ast_tree)
</code></pre>
<p>NodeTransformer: Класс, который позволяет модифицировать узлы AST путем замены, добавления или удаления узлов.</p>
<pre><code class="language-python">from gast import NodeTransformer

class MyTransformer(NodeTransformer):
    def visit_FunctionDef(self, node):
        # Изменение имени функции
        node.name = &quot;new_function_name&quot;
        return node

# Создание экземпляра класса и модификация AST
transformer = MyTransformer()
new_ast_tree = transformer.visit(ast_tree)
</code></pre>
<p>parse: Функция, которая преобразует исходный код в AST.</p>
<pre><code class="language-python">from gast import parse

source_code = &quot;print('Hello, World!')&quot;
ast_tree = parse(source_code)
</code></pre>