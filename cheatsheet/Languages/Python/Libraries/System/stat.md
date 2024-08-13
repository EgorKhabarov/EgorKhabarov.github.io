<p>Библиотека "stat" в Python используется для работы с информацией о файловой системе,
такой как атрибуты файла, права доступа и временные метки.</p>
<p>Методы модуля "stat" и его подмодулей:</p>
<p>stat.S_ISDIR(mode): Проверяет, является ли файл директорией.
stat.S_ISREG(mode): Проверяет, является ли файл обычным файлом.
stat.S_ISLNK(mode): Проверяет, является ли файл символической ссылкой.
stat.S_ISSOCK(mode): Проверяет, является ли файл сокетом.
stat.S_ISFIFO(mode): Проверяет, является ли файл каналом FIFO.
stat.S_ISBLK(mode): Проверяет, является ли файл блочным устройством.
stat.S_ISCHR(mode): Проверяет, является ли файл символьным устройством.
stat.S_IMODE(mode): Возвращает режим доступа к файлу.
stat.S_IFMT(mode): Возвращает тип файла и режим доступа.</p>
<p>Самые часто используемые методы:</p>
<p>stat.S_ISDIR(mode): Проверяет, является ли файл директорией.</p>
<pre><code class="language-python">import os
import stat

file_path = &quot;path/to/file.txt&quot;
file_stat = os.stat(file_path)
if stat.S_ISDIR(file_stat.st_mode):
    print(&quot;File is a directory&quot;)
else:
    print(&quot;File is not a directory&quot;)
</code></pre>
<p>stat.S_ISREG(mode): Проверяет, является ли файл обычным файлом.</p>
<pre><code class="language-python">import os
import stat

file_path = &quot;path/to/file.txt&quot;
file_stat = os.stat(file_path)
if stat.S_ISREG(file_stat.st_mode):
    print(&quot;File is a regular file&quot;)
else:
    print(&quot;File is not a regular file&quot;)
</code></pre>
<p>stat.S_IMODE(mode): Возвращает режим доступа к файлу.</p>
<pre><code class="language-python">import os
import stat

file_path = &quot;path/to/file.txt&quot;
file_stat = os.stat(file_path)
file_mode = stat.S_IMODE(file_stat.st_mode)
print(&quot;File mode:&quot;, file_mode)
</code></pre>