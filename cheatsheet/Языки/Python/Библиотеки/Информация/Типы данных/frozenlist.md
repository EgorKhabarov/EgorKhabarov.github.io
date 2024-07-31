<p>Описание: библиотека "frozenlist" служит для создания неизменяемых списков в Python,
аналогично тому, как <code>tuple</code> предоставляет неизменяемую версию <code>list</code>.</p>
<p>Таблица методов:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>__init__()</code></td>
<td>Инициализирует новый объект frozenlist.</td>
</tr>
<tr>
<td><code>__contains__()</code></td>
<td>Проверяет наличие элемента в списке.</td>
</tr>
<tr>
<td><code>__getitem__()</code></td>
<td>Получает элемент списка по индексу.</td>
</tr>
<tr>
<td><code>__len__()</code></td>
<td>Возвращает количество элементов в списке.</td>
</tr>
<tr>
<td><code>copy()</code></td>
<td>Возвращает копию frozenlist.</td>
</tr>
</tbody>
</table>
<p>Список самых частых методов, краткое описание и работающие примеры:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code36180a360d69f15570065f52bb9ba890b"onclick="copyCode(code36180a360d69f15570065f52bb9ba890, code36180a360d69f15570065f52bb9ba890b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code36180a360d69f15570065f52bb9ba890"><div class="highlight"><pre><span></span><span class="c1"># Метод __init__()</span>
<span class="n">flist</span> <span class="o">=</span> <span class="n">frozenlist</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">])</span>
<span class="c1"># Метод __contains__()</span>
<span class="nb">print</span><span class="p">(</span><span class="mi">3</span> <span class="ow">in</span> <span class="n">flist</span><span class="p">)</span>  <span class="c1"># Выведет True, так как 3 есть в списке</span>
<span class="c1"># Метод __getitem__()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">flist</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>  <span class="c1"># Выведет 2, так как это элемент на позиции 1</span>
<span class="c1"># Метод __len__()</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">flist</span><span class="p">))</span>  <span class="c1"># Выведет 5, так количество элементов в списке равно 5</span>
<span class="c1"># Метод copy()</span>
<span class="n">flist_copy</span> <span class="o">=</span> <span class="n">flist</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>  <span class="c1"># Создаст копию списка</span>
</pre></div></div></div>

<p>Пожалуйста, убедитесь, что установлена библиотека <code>frozenlist</code>.
Если нет, используйте данную команду для установки - <code>pip install frozenlist</code>.</p>