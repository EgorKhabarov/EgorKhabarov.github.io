<h1>inspect</h1>
<ul>
<li>Проверка типов объектов <code>ismodule()</code>, <code>isclass()</code>, <code>ismethod()</code>, <code>isfunction()</code>, <code>isgeneratorfunction()</code>,
<code>isgenerator()</code>, <code>istraceback()</code>, <code>isframe()</code>, <code>iscode()</code>, <code>isbuiltin()</code>, <code>isroutine()</code></li>
<li>Получение членов объекта, удовлетворяющих заданному условию - <code>getmembers()</code>
<br></li>
<li>Поиск исходного кода объекта - <code>getfile()</code>, <code>getsourcefile()</code>, <code>getsource()</code></li>
<li>Получение документации по объекту - <code>getdoc()</code>, <code>getcomments()</code></li>
<li>Определение модуля, из которого поступил объект - <code>getmodule()</code></li>
<li>Упорядочивание классов таким образом, чтобы они представляли их иерархию - <code>getclasstree()</code>
<br></li>
<li>Получение информации об аргументах функции - <code>getargvalues()</code>, <code>getcallargs()</code></li>
<li>То же самое, с поддержкой функций Python 3 - <code>getfullargspec()</code></li>
<li>Форматирование спецификации аргумента - <code>formatargvalues()</code></li>
<li>Получение информации о кадрах - <code>getouterframes()</code>, <code>getinnerframes()</code></li>
<li>Получение текущего кадра стека - <code>currentframe()</code></li>
<li>Получение информации о кадрах в стеке или в трассировке - <code>stack()</code>, <code>trace()</code>
<br></li>
<li>Получить объект Signature для вызываемого - <code>signature()</code>
<br></li>
<li>Безопасно вычислить аннотации объекта - <code>get_annotations()</code></li>
</ul>
<h1>__all__</h1>
<table>
<thead>
<tr>
<th><strong>Название</strong></th>
<th><strong>Описание</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ArgInfo</code></td>
<td>Класс, представляющий информацию об аргументах функции</td>
</tr>
<tr>
<td><code>Arguments</code></td>
<td>Класс, описывающий аргументы функции, включая позиционные, ключевые и их значения по умолчанию</td>
</tr>
<tr>
<td><code>Attribute</code></td>
<td>Класс для описания атрибутов объекта, используемый внутри библиотеки <code>inspect</code></td>
</tr>
<tr>
<td><code>BlockFinder</code></td>
<td>Внутренний класс для поиска блоков кода в исходном файле</td>
</tr>
<tr>
<td><code>BoundArguments</code></td>
<td>Класс, представляющий привязанные аргументы функции после вызова</td>
</tr>
<tr>
<td><code>CORO_CLOSED</code></td>
<td>Константа, указывающая, что корутина закрыта</td>
</tr>
<tr>
<td><code>CORO_CREATED</code></td>
<td>Константа, указывающая, что корутина создана, но еще не запущена</td>
</tr>
<tr>
<td><code>CORO_RUNNING</code></td>
<td>Константа, указывающая, что корутина в процессе выполнения</td>
</tr>
<tr>
<td><code>CORO_SUSPENDED</code></td>
<td>Константа, указывающая, что корутина приостановлена</td>
</tr>
<tr>
<td><code>CO_ASYNC_GENERATOR</code></td>
<td>Флаг состояния объекта кода, указывающий, что это асинхронный генератор</td>
</tr>
<tr>
<td><code>CO_COROUTINE</code></td>
<td>Флаг состояния объекта кода, указывающий, что это корутина</td>
</tr>
<tr>
<td><code>CO_GENERATOR</code></td>
<td>Флаг состояния объекта кода, указывающий, что это генератор</td>
</tr>
<tr>
<td><code>CO_ITERABLE_COROUTINE</code></td>
<td>Флаг состояния объекта кода, указывающий, что это итерируемая корутина</td>
</tr>
<tr>
<td><code>CO_NESTED</code></td>
<td>Флаг состояния объекта кода, указывающий, что функция является вложенной</td>
</tr>
<tr>
<td><code>CO_NEWLOCALS</code></td>
<td>Флаг состояния объекта кода, указывающий, что функция использует новые локальные переменные</td>
</tr>
<tr>
<td><code>CO_NOFREE</code></td>
<td>Флаг состояния объекта кода, указывающий, что функция не использует свободные переменные</td>
</tr>
<tr>
<td><code>CO_OPTIMIZED</code></td>
<td>Флаг состояния объекта кода, указывающий, что функция оптимизирована</td>
</tr>
<tr>
<td><code>CO_VARARGS</code></td>
<td>Флаг состояния объекта кода, указывающий,<br>что функция принимает произвольное количество позиционных аргументов (*args)</td>
</tr>
<tr>
<td><code>CO_VARKEYWORDS</code></td>
<td>Флаг состояния объекта кода, указывающий,<br>что функция принимает произвольное количество именованных аргументов (**kwargs)</td>
</tr>
<tr>
<td><code>ClassFoundException</code></td>
<td>Исключение, возникающее при поиске класса в дереве наследования</td>
</tr>
<tr>
<td><code>ClosureVars</code></td>
<td>Класс, представляющий закрытые переменные функции (closure variables)</td>
</tr>
<tr>
<td><code>EndOfBlock</code></td>
<td>Класс, обозначающий конец блока кода при анализе исходного файла</td>
</tr>
<tr>
<td><code>FrameInfo</code></td>
<td>Класс, представляющий информацию о фрейме стека вызовов (файл, строка, функция и т.д.)</td>
</tr>
<tr>
<td><code>FullArgSpec</code></td>
<td>Класс, представляющий полную спецификацию аргументов функции,<br>включая позиционные, ключевые, аргументы с дефолтными значениями и т.д</td>
</tr>
<tr>
<td><code>GEN_CLOSED</code></td>
<td>Константа, указывающая, что генератор закрыт</td>
</tr>
<tr>
<td><code>GEN_CREATED</code></td>
<td>Константа, указывающая, что генератор создан, но еще не запущен</td>
</tr>
<tr>
<td><code>GEN_RUNNING</code></td>
<td>Константа, указывающая, что генератор в процессе выполнения</td>
</tr>
<tr>
<td><code>GEN_SUSPENDED</code></td>
<td>Константа, указывающая, что генератор приостановлен</td>
</tr>
<tr>
<td><code>Parameter</code></td>
<td>Класс, представляющий отдельный параметр функции, включая его имя, тип и значение по умолчанию</td>
</tr>
<tr>
<td><code>Signature</code></td>
<td>Класс, представляющий сигнатуру функции, включая параметры и возвращаемое значение</td>
</tr>
<tr>
<td><code>TPFLAGS_IS_ABSTRACT</code></td>
<td>Константа флага, указывающая, что класс является абстрактным</td>
</tr>
<tr>
<td><code>Traceback</code></td>
<td>Класс, представляющий трассировку исключения (стек вызовов) в момент возникновения исключения</td>
</tr>
<tr>
<td><code>classify_class_attrs</code></td>
<td>Функция для классификации атрибутов класса на методы, поля и т.д</td>
</tr>
<tr>
<td><code>cleandoc</code></td>
<td>Функция для очистки строковой документации от лишних отступов и пустых строк</td>
</tr>
<tr>
<td><code>currentframe</code></td>
<td>Функция, возвращающая текущий фрейм стека вызовов</td>
</tr>
<tr>
<td><code>findsource</code></td>
<td>Функция для поиска исходного кода объекта (функции, класса и т.д.)</td>
</tr>
<tr>
<td><code>formatannotation</code></td>
<td>Функция для форматирования аннотаций типов</td>
</tr>
<tr>
<td><code>formatannotationrelativeto</code></td>
<td>Функция для форматирования аннотаций типов относительно указанного модуля</td>
</tr>
<tr>
<td><code>formatargvalues</code></td>
<td>Функция для форматирования значений аргументов функции</td>
</tr>
<tr>
<td><code>get_annotations</code></td>
<td>Функция для получения аннотаций типов объекта</td>
</tr>
<tr>
<td><code>getabsfile</code></td>
<td>Функция для получения абсолютного пути к файлу, в котором определен объект</td>
</tr>
<tr>
<td><code>getargs</code></td>
<td>Устаревшая функция для получения имен аргументов функции (используйте <code>getfullargspec</code> или <code>signature</code>)</td>
</tr>
<tr>
<td><code>getargvalues</code></td>
<td>Функция для получения значений аргументов в текущем фрейме</td>
</tr>
<tr>
<td><code>getattr_static</code></td>
<td>Функция для статического получения атрибута объекта без вызова<br><code>__getattr__</code> и других динамических механизмов доступа к атрибутам</td>
</tr>
<tr>
<td><code>getblock</code></td>
<td>Внутренняя функция для получения блока кода из исходного файла</td>
</tr>
<tr>
<td><code>getcallargs</code></td>
<td>Функция для получения соответствия между аргументами<br>и параметрами функции при вызове с конкретными аргументами</td>
</tr>
<tr>
<td><code>getclasstree</code></td>
<td>Функция для построения дерева наследования классов</td>
</tr>
<tr>
<td><code>getclosurevars</code></td>
<td>Функция для получения закрытых переменных функции (closure)</td>
</tr>
<tr>
<td><code>getcomments</code></td>
<td>Функция для получения комментариев,<br>предшествующих определению объекта (функции, класса и т.д.)</td>
</tr>
<tr>
<td><code>getcoroutinelocals</code></td>
<td>Функция для получения локальных переменных корутины</td>
</tr>
<tr>
<td><code>getcoroutinestate</code></td>
<td>Функция для получения текущего состояния корутины</td>
</tr>
<tr>
<td><code>getdoc</code></td>
<td>Функция для получения строки документации объекта</td>
</tr>
<tr>
<td><code>getfile</code></td>
<td>Функция для получения имени файла, в котором определен объект</td>
</tr>
<tr>
<td><code>getframeinfo</code></td>
<td>Функция для получения информации о фрейме стека вызовов</td>
</tr>
<tr>
<td><code>getfullargspec</code></td>
<td>Функция для получения полной спецификации аргументов функции</td>
</tr>
<tr>
<td><code>getgeneratorlocals</code></td>
<td>Функция для получения локальных переменных генератора</td>
</tr>
<tr>
<td><code>getgeneratorstate</code></td>
<td>Функция для получения текущего состояния генератора</td>
</tr>
<tr>
<td><code>getinnerframes</code></td>
<td>Функция для получения всех внутренних фреймов стека вызовов</td>
</tr>
<tr>
<td><code>getlineno</code></td>
<td>Функция для получения номера строки, где определен объект</td>
</tr>
<tr>
<td><code>getmembers</code></td>
<td>Функция для получения всех членов объекта<br>(атрибутов, методов и т.д.) с возможностью фильтрации</td>
</tr>
<tr>
<td><code>getmembers_static</code></td>
<td>Внутренняя функция для статического получения членов объекта</td>
</tr>
<tr>
<td><code>getmodule</code></td>
<td>Функция для получения модуля, в котором определен объект</td>
</tr>
<tr>
<td><code>getmodulename</code></td>
<td>Функция для получения имени модуля по пути к файлу</td>
</tr>
<tr>
<td><code>getmro</code></td>
<td>Функция для получения метода разрешения порядка (MRO) для класса</td>
</tr>
<tr>
<td><code>getouterframes</code></td>
<td>Функция для получения всех внешних фреймов стека вызовов</td>
</tr>
<tr>
<td><code>getsource</code></td>
<td>Функция для получения исходного кода объекта (функции, класса и т.д.)</td>
</tr>
<tr>
<td><code>getsourcefile</code></td>
<td>Функция для получения исходного файла объекта</td>
</tr>
<tr>
<td><code>getsourcelines</code></td>
<td>Функция для получения исходного кода объекта<br>в виде списка строк и номера начальной строки</td>
</tr>
<tr>
<td><code>indentsize</code></td>
<td>Внутренняя функция для определения размера отступа в исходном коде</td>
</tr>
<tr>
<td><code>isabstract</code></td>
<td>Функция для проверки, является ли класс абстрактным</td>
</tr>
<tr>
<td><code>isasyncgen</code></td>
<td>Функция для проверки, является ли объект асинхронным генератором</td>
</tr>
<tr>
<td><code>isasyncgenfunction</code></td>
<td>Функция для проверки, является ли объект функцией асинхронного генератора</td>
</tr>
<tr>
<td><code>isawaitable</code></td>
<td>Функция для проверки, можно ли ожидать<br>объект (поддерживает <code>__await__</code> или является корутиной)</td>
</tr>
<tr>
<td><code>isbuiltin</code></td>
<td>Функция для проверки, является ли объект встроенной функцией или методом</td>
</tr>
<tr>
<td><code>isclass</code></td>
<td>Функция для проверки, является ли объект классом</td>
</tr>
<tr>
<td><code>iscode</code></td>
<td>Функция для проверки, является ли объект объектом кода (<code>code object</code>)</td>
</tr>
<tr>
<td><code>iscoroutine</code></td>
<td>Функция для проверки, является ли объект корутиной</td>
</tr>
<tr>
<td><code>iscoroutinefunction</code></td>
<td>Функция для проверки, является ли объект функцией корутиной</td>
</tr>
<tr>
<td><code>isdatadescriptor</code></td>
<td>Функция для проверки, является ли объект дескриптором данных</td>
</tr>
<tr>
<td><code>isframe</code></td>
<td>Функция для проверки, является ли объект фреймом стека вызовов</td>
</tr>
<tr>
<td><code>isfunction</code></td>
<td>Функция для проверки, является ли объект функцией</td>
</tr>
<tr>
<td><code>isgenerator</code></td>
<td>Функция для проверки, является ли объект генератором</td>
</tr>
<tr>
<td><code>isgeneratorfunction</code></td>
<td>Функция для проверки, является ли объект функцией генератора</td>
</tr>
<tr>
<td><code>isgetsetdescriptor</code></td>
<td>Функция для проверки, является ли объект дескриптором getset</td>
</tr>
<tr>
<td><code>ismemberdescriptor</code></td>
<td>Функция для проверки, является ли объект дескриптором члена класса</td>
</tr>
<tr>
<td><code>ismethod</code></td>
<td>Функция для проверки, является ли объект методом</td>
</tr>
<tr>
<td><code>ismethoddescriptor</code></td>
<td>Функция для проверки, является ли объект дескриптором метода</td>
</tr>
<tr>
<td><code>ismethodwrapper</code></td>
<td>Функция для проверки, является ли объект оберткой метода</td>
</tr>
<tr>
<td><code>ismodule</code></td>
<td>Функция для проверки, является ли объект модулем</td>
</tr>
<tr>
<td><code>isroutine</code></td>
<td>Функция для проверки, является ли объект вызываемой рутиной (функцией или методом)</td>
</tr>
<tr>
<td><code>istraceback</code></td>
<td>Функция для проверки, является ли объект трассировкой исключения (<code>traceback object</code>)</td>
</tr>
<tr>
<td><code>signature</code></td>
<td>Функция для получения сигнатуры функции или метода</td>
</tr>
<tr>
<td><code>stack</code></td>
<td>Функция для получения текущего стека вызовов в виде списка <code>FrameInfo</code></td>
</tr>
<tr>
<td><code>trace</code></td>
<td>Функция для трассировки выполнения кода,<br>вызывающая заданную функцию для каждого фрейма стека</td>
</tr>
<tr>
<td><code>unwrap</code></td>
<td>Функция для получения оригинальной функции, удаляя все декораторы</td>
</tr>
<tr>
<td><code>walktree</code></td>
<td>Внутренняя функция для обхода дерева наследования классов</td>
</tr>
</tbody>
</table>
<h4>Примечание</h4>
<ul>
<li><strong>Константы состояния корутин и генераторов</strong> (<code>CORO_*</code>, <code>GEN_*</code>, <code>CO_*</code>)
используются для определения текущего состояния корутин и генераторов.</li>
<li><strong>Внутренние классы и функции</strong> (например, <code>BlockFinder</code>, <code>walktree</code>)
обычно используются внутри библиотеки <code>inspect</code>
и не предназначены для прямого использования пользователями.</li>
<li><strong>Функции для работы с аргументами и сигнатурами</strong> (<code>getfullargspec</code>, <code>signature</code>, <code>getcallargs</code>)
позволяют детально анализировать параметры функций и методы их вызова.</li>
<li><strong>Функции проверки типов объектов</strong> (<code>isclass</code>, <code>isfunction</code>, <code>ismethod</code> и т.д.)
полезны для динамического анализа объектов во время выполнения программы.</li>
<li><strong>Функции для получения исходного кода и документации</strong> (<code>getsource</code>, <code>getdoc</code>, <code>findsource</code>)
позволяют извлекать информацию о коде для целей отладки или генерации документации.</li>
<li><strong>Функции работы со стеком вызовов</strong> (<code>currentframe</code>, <code>stack</code>, <code>getframeinfo</code>)
полезны для отладки и анализа выполнения программы.</li>
</ul>
<h1>Примеры</h1>
<p><code>import inspect</code></p>
<h3>getmembers</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
  <span class="k">def</span> <span class="nf">method1</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      <span class="k">pass</span>

  <span class="k">def</span> <span class="nf">method2</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      <span class="k">pass</span>

