<p>Библиотека "fnmatch" используется в Python для сопоставления и фильтрации строк с использованием шаблонов, основанных на грамматике восходящих преобразований.
Вот таблица методов модуля "fnmatch" и их краткие описания:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>fnmatch(name, pattern)</td>
<td>Сопоставляет имя файла с заданным шаблоном.</td>
</tr>
<tr>
<td>filter(names, pattern)</td>
<td>Фильтрует список имен файлов, оставляя только те, которые соответствуют заданному шаблону.</td>
</tr>
<tr>
<td>translate(pattern)</td>
<td>Преобразует заданный шаблон во внутренний формат, используемый для сопоставления.</td>
</tr>
</tbody>
</table>
<p>Вот список наиболее часто используемых методов "fnmatch", их краткое описание и небольшой код, демонстрирующий их работу:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td>fnmatch(name, pattern)</td>
<td>Сопоставляет имя файла с шаблоном.</td>
<td>fnmatch("example.txt", "*.txt") # True</td>
</tr>
<tr>
<td>filter(names, pattern)</td>
<td>Фильтрует список имен файлов.</td>
<td>filter(['file1.txt', 'file2.py'], "*.txt") # ['file1.txt']</td>
</tr>
<tr>
<td>translate(pattern)</td>
<td>Преобразует шаблон во внутренний формат.</td>
<td>translate("*.txt") # '[A-Za-z0-9]+.txt$'</td>
</tr>
</tbody>
</table>