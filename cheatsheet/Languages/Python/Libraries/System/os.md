<p>Получение информации о текущей директории:</p>
<pre><code class="language-python">import os

print(os.getcwd())
</code></pre>
<p>Создание директории:</p>
<pre><code class="language-python">import os

os.mkdir(&quot;new_dir&quot;)
</code></pre>
<p>Удаление директории:</p>
<pre><code class="language-python">import os

os.rmdir(&quot;dir_to_remove&quot;)
</code></pre>
<p>Проверка наличия файла или директории:</p>
<pre><code class="language-python">import os

if os.path.exists(&quot;file.txt&quot;):
    print(&quot;File exists!&quot;)

if os.path.exists(&quot;dir&quot;):
    print(&quot;Directory exists!&quot;)
</code></pre>
<p>Получение списка файлов в директории:</p>
<pre><code class="language-python">import os

files = os.listdir(&quot;my_dir&quot;)
for file in files:
    print(file)
</code></pre>
<p>Переименование файла или директории:</p>
<pre><code class="language-python">import os

os.rename(&quot;old_file.txt&quot;, &quot;new_file.txt&quot;)
</code></pre>
<p>Удаление файла:</p>
<pre><code class="language-python">import os

os.remove(&quot;file_to_remove.txt&quot;)
</code></pre>
<p>Получение информации о файле:</p>
<pre><code class="language-python">import os

file_stat = os.stat(&quot;file.txt&quot;)

print(&quot;Size of file:&quot;, file_stat.st_size)
print(&quot;Last accessed time:&quot;, file_stat.st_atime)
</code></pre>
<p>Проверка, является ли путь директорией или файлом:</p>
<pre><code class="language-python">import os

if os.path.isfile(&quot;my_file.txt&quot;):
    print(&quot;This is a file!&quot;)

if os.path.isdir(&quot;my_file.txt&quot;):
    print(&quot;This is a directory!&quot;)
</code></pre>
<p>Получение имени файла из пути:</p>
<pre><code class="language-python">import os

print(os.path.basename(&quot;/my_dir/my_file.txt&quot;))
</code></pre>
<p>Получение пути к директории из пути к файлу:</p>
<pre><code class="language-python">import os

print(os.path.dirname(&quot;/my_dir/my_file.txt&quot;))
</code></pre>
<p>Получение абсолютного пути:</p>
<pre><code class="language-python">import os

print(os.path.abspath(&quot;my_dir/my_file.txt&quot;))
</code></pre>
<p>Объединение путей:</p>
<pre><code class="language-python">import os

print(os.path.join(&quot;/my_dir&quot;, &quot;my_file.txt&quot;))
</code></pre>
<p>Получение расширения файла:</p>
<pre><code class="language-python">import os

print(os.path.splitext(&quot;my_file.txt&quot;)[1])
</code></pre>
<p>Получение списка всех поддиректорий в директории:</p>
<pre><code class="language-python">import os

print([f.path for f in os.scandir(&quot;my_dir&quot;) if f.is_dir()])
</code></pre>