<span class="n">inspect</span><span class="o">.</span><span class="n">getmembers</span><span class="p">(</span><span class="n">MyClass</span><span class="p">,</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">)</span>
<span class="c1"># [(&quot;method1&quot;, &lt;function MyClass.method1&gt;), (&quot;method2&quot;, &lt;function MyClass.method2&gt;)]</span>
</pre></div></div></div>

<h3>signature</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">my_function</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
  <span class="k">pass</span>

<span class="n">sig</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">signature</span><span class="p">(</span><span class="n">my_function</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sig</span><span class="p">)</span>  <span class="c1"># &lt;Signature (a, b=10, *args, **kwargs)&gt;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sig</span><span class="o">.</span><span class="n">parameters</span><span class="p">)</span>
<span class="c1"># mappingproxy(OrderedDict([</span>
<span class="c1">#     (&quot;a&quot;, &lt;Parameter &quot;a&quot;&gt;),</span>
<span class="c1">#     (&quot;b&quot;, &lt;Parameter &quot;b=10&quot;&gt;),</span>
<span class="c1">#     (&quot;args&quot;, &lt;Parameter &quot;*args&quot;&gt;),</span>
<span class="c1">#     (&quot;kwargs&quot;, &lt;Parameter &quot;**kwargs&quot;&gt;)</span>
<span class="c1"># ]))</span>
</pre></div></div></div>

<h3>stack</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">function_a</span><span class="p">():</span>
    <span class="n">function_b</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">function_b</span><span class="p">():</span>
    <span class="n">stack</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">stack</span><span class="p">()</span>  <span class="c1"># Получение информации о стеке</span>
    <span class="k">for</span> <span class="n">frame</span> <span class="ow">in</span> <span class="n">stack</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Function </span><span class="si">{</span><span class="n">frame</span><span class="o">.</span><span class="n">function</span><span class="si">}</span><span class="s2"> at line </span><span class="si">{</span><span class="n">frame</span><span class="o">.</span><span class="n">lineno</span><span class="si">}</span><span class="s2"> in </span><span class="si">{</span><span class="n">frame</span><span class="o">.</span><span class="n">filename</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="n">function_a</span><span class="p">()</span>
</pre></div></div></div>

<h3>currentframe</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">frame</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">()</span>  <span class="c1"># Получение текущего фрейма</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Current frame at line </span><span class="si">{</span><span class="n">frame</span><span class="o">.</span><span class="n">f_lineno</span><span class="si">}</span><span class="s2"> in </span><span class="si">{</span><span class="n">frame</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_filename</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h1>Полезные ссылки</h1>
<ul>
<li><a href="https://docs.python.org/3/library/inspect.html">Официальная документация</a></li>
<li><a href="https://www.python.org/dev/peps/pep-0362/">PEP 362 - Подписи вызовов</a></li>
<li><a href="https://realpython.com/python-inspect-module/">Real Python - Inspect Module</a></li>
</ul>