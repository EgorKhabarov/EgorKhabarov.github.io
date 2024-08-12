<p>Библиотека "pyclbr" в Python используется для анализа и чтения исходного кода классов и функций в модуле.
Она позволяет получить информацию о структуре программы, такую как классы, методы, атрибуты и их связи.</p>
<p>Таблица методов модуля "pyclbr" и его подмодулей:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>readmodule()</code></td>
<td>Читает и анализирует модуль, возвращая словарь классов и функций.</td>
</tr>
<tr>
<td><code>readmodule_ex()</code></td>
<td>Похож на <code>readmodule()</code>, но также возвращает дополнительную информацию о модуле.</td>
</tr>
<tr>
<td><code>Class</code></td>
<td>Класс, представляющий отдельный класс из исходного кода.</td>
</tr>
<tr>
<td><code>Function</code></td>
<td>Класс, представляющий отдельную функцию из исходного кода.</td>
</tr>
<tr>
<td><code>Module</code></td>
<td>Класс, представляющий модуль и его структуру.</td>
</tr>
</tbody>
</table>
<p><code>readmodule()</code> Читает и анализирует модуль, возвращая словарь классов и функций.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pyclbr</span>

<span class="n">module_data</span> <span class="o">=</span> <span class="n">pyclbr</span><span class="o">.</span><span class="n">readmodule</span><span class="p">(</span><span class="s2">&quot;module_name&quot;</span><span class="p">)</span>

<span class="k">for</span> <span class="n">class_name</span><span class="p">,</span> <span class="n">class_data</span> <span class="ow">in</span> <span class="n">module_data</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Class: </span><span class="si">{</span><span class="n">class_name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">method_name</span><span class="p">,</span> <span class="n">method_data</span> <span class="ow">in</span> <span class="n">class_data</span><span class="o">.</span><span class="n">methods</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Method: </span><span class="si">{</span><span class="n">method_name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p><code>Class</code> Класс, представляющий отдельный класс из исходного кода.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pyclbr</span>

<span class="n">class_data</span> <span class="o">=</span> <span class="n">pyclbr</span><span class="o">.</span><span class="n">Class</span><span class="p">(</span><span class="s2">&quot;class_name&quot;</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Class: </span><span class="si">{</span><span class="n">class_data</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">method_name</span><span class="p">,</span> <span class="n">method_data</span> <span class="ow">in</span> <span class="n">class_data</span><span class="o">.</span><span class="n">methods</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Method: </span><span class="si">{</span><span class="n">method_name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p><code>Function</code> Класс, представляющий отдельную функцию из исходного кода.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pyclbr</span>

<span class="n">function_data</span> <span class="o">=</span> <span class="n">pyclbr</span><span class="o">.</span><span class="n">Function</span><span class="p">(</span><span class="s2">&quot;function_name&quot;</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Function: </span><span class="si">{</span><span class="n">function_data</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Start line: </span><span class="si">{</span><span class="n">function_data</span><span class="o">.</span><span class="n">lineno</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p><code>Module</code> Класс, представляющий модуль и его структуру.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pyclbr</span>

<span class="n">module_data</span> <span class="o">=</span> <span class="n">pyclbr</span><span class="o">.</span><span class="n">Module</span><span class="p">(</span><span class="s2">&quot;module_name&quot;</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Module: </span><span class="si">{</span><span class="n">module_data</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">class_name</span><span class="p">,</span> <span class="n">class_data</span> <span class="ow">in</span> <span class="n">module_data</span><span class="o">.</span><span class="n">classes</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Class: </span><span class="si">{</span><span class="n">class_name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div>
</div>