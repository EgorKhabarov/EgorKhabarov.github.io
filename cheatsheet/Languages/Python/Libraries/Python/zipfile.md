<p>Библиотека "zipfile" в Python используется для работы с архивами формата ZIP.
Она предоставляет функциональность для создания, чтения, обновления и извлечения файлов из архива.</p>
<p>Таблица методов библиотеки "zipfile" и их краткого описания:</p>
<p><code>ZipFile(file, mode="r", compression=ZIP_STORED, allowZip64=True)</code> - создает объект ZipFile, представляющий архив ZIP из файла. Режимы могут быть чтение ("r"), запись ("w") или добавление ("a").
<code>ZipFile.extractall(path=None, members=None, pwd=None)</code> - извлекает все файлы из архива в указанную папку.
<code>ZipFile.extract(member, path=None, pwd=None)</code> - извлекает конкретный файл из архива.
<code>ZipFile.namelist()</code> - возвращает список имен файлов в архиве.
<code>ZipFile.open(name, mode="r", pwd=None)</code> - открывает файл в архиве и возвращает объект файлового дескриптора.
<code>ZipFile.close()</code> - закрывает объект ZipFile и освобождает ресурсы.</p>
<p>Список самых часто используемых методов, их краткого описания и пример демонстрирующий их работу:</p>
<p><code>extractall(path=None, members=None, pwd=None)</code> - извлекает все файлы из архива в указанную папку.</p>
<pre><code class="language-python">import zipfile

# Открываем архив
with zipfile.ZipFile(&quot;archive.zip&quot;, &quot;r&quot;) as zip_ref:
    # Извлекаем все файлы
    zip_ref.extractall(&quot;destination_folder&quot;)
</code></pre>
<p><code>namelist()</code> - возвращает список имен файлов в архиве.</p>
<pre><code class="language-python">import zipfile

# Открываем архив
with zipfile.ZipFile(&quot;archive.zip&quot;, &quot;r&quot;) as zip_ref:
    # Получаем список имен файлов
    file_names = zip_ref.namelist()

    # Выводим список имен файлов
    for name in file_names:
        print(name)
</code></pre>
<p><code>extract(member, path=None, pwd=None)</code> - извлекает конкретный файл из архива.</p>
<pre><code class="language-python">import zipfile

# Открываем архив
with zipfile.ZipFile(&quot;archive.zip&quot;, &quot;r&quot;) as zip_ref:
    # Извлекаем файл с именем &quot;file.txt&quot;
    zip_ref.extract(&quot;file.txt&quot;, &quot;destination_folder&quot;)
</code></pre>