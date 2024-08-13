<table>
<thead>
<tr>
<th style="text-align: left;">Метод</th>
<th style="text-align: left;">Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">dict.clear()</td>
<td style="text-align: left;">Удаляет все элементы<br><pre><code class="language-python">&gt;&gt;&gt; d = {1: 2, 3: 4}<br>&gt;&gt;&gt; d.clear()<br>&gt;&gt;&gt; print(d)<br>{}</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">dict.copy()</td>
<td style="text-align: left;">Возвращает поверхностную копию словаря<br><pre><code class="language-python">&gt;&gt;&gt; d = {1: 2, 3: 4}<br>&gt;&gt;&gt; d.copy()<br>&gt;&gt;&gt; print(d)<br>{1: 2, 3: 4}</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">dict.fromkeys()</td>
<td style="text-align: left;">Создает словарь из заданной последовательности<br><pre><code class="language-python">&gt;&gt;&gt; print(dict.fromkeys(("key1", "key2", "key3"), 0))<br>{"key1": 0, "key2": 0, "key3": 0}</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">dict.get()</td>
<td style="text-align: left;">Возвращает значение ключа<br><pre><code class="language-python">&gt;&gt;&gt; print({"model": "Mustang", "year": 1964}.get("model"))<br>Mustang<br>&gt;&gt;&gt; print({"model": "Mustang", "year": 1964}.get("color", "red"))<br>red</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">dict.pop()</td>
<td style="text-align: left;">Удаляет и возвращает элемент с заданным ключом<br><pre><code class="language-python">&gt;&gt;&gt; d = {1: 2, 3: 4}<br>&gt;&gt;&gt; print(d.pop(3))<br>4<br>&gt;&gt;&gt; print(d)<br>{1: 2}</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">dict.popitem()</td>
<td style="text-align: left;">Возвращает и удаляет последний элемент из словаря<br><pre><code class="language-python">&gt;&gt;&gt; d = {1: 2, 3: 4}<br>&gt;&gt;&gt; print(d.popitem())<br>(3, 4)<br>&gt;&gt;&gt; print(d)<br>{1: 2}</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">dict.setdefault()</td>
<td style="text-align: left;">Возвращает значение по ключу. Если ключ отсутствует он вставляет ключ<br><pre><code class="language-python">&gt;&gt;&gt; d = {}<br>&gt;&gt;&gt; d.setdefault("k", "d")<br>"d"<br>&gt;&gt;&gt; d<br>{"k": "d"}</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">dict.update()</td>
<td style="text-align: left;">Обновляет словарь указанными парами ключ-значение.<br><pre><code class="language-python">&gt;&gt;&gt; d = {1: 2, 3: 4}<br>&gt;&gt;&gt; d.update({3: 5, 6: 7})<br>&gt;&gt;&gt; print(d)<br>{1: 2, 3: 5, 6: 7}</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">dict.items()</td>
<td style="text-align: left;">Возвращает вид пары словаря (ключ, значение)<br><pre><code class="language-python">&gt;&gt;&gt; d = {1: 2, 3: 4}<br>&gt;&gt;&gt; print(d.items())<br>dict_items([(1, 2), (3, 4)])</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">dict.keys()</td>
<td style="text-align: left;">Возвращает объект просмотра всех ключей<br><pre><code class="language-python">&gt;&gt;&gt; d = {1: 2, 3: 4}<br>&gt;&gt;&gt; print(d.keys())<br>dict_keys([1, 3])</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">dict.values()</td>
<td style="text-align: left;">Возвращает список всех значений в словаре<br><pre><code class="language-python">&gt;&gt;&gt; d = {1: 2, 3: 4}<br>&gt;&gt;&gt; print(d.values())<br>dict_values([2, 4])</code></pre></td>
</tr>
</tbody>
</table>