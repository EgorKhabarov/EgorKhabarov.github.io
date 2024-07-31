<p>Модуль queue предоставляет различные классы для реализации очередей в Python.
Очереди используются для хранения и управления элементами данных в порядке "первым поступил - первым обслужен".</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>Queue(maxsize)</td>
<td>Создает новую очередь с максимальным размером maxsize.</td>
</tr>
<tr>
<td>q.put(item)</td>
<td>Добавляет элемент item в очередь q.</td>
</tr>
<tr>
<td>q.get()</td>
<td>Удаляет и возвращает элемент из очереди q.</td>
</tr>
<tr>
<td>q.empty()</td>
<td>Возвращает True, если очередь q пуста, иначе False.</td>
</tr>
<tr>
<td>q.full()</td>
<td>Возвращает True, если очередь q полна, иначе False.</td>
</tr>
<tr>
<td>q.qsize()</td>
<td>Возвращает количество элементов в очереди q.</td>
</tr>
</tbody>
</table>
<p><strong>put(item)</strong> Добавляет элемент в очередь.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code55f2f1c8f8f59bc2319441035997425cb"onclick="copyCode(code55f2f1c8f8f59bc2319441035997425c, code55f2f1c8f8f59bc2319441035997425cb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code55f2f1c8f8f59bc2319441035997425c"><div class="highlight"><pre><span></span><span class="n">q</span> <span class="o">=</span> <span class="n">Queue</span><span class="p">()</span>
<span class="n">q</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">q</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">q</span><span class="o">.</span><span class="n">qsize</span><span class="p">())</span>  <span class="c1"># Вывод: 2</span>
</pre></div></div></div>

<p><strong>get()</strong> Удаляет и возвращает первый элемент из очереди.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code01b0321ffee93443f9639ed43363a230b"onclick="copyCode(code01b0321ffee93443f9639ed43363a230, code01b0321ffee93443f9639ed43363a230b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code01b0321ffee93443f9639ed43363a230"><div class="highlight"><pre><span></span><span class="n">q</span> <span class="o">=</span> <span class="n">Queue</span><span class="p">()</span>
<span class="n">q</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">q</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">q</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>  <span class="c1"># Вывод: 1</span>
</pre></div></div></div>

<p><strong>empty()</strong> Проверяет, пуста ли очередь.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codea28cd972ce8a6fd70ed0ae2a460fc242b"onclick="copyCode(codea28cd972ce8a6fd70ed0ae2a460fc242, codea28cd972ce8a6fd70ed0ae2a460fc242b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codea28cd972ce8a6fd70ed0ae2a460fc242"><div class="highlight"><pre><span></span><span class="n">q</span> <span class="o">=</span> <span class="n">Queue</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">q</span><span class="o">.</span><span class="n">empty</span><span class="p">())</span>  <span class="c1"># Вывод: True</span>
</pre></div></div></div>