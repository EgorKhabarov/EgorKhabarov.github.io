<p>Библиотека "gast" используется для анализа и модификации абстрактного синтаксического дерева (AST) в Python.
Она предоставляет инструменты для работы с AST, такие как обход узлов дерева, замена узлов, добавление новых узлов и т.д.</p>
<p>Методы модуля "gast" и его подмодулей:</p>
<p>Модуль "gast":
NodeVisitor: Класс для обхода узлов AST.
NodeTransformer: Класс для модификации узлов AST.
parse: Функция для преобразования исходного кода в AST.</p>
<p>NodeVisitor: Класс, который позволяет обойти все узлы AST и выполнить определенные действия для каждого узла.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gast</span> <span class="kn">import</span> <span class="n">NodeVisitor</span>

<span class="k">class</span> <span class="nc">MyVisitor</span><span class="p">(</span><span class="n">NodeVisitor</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">visit_FunctionDef</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Found a function definition:&quot;</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>

<span class="c1"># Создание экземпляра класса и обход AST</span>
<span class="n">visitor</span> <span class="o">=</span> <span class="n">MyVisitor</span><span class="p">()</span>
<span class="n">visitor</span><span class="o">.</span><span class="n">visit</span><span class="p">(</span><span class="n">ast_tree</span><span class="p">)</span>
</pre></div></div></div>

<p>NodeTransformer: Класс, который позволяет модифицировать узлы AST путем замены, добавления или удаления узлов.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gast</span> <span class="kn">import</span> <span class="n">NodeTransformer</span>

<span class="k">class</span> <span class="nc">MyTransformer</span><span class="p">(</span><span class="n">NodeTransformer</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">visit_FunctionDef</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">):</span>
        <span class="c1"># Изменение имени функции</span>
        <span class="n">node</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;new_function_name&quot;</span>
        <span class="k">return</span> <span class="n">node</span>

<span class="c1"># Создание экземпляра класса и модификация AST</span>
<span class="n">transformer</span> <span class="o">=</span> <span class="n">MyTransformer</span><span class="p">()</span>
<span class="n">new_ast_tree</span> <span class="o">=</span> <span class="n">transformer</span><span class="o">.</span><span class="n">visit</span><span class="p">(</span><span class="n">ast_tree</span><span class="p">)</span>
</pre></div></div></div>

<p>parse: Функция, которая преобразует исходный код в AST.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gast</span> <span class="kn">import</span> <span class="n">parse</span>

<span class="n">source_code</span> <span class="o">=</span> <span class="s2">&quot;print(&#39;Hello, World!&#39;)&quot;</span>
<span class="n">ast_tree</span> <span class="o">=</span> <span class="n">parse</span><span class="p">(</span><span class="n">source_code</span><span class="p">)</span>
</pre></div></div></div>