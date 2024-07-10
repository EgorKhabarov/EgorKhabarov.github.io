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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codecf7a0fbc25845d41650b49f89992872fb" onclick="copyCode(codecf7a0fbc25845d41650b49f89992872f, codecf7a0fbc25845d41650b49f89992872fb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codecf7a0fbc25845d41650b49f89992872f"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook</span> <span class="kn">import</span> <span class="n">list_notebooks</span>

<span class="n">notebooks</span> <span class="o">=</span> <span class="n">list_notebooks</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">notebooks</span><span class="p">)</span>
</pre></div></div></div>

<p><code>open_notebook(path)</code>: открывает блокнот по указанному пути.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code6978a54b9ec661c0b3f23689fc4cf11cb" onclick="copyCode(code6978a54b9ec661c0b3f23689fc4cf11c, code6978a54b9ec661c0b3f23689fc4cf11cb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code6978a54b9ec661c0b3f23689fc4cf11c"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook</span> <span class="kn">import</span> <span class="n">open_notebook</span>

<span class="n">notebook</span> <span class="o">=</span> <span class="n">open_notebook</span><span class="p">(</span><span class="s1">&#39;path/to/notebook.ipynb&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">notebook</span><span class="p">)</span>
</pre></div></div></div>

<p><code>create_notebook()</code>: создает новый блокнот.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codec3d816375627404f34f9f9148c843e6cb" onclick="copyCode(codec3d816375627404f34f9f9148c843e6c, codec3d816375627404f34f9f9148c843e6cb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codec3d816375627404f34f9f9148c843e6c"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook</span> <span class="kn">import</span> <span class="n">create_notebook</span>

<span class="n">notebook</span> <span class="o">=</span> <span class="n">create_notebook</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">notebook</span><span class="p">)</span>
</pre></div></div></div>

<p><code>save_notebook(path)</code>: сохраняет текущий блокнот по указанному пути.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code54b8ddfa87cc72bb8749d5de840d69e6b" onclick="copyCode(code54b8ddfa87cc72bb8749d5de840d69e6, code54b8ddfa87cc72bb8749d5de840d69e6b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code54b8ddfa87cc72bb8749d5de840d69e6"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook</span> <span class="kn">import</span> <span class="n">save_notebook</span>

<span class="n">save_notebook</span><span class="p">(</span><span class="s1">&#39;path/to/save.ipynb&#39;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>list_cells()</code>: возвращает список всех ячеек в текущем блокноте.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code237faa959cdd8200bd3806689a00c172b" onclick="copyCode(code237faa959cdd8200bd3806689a00c172, code237faa959cdd8200bd3806689a00c172b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code237faa959cdd8200bd3806689a00c172"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook.cells</span> <span class="kn">import</span> <span class="n">list_cells</span>

<span class="n">cells</span> <span class="o">=</span> <span class="n">list_cells</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cells</span><span class="p">)</span>
</pre></div></div></div>

<p><code>add_code_cell()</code>: добавляет новую ячейку с кодом.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code721aa27227c883f306c094ee3bd60569b" onclick="copyCode(code721aa27227c883f306c094ee3bd60569, code721aa27227c883f306c094ee3bd60569b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code721aa27227c883f306c094ee3bd60569"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook.cells</span> <span class="kn">import</span> <span class="n">add_code_cell</span>

<span class="n">cell</span> <span class="o">=</span> <span class="n">add_code_cell</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cell</span><span class="p">)</span>
</pre></div></div></div>

<p><code>add_markdown_cell()</code>: добавляет новую ячейку с текстом в формате Markdown.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code9fa46b9565930db796c4cb22218212d0b" onclick="copyCode(code9fa46b9565930db796c4cb22218212d0, code9fa46b9565930db796c4cb22218212d0b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code9fa46b9565930db796c4cb22218212d0"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook.cells</span> <span class="kn">import</span> <span class="n">add_markdown_cell</span>

<span class="n">cell</span> <span class="o">=</span> <span class="n">add_markdown_cell</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cell</span><span class="p">)</span>
</pre></div></div></div>

<p><code>delete_cell(index)</code>: удаляет ячейку по указанному индексу.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code74f649098765c3bf411101c13e694c6eb" onclick="copyCode(code74f649098765c3bf411101c13e694c6e, code74f649098765c3bf411101c13e694c6eb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code74f649098765c3bf411101c13e694c6e"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">notebook.cells</span> <span class="kn">import</span> <span class="n">delete_cell</span>

<span class="n">delete_cell</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</pre></div></div></div>