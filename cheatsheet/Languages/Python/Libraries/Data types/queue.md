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
<pre><code class="language-python">q = Queue()
q.put(1)
q.put(2)
print(q.qsize())  # Вывод: 2
</code></pre>
<p><strong>get()</strong> Удаляет и возвращает первый элемент из очереди.</p>
<pre><code class="language-python">q = Queue()
q.put(1)
q.put(2)
print(q.get())  # Вывод: 1
</code></pre>
<p><strong>empty()</strong> Проверяет, пуста ли очередь.</p>
<pre><code class="language-python">q = Queue()
print(q.empty())  # Вывод: True
</code></pre>