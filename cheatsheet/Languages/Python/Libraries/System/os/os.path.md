<table>
<thead>
<tr>
<th>Функция/Метод</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>os.path.basename(path)</code></td>
<td>Возвращает имя файла из пути</td>
<td><code>os.path.basename("/path/to/file.txt")</code></td>
</tr>
<tr>
<td><code>os.path.dirname(path)</code></td>
<td>Возвращает путь к директории без имени файла</td>
<td><code>os.path.dirname("/path/to/file.txt")</code></td>
</tr>
<tr>
<td><code>os.path.split(path)</code></td>
<td>Разделяет путь на кортеж <code>(dirname, basename)</code></td>
<td><code>os.path.split("/path/to/file.txt")</code></td>
</tr>
<tr>
<td><code>os.path.splitext(path)</code></td>
<td>Разделяет путь на кортеж <code>(root, ext)</code> с корнем и расширением файла</td>
<td><code>os.path.splitext("/path/to/file.txt")</code></td>
</tr>
<tr>
<td><code>os.path.join(path, *paths)</code></td>
<td>Соединяет компоненты пути в единый путь</td>
<td><code>os.path.join("path", "to", "file.txt")</code></td>
</tr>
<tr>
<td><code>os.path.abspath(path)</code></td>
<td>Преобразует путь в абсолютный путь</td>
<td><code>os.path.abspath("file.txt")</code></td>
</tr>
<tr>
<td><code>os.path.realpath(path)</code></td>
<td>Возвращает канонический путь, учитывая символические ссылки</td>
<td><code>os.path.realpath("symlink")</code></td>
</tr>
<tr>
<td><code>os.path.exists(path)</code></td>
<td>Проверяет, существует ли путь</td>
<td><code>os.path.exists("file.txt")</code></td>
</tr>
<tr>
<td><code>os.path.isfile(path)</code></td>
<td>Проверяет, является ли путь файлом</td>
<td><code>os.path.isfile("file.txt")</code></td>
</tr>
<tr>
<td><code>os.path.isdir(path)</code></td>
<td>Проверяет, является ли путь директорией</td>
<td><code>os.path.isdir("directory")</code></td>
</tr>
<tr>
<td><code>os.path.getsize(path)</code></td>
<td>Возвращает размер файла в байтах</td>
<td><code>os.path.getsize("file.txt")</code></td>
</tr>
<tr>
<td><code>os.path.abspath(path)</code></td>
<td>Возвращает абсолютный путь</td>
<td><code>os.path.abspath("file.txt")</code></td>
</tr>
</tbody>
</table>