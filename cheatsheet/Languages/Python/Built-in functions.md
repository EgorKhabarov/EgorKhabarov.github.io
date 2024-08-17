<ul>
<li>slice</li>
<li>frozenset</li>
<li>memoryview</li>
<li>hasattr</li>
<li>reversed</li>
<li>&#95;&#95;import&#95;&#95;</li>
<li>staticmethod</li>
<li>setattr</li>
<li>property</li>
<li>object, </li>
<li>locals</li>
<li>globals</li>
<li>getattr</li>
<li>complex</li>
<li>compile</li>
<li>bytearray</li>
<li>abs</li>
<li>bin</li>
<li>bytes</li>
<li>callable</li>
<li>chr</li>
<li>classmethod</li>
<li>delattr</li>
<li>dir</li>
<li>divmod</li>
<li>filter</li>
<li>oct</li>
<li>nonlocal</li>
</ul>
<h2>slice</h2>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">][</span><span class="mi">1</span><span class="p">:</span><span class="mi">4</span><span class="p">])</span>  <span class="c1"># [2, 3, 4]</span>
<span class="nb">print</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">][</span><span class="nb">slice</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">)])</span>  <span class="c1"># [2, 3, 4]</span>
</pre></div></div></div>

<h2>frozenset</h2>
<p>Неизменяемый тип данных, представляющий собой неупорядоченное множество уникальных элементов.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">frozenset</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">]))</span>  <span class="c1"># frozenset({1, 2, 3, 4})</span>
</pre></div></div></div>

<h2>memoryview</h2>
<p>Доступ к буферу памяти объекта без копирования его данных.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="n">my_bytes</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">memoryview</span><span class="p">(</span><span class="n">my_bytes</span><span class="p">)[</span><span class="mi">1</span><span class="p">])</span>  <span class="c1"># 2</span>
</pre></div></div></div>

<h2>hasattr</h2>
<p>Для проверки наличия атрибута (метода или свойства) у объекта.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">my_attr</span> <span class="o">=</span> <span class="mi">42</span>

<span class="n">my_obj</span> <span class="o">=</span> <span class="n">MyClass</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">hasattr</span><span class="p">(</span><span class="n">my_obj</span><span class="p">,</span> <span class="s2">&quot;my_attr&quot;</span><span class="p">))</span>  <span class="c1"># True</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">hasattr</span><span class="p">(</span><span class="n">my_obj</span><span class="p">,</span> <span class="s2">&quot;non_existent_attr&quot;</span><span class="p">))</span>  <span class="c1"># False</span>
</pre></div></div></div>

<h2>reversed</h2>
<p>Для переворачивания последовательности (sequence).</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="n">my_list</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="n">reversed_list</span> <span class="o">=</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">my_list</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">reversed_list</span><span class="p">))</span>  <span class="c1"># [5, 4, 3, 2, 1]</span>
</pre></div></div></div>

<h2><strong>import</strong></h2>
<p>Для импорта модуля во время выполнения программы.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="n">math</span> <span class="o">=</span> <span class="nb">__import__</span><span class="p">(</span><span class="s2">&quot;math&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">pi</span><span class="p">)</span>  <span class="c1"># 3.141592653589793</span>
</pre></div></div></div>

<h2>staticmethod</h2>
<p>Для создания метода класса, который не принимает первый аргумент self (или cls для методов класса).</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">my_static_method</span><span class="p">():</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;This is a static method&quot;</span><span class="p">)</span>

<span class="n">MyClass</span><span class="o">.</span><span class="n">my_static_method</span><span class="p">()</span>  <span class="c1"># This is a static method</span>
</pre></div></div></div>

<h2>setattr</h2>
<p>Для установки значения атрибута объекта.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">my_attr</span> <span class="o">=</span> <span class="mi">42</span>

<span class="n">my_obj</span> <span class="o">=</span> <span class="n">MyClass</span><span class="p">()</span>
<span class="nb">setattr</span><span class="p">(</span><span class="n">my_obj</span><span class="p">,</span> <span class="s2">&quot;my_attr&quot;</span><span class="p">,</span> <span class="mi">43</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">my_obj</span><span class="o">.</span><span class="n">my_attr</span><span class="p">)</span>  <span class="c1"># 43</span>
</pre></div></div></div>

<h2>property</h2>
<p>Для создания свойства объекта, которое можно читать и записывать, как обычный атрибут.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_my_attr</span> <span class="o">=</span> <span class="mi">42</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">my_attr</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_my_attr</span>

    <span class="nd">@my_attr</span><span class="o">.</span><span class="n">setter</span>
    <span class="k">def</span> <span class="nf">my_attr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_my_attr</span>
</pre></div></div></div>

<h2>object</h2>
<p>Базовый класс, от которого наследуются все остальные классы в Python.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">pass</span>
</pre></div></div></div>

<h2>locals</h2>
<p>Для получения словаря с локальными переменными в текущем контексте выполнения.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">my_func</span><span class="p">():</span>
    <span class="n">a</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">b</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="nb">print</span><span class="p">(</span><span class="nb">locals</span><span class="p">())</span>

<span class="n">my_func</span><span class="p">()</span>  <span class="c1"># {&quot;a&quot;: 1, &quot;b&quot;: 2}</span>
</pre></div></div></div>

<h2>globals</h2>
<p>Для получения словаря с глобальными переменными в текущем модуле.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="n">my_var</span> <span class="o">=</span> <span class="mi">42</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">globals</span><span class="p">())</span>  <span class="c1"># {&quot;__name__&quot;: &quot;__main__&quot;, &quot;__doc__&quot;: None, &quot;__package__&quot;: None, &quot;my_var&quot;: 42, ...}</span>
</pre></div></div></div>

<h2>getattr</h2>
<p>Для получения значения атрибута объекта по его имени.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">my_attr</span> <span class="o">=</span> <span class="mi">42</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">MyClass</span><span class="p">(),</span> <span class="s2">&quot;my_attr&quot;</span><span class="p">))</span>  <span class="c1"># 42</span>
</pre></div></div></div>

