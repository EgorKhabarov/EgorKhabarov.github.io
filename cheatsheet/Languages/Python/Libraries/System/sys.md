<p>Этот модуль предоставляет доступ к некоторым объектам, используемым или поддерживаемым
интерпретатором, и к функциям, которые тесно взаимодействуют с интерпретатором.</p>
<h1>Динамические объекты</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>argv</code></td>
<td>Аргументы командной строки<br><code>argv[0]</code> — путь к скрипту, если он известен</td>
</tr>
<tr>
<td><code>path</code></td>
<td>Путь поиска модуля<br><code>path[0]</code> — каталог скрипта, иначе <code>""</code></td>
</tr>
<tr>
<td><code>modules</code></td>
<td>Словарь загруженных модулей</td>
</tr>
<tr>
<td><code>displayhook</code></td>
<td>Вызывается для отображения результатов в интерактивном сеансе</td>
</tr>
<tr>
<td><code>excepthook</code></td>
<td>Вызывается для обработки любого неперехваченного исключения, отличного от <code>SystemExit</code><br>Чтобы настроить печать в интерактивном сеансе или установить пользовательский<br>обработчик исключений верхнего уровня, назначьте другие функции для замены этих</td>
</tr>
<tr>
<td><code>stdin</code></td>
<td>Стандартный объект входного файла<br><code>input()</code></td>
</tr>
<tr>
<td><code>stdout</code></td>
<td>Стандартный объект выходного файла<br><code>print()</code></td>
</tr>
<tr>
<td><code>stderr</code></td>
<td>Стандартный объект ошибки; используется для сообщений об ошибках<br>Назначая им другие объекты файлов (или объекты, которые ведут себя как файлы),<br>можно перенаправить весь ввод-вывод интерпретатора</td>
</tr>
<tr>
<td><code>last_type</code></td>
<td>Тип последнего неперехваченного исключения</td>
</tr>
<tr>
<td><code>last_value</code></td>
<td>Значение последнего неперехваченного исключения</td>
</tr>
<tr>
<td><code>last_traceback</code></td>
<td>Трассировка последнего неперехваченного исключения<br>Эти три доступны только в интерактивном сеансе после того, как<br>трассировка была напечатана</td>
</tr>
</tbody>
</table>
<h1>Статические объекты</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>builtin_module_names</code></td>
<td>Кортеж имен модулей, встроенных в этот интерпретатор</td>
</tr>
<tr>
<td><code>copyright</code></td>
<td>Уведомление об авторских правах, относящееся к этому интерпретатору</td>
</tr>
<tr>
<td><code>exec_prefix</code></td>
<td>Префикс, используемый для поиска машинно-специфической библиотеки Python</td>
</tr>
<tr>
<td><code>executable</code></td>
<td>Абсолютный путь к исполняемому двоичному файлу интерпретатора Python</td>
</tr>
<tr>
<td><code>float_info</code></td>
<td>Именованный кортеж с информацией о реализации <code>float</code></td>
</tr>
<tr>
<td><code>float_repr_style</code></td>
<td>Строка, указывающая стиль вывода <code>repr()</code> для <code>float</code></td>
</tr>
<tr>
<td><code>hash_info</code></td>
<td>Именованный кортеж с информацией о хеш-алгоритме</td>
</tr>
<tr>
<td><code>hexversion</code></td>
<td>Информация о версии, закодированная как одно целое число</td>
</tr>
<tr>
<td><code>implementation</code></td>
<td>Информация о реализации Python</td>
</tr>
<tr>
<td><code>int_info</code></td>
<td>Именованный кортеж с информацией о реализации <code>int</code></td>
</tr>
<tr>
<td><code>maxsize</code></td>
<td>Наибольшая поддерживаемая длина контейнеров</td>
</tr>
<tr>
<td><code>maxunicode</code></td>
<td>Значение наибольшей кодовой точки <code>Unicode</code></td>
</tr>
<tr>
<td><code>platform</code></td>
<td>Идентификатор платформы</td>
</tr>
<tr>
<td><code>prefix</code></td>
<td>Префикс, используемый для поиска библиотеки Python</td>
</tr>
<tr>
<td><code>thread_info</code></td>
<td>Именованный кортеж с информацией о реализации потока</td>
</tr>
<tr>
<td><code>version</code></td>
<td>Версия этого интерпретатора в виде строки</td>
</tr>
<tr>
<td><code>version_info</code></td>
<td>Информация о версии в виде именованного кортежа</td>
</tr>
<tr>
<td><code>dllhandle</code></td>
<td><strong>[только для Windows]</strong> целочисленный дескриптор библиотеки <code>DLL Python</code></td>
</tr>
<tr>
<td><code>winver</code></td>
<td><strong>[только для Windows]</strong> номер версии библиотеки <code>DLL Python</code></td>
</tr>
<tr>
<td><code>_enablelegacywindowsfsencoding</code></td>
<td><strong>[только для Windows]</strong></td>
</tr>
<tr>
<td><code>__stdin__</code></td>
<td>Исходный <code>stdin</code><br><strong>не трогать!</strong></td>
</tr>
<tr>
<td><code>__stdout__</code></td>
<td>Исходный <code>stdout</code><br><strong>не трогать!</strong></td>
</tr>
<tr>
<td><code>__stderr__</code></td>
<td>Исходный <code>stderr</code><br><strong>не трогать!</strong></td>
</tr>
<tr>
<td><code>__displayhook__</code></td>
<td>Исходный <code>displayhook</code><br><strong>не трогать!</strong></td>
</tr>
<tr>
<td><code>__excepthook__</code></td>
<td>Исходный <code>excepthook</code><br><strong>не трогать!</strong></td>
</tr>
</tbody>
</table>
<h1>Функции</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>displayhook()</code></td>
<td>Вывести объект на экран и сохранить его в <code>builtins._</code></td>
</tr>
<tr>
<td><code>excepthook()</code></td>
<td>Вывести исключение и его трассировку в <code>sys.stderr</code></td>
</tr>
<tr>
<td><code>exception()</code></td>
<td>Вернуть активное исключение текущего потока</td>
</tr>
<tr>
<td><code>exc_info()</code></td>
<td>Вернуть информацию об активном исключении текущего потока</td>
</tr>
<tr>
<td><code>exit()</code></td>
<td>Выйти из интерпретатора, вызвав <code>SystemExit</code></td>
</tr>
<tr>
<td><code>getdlopenflags()</code></td>
<td>Вернуть флаги, которые будут использоваться для вызовов <code>dlopen()</code></td>
</tr>
<tr>
<td><code>getprofile()</code></td>
<td>Получить глобальную функцию профилирования</td>
</tr>
<tr>
<td><code>getrefcount()</code></td>
<td>Вернуть счетчик ссылок для объекта (плюс один :-)</td>
</tr>
<tr>
<td><code>getrecursionlimit()</code></td>
<td>Вернуть максимальную глубину рекурсии для интерпретатора</td>
</tr>
<tr>
<td><code>getsizeof()</code></td>
<td>Вернуть размер объекта в байтах</td>
</tr>
<tr>
<td><code>gettrace()</code></td>
<td>Получить глобальную функцию трассировки отладки</td>
</tr>
<tr>
<td><code>setdlopenflags()</code></td>
<td>Установить флаги, которые будут использоваться для вызовов <code>dlopen()</code></td>
</tr>
<tr>
<td><code>setprofile()</code></td>
<td>Установить глобальную функцию профилирования</td>
</tr>
<tr>
<td><code>setrecursionlimit()</code></td>
<td>Установить макс. глубина рекурсии для интерпретатора</td>
</tr>
<tr>
<td><code>settrace()</code></td>
<td>Установить глобальную функцию трассировки отладки</td>
</tr>
</tbody>
</table>
<h2>Примеры</h2>
<h3>argv</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="c1"># Передаем два аргумента при запуске скрипта</span>
<span class="c1"># python myscript.py arg1 arg2</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>  <span class="c1"># myscript.py</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>  <span class="c1"># arg1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>  <span class="c1"># arg2</span>
</pre></div></div></div>

