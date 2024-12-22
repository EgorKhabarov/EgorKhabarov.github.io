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
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook</span> <span class="kn">import</span> <span class="n">list_notebooks</span>

<span class="n">notebooks</span> <span class="o">=</span> <span class="n">list_notebooks</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">notebooks</span><span class="p">)</span>
</pre></div></div></div>

<p><code>open_notebook(path)</code>: открывает блокнот по указанному пути.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook</span> <span class="kn">import</span> <span class="n">open_notebook</span>

<span class="n">notebook</span> <span class="o">=</span> <span class="n">open_notebook</span><span class="p">(</span><span class="s2">&quot;path/to/notebook.ipynb&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">notebook</span><span class="p">)</span>
</pre></div></div></div>

<p><code>create_notebook()</code>: создает новый блокнот.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook</span> <span class="kn">import</span> <span class="n">create_notebook</span>

<span class="n">notebook</span> <span class="o">=</span> <span class="n">create_notebook</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">notebook</span><span class="p">)</span>
</pre></div></div></div>

<p><code>save_notebook(path)</code>: сохраняет текущий блокнот по указанному пути.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook</span> <span class="kn">import</span> <span class="n">save_notebook</span>

<span class="n">save_notebook</span><span class="p">(</span><span class="s2">&quot;path/to/save.ipynb&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>list_cells()</code>: возвращает список всех ячеек в текущем блокноте.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook.cells</span> <span class="kn">import</span> <span class="n">list_cells</span>

<span class="n">cells</span> <span class="o">=</span> <span class="n">list_cells</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cells</span><span class="p">)</span>
</pre></div></div></div>

<p><code>add_code_cell()</code>: добавляет новую ячейку с кодом.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook.cells</span> <span class="kn">import</span> <span class="n">add_code_cell</span>

<span class="n">cell</span> <span class="o">=</span> <span class="n">add_code_cell</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cell</span><span class="p">)</span>
</pre></div></div></div>

<p><code>add_markdown_cell()</code>: добавляет новую ячейку с текстом в формате Markdown.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook.cells</span> <span class="kn">import</span> <span class="n">add_markdown_cell</span>

<span class="n">cell</span> <span class="o">=</span> <span class="n">add_markdown_cell</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cell</span><span class="p">)</span>
</pre></div></div></div>

<p><code>delete_cell(index)</code>: удаляет ячейку по указанному индексу.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook.cells</span> <span class="kn">import</span> <span class="n">delete_cell</span>

<span class="n">delete_cell</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</pre></div></div></div>