<h2>complex</h2>
<p>Для создания комплексного числа.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">complex</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>  <span class="c1"># (1+2j)</span>
</pre></div></div></div>

<h2>compile</h2>
<p>Для компиляции строки с кодом Python в объект-код.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="n">exec</span><span class="p">(</span><span class="nb">compile</span><span class="p">(</span><span class="s1">&#39;print(&quot;Hello, world!&quot;)&#39;</span><span class="p">,</span> <span class="s2">&quot;&lt;string&gt;&quot;</span><span class="p">,</span> <span class="s2">&quot;exec&quot;</span><span class="p">))</span>  <span class="c1"># Hello, world!</span>
</pre></div></div></div>

<h2>bytearray</h2>
<p>Изменяемый тип данных, представляющий собой массив байтов.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">bytearray</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]))</span>  <span class="c1"># bytearray(b&quot;\x01\x02\x03\x04\x05&quot;)</span>
</pre></div></div></div>

<h2>abs</h2>
<p>Получения абсолютного значения числа.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="o">-</span><span class="mi">42</span><span class="p">))</span>  <span class="c1"># 42</span>
</pre></div></div></div>

<h2>bin</h2>
<p>Получения двоичного представления числа.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">bin</span><span class="p">(</span><span class="mi">42</span><span class="p">))</span>  <span class="c1"># 0b101010</span>
</pre></div></div></div>

<h2>bytes</h2>
<p>Неизменяемый тип данных, представляющий собой массив байтов.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">bytes</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]))</span>  <span class="c1"># b&quot;\x01\x02\x03\x04\x05&quot;</span>
</pre></div></div></div>

<h2>callable</h2>
<p>Является ли объект вызываемым (т.е. функцией или методом).</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">my_func</span><span class="p">():</span>
    <span class="k">pass</span>

<span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">my_method</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">callable</span><span class="p">(</span><span class="n">my_func</span><span class="p">))</span>  <span class="c1"># True</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">callable</span><span class="p">(</span><span class="n">MyClass</span><span class="p">()</span><span class="o">.</span><span class="n">my_method</span><span class="p">))</span>  <span class="c1"># True</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">callable</span><span class="p">(</span><span class="mi">42</span><span class="p">))</span>  <span class="c1"># False</span>
</pre></div></div></div>

<h2>chr</h2>
<p>Получение символа Unicode по его коду.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">chr</span><span class="p">(</span><span class="mi">97</span><span class="p">))</span>  <span class="c1"># &quot;a&quot;</span>
</pre></div></div></div>

<h2>classmethod</h2>
<p>Создание метода класса. Этот метод может быть вызван без создания экземпляра класса.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="n">my_class_attr</span> <span class="o">=</span> <span class="mi">42</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">my_class_method</span><span class="p">(</span><span class="bp">cls</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="bp">cls</span><span class="o">.</span><span class="n">my_class_attr</span><span class="p">)</span>

<span class="n">MyClass</span><span class="o">.</span><span class="n">my_class_method</span><span class="p">()</span>  <span class="c1"># 42</span>
</pre></div></div></div>

<h2>delattr</h2>
<p>Удаление атрибута объекта.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="n">my_attr</span> <span class="o">=</span> <span class="mi">42</span>

<span class="n">my_obj</span> <span class="o">=</span> <span class="n">MyClass</span><span class="p">()</span>
<span class="nb">delattr</span><span class="p">(</span><span class="n">my_obj</span><span class="p">,</span> <span class="s2">&quot;my_attr&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">hasattr</span><span class="p">(</span><span class="n">my_obj</span><span class="p">,</span> <span class="s2">&quot;my_attr&quot;</span><span class="p">))</span>  <span class="c1"># False</span>
</pre></div></div></div>

<h2>dir</h2>
<p>Получение списка всех атрибутов объекта.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">dir</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]))</span>  <span class="c1"># [&quot;__add__&quot;, &quot;__class__&quot;, &quot;__contains__&quot;, ...]</span>
</pre></div></div></div>

<h2>divmod</h2>
<p>Получения частного и остатка от деления двух чисел.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">divmod</span><span class="p">(</span><span class="mi">42</span><span class="p">,</span> <span class="mi">5</span><span class="p">))</span>  <span class="c1"># (8, 2)</span>
</pre></div></div></div>

<h2>filter</h2>
<p>Фильтрация элементов последовательности с помощью функции.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="nb">filter</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="mi">0</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">])))</span>  <span class="c1"># [2, 4]</span>
</pre></div></div></div>

<h2>oct</h2>
<p>Получение восьмеричного представления числа.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">oct</span><span class="p">(</span><span class="mi">42</span><span class="p">))</span>  <span class="c1"># 0o52</span>
</pre></div></div></div>

<h2>nonlocal</h2>
<p>Объявление переменной из внешней области видимости внутри функции.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">my_func</span><span class="p">():</span>
    <span class="n">my_var</span> <span class="o">=</span> <span class="mi">42</span>
    <span class="k">def</span> <span class="nf">inner_func</span><span class="p">():</span>
        <span class="k">nonlocal</span> <span class="n">my_var</span>
        <span class="n">my_var</span> <span class="o">=</span> <span class="mi">43</span>
    <span class="n">inner_func</span><span class="p">()</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">my_var</span><span class="p">)</span>

<span class="n">my_func</span><span class="p">()</span>  <span class="c1"># 43</span>
</pre></div></div></div>