<h3>stdin, stdout, stderr</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="c1"># Читаем данные из стандартного потока ввода</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span>

<span class="c1"># Пишем данные в стандартный поток вывода</span>
<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;Hello, world!</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="c1"># Пишем ошибки в стандартный поток ошибок</span>
<span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;Error occurred</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>platform</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;win32&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Windows&quot;</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;linux&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Linux&quot;</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;darwin&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;MacOS&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>getsizeof</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getsizeof</span><span class="p">(</span><span class="n">a</span><span class="p">))</span>  <span class="c1"># 88 размер объекта в байтах</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">path</span><span class="p">)</span>
<span class="p">[</span>
    <span class="s2">&quot;&quot;</span><span class="p">,</span>
    <span class="s2">&quot;C:/Users/User/AppData/Local/Programs/Python/Python311/python311.zip&quot;</span><span class="p">,</span>
    <span class="s2">&quot;C:/Users/User/AppData/Local/Programs/Python/Python311/DLLs&quot;</span><span class="p">,</span>
    <span class="s2">&quot;C:/Users/User/AppData/Local/Programs/Python/Python311/Lib&quot;</span><span class="p">,</span>
    <span class="s2">&quot;C:/Users/User/AppData/Local/Programs/Python/Python311&quot;</span><span class="p">,</span>
    <span class="s2">&quot;C:/Users/User/AppData/Local/Programs/Python/Python311/Lib/site-packages&quot;</span>
<span class="p">]</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="k">def</span> <span class="nf">divide</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">x</span> <span class="o">/</span> <span class="n">y</span>
    <span class="k">except</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">())</span>

<span class="n">divide</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
<span class="c1"># (&lt;class &quot;ZeroDivisionError&quot;&gt;, ZeroDivisionError(&quot;division by zero&quot;), &lt;traceback object&gt;)</span>
</pre></div></div></div>