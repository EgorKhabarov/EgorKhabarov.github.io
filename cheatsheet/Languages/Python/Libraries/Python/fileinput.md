<p>Библиотека "fileinput" используется для обработки текстовых файлов в Python.
Она предоставляет удобные инструменты для чтения и обработки содержимого файлов.</p>
<p>Методы модуля "fileinput" и его подмодулей:</p>
<p>input(): Возвращает итератор, который построчно читает файлы.
filename(): Возвращает текущее имя файла.
lineno(): Возвращает текущий номер строки файла.
filelineno(): Возвращает текущий номер строки относительно текущего файла.
isfirstline(): Проверяет, является ли текущая строка первой в файле.
isstdin(): Проверяет, читается ли текущая строка с stdin.
nextfile(): Переходит к следующему файлу.
close(): Закрывает файлы, открытые с помощью fileinput.</p>
<p>Некоторые из самых часто используемых методов библиотеки "fileinput" вместе с кратким описанием и примером кода:</p>
<p>input(): Возвращает итератор для построчного чтения файлов.</p>
<pre><code class="language-python">import fileinput

for line in fileinput.input():
    print(line)
</code></pre>
<p>filename(): Возвращает текущее имя файла.</p>
<pre><code class="language-python">import fileinput

for line in fileinput.input():
    print(f&quot;Current file: {fileinput.filename()}&quot;)
</code></pre>
<p>lineno(): Возвращает текущий номер строки файла.</p>
<pre><code class="language-python">import fileinput

for line in fileinput.input():
    print(f&quot;Line number: {fileinput.lineno()}&quot;)
</code></pre>