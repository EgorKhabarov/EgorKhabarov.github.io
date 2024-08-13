<p>Библиотека "genericpath" в Python используется для работы с путями и файловой системой на разных платформах.
Она предоставляет универсальные методы для обработки путей, создания новых путей, проверки наличия файлов и директорий,
а также для работы с именами файлов.</p>
<p>Таблица методов и их описания в модуле "genericpath":</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>isdir(path)</td>
<td>Проверяет, является ли указанный путь директорией.</td>
</tr>
<tr>
<td>isfile(path)</td>
<td>Проверяет, является ли указанный путь файлом.</td>
</tr>
<tr>
<td>exists(path)</td>
<td>Проверяет, существует ли указанный путь.</td>
</tr>
<tr>
<td>lexists(path)</td>
<td>Проверяет, существует ли указанный путь (обходя символические ссылки).</td>
</tr>
<tr>
<td>split(path)</td>
<td>Разделяет путь на директорию и базовое имя файла.</td>
</tr>
<tr>
<td>splitext(path)</td>
<td>Разделяет путь на базовое имя файла и расширение.</td>
</tr>
<tr>
<td>basename(path)</td>
<td>Возвращает последний компонент пути (имя файла или директории).</td>
</tr>
<tr>
<td>dirname(path)</td>
<td>Возвращает директорию из пути.</td>
</tr>
<tr>
<td>join(path, *paths)</td>
<td>Объединяет пути в переносимый образ.</td>
</tr>
<tr>
<td>normpath(path)</td>
<td>Преобразует путь, удаляя избыточные разделители и ссылки "." и "..".</td>
</tr>
<tr>
<td>abspath(path)</td>
<td>Возвращает абсолютный путь.</td>
</tr>
</tbody>
</table>
<p>isdir(path): Проверяет, является ли указанный путь директорией.</p>
<pre><code class="language-python">import os.path

path = &quot;/path/to/directory&quot;
if os.path.isdir(path):
    print(f&quot;{path} is a directory.&quot;)
</code></pre>
<p>isfile(path): Проверяет, является ли указанный путь файлом.</p>
<pre><code class="language-python">import os.path

path = &quot;/path/to/file.txt&quot;
if os.path.isfile(path):
    print(f&quot;{path} is a file.&quot;)
</code></pre>
<p>exists(path): Проверяет, существует ли указанный путь.</p>
<pre><code class="language-python">import os.path

path = &quot;/path/to/file.txt&quot;
if os.path.exists(path):
    print(f&quot;{path} exists.&quot;)
</code></pre>
<p>splitext(path): Разделяет путь на базовое имя файла и расширение.</p>
<pre><code class="language-python">import os.path

path = &quot;/path/to/file.txt&quot;
base_name, extension = os.path.splitext(path)
print(f&quot;Base name: {base_name}&quot;)
print(f&quot;Extension: {extension}&quot;)
</code></pre>