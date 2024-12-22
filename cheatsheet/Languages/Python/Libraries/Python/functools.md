<p><code>functools</code> - Утилиты для работы с функциями, упрощая их применение, создание и комбинирование</p>
<table>
<thead>
<tr>
<th>Функция/Атрибут</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>partial()</code></td>
<td>Создает новую функцию с частично фиксированными аргументами,<br>позволяя упростить вызов функции с заранее определенными аргументами</td>
<td><code>double = partial(multiply, y=2)</code></td>
</tr>
<tr>
<td><code>reduce()</code></td>
<td>Последовательно применяет функцию, принимающую два аргумента,<br>к элементам последовательности, сводя их к одному результату</td>
<td><code>result = reduce(lambda x, y: x + y, numbers)</code></td>
</tr>
<tr>
<td><code>lru_cache()</code></td>
<td>Декоратор для кэширования результатов функции,<br>что помогает избежать повторных вычислений при одинаковых входных данных</td>
<td><code>@lru_cache(maxsize=None)</code></td>
</tr>
<tr>
<td><code>wraps()</code></td>
<td>Декоратор, сохраняющий метаданные оригинальной функции<br>(например, <code>__name__</code>, <code>__doc__</code>) при использовании декораторов</td>
<td><code>@wraps(func)</code></td>
</tr>
<tr>
<td><code>total_ordering()</code></td>
<td>Класс-декоратор, который автоматически добавляет все методы сравнения<br>(<code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, <code>&gt;=</code>), если определены <code>__eq__</code><br>и один из (<code>__lt__</code>, <code>__le__</code>, <code>__gt__</code>, <code>__ge__</code>)</td>
<td><code>@total_ordering</code></td>
</tr>
<tr>
<td><code>cmp_to_key()</code></td>
<td>Преобразует функцию сравнения старого стиля в функцию,<br>возвращающую ключ для сортировки<br>(например, для использования в <code>sorted()</code> или <code>min()</code>)</td>
<td><code>sorted_data = sorted(data, key=cmp_to_key(compare))</code></td>
</tr>
<tr>
<td><code>cache()</code></td>
<td>Декоратор для кэширования результатов функции,<br>аналогичный <code>lru_cache</code>, но без ограничений на размер кэша</td>
<td><code>@cache</code></td>
</tr>
<tr>
<td><code>update_wrapper()</code></td>
<td>Обновляет метаданные функции-декоратора,<br>чтобы они соответствовали оригинальной функции</td>
<td><code>update_wrapper(wrapper, wrapped)</code></td>
</tr>
<tr>
<td><code>partialmethod()</code></td>
<td>Позволяет создавать методы с частично<br>фиксированными аргументами для использования в классах</td>
<td><code>partialmethod(func, arg1, arg2)</code></td>
</tr>
<tr>
<td><code>singledispatch()</code></td>
<td>Декоратор, который преобразует функцию<br>в обобщенную функцию с поддержкой однотипного диспетчеризации,<br>позволяя создавать перегрузки для разных типов аргументов</td>
<td><code>@singledispatch</code></td>
</tr>
<tr>
<td><code>singledispatchmethod()</code></td>
<td>Версия <code>singledispatch</code>, предназначенная<br>для использования в классах как метод, а не как функция</td>
<td><code>@singledispatchmethod</code></td>
</tr>
<tr>
<td><code>cached_property()</code></td>
<td>Декоратор, который превращает метод класса в свойство,<br>кэшируемое после первого вычисления</td>
<td><code>@cached_property</code></td>
</tr>
<tr>
<td><code>WRAPPER_ASSIGNMENTS</code></td>
<td>Список атрибутов, которые копируются<br>из оригинальной функции в функцию-декоратор</td>
<td>По умолчанию: <code>__module__</code> <code>__name__</code><br><code>__qualname__</code> <code>__doc__</code> <code>__annotations__</code></td>
</tr>
<tr>
<td><code>WRAPPER_UPDATES</code></td>
<td>Список атрибутов, которые обновляются<br>из оригинальной функции в функцию-декоратор</td>
<td>По умолчанию: <code>__dict__</code></td>
</tr>
</tbody>
</table>
<h1>partial</h1>
<p>Создает новую функцию с частично фиксированными аргументами
Удобно для переиспользования функций с предустановленными параметрами</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">partial</span>

