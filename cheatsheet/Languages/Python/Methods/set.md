<table>
<thead>
<tr>
<th style="text-align: left;">Метод</th>
<th style="text-align: left;">Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">set<code>.add</code>(element)</td>
<td style="text-align: left;">Добавляет элемент <code>element</code> во множество. Если элемент уже присутствует, ничего не происходит.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.issubset</code>(set2)</td>
<td style="text-align: left;">Проверяет, является ли <code>set</code> подмножеством <code>set2</code>. Возвращает <code>True</code>, если так, иначе <code>False</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.isdisjoint</code>(set2)</td>
<td style="text-align: left;">Проверяет, есть ли общие элементы между <code>set</code> и <code>set2</code>. Возвращает <code>True</code>, если нет, иначе <code>False</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.issuperset</code>(set2)</td>
<td style="text-align: left;">Проверяет, является ли <code>set</code> надмножеством <code>set2</code>. Возвращает <code>True</code>, если так, иначе <code>False</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.copy()</code></td>
<td style="text-align: left;">Возвращает копию множества.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.union</code>(set2) <code>|</code></td>
<td style="text-align: left;">Возвращает новое множество, содержащее все элементы из <code>set</code> и <code>set2</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.difference</code>(set2) <code>-</code></td>
<td style="text-align: left;">Возвращает новое множество, содержащее элементы из <code>set</code>, которые отсутствуют в <code>set2</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.intersection</code>(set2) <code>&amp;</code></td>
<td style="text-align: left;">Возвращает новое множество, содержащее только элементы, присутствующие одновременно в <code>set</code> и <code>set2</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.symmetric_difference</code>(set2) <code>^</code></td>
<td style="text-align: left;">Возвращает новое множество, содержащее элементы, присутствующие только в одном из <code>set</code> и <code>set2</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.update</code>(set2) <code>|=</code></td>
<td style="text-align: left;">Обновляет множество, добавляя элементы из <code>set2</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.difference_update</code>(set2) <code>-=</code></td>
<td style="text-align: left;">Обновляет множество, удаляя элементы из <code>set</code>, которые присутствуют в <code>set2</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.intersection_update</code>(set2) <code>&amp;=</code></td>
<td style="text-align: left;">Обновляет множество, оставляя только элементы, присутствующие одновременно в <code>set</code> и <code>set2</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.symmetric_difference_update</code>(set2) <code>^=</code></td>
<td style="text-align: left;">Обновляет множество, оставляя только элементы, присутствующие только в одном из <code>set</code> и <code>set2</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.pop()</code></td>
<td style="text-align: left;">Удаляет и возвращает произвольный элемент из множества. Если множество пустое, возникает исключение <code>KeyError</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.clear()</code></td>
<td style="text-align: left;">Удаляет все элементы из множества, делая его пустым.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.remove</code>(element)</td>
<td style="text-align: left;">Удаляет элемент <code>element</code> из множества. Если элемент не найден, возникает исключение <code>KeyError</code>.</td>
</tr>
<tr>
<td style="text-align: left;">set<code>.discard</code>(element)</td>
<td style="text-align: left;">Удаляет элемент <code>element</code> из множества. Если элемент не найден, ничего не происходит.</td>
</tr>
</tbody>
</table>
<h1 id="frozenset">frozenset</h1>
<p>В Python «замороженный» означает, что объект не может быть изменен. Например, рассмотрим <code>set</code> и <code>frozenset</code>:</p>
<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">s</span> <span class="o">=</span> <span class="nb">set</span><span class="p">((</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">))</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">s</span>
<span class="unselectable"><span class="go">{1, 2, 3}</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">s</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">s</span>
<span class="unselectable"><span class="go">{1, 2, 3, 4}</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">fs</span> <span class="o">=</span> <span class="nb">frozenset</span><span class="p">((</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">))</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">fs</span>
<span class="unselectable"><span class="go">frozenset({1, 2, 3})</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">fs</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>
<span class="unselectable"><span class="gt">Traceback (most recent call last):</span></span>
<span class="unselectable">  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span></span>
<span class="unselectable"><span class="gr">AttributeError</span>: <span class="n">&#39;frozenset&#39; object has no attribute &#39;add&#39;</span></span>
</pre></div></div>
</div>