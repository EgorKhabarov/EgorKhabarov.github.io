<p>Библиотека <code>operator</code> в Python предоставляет функции, которые соответствуют основным операциям,
таким как арифметические, логические, сравнения и работа с атрибутами, элементами и срезами.
Эти функции полезны для повышения читабельности и производительности кода, особенно
при использовании в функциях высшего порядка, таких как <code>map()</code>, <code>filter()</code> и <code>reduce()</code>.</p>
<h1>Арифметические операции</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>operator.add(a, b)</code></td>
<td>Возвращает <code>a + b</code></td>
<td><code>operator.add(2, 3)</code> =&gt; <code>5</code></td>
</tr>
<tr>
<td><code>operator.sub(a, b)</code></td>
<td>Возвращает <code>a - b</code></td>
<td><code>operator.sub(5, 3)</code> =&gt; <code>2</code></td>
</tr>
<tr>
<td><code>operator.mul(a, b)</code></td>
<td>Возвращает <code>a * b</code></td>
<td><code>operator.mul(2, 3)</code> =&gt; <code>6</code></td>
</tr>
<tr>
<td><code>operator.truediv(a, b)</code></td>
<td>Возвращает <code>a / b</code></td>
<td><code>operator.truediv(7, 2)</code> =&gt; <code>3.5</code></td>
</tr>
<tr>
<td><code>operator.floordiv(a, b)</code></td>
<td>Возвращает <code>a // b</code></td>
<td><code>operator.floordiv(7, 2)</code> =&gt; <code>3</code></td>
</tr>
<tr>
<td><code>operator.mod(a, b)</code></td>
<td>Возвращает <code>a % b</code></td>
<td><code>operator.mod(7, 2)</code> =&gt; <code>1</code></td>
</tr>
<tr>
<td><code>operator.pow(a, b)</code></td>
<td>Возвращает <code>a ** b</code></td>
<td><code>operator.pow(2, 3)</code> =&gt; <code>8</code></td>
</tr>
<tr>
<td><code>operator.neg(a)</code></td>
<td>Возвращает <code>-a</code></td>
<td><code>operator.neg(5)</code> =&gt; <code>-5</code></td>
</tr>
<tr>
<td><code>operator.pos(a)</code></td>
<td>Возвращает <code>+a</code></td>
<td><code>operator.pos(-5)</code> =&gt; <code>-5</code></td>
</tr>
<tr>
<td><code>operator.abs(a)</code></td>
<td>Возвращает <code>abs(a)</code></td>
<td><code>operator.abs(-5)</code> =&gt; <code>5</code></td>
</tr>
</tbody>
</table>
<h1>Логические операции</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>operator.and_(a, b)</code></td>
<td>Логическое <strong>И</strong>: <code>a &amp; b</code></td>
<td><code>operator.and_(True, False)</code> =&gt; <code>False</code></td>
</tr>
<tr>
<td><code>operator.or_(a, b)</code></td>
<td>Логическое <strong>ИЛИ</strong>: <code>a | b</code></td>
<td><code>operator.or_(True, False)</code> =&gt; <code>True</code></td>
</tr>
<tr>
<td><code>operator.xor(a, b)</code></td>
<td>Логическое <strong>XOR</strong>: <code>a ^ b</code></td>
<td><code>operator.xor(True, False)</code> =&gt; <code>True</code></td>
</tr>
<tr>
<td><code>operator.not_(a)</code></td>
<td>Логическое <strong>НЕ</strong>: <code>not a</code></td>
<td><code>operator.not_(True)</code> =&gt; <code>False</code></td>
</tr>
</tbody>
</table>
<h1>Сравнения</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>operator.eq(a, b)</code></td>
<td>Возвращает <code>a == b</code></td>
<td><code>operator.eq(2, 2)</code> =&gt; <code>True</code></td>
</tr>
<tr>
<td><code>operator.ne(a, b)</code></td>
<td>Возвращает <code>a != b</code></td>
<td><code>operator.ne(2, 3)</code> =&gt; <code>True</code></td>
</tr>
<tr>
<td><code>operator.lt(a, b)</code></td>
<td>Возвращает <code>a &lt; b</code></td>
<td><code>operator.lt(2, 3)</code> =&gt; <code>True</code></td>
</tr>
<tr>
<td><code>operator.le(a, b)</code></td>
<td>Возвращает <code>a &lt;= b</code></td>
<td><code>operator.le(2, 2)</code> =&gt; <code>True</code></td>
</tr>
<tr>
<td><code>operator.gt(a, b)</code></td>
<td>Возвращает <code>a &gt; b</code></td>
<td><code>operator.gt(3, 2)</code> =&gt; <code>True</code></td>
</tr>
<tr>
<td><code>operator.ge(a, b)</code></td>
<td>Возвращает <code>a &gt;= b</code></td>
<td><code>operator.ge(3, 2)</code> =&gt; <code>True</code></td>
</tr>
<tr>
<td><code>operator.is_(a, b)</code></td>
<td>Возвращает <code>a is b</code></td>
<td><code>operator.is_(a, b)</code> =&gt; <code>True/False</code></td>
</tr>
<tr>
<td><code>operator.is_not(a, b)</code></td>
<td>Возвращает <code>a is not b</code></td>
<td><code>operator.is_not(a, b)</code> =&gt; <code>True/False</code></td>
</tr>
</tbody>
</table>
<h1>Операции с последовательностями</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>operator.concat(a, b)</code></td>
<td>Соединяет две последовательности</td>
<td><code>operator.concat([1, 2], [3, 4])</code> =&gt; <code>[1, 2, 3, 4]</code></td>
</tr>
<tr>
<td><code>operator.contains(a, b)</code></td>
<td>Проверяет, содержится ли <code>b</code> в <code>a</code></td>
<td><code>operator.contains([1, 2, 3], 2)</code> =&gt; <code>True</code></td>
</tr>
<tr>
<td><code>operator.countOf(a, b)</code></td>
<td>Возвращает количество вхождений <code>b</code> в <code>a</code></td>
<td><code>operator.countOf([1, 2, 2, 3], 2)</code> =&gt; <code>2</code></td>
</tr>
<tr>
<td><code>operator.indexOf(a, b)</code></td>
<td>Возвращает индекс первого вхождения <code>b</code> в <code>a</code></td>
<td><code>operator.indexOf([1, 2, 3], 2)</code> =&gt; <code>1</code></td>
</tr>
<tr>
<td><code>operator.itemgetter(*items)</code></td>
<td>Возвращает функцию, которая извлекает элементы по индексам</td>
<td><code>f = operator.itemgetter(1, 2); f([1, 2, 3])</code> =&gt; <code>(2, 3)</code></td>
</tr>
</tbody>
</table>
<h1>Операции с атрибутами и элементами</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>operator.attrgetter(attr)</code></td>
<td>Возвращает функцию, которая извлекает атрибут <code>attr</code></td>
<td><code>f = operator.attrgetter("name"); f(obj)</code> =&gt; <code>"name"</code></td>
</tr>
<tr>
<td><code>operator.itemgetter(*items)</code></td>
<td>Возвращает функцию, которая извлекает элементы по индексам</td>
<td><code>f = operator.itemgetter(1, 2); f([1, 2, 3])</code> =&gt; <code>(2, 3)</code></td>
</tr>
<tr>
<td><code>operator.setitem(a, b, c)</code></td>
<td>Устанавливает значение <code>c</code> элементу <code>b</code> в <code>a</code></td>
<td><code>operator.setitem(my_dict, "key", "value")</code></td>
</tr>
<tr>
<td><code>operator.delitem(a, b)</code></td>
<td>Удаляет элемент <code>b</code> из <code>a</code></td>
<td><code>operator.delitem(my_dict, "key")</code></td>
</tr>
<tr>
<td><code>operator.getitem(a, b)</code></td>
<td>Извлекает элемент <code>b</code> из <code>a</code></td>
<td><code>operator.getitem(my_list, 0)</code> =&gt; <code>1</code></td>
</tr>
</tbody>
</table>
<h1>Работа с срезами</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>operator.index(a)</code></td>
<td>Возвращает индекс <code>a</code></td>
<td><code>operator.index([1, 2, 3], 2)</code> =&gt; <code>1</code></td>
</tr>
<tr>
<td><code>operator.getslice(a, start, end)</code></td>
<td>Возвращает срез списка от <code>start</code> до <code>end</code></td>
<td><code>operator.getslice([1, 2, 3, 4], 1, 3)</code> =&gt; <code>[2, 3]</code></td>
</tr>
<tr>
<td><code>operator.setslice(a, start, end, b)</code></td>
<td>Заменяет срез списка от <code>start</code> до <code>end</code> на <code>b</code></td>
<td><code>operator.setslice(my_list, 1, 3, [7, 8])</code></td>
</tr>
<tr>
<td><code>operator.delslice(a, start, end)</code></td>
<td>Удаляет срез списка от <code>start</code> до <code>end</code></td>
<td><code>operator.delslice(my_list, 1, 3)</code></td>
</tr>
</tbody>
</table>
<h1>Примеры использования</h1>
<h3>Применение функций <code>operator</code> в <code>map()</code></h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">operator</span>

