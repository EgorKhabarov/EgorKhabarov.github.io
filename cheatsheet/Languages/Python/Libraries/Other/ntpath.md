<p>Библиотека "ntpath" в Python используется для обработки и манипулирования путями файловой системы
с учетом специфических особенностей операционной системы Windows.</p>
<p>Таблица методов модуля и его подмодуля "ntpath" и их краткое описание:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>ntpath.abspath(path)</td>
<td>Возвращает абсолютный путь к указанному пути.</td>
</tr>
<tr>
<td>ntpath.basename(path)</td>
<td>Возвращает базовое имя файла или каталога из указанного пути.</td>
</tr>
<tr>
<td>ntpath.commonprefix(list)</td>
<td>Возвращает наибольший общий префикс из списка путей.</td>
</tr>
<tr>
<td>ntpath.dirname(path)</td>
<td>Возвращает каталог, содержащий указанный путь.</td>
</tr>
<tr>
<td>ntpath.exists(path)</td>
<td>Проверяет, существует ли указанный путь.</td>
</tr>
<tr>
<td>ntpath.expanduser(path)</td>
<td>Заменяет в указанном пути тильду (~) на домашний каталог пользователя.</td>
</tr>
<tr>
<td>ntpath.expandvars(path)</td>
<td>Заменяет переменные окружения в указанном пути на их значения.</td>
</tr>
<tr>
<td>ntpath.isfile(path)</td>
<td>Проверяет, является ли указанный путь файлом.</td>
</tr>
<tr>
<td>ntpath.isdir(path)</td>
<td>Проверяет, является ли указанный путь каталогом.</td>
</tr>
<tr>
<td>ntpath.join(path, *paths)</td>
<td>Объединяет пути с использованием разделителя.</td>
</tr>
<tr>
<td>ntpath.normpath(path)</td>
<td>Нормализует указанный путь, удаляя двойные слеши и точки.</td>
</tr>
<tr>
<td>ntpath.realpath(path)</td>
<td>Возвращает канонический абсолютный путь к указанному пути.</td>
</tr>
<tr>
<td>ntpath.relpath(path, start)</td>
<td>Возвращает относительный путь от исходного пути до указанного пути.</td>
</tr>
<tr>
<td>ntpath.split(path)</td>
<td>Разделяет указанный путь на имя каталога и имя файла.</td>
</tr>
</tbody>
</table>
<p>Несколько часто используемых методов "ntpath" с их кратким описанием и примерами кода:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td>ntpath.basename(path)</td>
<td>Возвращает базовое имя файла или каталога из указанного пути</td>
<td>dirname, filename = ntpath.split("/path/to/file.txt") print(filename) -&gt; "file.txt"</td>
</tr>
<tr>
<td>ntpath.exists(path)</td>
<td>Проверяет, существует ли указанный путь</td>
<td>if ntpath.exists("/path/to/file.txt"): print("File exists")</td>
</tr>
<tr>
<td>ntpath.join(path, *paths)</td>
<td>Объединяет пути с использованием разделителя</td>
<td>full_path = ntpath.join("/path/to", "file.txt") print(full_path) -&gt; "/path/to/file.txt"</td>
</tr>
</tbody>
</table>