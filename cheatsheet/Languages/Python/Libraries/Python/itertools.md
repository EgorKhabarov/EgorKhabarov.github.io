<h1>Основные функции и атрибуты</h1>
<table>
<thead>
<tr>
<th>Функция/Атрибут</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>accumulate()</code></td>
<td>Возвращает итератор, который вычисляет частичные суммы<br>(или другие накопленные функции, если указана) от переданного итератора</td>
</tr>
<tr>
<td><code>chain()</code></td>
<td>Принимает несколько итераторов и возвращает один итератор,<br>объединяющий все их элементы последовательно</td>
</tr>
<tr>
<td><code>combinations()</code></td>
<td>Возвращает все возможные комбинации заданной длины из элементов итератора (без повторений)</td>
</tr>
<tr>
<td><code>combinations_with_replacement()</code></td>
<td>Возвращает все возможные комбинации с повторениями заданной длины из элементов итератора</td>
</tr>
<tr>
<td><code>compress()</code></td>
<td>Возвращает элементы из первого итератора,<br>где соответствующий элемент из второго итератора (маски) истинный</td>
</tr>
<tr>
<td><code>count()</code></td>
<td>Возвращает итератор, который генерирует последовательность чисел,<br>начиная с <code>start</code> (по умолчанию 0) с шагом <code>step</code> (по умолчанию 1)</td>
</tr>
<tr>
<td><code>cycle()</code></td>
<td>Бесконечно повторяет элементы переданного итератора</td>
</tr>
<tr>
<td><code>dropwhile()</code></td>
<td>Возвращает элементы из итератора, начиная с первого элемента,<br>для которого условие становится ложным</td>
</tr>
<tr>
<td><code>filterfalse()</code></td>
<td>Возвращает элементы итератора, для которых условие ложно (противоположно <code>filter</code>)</td>
</tr>
<tr>
<td><code>groupby()</code></td>
<td>Группирует элементы последовательности по ключу (или значению функции).<br>Возвращает итератор с парами <code>(ключ, группа)</code></td>
</tr>
<tr>
<td><code>islice()</code></td>
<td>Возвращает срез итератора (аналогично <code>slice()</code> для списков)</td>
</tr>
<tr>
<td><code>pairwise()</code></td>
<td>Выдаёт пары соседних элементов из <code>iterable</code></td>
</tr>
<tr>
<td><code>permutations()</code></td>
<td>Возвращает все возможные перестановки заданной длины (или длины итератора)</td>
</tr>
<tr>
<td><code>product()</code></td>
<td>Возвращает декартово произведение входных итераторов (все возможные комбинации)</td>
</tr>
<tr>
<td><code>repeat()</code></td>
<td>Повторяет переданный элемент <code>object</code> бесконечно или заданное количество раз <code>times</code></td>
</tr>
<tr>
<td><code>starmap()</code></td>
<td>Применяет функцию к каждому элементу итератора, передавая элементы<br>как аргументы по позициям (аналогично <code>map()</code>, но с распаковкой аргументов)</td>
</tr>
<tr>
<td><code>takewhile()</code></td>
<td>Возвращает элементы из итератора до тех пор, пока условие истинно</td>
</tr>
<tr>
<td><code>tee()</code></td>
<td>Разделяет итератор на заданное количество независимых копий</td>
</tr>
<tr>
<td><code>zip_longest()</code></td>
<td>Объединяет элементы из нескольких итераторов, заполняя отсутствующие значения <code>fillvalue</code></td>
</tr>
</tbody>
</table>
<h1>accumulate</h1>
<p>Возвращает итератор, который вычисляет частичные суммы (или другие накопленные функции).</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">accumulate</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">accumulate</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">])))</span>
<span class="c1"># [1, 3, 6, 10]</span>
</pre></div></div></div>

<h1>chain</h1>
<p>Объединяет несколько итераторов в один.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">chain</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">chain</span><span class="p">(</span><span class="s2">&quot;ABC&quot;</span><span class="p">,</span> <span class="s2">&quot;DEF&quot;</span><span class="p">)))</span>
<span class="c1"># [&quot;A&quot;, &quot;B&quot;, &quot;C&quot;, &quot;D&quot;, &quot;E&quot;, &quot;F&quot;]</span>
</pre></div></div></div>

