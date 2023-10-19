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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code123b" onclick="copyCode(code123, code123b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code123"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook</span> <span class="kn">import</span> <span class="n">list_notebooks</span>

<span class="n">notebooks</span> <span class="o">=</span> <span class="n">list_notebooks</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">notebooks</span><span class="p">)</span>
</pre></div></div></div>

<p><code>open_notebook(path)</code>: открывает блокнот по указанному пути.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code124b" onclick="copyCode(code124, code124b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code124"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook</span> <span class="kn">import</span> <span class="n">open_notebook</span>

<span class="n">notebook</span> <span class="o">=</span> <span class="n">open_notebook</span><span class="p">(</span><span class="s1">&#39;path/to/notebook.ipynb&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">notebook</span><span class="p">)</span>
</pre></div></div></div>

<p><code>create_notebook()</code>: создает новый блокнот.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code125b" onclick="copyCode(code125, code125b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code125"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook</span> <span class="kn">import</span> <span class="n">create_notebook</span>

<span class="n">notebook</span> <span class="o">=</span> <span class="n">create_notebook</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">notebook</span><span class="p">)</span>
</pre></div></div></div>

<p><code>save_notebook(path)</code>: сохраняет текущий блокнот по указанному пути.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code126b" onclick="copyCode(code126, code126b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code126"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook</span> <span class="kn">import</span> <span class="n">save_notebook</span>

<span class="n">save_notebook</span><span class="p">(</span><span class="s1">&#39;path/to/save.ipynb&#39;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>list_cells()</code>: возвращает список всех ячеек в текущем блокноте.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code127b" onclick="copyCode(code127, code127b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code127"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook.cells</span> <span class="kn">import</span> <span class="n">list_cells</span>

<span class="n">cells</span> <span class="o">=</span> <span class="n">list_cells</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cells</span><span class="p">)</span>
</pre></div></div></div>

<p><code>add_code_cell()</code>: добавляет новую ячейку с кодом.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code128b" onclick="copyCode(code128, code128b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code128"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook.cells</span> <span class="kn">import</span> <span class="n">add_code_cell</span>

<span class="n">cell</span> <span class="o">=</span> <span class="n">add_code_cell</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cell</span><span class="p">)</span>
</pre></div></div></div>

<p><code>add_markdown_cell()</code>: добавляет новую ячейку с текстом в формате Markdown.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code129b" onclick="copyCode(code129, code129b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code129"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook.cells</span> <span class="kn">import</span> <span class="n">add_markdown_cell</span>

<span class="n">cell</span> <span class="o">=</span> <span class="n">add_markdown_cell</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cell</span><span class="p">)</span>
</pre></div></div></div>

<p><code>delete_cell(index)</code>: удаляет ячейку по указанному индексу.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code130b" onclick="copyCode(code130, code130b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code130"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook.cells</span> <span class="kn">import</span> <span class="n">delete_cell</span>

<span class="n">delete_cell</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</pre></div></div></div>