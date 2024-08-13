<p>Библиотека "warnings" в Python используется для управления предупреждениями, которые могут возникать во время выполнения программы.
Она позволяет контролировать вывод предупреждений и принимать соответствующие действия.</p>
<p>Методы и подмодули библиотеки "warnings":</p>
<p><code>warn(message, warning_type, stacklevel)</code> - генерирует предупреждение с указанным сообщением, типом предупреждения и уровнем стека.
<code>filterwarnings(action, message, category, module, lineno, append)</code> - устанавливает фильтр для предупреждений, определяя действие, текст сообщения, категорию предупреждения, модуль, номер строки и флаг добавления фильтра.
<code>simplefilter(action, category=Warning, lineno=0, append=False)</code> - устанавливает простой фильтр для предупреждений с указанным действием, категорией, номером строки и флагом добавления фильтра.
<code>resetwarnings()</code> - сбрасывает все установленные фильтры предупреждений.
<code>showwarning(message, category, filename, lineno, file=None, line=None)</code> - выводит предупреждение с указанным сообщением, категорией, исходным файлом, номером строки, файлом вывода и строкой кода.
<code>catch_warnings(*, record=False, module=None)</code> - возвращает контекстный менеджер для временного перехвата предупреждений с опциональной записью в список или указанный модуль.</p>
<p><code>warn(message, warning_type, stacklevel)</code> - генерирует предупреждение с заданным сообщением, типом предупреждения и уровнем стека.</p>
<pre><code class="language-python">import warnings

warnings.warn(&quot;This is a warning message&quot;, UserWarning, stacklevel=2)
</code></pre>
<p><code>filterwarnings(action, message, category, module, lineno, append)</code> - устанавливает фильтр для предупреждений с указанными параметрами.</p>
<pre><code class="language-python">import warnings

warnings.filterwarnings(&quot;ignore&quot;, category=DeprecationWarning, module=&quot;my_module&quot;)
</code></pre>
<p><code>simplefilter(action, category=Warning, lineno=0, append=False)</code> - устанавливает простой фильтр для предупреждений с указанным действием и категорией.</p>
<pre><code class="language-python">import warnings

warnings.simplefilter(&quot;ignore&quot;, DeprecationWarning)
</code></pre>
<p><code>resetwarnings()</code> - сбрасывает все установленные фильтры предупреждений.</p>
<pre><code class="language-python">import warnings

warnings.resetwarnings()
</code></pre>
<p><code>showwarning(message, category, filename, lineno, file=None, line=None)</code> - выводит предупреждение с указанными параметрами.</p>
<pre><code class="language-python">import warnings

warnings.showwarning(&quot;This is a warning message&quot;, UserWarning, &quot;example.py&quot;, 10)
</code></pre>
<p><code>catch_warnings(*, record=False, module=None)</code> - контекстный менеджер для временного перехвата предупреждений.</p>
<pre><code class="language-python">import warnings

with warnings.catch_warnings(record=True) as w:
    warnings.warn(&quot;This is a warning message&quot;)
    print(w[0].message)
</code></pre>