<table>
<thead>
<tr>
<th>Класс/Функция</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Cache</code></td>
<td>Базовый класс для всех кэшей. Не используется напрямую, а служит основой для других типов кэшей.</td>
</tr>
<tr>
<td><code>FIFOCache(maxsize)</code></td>
<td>Кэш с алгоритмом замещения <strong>FIFO</strong> (First In, First Out).</td>
</tr>
<tr>
<td><code>LFUCache(maxsize)</code></td>
<td>Кэш с алгоритмом замещения <strong>LFU</strong> (Least Frequently Used).</td>
</tr>
<tr>
<td><code>LRUCache(maxsize)</code></td>
<td>Кэш с алгоритмом замещения <strong>LRU</strong> (Least Recently Used).</td>
</tr>
<tr>
<td><code>MRUCache(maxsize)</code></td>
<td>Кэш с алгоритмом замещения <strong>MRU</strong> (Most Recently Used).</td>
</tr>
<tr>
<td><code>RRCache(maxsize)</code></td>
<td>Кэш с случайным замещением (Random Replacement).</td>
</tr>
<tr>
<td><code>TLRUCache(maxsize, ttl)</code></td>
<td>Кэш с временным ограничением и алгоритмом замещения <strong>LRU</strong> (Time-aware Least Recently Used).</td>
</tr>
<tr>
<td><code>TTLCache(maxsize, ttl)</code></td>
<td>Кэш с временным ограничением (<strong>Time-to-Live</strong>) и алгоритмом замещения <strong>LRU</strong>.</td>
</tr>
<tr>
<td><code>cached(cache)</code></td>
<td>Декоратор для кэширования возвращаемого значения функции.</td>
</tr>
<tr>
<td><code>cachedmethod(cache)</code></td>
<td>Декоратор для кэширования возвращаемого значения метода класса.</td>
</tr>
</tbody>
</table>
<h1>Cache</h1>
<p>Базовый класс для всех кэшей.
Он не используется напрямую, но служит основой для других классов,
предоставляя основные методы для работы с кэшем.</p>
<h1>FIFOCache</h1>
<p>Использует алгоритм <strong>FIFO</strong> (First In, First Out).
Когда кэш заполняется, самый старый элемент удаляется, чтобы освободить место для нового.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">cachetools</span> <span class="kn">import</span> <span class="n">FIFOCache</span>

<span class="n">cache</span> <span class="o">=</span> <span class="n">FIFOCache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">3</span><span class="p">)</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;c&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span>

<span class="nb">print</span><span class="p">(</span><span class="n">cache</span><span class="p">)</span>  <span class="c1"># FIFOCache([(&quot;a&quot;, 1), (&quot;b&quot;, 2), (&quot;c&quot;, 3)])</span>

<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;d&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">4</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cache</span><span class="p">)</span>  <span class="c1"># FIFOCache([(&quot;b&quot;, 2), (&quot;c&quot;, 3), (&quot;d&quot;, 4)])</span>
</pre></div></div></div>

<h1>LFUCache</h1>
<p>Использует алгоритм <strong>LFU</strong> (Least Frequently Used).
Наименее часто используемые элементы удаляются первыми при необходимости освобождения места.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">cachetools</span> <span class="kn">import</span> <span class="n">LFUCache</span>

<span class="n">cache</span> <span class="o">=</span> <span class="n">LFUCache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span>

<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span>  <span class="c1"># Доступ к элементу увеличивает счетчик использования</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;c&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># Удаляет &quot;b&quot;, так как он использовался реже</span>

<span class="nb">print</span><span class="p">(</span><span class="n">cache</span><span class="p">)</span>  <span class="c1"># LFUCache([(&quot;a&quot;, 1), (&quot;c&quot;, 3)])</span>
</pre></div></div></div>

<h1>LRUCache</h1>
<p>Использует алгоритм <strong>LRU</strong> (Least Recently Used).
Наименее недавно используемые элементы удаляются первыми.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">cachetools</span> <span class="kn">import</span> <span class="n">LRUCache</span>

<span class="n">cache</span> <span class="o">=</span> <span class="n">LRUCache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span>

<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span>  <span class="c1"># Доступ к элементу делает его &quot;самым недавно использованным&quot;</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;c&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># Удаляет &quot;b&quot;, так как он был использован давнее всего</span>

<span class="nb">print</span><span class="p">(</span><span class="n">cache</span><span class="p">)</span>  <span class="c1"># LRUCache([(&quot;a&quot;, 1), (&quot;c&quot;, 3)])</span>
</pre></div></div></div>

<h1>MRUCache</h1>
<p>Использует алгоритм <strong>MRU</strong> (Most Recently Used).
Самый недавно использованный элемент удаляется первым при необходимости освобождения места.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">cachetools</span> <span class="kn">import</span> <span class="n">MRUCache</span>

