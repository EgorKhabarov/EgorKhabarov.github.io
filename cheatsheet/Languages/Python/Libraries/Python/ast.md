<h1>ast</h1>
<p><strong>Abstract Syntax Tree</strong> — абстрактное синтаксическое дерево
Позволяет анализировать и изменять исходный код Python программ.
Она предоставляет инструменты для разбора (парсинга) Python-кода в дерево синтаксических структур,
а также для создания, модификации и компиляции этих деревьев обратно в исполняемый код.</p>
<h1>Основные функции и классы</h1>
<h3>parse</h3>
<p>Разбирает Python-код, представленный в виде строки, и возвращает его в виде абстрактного синтаксического дерева (AST).</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">ast</span>

<span class="n">code</span> <span class="o">=</span> <span class="s2">&quot;x = 42&quot;</span>
<span class="n">tree</span> <span class="o">=</span> <span class="n">ast</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ast</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">tree</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">))</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">Module(</span>
<span class="sd">   body=[</span>
<span class="sd">       Assign(</span>
<span class="sd">           targets=[Name(id=&quot;x&quot;, ctx=Store())],</span>
<span class="sd">           value=Constant(value=42))</span>
<span class="sd">   ],</span>
<span class="sd">   type_ignores=[])</span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div></div></div>

<h3>dump</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">ast</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">annotate_fields</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">include_attributes</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
</pre></div></div></div>
<p>Возвращает строковое представление AST-дерева. Если <code>annotate_fields=True</code>,
добавляет аннотации полей, если <code>include_attributes=True</code>, включает информацию об атрибутах.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">code</span> <span class="o">=</span> <span class="s2">&quot;y = x + 2&quot;</span>
<span class="n">tree</span> <span class="o">=</span> <span class="n">ast</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ast</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">tree</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">))</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">Module(</span>
<span class="sd">    body=[</span>
<span class="sd">        Assign(</span>
<span class="sd">            targets=[</span>
<span class="sd">                Name(id=&quot;y&quot;, ctx=Store())],</span>
<span class="sd">            value=BinOp(</span>
<span class="sd">                left=Name(id=&quot;x&quot;, ctx=Load()),</span>
<span class="sd">                op=Add(),</span>
<span class="sd">                right=Constant(value=2)))],</span>
<span class="sd">    type_ignores=[])</span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div></div></div>

<h3>NodeVisitor</h3>
<p>Класс, предназначенный для обхода узлов дерева.
Переопределяя методы этого класса, можно обрабатывать определённые типы узлов (например, выражения, переменные, функции).</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyVisitor</span><span class="p">(</span><span class="n">ast</span><span class="o">.</span><span class="n">NodeVisitor</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">visit_Assign</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Присваивание найдено: </span><span class="si">{</span><span class="n">ast</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">node</span><span class="p">)</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">generic_visit</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

<span class="n">tree</span> <span class="o">=</span> <span class="n">ast</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="s2">&quot;x = 5&quot;</span><span class="p">)</span>
<span class="n">visitor</span> <span class="o">=</span> <span class="n">MyVisitor</span><span class="p">()</span>
<span class="n">visitor</span><span class="o">.</span><span class="n">visit</span><span class="p">(</span><span class="n">tree</span><span class="p">)</span>
<span class="c1"># Присваивание найдено: Assign(targets=[Name(id=&quot;x&quot;, ctx=Store())], value=Constant(value=5))</span>
</pre></div></div></div>

<h3>NodeTransformer</h3>
<p>Этот класс позволяет изменять дерево <code>AST</code>.
Переопределяя методы, можно модифицировать узлы.
Методы, возвращающие новые узлы, заменяют существующие.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Transformer</span><span class="p">(</span><span class="n">ast</span><span class="o">.</span><span class="n">NodeTransformer</span><span class="p">):</span>
   <span class="k">def</span> <span class="nf">visit_BinOp</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">):</span>
       <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">op</span><span class="p">,</span> <span class="n">ast</span><span class="o">.</span><span class="n">Add</span><span class="p">):</span>
           <span class="n">node</span><span class="o">.</span><span class="n">op</span> <span class="o">=</span> <span class="n">ast</span><span class="o">.</span><span class="n">Sub</span><span class="p">()</span>
       <span class="k">return</span> <span class="n">node</span>

<span class="n">code</span> <span class="o">=</span> <span class="s2">&quot;x = 1 + 2&quot;</span>
<span class="n">tree</span> <span class="o">=</span> <span class="n">ast</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
<span class="n">transformer</span> <span class="o">=</span> <span class="n">Transformer</span><span class="p">()</span>
<span class="n">new_tree</span> <span class="o">=</span> <span class="n">transformer</span><span class="o">.</span><span class="n">visit</span><span class="p">(</span><span class="n">tree</span><span class="p">)</span>