<span class="n">numbers</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="n">squared</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="n">operator</span><span class="o">.</span><span class="n">pow</span><span class="p">,</span> <span class="n">numbers</span><span class="p">,</span> <span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="n">numbers</span><span class="p">)))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">squared</span><span class="p">)</span>  <span class="c1"># [1, 4, 9, 16, 25]</span>
</pre></div></div></div>

<h3>Использование <code>itemgetter</code> для сортировки списка словарей</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">operator</span>

<span class="n">students</span> <span class="o">=</span> <span class="p">[</span>
  <span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Alice&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">25</span><span class="p">},</span>
  <span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Bob&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">20</span><span class="p">},</span>
  <span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Charlie&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">23</span><span class="p">},</span>
<span class="p">]</span>
<span class="n">sorted_students</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">students</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="n">operator</span><span class="o">.</span><span class="n">itemgetter</span><span class="p">(</span><span class="s2">&quot;age&quot;</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sorted_students</span><span class="p">)</span>
<span class="c1"># [{&quot;name&quot;: &quot;Bob&quot;, &quot;age&quot;: 20}, {&quot;name&quot;: &quot;Charlie&quot;, &quot;age&quot;: 23}, {&quot;name&quot;: &quot;Alice&quot;, &quot;age&quot;: 25}]</span>
</pre></div></div></div>