<span class="k">def</span> <span class="nf">multiply</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">x</span> <span class="o">*</span> <span class="n">y</span>

<span class="c1"># &#x60;y&#x60; всегда равен 2</span>
<span class="nb">print</span><span class="p">(</span><span class="n">partial</span><span class="p">(</span><span class="n">multiply</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="mi">2</span><span class="p">)(</span><span class="mi">5</span><span class="p">))</span>  <span class="c1"># 10</span>
</pre></div></div></div>

<h1>reduce</h1>
<p>Последовательно применяет функцию, принимающую два аргумента,
к элементам последовательности, сводя их к одному результату</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">reduce</span>

<span class="n">numbers</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">reduce</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="n">x</span> <span class="o">+</span> <span class="n">y</span><span class="p">,</span> <span class="n">numbers</span><span class="p">))</span>  <span class="c1"># 15</span>
</pre></div></div></div>

<h1>lru_cache</h1>
<p>Кэширует результаты функции, улучшая производительность за счет предотвращения повторных вычислений
С ограничением на количество сохраненных значений
Это полезно для оптимизации рекурсивных функций</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">lru_cache</span>

<span class="nd">@lru_cache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">fibonacci</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">2</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">n</span>
    <span class="k">return</span> <span class="n">fibonacci</span><span class="p">(</span><span class="n">n</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span> <span class="o">+</span> <span class="n">fibonacci</span><span class="p">(</span><span class="n">n</span><span class="o">-</span><span class="mi">2</span><span class="p">)</span>

<span class="nd">@lru_cache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">128</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">factorial</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">n</span> <span class="o">*</span> <span class="n">factorial</span><span class="p">(</span><span class="n">n</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span> <span class="k">if</span> <span class="n">n</span> <span class="k">else</span> <span class="mi">1</span>

<span class="nb">print</span><span class="p">(</span><span class="n">fibonacci</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>  <span class="c1"># 55</span>
<span class="nb">print</span><span class="p">(</span><span class="n">factorial</span><span class="p">(</span><span class="mi">5</span><span class="p">))</span>  <span class="c1"># 120</span>
</pre></div></div></div>

<h1>wraps</h1>
<p>Используется для создания декораторов, которые сохраняют метаданные декорируемой функции</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">wraps</span>

<span class="k">def</span> <span class="nf">my_decorator</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
    <span class="nd">@wraps</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Вызов функции </span><span class="si">{</span><span class="n">func</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">wrapper</span>

<span class="nd">@my_decorator</span>
<span class="k">def</span> <span class="nf">greet</span><span class="p">(</span><span class="n">name</span><span class="p">):</span>
<span class="w">    </span><span class="sd">&quot;&quot;&quot;Приветствие пользователя&quot;&quot;&quot;</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;Hello, </span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2">!&quot;</span>

<span class="nb">print</span><span class="p">(</span><span class="n">greet</span><span class="p">(</span><span class="s2">&quot;Alice&quot;</span><span class="p">))</span>  <span class="c1"># &quot;Hello, Alice!&quot;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">greet</span><span class="o">.</span><span class="vm">__name__</span><span class="p">)</span>  <span class="c1"># &quot;greet&quot;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">greet</span><span class="o">.</span><span class="vm">__doc__</span><span class="p">)</span>   <span class="c1"># &quot;Приветствие пользователя&quot;</span>
</pre></div></div></div>

<h1>total_ordering</h1>
<p>Класс-декоратор, который добавляет методы сравнения (<code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, <code>&gt;=</code>) к классу,
если определены <code>__eq__</code> и один из (<code>__lt__</code>, <code>__le__</code>, <code>__gt__</code>, <code>__ge__</code>)</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">total_ordering</span>

<span class="nd">@total_ordering</span>
<span class="k">class</span> <span class="nc">Number</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span>

    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">value</span>

    <span class="k">def</span> <span class="fm">__lt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">&lt;</span> <span class="n">other</span><span class="o">.</span><span class="n">value</span>

<span class="n">n1</span> <span class="o">=</span> <span class="n">Number</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">n2</span> <span class="o">=</span> <span class="n">Number</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">n1</span> <span class="o">&lt;</span> <span class="n">n2</span><span class="p">)</span>  <span class="c1"># True</span>
<span class="nb">print</span><span class="p">(</span><span class="n">n1</span> <span class="o">&gt;</span> <span class="n">n2</span><span class="p">)</span>  <span class="c1"># False</span>
</pre></div></div></div>

<h1>cmp_to_key</h1>
<p>Преобразует функцию сравнения старого стиля в функцию, возвращающую ключ для сортировки</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">cmp_to_key</span>

<span class="k">def</span> <span class="nf">compare</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">x</span> <span class="o">-</span> <span class="n">y</span>

<span class="n">sorted_list</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">([</span><span class="mi">5</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">key</span><span class="o">=</span><span class="n">cmp_to_key</span><span class="p">(</span><span class="n">compare</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sorted_list</span><span class="p">)</span>  <span class="c1"># [1, 2, 3, 5, 6]</span>
</pre></div></div></div>

<h1>cache</h1>
<p>Декоратор, который кэширует результаты вызовов функции <code>func</code>
с одинаковыми аргументами, чтобы избежать повторных вычислений</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">cache</span>

<span class="nd">@cache</span>
<span class="k">def</span> <span class="nf">factorial</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">1</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">n</span> <span class="o">*</span> <span class="n">factorial</span><span class="p">(</span><span class="n">n</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span>

<span class="nd">@cache</span>
<span class="k">def</span> <span class="nf">fibonacci</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">2</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">n</span>
    <span class="k">return</span> <span class="n">fibonacci</span><span class="p">(</span><span class="n">n</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span> <span class="o">+</span> <span class="n">fibonacci</span><span class="p">(</span><span class="n">n</span><span class="o">-</span><span class="mi">2</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">factorial</span><span class="p">(</span><span class="mi">5</span><span class="p">))</span>  <span class="c1"># 120</span>
<span class="nb">print</span><span class="p">(</span><span class="n">fibonacci</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>  <span class="c1"># 55</span>
</pre></div></div></div>

<h1>update_wrapper</h1>
<p>Обновляет метаданные функции-декоратора, чтобы они соответствовали оригинальной функции</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">update_wrapper</span>

<span class="k">def</span> <span class="nf">my_decorator</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;До вызова функции&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">update_wrapper</span><span class="p">(</span><span class="n">wrapper</span><span class="p">,</span> <span class="n">func</span><span class="p">)</span>

<span class="nd">@my_decorator</span>
<span class="k">def</span> <span class="nf">my_function</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Выполнение функции&quot;</span><span class="p">)</span>

<span class="n">my_function</span><span class="p">()</span>  <span class="c1"># До вызова функции Выполнение функции</span>
</pre></div></div></div>

<h1>partialmethod</h1>
<p>Аналог <code>partial</code>, но используется для создания методов с частично фиксированными аргументами</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">partialmethod</span>

<span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">multiply</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">x</span> <span class="o">*</span> <span class="n">y</span>

    <span class="n">double</span> <span class="o">=</span> <span class="n">partialmethod</span><span class="p">(</span><span class="n">multiply</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>

<span class="n">obj</span> <span class="o">=</span> <span class="n">MyClass</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="n">double</span><span class="p">(</span><span class="mi">5</span><span class="p">))</span>  <span class="c1"># 10</span>
</pre></div></div></div>

<h1>singledispatch</h1>
<p>Позволяет создавать обобщенные функции с поддержкой
однотипного диспетчеризации (перегрузки) на основе типа первого аргумента</p>
<p><a target="_self" href="?Languages/Python/Decorators Closure/singledispatch.md" class="wikilink">singledispatch</a></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">singledispatch</span>

<span class="nd">@singledispatch</span>
<span class="k">def</span> <span class="nf">process</span><span class="p">(</span><span class="n">value</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Обработка объекта: </span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="nd">@process</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">_</span><span class="p">(</span><span class="n">value</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Обработка целого числа: </span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="nd">@process</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">_</span><span class="p">(</span><span class="n">value</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Обработка строки: </span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="n">process</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>   <span class="c1"># Обработка целого числа: 10</span>
<span class="n">process</span><span class="p">(</span><span class="s2">&quot;hi&quot;</span><span class="p">)</span> <span class="c1"># Обработка строки: hi</span>
</pre></div></div></div>

<h1>singledispatchmethod</h1>
<p>То же самое, что <code>singledispatch</code>, но используется как метод класса</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">singledispatchmethod</span>

<span class="k">class</span> <span class="nc">Processor</span><span class="p">:</span>
    <span class="nd">@singledispatchmethod</span>
    <span class="k">def</span> <span class="nf">process</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Обработка объекта: </span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

    <span class="nd">@process</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">_</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Обработка целого числа: </span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

    <span class="nd">@process</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">_</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Обработка строки: </span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="n">processor</span> <span class="o">=</span> <span class="n">Processor</span><span class="p">()</span>
<span class="n">processor</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>   <span class="c1"># Обработка целого числа: 10</span>
<span class="n">processor</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="s2">&quot;hi&quot;</span><span class="p">)</span> <span class="c1"># Обработка строки: hi</span>
</pre></div></div></div>

<h1>cached_property</h1>
<p>Позволяет кэшировать результат вычислений метода и использовать его как свойство.
Значение вычисляется только один раз</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">cached_property</span>

<span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="nd">@cached_property</span>
    <span class="k">def</span> <span class="nf">heavy_computation</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Выполняется вычисление...&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="mi">42</span>

<span class="n">obj</span> <span class="o">=</span> <span class="n">MyClass</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="n">heavy_computation</span><span class="p">)</span>  <span class="c1"># Выполняется вычисление ... 42</span>
<span class="nb">print</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="n">heavy_computation</span><span class="p">)</span>  <span class="c1"># 42 (вычисление не выполняется повторно)</span>
</pre></div></div></div>

<h1>WRAPPER_ASSIGNMENTS</h1>
<p>Это кортеж, определяющий, какие атрибуты копируются из оригинальной функции в декорированную
По умолчанию копируются атрибуты: <code>__module__</code>, <code>__name__</code>, <code>__qualname__</code>, <code>__doc__</code>, <code>__annotations__</code></p>
<h1>WRAPPER_UPDATES</h1>
<p>Это кортеж, определяющий, какие атрибуты обновляются в декорированной функции
По умолчанию обновляется <code>__dict__</code></p>
<h1>Частые применения</h1>
<ol>
<li>Оптимизация работы с функциями — использование <code>partial()</code> и <code>lru_cache()</code> для ускорения работы с часто вызываемыми функциями</li>
<li>Создание декораторов — с сохранением метаданных функции с помощью <code>wraps()</code></li>
<li>Упрощение сравнения — автоматическое добавление методов сравнения с <code>total_ordering()</code></li>
</ol>
<h1>Полезные ссылки</h1>
<ul>
<li><a href="https://docs.python.org/3/library/functools.html">Официальная документация</a></li>
<li><a href="https://realpython.com/python-functools/">Real Python - Guide to Python’s functools Module</a></li>
</ul>