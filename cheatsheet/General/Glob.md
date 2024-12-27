<p><strong>Glob</strong> — это шаблон сопоставления имен файлов и директорий</p>
<table>
<thead>
<tr>
<th>Шаблон</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>*</code></td>
<td>Соответствует любому количеству символов (включая 0) в имени файла или папки</td>
<td><code>*.txt</code> — все файлы с расширением <code>.txt</code></td>
</tr>
<tr>
<td><code>?</code></td>
<td>Соответствует любому одиночному символу</td>
<td><code>file?.txt</code> — <code>file1.txt</code>, <code>file2.txt</code></td>
</tr>
<tr>
<td><code>[abc]</code></td>
<td>Соответствует любому символу из указанного набора</td>
<td><code>file[12].txt</code> — <code>file1.txt</code>, <code>file2.txt</code></td>
</tr>
<tr>
<td><code>[a-z]</code></td>
<td>Соответствует любому символу в заданном диапазоне</td>
<td><code>[a-c].txt</code> — <code>a.txt</code>, <code>b.txt</code>, <code>c.txt</code></td>
</tr>
<tr>
<td><code>[!abc]</code></td>
<td>Соответствует любому символу, <strong>кроме</strong> указанных в наборе</td>
<td><code>file[!10].txt</code> — исключает цифры 1 и 0</td>
</tr>
<tr>
<td><code>[!a-z]</code></td>
<td>Соответствует любому символу, <strong>кроме</strong> указанных в заданном диапазоне</td>
<td><code>file[!0-9].txt</code> — исключает цифры</td>
</tr>
<tr>
<td><code>**</code></td>
<td>Соответствует любому количеству поддиректорий (требуется параметр <code>recursive=True</code>)</td>
<td><code>**/*.py</code> — все <code>.py</code> файлы в проекте</td>
</tr>
</tbody>
</table>
<p><a href="https://en.wikipedia.org/wiki/Glob_(programming)">https://en.wikipedia.org/wiki/Glob_(programming)</a></p>
<p>Для сложной фильтрации в Python лучше использовать <a href="?Languages/Python/Libraries/System/fnmatch.md"><code>fnmatch</code></a></p>