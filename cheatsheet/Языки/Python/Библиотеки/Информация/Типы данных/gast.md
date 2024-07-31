<p>Библиотека "gast" используется для анализа и модификации абстрактного синтаксического дерева (AST) в Python.
Она предоставляет инструменты для работы с AST, такие как обход узлов дерева, замена узлов, добавление новых узлов и т.д.</p>
<p>Методы модуля "gast" и его подмодулей:</p>
<p>Модуль "gast":
NodeVisitor: Класс для обхода узлов AST.
NodeTransformer: Класс для модификации узлов AST.
parse: Функция для преобразования исходного кода в AST.</p>
<p>NodeVisitor: Класс, который позволяет обойти все узлы AST и выполнить определенные действия для каждого узла.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="coded4d2f5a81a16203a844b0a949affb79ab"
          onclick="copyCode(coded4d2f5a81a16203a844b0a949affb79a, coded4d2f5a81a16203a844b0a949affb79ab)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
      <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
  </button>

</div>
<div class="code" id="coded4d2f5a81a16203a844b0a949affb79a"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gast</span> <span class="kn">import</span> <span class="n">NodeVisitor</span>

<span class="k">class</span> <span class="nc">MyVisitor</span><span class="p">(</span><span class="n">NodeVisitor</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">visit_FunctionDef</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Found a function definition:&quot;</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>

<span class="c1"># Создание экземпляра класса и обход AST</span>
<span class="n">visitor</span> <span class="o">=</span> <span class="n">MyVisitor</span><span class="p">()</span>
<span class="n">visitor</span><span class="o">.</span><span class="n">visit</span><span class="p">(</span><span class="n">ast_tree</span><span class="p">)</span>
</pre></div></div>
</div>

<p>NodeTransformer: Класс, который позволяет модифицировать узлы AST путем замены, добавления или удаления узлов.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codedaa897da5c9412415ab8f96e30b70499b"
          onclick="copyCode(codedaa897da5c9412415ab8f96e30b70499, codedaa897da5c9412415ab8f96e30b70499b)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
      <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
  </button>

</div>
<div class="code" id="codedaa897da5c9412415ab8f96e30b70499"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gast</span> <span class="kn">import</span> <span class="n">NodeTransformer</span>

<span class="k">class</span> <span class="nc">MyTransformer</span><span class="p">(</span><span class="n">NodeTransformer</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">visit_FunctionDef</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">):</span>
        <span class="c1"># Изменение имени функции</span>
        <span class="n">node</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;new_function_name&quot;</span>
        <span class="k">return</span> <span class="n">node</span>

<span class="c1"># Создание экземпляра класса и модификация AST</span>
<span class="n">transformer</span> <span class="o">=</span> <span class="n">MyTransformer</span><span class="p">()</span>
<span class="n">new_ast_tree</span> <span class="o">=</span> <span class="n">transformer</span><span class="o">.</span><span class="n">visit</span><span class="p">(</span><span class="n">ast_tree</span><span class="p">)</span>
</pre></div></div>
</div>

<p>parse: Функция, которая преобразует исходный код в AST.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code0d80563a79afdaf4d58b479f689c99f9b"
          onclick="copyCode(code0d80563a79afdaf4d58b479f689c99f9, code0d80563a79afdaf4d58b479f689c99f9b)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
      <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
  </button>

</div>
<div class="code" id="code0d80563a79afdaf4d58b479f689c99f9"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gast</span> <span class="kn">import</span> <span class="n">parse</span>

<span class="n">source_code</span> <span class="o">=</span> <span class="s2">&quot;print(&#39;Hello, World!&#39;)&quot;</span>
<span class="n">ast_tree</span> <span class="o">=</span> <span class="n">parse</span><span class="p">(</span><span class="n">source_code</span><span class="p">)</span>
</pre></div></div>
</div>