<span class="c1"># Скомпилируем и выполним новый код</span>
<span class="n">exec</span><span class="p">(</span><span class="nb">compile</span><span class="p">(</span><span class="n">new_tree</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="s2">&quot;&lt;ast&gt;&quot;</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s2">&quot;exec&quot;</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>  <span class="c1"># 1 - 2, то есть -1</span>
</pre></div></div></div>

<h3>Expression &amp; Module</h3>
<p>Узлы верхнего уровня. <code>ast.Module</code> — это представление программы или модуля, состоящего из списка операторов.
<code>ast.Expression</code> — выражение, которое можно выполнить и получить значение.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">tree</span> <span class="o">=</span> <span class="n">ast</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="s2">&quot;x = 5&quot;</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s2">&quot;exec&quot;</span><span class="p">)</span>  <span class="c1"># Режим модуля</span>
<span class="n">expr_tree</span> <span class="o">=</span> <span class="n">ast</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="s2">&quot;x + 2&quot;</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s2">&quot;eval&quot;</span><span class="p">)</span>  <span class="c1"># Режим выражения</span>
</pre></div></div></div>

<h3>literal_eval</h3>
<p>Безопасная функция для вычисления литеральных выражений из строки или узла <code>AST</code>.
Поддерживает только простые типы, такие как строки, числа, списки и словари.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">ast</span><span class="o">.</span><span class="n">literal_eval</span><span class="p">(</span><span class="s2">&quot;[1, 2, 3]&quot;</span><span class="p">))</span>  <span class="c1"># [1, 2, 3]</span>
</pre></div></div></div>

<h1>Важные узлы AST</h1>
<ul>
<li><strong><code>Module</code></strong>: Главный узел для кода, представляющий модуль.</li>
<li><strong><code>Expr</code></strong>: Узел для выражений.</li>
<li><strong><code>Assign</code></strong>: Операция присваивания.</li>
<li><strong><code>BinOp</code></strong>: Бинарные операции (например, <code>+</code>, <code>-</code>, <code>*</code>).</li>
<li><strong><code>FunctionDef</code></strong>: Определение функции.</li>
<li><strong><code>If</code></strong>: Оператор <code>if</code>.</li>
<li><strong><code>For</code></strong>: Цикл <code>for</code>.</li>
<li><strong><code>While</code></strong>: Цикл <code>while</code>.</li>
<li><strong><code>Call</code></strong>: Вызов функции.</li>
</ul>
<h3>Пример сложного AST-дерева</h3>
<p>Рассмотрим более сложный пример с условием и циклом.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">ast</span>

<span class="n">code</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span>
<span class="s2">def foo(x):</span>
<span class="s2">    if x &gt; 10:</span>
<span class="s2">        return x * 2</span>
<span class="s2">    else:</span>
<span class="s2">        return x + 2</span>
<span class="s2">&quot;&quot;&quot;</span>

<span class="n">tree</span> <span class="o">=</span> <span class="n">ast</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ast</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">tree</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">))</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">Module(</span>
<span class="sd">    body=[</span>
<span class="sd">        FunctionDef(</span>
<span class="sd">            name=&quot;foo&quot;,</span>
<span class="sd">            args=arguments(</span>
<span class="sd">                posonlyargs=[],</span>
<span class="sd">                args=[</span>
<span class="sd">                    arg(arg=&quot;x&quot;)],</span>
<span class="sd">                kwonlyargs=[],</span>
<span class="sd">                kw_defaults=[],</span>
<span class="sd">                defaults=[]),</span>
<span class="sd">            body=[</span>
<span class="sd">                If(</span>
<span class="sd">                    test=Compare(</span>
<span class="sd">                        left=Name(id=&quot;x&quot;, ctx=Load()),</span>
<span class="sd">                        ops=[</span>
<span class="sd">                            Gt()],</span>
<span class="sd">                        comparators=[</span>
<span class="sd">                            Constant(value=10)]),</span>
<span class="sd">                    body=[</span>
<span class="sd">                        Return(</span>
<span class="sd">                            value=BinOp(</span>
<span class="sd">                                left=Name(id=&quot;x&quot;, ctx=Load()),</span>
<span class="sd">                                op=Mult(),</span>
<span class="sd">                                right=Constant(value=2)))],</span>
<span class="sd">                    orelse=[</span>
<span class="sd">                        Return(</span>
<span class="sd">                            value=BinOp(</span>
<span class="sd">                                left=Name(id=&quot;x&quot;, ctx=Load()),</span>
<span class="sd">                                op=Add(),</span>
<span class="sd">                                right=Constant(value=2)))])],</span>
<span class="sd">            decorator_list=[])],</span>
<span class="sd">    type_ignores=[])</span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div></div></div>

<p>Вывод будет содержать структуру дерева, описывающую определение функции, условие <code>if</code> и возврат значений.</p>
<h3>Обработка и трансформация кода</h3>
<p><code>ast</code> позволяет писать программы, которые автоматически модифицируют Python-код.
Например, можно автоматически заменять одну операцию на другую, добавлять или изменять функции и так далее.</p>
<h3>Пример: замена оператора сложения на вычитание</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">ast</span>

<span class="k">class</span> <span class="nc">SubtractTransformer</span><span class="p">(</span><span class="n">ast</span><span class="o">.</span><span class="n">NodeTransformer</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">visit_BinOp</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">):</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">op</span><span class="p">,</span> <span class="n">ast</span><span class="o">.</span><span class="n">Add</span><span class="p">):</span>
            <span class="n">node</span><span class="o">.</span><span class="n">op</span> <span class="o">=</span> <span class="n">ast</span><span class="o">.</span><span class="n">Sub</span><span class="p">()</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">generic_visit</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

<span class="n">code</span> <span class="o">=</span> <span class="s2">&quot;result = 1 + 2 + 3&quot;</span>
<span class="n">tree</span> <span class="o">=</span> <span class="n">ast</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
<span class="n">transformed_tree</span> <span class="o">=</span> <span class="n">SubtractTransformer</span><span class="p">()</span><span class="o">.</span><span class="n">visit</span><span class="p">(</span><span class="n">tree</span><span class="p">)</span>

<span class="c1"># Компилируем и выполняем новый код</span>
<span class="n">exec</span><span class="p">(</span><span class="nb">compile</span><span class="p">(</span><span class="n">transformed_tree</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="s2">&quot;&lt;ast&gt;&quot;</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s2">&quot;exec&quot;</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>  <span class="c1"># -4 (1 - 2 - 3)</span>
</pre></div></div></div>