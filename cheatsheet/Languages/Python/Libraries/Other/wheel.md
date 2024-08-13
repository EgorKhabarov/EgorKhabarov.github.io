<p>Библиотека "wheel" в Python используется для упрощения установки пакетов и их распространения.
Она представляет собой формат пакета, который содержит предварительно
скомпилированные бинарные файлы, что позволяет ускорить процесс установки.</p>
<h3>Методы модуля "wheel":</h3>
<p><code>convert</code>: используется для преобразования исходных файлов пакета в формат wheel.
<code>install</code>: позволяет установить пакет из wheel-файла.
<code>unpack</code>: распаковывает содержимое wheel-файла.
<code>pack</code>: упаковывает исходные файлы пакета в wheel-файл.</p>
<h3>Подмодули:</h3>
<p><code>metadata</code>: содержит методы для работы с метаданными пакета, такими как версия, автор и описание.
<code>tags</code>: предоставляет информацию о поддерживаемых платформах и интерпретаторах.
<code>signatures</code>: позволяет работать с подписями wheel-файлов.
<code>pep425tags</code>: предоставляет методы для работы с тегами PEP 425,
которые описывают совместимость пакетов с определенными версиями Python и операционных систем.</p>
<h3>convert</h3>
<p>Преобразует исходные файлы пакета в формат wheel.</p>
<pre><code class="language-python">from wheel import convert

convert.pack(&quot;path/to/source/package&quot;)
</code></pre>
<h3>install</h3>
<p>Устанавливает пакет из wheel-файла.</p>
<pre><code class="language-python">from wheel import install

install.install(&quot;path/to/wheel/file.whl&quot;)
</code></pre>
<h3>unpack</h3>
<p>Распаковывает содержимое wheel-файла.</p>
<pre><code class="language-python">from wheel import unpack

unpack.unpack(&quot;path/to/wheel/file.whl&quot;, &quot;path/to/destination&quot;)
</code></pre>
<h3>pack</h3></h3>
<p>Упаковывает исходные файлы пакета в wheel-файл.</p>
<pre><code class="language-python">from wheel import pack

pack.pack(&quot;path/to/source/package&quot;, &quot;path/to/destination/file.whl&quot;)
</code></pre>