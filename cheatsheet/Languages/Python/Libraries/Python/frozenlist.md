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
<td><strong>init</strong>()</td>
<td>Инициализирует новый объект frozenlist.</td>
</tr>
<tr>
<td><strong>contains</strong>()</td>
<td>Проверяет наличие элемента в списке.</td>
</tr>
<tr>
<td><strong>getitem</strong>()</td>
<td>Получает элемент списка по индексу.</td>
</tr>
<tr>
<td><strong>len</strong>()</td>
<td>Возвращает количество элементов в списке.</td>
</tr>
<tr>
<td>copy()</td>
<td>Возвращает копию frozenlist.</td>
</tr>
</tbody>
</table>
<p>Список самых частых методов, краткое описание и работающие примеры:</p>
<pre><code class="language-python"># Метод __init__()
flist = frozenlist([1, 2, 3, 4, 5])
# Метод __contains__()
print(3 in flist)  # Выведет True, так как 3 есть в списке
# Метод __getitem__()
print(flist[1])  # Выведет 2, так как это элемент на позиции 1
# Метод __len__()
print(len(flist))  # Выведет 5, так количество элементов в списке равно 5
# Метод copy()
flist_copy = flist.copy()  # Создаст копию списка
</code></pre>
<p>Пожалуйста, убедитесь, что установлена библиотека <code>frozenlist</code>.
Если нет, используйте данную команду для установки - <code>pip install frozenlist</code>.</p>