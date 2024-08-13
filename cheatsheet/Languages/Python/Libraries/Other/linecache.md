<p>Библиотека "linecache" в Python используется для чтения линий из файлов с исходным кодом.
Она предоставляет функции для извлечения строк из файла по их номеру.</p>
<p>Методы модуля "linecache" включают:
<code>getline(filename, lineno)</code>: Возвращает указанную строку из указанного файла.
<code>getlines(filename)</code>: Возвращает все строки из указанного файла в виде списка.
<code>clearcache()</code>: Очищает кэш, используемый для хранения строк файла.</p>
<p>Примеры подмодулей отсутствуют.</p>
<p>Некоторые из самых часто используемых методов "linecache" включают:
Метод <code>getline(filename, lineno)</code> - возвращает указанную строку из указанного файла.</p>
<pre><code class="language-python">import linecache

line = linecache.getline(&quot;file.txt&quot;, 5)
print(line)
</code></pre>
<p>Этот код выведет пятую строку из файла "file.txt".</p>
<p>Метод <code>getlines(filename)</code> - возвращает все строки из указанного файла в виде списка.</p>
<pre><code class="language-python">import linecache

lines = linecache.getlines(&quot;file.txt&quot;)
for line in lines:
    print(line)
</code></pre>
<p>Этот код выведет все строки из файла "file.txt" по одной строке на каждую итерацию цикла.</p>
<p>Метод <code>clearcache()</code> - очищает кэш, используемый для хранения строк файла.
Это может быть полезно, если файл изменился и требуется обновить строки в кэше.</p>
<pre><code class="language-python">import linecache

# Изменения в файле &quot;file.txt&quot;

linecache.clearcache()
line = linecache.getline(&quot;file.txt&quot;, 5)
print(line)
</code></pre>
<p>Этот код сначала очищает кэш, а затем возвращает пятую строку из обновленного файла "file.txt".</p>
<p>Примечание: Убедитесь, что файл "file.txt" существует и содержит нужные строки.</p>