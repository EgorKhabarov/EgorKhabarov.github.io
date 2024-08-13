<p>Библиотека "notebook" используется для создания интерактивных блокнотов в среде Jupyter Notebook.
Она предоставляет возможность комбинировать код, текст, графики и другие элементы в одном документе,
что делает его удобным инструментом для исследования данных, прототипирования и обучения.</p>
<p>Методы модуля "notebook" и его подмодулей:</p>
<p>Модуль "notebook":
<code>list_notebooks()</code>: возвращает список всех блокнотов в текущем рабочем каталоге.
<code>open_notebook(path)</code>: открывает блокнот по указанному пути.
<code>create_notebook()</code>: создает новый блокнот.
<code>save_notebook(path)</code>: сохраняет текущий блокнот по указанному пути.
<code>export_notebook(path, format)</code>: экспортирует блокнот в указанный формат (например, HTML, PDF).</p>
<p>Подмодуль "cells":
<code>list_cells()</code>: возвращает список всех ячеек в текущем блокноте.
<code>add_code_cell()</code>: добавляет новую ячейку с кодом.
<code>add_markdown_cell()</code>: добавляет новую ячейку с текстом в формате Markdown.
<code>delete_cell(index)</code>: удаляет ячейку по указанному индексу.</p>
<p>Самые часто используемые методы:</p>
<p><code>list_notebooks()</code>: возвращает список всех блокнотов в текущем рабочем каталоге.</p>
<pre><code class="language-python">from notebook import list_notebooks

notebooks = list_notebooks()
print(notebooks)
</code></pre>
<p><code>open_notebook(path)</code>: открывает блокнот по указанному пути.</p>
<pre><code class="language-python">from notebook import open_notebook

notebook = open_notebook(&quot;path/to/notebook.ipynb&quot;)
print(notebook)
</code></pre>
<p><code>create_notebook()</code>: создает новый блокнот.</p>
<pre><code class="language-python">from notebook import create_notebook

notebook = create_notebook()
print(notebook)
</code></pre>
<p><code>save_notebook(path)</code>: сохраняет текущий блокнот по указанному пути.</p>
<pre><code class="language-python">from notebook import save_notebook

save_notebook(&quot;path/to/save.ipynb&quot;)
</code></pre>
<p><code>list_cells()</code>: возвращает список всех ячеек в текущем блокноте.</p>
<pre><code class="language-python">from notebook.cells import list_cells

cells = list_cells()
print(cells)
</code></pre>
<p><code>add_code_cell()</code>: добавляет новую ячейку с кодом.</p>
<pre><code class="language-python">from notebook.cells import add_code_cell

cell = add_code_cell()
print(cell)
</code></pre>
<p><code>add_markdown_cell()</code>: добавляет новую ячейку с текстом в формате Markdown.</p>
<pre><code class="language-python">from notebook.cells import add_markdown_cell

cell = add_markdown_cell()
print(cell)
</code></pre>
<p><code>delete_cell(index)</code>: удаляет ячейку по указанному индексу.</p>
<pre><code class="language-python">from notebook.cells import delete_cell

delete_cell(0)
</code></pre>