<span class="n">cache</span> <span class="o">=</span> <span class="n">MRUCache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span>

<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span>  <span class="c1"># Доступ к элементу делает его &quot;самым недавно использованным&quot;</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;c&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># Удаляет &quot;a&quot;, так как он был использован последним</span>

<span class="nb">print</span><span class="p">(</span><span class="n">cache</span><span class="p">)</span>  <span class="c1"># MRUCache([(&quot;b&quot;, 2), (&quot;c&quot;, 3)])</span>
</pre></div></div></div>

<h1>RRCache</h1>
<p>Использует случайное замещение (Random Replacement).
Элементы удаляются случайным образом, когда кэш заполняется.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">cachetools</span> <span class="kn">import</span> <span class="n">RRCache</span>

<span class="n">cache</span> <span class="o">=</span> <span class="n">RRCache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;c&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span>

<span class="nb">print</span><span class="p">(</span><span class="n">cache</span><span class="p">)</span>  <span class="c1"># Один из элементов (&quot;a&quot; или &quot;b&quot;) будет удален случайным образом</span>
</pre></div></div></div>

<h1>TLRUCache</h1>
<p>Сочетает в себе временное ограничение (<code>ttl</code>) и алгоритм <strong>LRU</strong>.
Элементы удаляются либо при истечении времени жизни, либо по принципу <strong>LRU</strong>.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">cachetools</span> <span class="kn">import</span> <span class="n">TLRUCache</span>
<span class="kn">import</span> <span class="nn">time</span>

<span class="n">cache</span> <span class="o">=</span> <span class="n">TLRUCache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">ttl</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">6</span><span class="p">)</span>  <span class="c1"># Ждем 6 секунд</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span>

<span class="nb">print</span><span class="p">(</span><span class="n">cache</span><span class="p">)</span>  <span class="c1"># &quot;a&quot; будет удален, так как его TTL истек</span>
</pre></div></div></div>

<h1>TTLCache</h1>
<p>Кэш с временным ограничением (Time-to-Live) и алгоритмом <strong>LRU</strong>.
Элементы удаляются либо по истечению времени жизни (<code>ttl</code>), либо по принципу <strong>LRU</strong>, если кэш переполнен.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">cachetools</span> <span class="kn">import</span> <span class="n">TTLCache</span>
<span class="kn">import</span> <span class="nn">time</span>

<span class="n">cache</span> <span class="o">=</span> <span class="n">TTLCache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">ttl</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">6</span><span class="p">)</span>  <span class="c1"># Ждем 6 секунд</span>
<span class="n">cache</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span>

<span class="nb">print</span><span class="p">(</span><span class="n">cache</span><span class="p">)</span>  <span class="c1"># &quot;a&quot; будет удален, так как его TTL истек</span>
</pre></div></div></div>

<h1>cached</h1>
<p>Декоратор, который используется для кэширования возвращаемого значения функции.
Он может использовать любой из предоставленных кэшей.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">cachetools</span> <span class="kn">import</span> <span class="n">cached</span><span class="p">,</span> <span class="n">LRUCache</span>

<span class="n">cache</span> <span class="o">=</span> <span class="n">LRUCache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>

<span class="nd">@cached</span><span class="p">(</span><span class="n">cache</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">get_value</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">x</span> <span class="o">*</span> <span class="mi">2</span>

<span class="nb">print</span><span class="p">(</span><span class="n">get_value</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>  <span class="c1"># Вычисляет и кэширует результат</span>
<span class="nb">print</span><span class="p">(</span><span class="n">get_value</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>  <span class="c1"># Возвращает кэшированный результат</span>
</pre></div></div></div>

<h1>cachedmethod</h1>
<p>Декоратор для кэширования возвращаемого значения метода класса.
Декоратор позволяет задать кэш на уровне экземпляра класса.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">cachetools</span> <span class="kn">import</span> <span class="n">cachedmethod</span><span class="p">,</span> <span class="n">LRUCache</span>

<span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_cache</span> <span class="o">=</span> <span class="n">LRUCache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>

    <span class="nd">@cachedmethod</span><span class="p">(</span><span class="n">cache</span><span class="o">=</span><span class="k">lambda</span> <span class="bp">self</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cache</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">get_value</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">x</span> <span class="o">*</span> <span class="mi">2</span>

<span class="n">obj</span> <span class="o">=</span> <span class="n">MyClass</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="n">get_value</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>  <span class="c1"># Вычисляет и кэширует результат</span>
<span class="nb">print</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="n">get_value</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>  <span class="c1"># Возвращает кэшированный результат</span>
</pre></div></div></div>