<h1>combinations</h1>
<p>Возвращает все возможные комбинации заданной длины без повторений.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">combinations</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">combinations</span><span class="p">(</span><span class="s2">&quot;ABC&quot;</span><span class="p">,</span> <span class="mi">2</span><span class="p">)))</span>
<span class="c1"># [(&quot;A&quot;, &quot;B&quot;), (&quot;A&quot;, &quot;C&quot;), (&quot;B&quot;, &quot;C&quot;)]</span>
</pre></div></div></div>

<h1>combinations_with_replacement</h1>
<p>Возвращает все возможные комбинации заданной длины с повторениями.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">combinations_with_replacement</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">combinations_with_replacement</span><span class="p">(</span><span class="s2">&quot;AB&quot;</span><span class="p">,</span> <span class="mi">2</span><span class="p">)))</span>
<span class="c1"># [(&quot;A&quot;, &quot;A&quot;), (&quot;A&quot;, &quot;B&quot;), (&quot;B&quot;, &quot;B&quot;)]</span>
</pre></div></div></div>

<h1>compress</h1>
<p>Возвращает элементы из первого итератора, где соответствующий элемент из второго итератора истинный.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">compress</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">compress</span><span class="p">(</span><span class="s2">&quot;ABCDEF&quot;</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">])))</span>
<span class="c1"># [&quot;A&quot;, &quot;C&quot;, &quot;E&quot;]</span>
</pre></div></div></div>

<h1>count</h1>
<p>Создает бесконечный итератор, который начинает с заданного числа и увеличивается на заданный шаг.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">count</span>

<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">count</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">2</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">i</span> <span class="o">&gt;</span> <span class="mi">20</span><span class="p">:</span>
        <span class="k">break</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
<span class="c1"># 10, 12, 14, 16, 18, 20</span>
</pre></div></div></div>

<h1>cycle</h1>
<p>Бесконечно повторяет элементы из итератора.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">cycle</span>

<span class="n">counter</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">cycle</span><span class="p">(</span><span class="s2">&quot;AB&quot;</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">counter</span> <span class="o">&gt;=</span> <span class="mi">6</span><span class="p">:</span>
        <span class="k">break</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>  <span class="c1"># A, B, A, B, A, B</span>
    <span class="n">counter</span> <span class="o">+=</span> <span class="mi">1</span>
</pre></div></div></div>

<h1>dropwhile</h1>
<p>Пропускает элементы, пока условие истинно, затем возвращает оставшиеся элементы.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">dropwhile</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">dropwhile</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span> <span class="o">&lt;</span> <span class="mi">5</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">])))</span>
<span class="c1"># [6, 7]</span>
</pre></div></div></div>

<h1>filterfalse</h1>
<p>Возвращает элементы итератора, для которых условие ложно.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">filterfalse</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">filterfalse</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span> <span class="o">%</span> <span class="mi">2</span><span class="p">,</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">))))</span>
<span class="c1"># [0, 2, 4, 6, 8]</span>
</pre></div></div></div>

<h1>groupby</h1>
<p>Группирует элементы по ключу. Возвращает итератор с парами <code>(ключ, группа)</code>.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">groupby</span>

<span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">group</span> <span class="ow">in</span> <span class="n">groupby</span><span class="p">(</span><span class="s2">&quot;AAAABBBCCDA&quot;</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="nb">list</span><span class="p">(</span><span class="n">group</span><span class="p">))</span>
<span class="c1"># A [&quot;A&quot;, &quot;A&quot;, &quot;A&quot;, &quot;A&quot;]</span>
<span class="c1"># B [&quot;B&quot;, &quot;B&quot;, &quot;B&quot;]</span>
<span class="c1"># C [&quot;C&quot;, &quot;C&quot;]</span>
<span class="c1"># D [&quot;D&quot;]</span>
<span class="c1"># A [&quot;A&quot;]</span>
</pre></div></div></div>

<h1>islice</h1>
<p>Возвращает срез итератора.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">islice</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">islice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">),</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">2</span><span class="p">)))</span>  <span class="c1"># [2, 4, 6]</span>
</pre></div></div></div>

