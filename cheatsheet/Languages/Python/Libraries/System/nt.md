<p>Библиотека "nt" в Python используется для работы с функциями операционной системы Windows.</p>
<p>Методы модуля "nt" и его подмодулей:</p>
<p>Модуль "nt":
nt.getcwd(): Возвращает текущую рабочую директорию.
nt.listdir(path): Возвращает список файлов и директорий в указанном пути.
nt.mkdir(path): Создает новую директорию по указанному пути.
nt.remove(path): Удаляет файл по указанному пути.
nt.rename(src, dst): Переименовывает файл или директорию.
nt.system(command): Выполняет команду операционной системы.</p>
<p>Подмодуль "ntpath":
ntpath.basename(path): Возвращает имя файла или директории из указанного пути.
ntpath.dirname(path): Возвращает имя директории из указанного пути.
ntpath.exists(path): Проверяет, существует ли файл или директория по указанному пути.
ntpath.join(path, *paths): Объединяет пути в один.
ntpath.split(path): Разделяет путь на имя директории и имя файла.</p>
<p>Некоторые часто используемые методы и их описание:</p>
<p>nt.getcwd(): Возвращает текущую рабочую директорию.</p>
<pre><code class="language-python">import nt
current_dir = nt.getcwd()
print(current_dir)
</code></pre>
<p>nt.listdir(path): Возвращает список файлов и директорий в указанном пути.</p>
<pre><code class="language-python">import nt
file_list = nt.listdir(&quot;C:/Users&quot;)
print(file_list)
</code></pre>
<p>nt.mkdir(path): Создает новую директорию по указанному пути.</p>
<pre><code class="language-python">import nt
nt.mkdir(&quot;C:/Users/NewDirectory&quot;)
</code></pre>
<p>nt.remove(path): Удаляет файл по указанному пути.</p>
<pre><code class="language-python">import nt
nt.remove(&quot;C:/Users/example.txt&quot;)
</code></pre>
<p>nt.rename(src, dst): Переименовывает файл или директорию.</p>
<pre><code class="language-python">import nt
nt.rename(&quot;C:/Users/old_name.txt&quot;, &quot;C:/Users/new_name.txt&quot;)
</code></pre>
<p>nt.system(command): Выполняет команду операционной системы.</p>
<pre><code class="language-python">import nt
nt.system(&quot;dir&quot;)
</code></pre>