<h1>pairwise</h1>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">pairwise</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">pairwise</span><span class="p">(</span><span class="s2">&quot;ABcd12&quot;</span><span class="p">)))</span>
<span class="c1"># [(&quot;A&quot;, &quot;B&quot;), (&quot;B&quot;, &quot;c&quot;), (&quot;c&quot;, &quot;d&quot;), (&quot;d&quot;, &quot;1&quot;), (&quot;1&quot;, &quot;2&quot;)]</span>
</pre></div></div></div>

<h1>permutations</h1>
<p>Возвращает все возможные перестановки заданной длины.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">permutations</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">permutations</span><span class="p">(</span><span class="s2">&quot;ABC&quot;</span><span class="p">,</span> <span class="mi">2</span><span class="p">)))</span>
<span class="c1"># [(&quot;A&quot;, &quot;B&quot;), (&quot;A&quot;, &quot;C&quot;), (&quot;B&quot;, &quot;A&quot;), (&quot;B&quot;, &quot;C&quot;), (&quot;C&quot;, &quot;A&quot;), (&quot;C&quot;, &quot;B&quot;)]</span>
</pre></div></div></div>

<h1>product</h1>
<p>Возвращает декартово произведение входных итераторов.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">product</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">product</span><span class="p">(</span><span class="s2">&quot;AB&quot;</span><span class="p">,</span> <span class="s2">&quot;12&quot;</span><span class="p">)))</span>
<span class="c1"># [(&quot;A&quot;, &quot;1&quot;), (&quot;A&quot;, &quot;2&quot;), (&quot;B&quot;, &quot;1&quot;), (&quot;B&quot;, &quot;2&quot;)]</span>
</pre></div></div></div>

<h1>repeat</h1>
<p>Повторяет указанный элемент бесконечно или заданное количество раз.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">repeat</span>

<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">repeat</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">3</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
<span class="c1"># 10, 10, 10</span>
</pre></div></div></div>

<h1>starmap</h1>
<p>Применяет функцию к каждому элементу итератора, распаковывая элементы как аргументы.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">starmap</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">starmap</span><span class="p">(</span><span class="nb">pow</span><span class="p">,</span> <span class="p">[(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">5</span><span class="p">),</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">3</span><span class="p">)])))</span>  <span class="c1"># [32, 9, 1000]</span>
</pre></div></div></div>

<h1>takewhile</h1>
<p>Возвращает элементы из итератора до тех пор, пока условие истинно.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">takewhile</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">takewhile</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span> <span class="o">&lt;</span> <span class="mi">5</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">])))</span>  <span class="c1"># [1, 4]</span>
</pre></div></div></div>

<h1>tee</h1>
<p>Создает несколько независимых копий одного итератора.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">tee</span>

<span class="n">it1</span><span class="p">,</span> <span class="n">it2</span> <span class="o">=</span> <span class="n">tee</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">),</span> <span class="mi">2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">it1</span><span class="p">))</span>  <span class="c1"># [0, 1, 2, 3, 4]</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">it2</span><span class="p">))</span>  <span class="c1"># [0, 1, 2, 3, 4]</span>
</pre></div></div></div>

<h1>zip_longest</h1>
<p>Объединяет элементы из нескольких итераторов, заполняя отсутствующие значения <code>fillvalue</code>.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">zip_longest</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">zip_longest</span><span class="p">(</span><span class="s2">&quot;AB&quot;</span><span class="p">,</span> <span class="s2">&quot;12&quot;</span><span class="p">,</span> <span class="n">fillvalue</span><span class="o">=</span><span class="s2">&quot;-&quot;</span><span class="p">)))</span>
<span class="c1"># [(&quot;A&quot;, &quot;1&quot;), (&quot;B&quot;, &quot;2&quot;)]</span>
</pre></div></div></div>