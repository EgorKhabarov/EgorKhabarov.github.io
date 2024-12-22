<h1>locals()</h1>
<table>
<thead>
<tr>
<th>Переменная</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>__annotations__</code></td>
<td>Словарь, содержащий аннотации типов, заданные в модуле<br><code>def func(a: int, b: str) -&gt; bool: pass</code><br><code>print(func.__annotations__)  # {'a': &lt;class 'int'&gt;, 'b': &lt;class 'str'&gt;, 'return': &lt;class 'bool'&gt;}</code></td>
</tr>
<tr>
<td><code>__builtins__</code></td>
<td>Ссылка на встроенные объекты Python, такие как функции (<code>len</code>, <code>print</code>) и исключения (<code>ValueError</code>)</td>
</tr>
<tr>
<td><code>__cached__</code></td>
<td>Указывает путь к закэшированному файлу <code>.pyc</code>, созданному для текущего модуля</td>
</tr>
<tr>
<td><code>__doc__</code></td>
<td>Строка документации текущего модуля. Если документации нет, то значение будет <code>None</code></td>
</tr>
<tr>
<td><code>__file__</code></td>
<td>Путь к файлу, из которого был загружен текущий модуль</td>
</tr>
<tr>
<td><code>__loader__</code></td>
<td>Объект, ответственный за загрузку текущего модуля</td>
</tr>
<tr>
<td><code>__name__</code></td>
<td>Имя текущего модуля. Для основного исполняемого скрипта значение будет <code>'__main__'</code></td>
</tr>
<tr>
<td><code>__package__</code></td>
<td>Имя пакета, в котором находится модуль. Если модуль находится на верхнем уровне, то значение будет <code>None</code></td>
</tr>
<tr>
<td><code>__spec__</code></td>
<td>Спецификация загрузки модуля. Это объект, содержащий информацию о модуле, такой как его путь, имя и пакет</td>
</tr>
</tbody>
</table>
<h1>object</h1>
<table>
<thead>
<tr>
<th>Атрибут</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>__code__</code></td>
<td>Содержит объект типа <code>code</code>, представляющий байт-код функции.<br>Можно использовать для анализа и изменения</td>
<td><code>func.__code__.co_varnames</code></td>
</tr>
<tr>
<td><code>__closure__</code></td>
<td>Кортеж объектов <code>cell</code>, хранящих значения переменных,<br>захваченных замыканием (если функция использует замыкания)</td>
<td><code>func.__closure__[0].cell_contents</code></td>
</tr>
<tr>
<td><code>__module__</code></td>
<td>Имя модуля, в котором определена функция.<br>Полезно для понимания контекста определения функции</td>
<td><code>func.__module__</code></td>
</tr>
<tr>
<td><code>__annotations__</code></td>
<td>Словарь с аннотациями типов для аргументов функции и возвращаемого значения</td>
<td><code>func.__annotations__</code></td>
</tr>
<tr>
<td><code>__globals__</code></td>
<td>Словарь глобальных переменных, доступных функции.<br>Позволяет доступ к глобальному пространству имен.<br>Если функция func была определена в модуле module,<br>то <code>func.__globals__</code> будет ссылаться<br>на глобальный символический словарь этого модуля</td>
<td><code>func.__globals__["variable_name"]</code></td>
</tr>
<tr>
<td><code>__defaults__</code></td>
<td>Кортеж значений по умолчанию для позиционных<br>и именованных аргументов функции (если они определены)</td>
<td><code>func.__defaults__</code></td>
</tr>
<tr>
<td><code>__kwdefaults__</code></td>
<td>Словарь значений по умолчанию для только ключевых аргументов функции (если они определены)</td>
<td><code>func.__kwdefaults__</code></td>
</tr>
<tr>
<td><code>__qualname__</code></td>
<td>Полное имя функции, включая контексты, такие как класс или модуль, в котором она определена</td>
<td><code>func.__qualname__</code></td>
</tr>
</tbody>
</table>
<h2>&#x5f;&#x5f;code&#x5f;&#x5f;</h2>
<table>
<thead>
<tr>
<th>Атрибут</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>co_argcount</code></td>
<td>Количество аргументов, принимаемых функцией (без <code>*args</code> и <code>**kwargs</code>)</td>
<td><code>func.__code__.co_argcount</code></td>
</tr>
<tr>
<td><code>co_cellvars</code></td>
<td>Кортеж с именами переменных, которые являются локальными, но используются в замыканиях</td>
<td><code>func.__code__.co_cellvars</code></td>
</tr>
<tr>
<td><code>co_code</code></td>
<td>Сырые байт-коды, представляющие тело функции</td>
<td><code>func.__code__.co_code</code></td>
</tr>
<tr>
<td><code>co_consts</code></td>
<td>Кортеж с константами, используемыми в функции (например, числа, строки)</td>
<td><code>func.__code__.co_consts</code></td>
</tr>
<tr>
<td><code>co_exceptiontable</code></td>
<td>Таблица, описывающая обработку исключений в байт-коде.<br>Содержит информацию о try/except блоках и местах, где нужно ловить исключения</td>
<td><code>func.__code__.co_exceptiontable</code></td>
</tr>
<tr>
<td><code>co_filename</code></td>
<td>Имя файла, в котором определена функция</td>
<td><code>func.__code__.co_filename</code></td>
</tr>
<tr>
<td><code>co_firstlineno</code></td>
<td>Номер первой строки, содержащей исходный код функции</td>
<td><code>func.__code__.co_firstlineno</code></td>
</tr>
<tr>
<td><code>co_flags</code></td>
<td>Флаги, описывающие состояние функции (например, использование генераторов)<br>Этот атрибут — битовая маска, содержащая информацию о функции, например,<br>используется ли функция как генератор, имеет ли она <code>*args</code> или <code>**kwargs</code> и т.д<br>Например, <code>0x20</code> указывает, что функция — генератор</td>
<td><code>func.__code__.co_flags</code></td>
</tr>
<tr>
<td><code>co_freevars</code></td>
<td>Кортеж с именами переменных, которые используются в функции,<br>но не являются локальными (замыкания)</td>
<td><code>func.__code__.co_freevars</code></td>
</tr>
<tr>
<td><code>co_kwonlyargcount</code></td>
<td>Количество ключевых-only аргументов</td>
<td><code>func.__code__.co_kwonlyargcount</code></td>
</tr>
<tr>
<td><code>co_lines</code></td>
<td>Итератор, который возвращает пары <code>(начало строки, конец строки)</code><br>для каждого блока байт-кода, позволяя точно определить,<br>какая часть кода соответствует определенным строкам исходного кода</td>
<td><code>list(func.__code__.co_lines())</code></td>
</tr>
<tr>
<td><code>co_linetable</code></td>
<td>Байт-код таблицы, содержащей информацию о соответствии номеров строк исходному коду<br>(используется в интерпретаторе Python для трассировки)</td>
<td><code>func.__code__.co_linetable</code></td>
</tr>
<tr>
<td><code>co_lnotab</code></td>
<td>Содержит информацию для отображения байт-кодов в номера строк исходного кода</td>
<td><code>func.__code__.co_lnotab</code></td>
</tr>
<tr>
<td><code>co_name</code></td>
<td>Имя функции</td>
<td><code>func.__code__.co_name</code></td>
</tr>
<tr>
<td><code>co_names</code></td>
<td>Кортеж с именами всех объектов (функций, классов, переменных), используемых в функции</td>
<td><code>func.__code__.co_names</code></td>
</tr>
<tr>
<td><code>co_nlocals</code></td>
<td>Количество локальных переменных, используемых в функции</td>
<td><code>func.__code__.co_nlocals</code></td>
</tr>
<tr>
<td><code>co_positions</code></td>
<td>Итератор, возвращающий позиции в коде: <code>(start_line, start_col, end_line, end_col)</code><br>для каждого выражения или инструкции в функции.<br>Это позволяет точно определить позиции в исходном коде</td>
<td><code>list(func.__code__.co_positions())</code></td>
</tr>
<tr>
<td><code>co_posonlyargcount</code></td>
<td>Количество позиционных-only аргументов</td>
<td><code>func.__code__.co_posonlyargcount</code></td>
</tr>
<tr>
<td><code>co_qualname</code></td>
<td>Полное имя функции, включая контексты, такие как класс или модуль.<br>Полезно для определения квалифицированного имени метода класса или вложенной функции</td>
<td><code>func.__code__.co_qualname</code></td>
</tr>
<tr>
<td><code>co_stacksize</code></td>
<td>Размер стека, необходимый для выполнения функции</td>
<td><code>func.__code__.co_stacksize</code></td>
</tr>
<tr>
<td><code>co_varnames</code></td>
<td>Кортеж с именами всех локальных переменных, включая аргументы функции</td>
<td><code>func.__code__.co_varnames</code></td>
</tr>
<tr>
<td><code>replace</code></td>
<td>Позволяет создать новый объект code, заменив выбранные атрибуты</td>
<td><code>func.__code__.replace(**kwargs)</code></td>
</tr>
</tbody>
</table>
<h1>Примеры использования</h1>
<h3>Получение количества аргументов функции</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">example_func</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="n">c</span><span class="o">=</span><span class="mi">10</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span> <span class="o">+</span> <span class="n">c</span>

<span class="nb">print</span><span class="p">(</span><span class="n">example_func</span><span class="o">.</span><span class="vm">__code__</span><span class="o">.</span><span class="n">co_argcount</span><span class="p">)</span>  <span class="c1"># 2</span>
</pre></div></div></div>

<h3>Извлечение имен аргументов и локальных переменных</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">example_func</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
    <span class="n">z</span> <span class="o">=</span> <span class="n">x</span> <span class="o">+</span> <span class="n">y</span>
    <span class="k">return</span> <span class="n">z</span>

<span class="nb">print</span><span class="p">(</span><span class="n">example_func</span><span class="o">.</span><span class="vm">__code__</span><span class="o">.</span><span class="n">co_varnames</span><span class="p">)</span>  <span class="c1"># (&quot;x&quot;, &quot;y&quot;, &quot;z&quot;)</span>
</pre></div></div></div>

<h3>Получение имени файла и строки, где определена функция</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">example_func</span><span class="p">():</span>
    <span class="k">pass</span>

<span class="nb">print</span><span class="p">(</span><span class="n">example_func</span><span class="o">.</span><span class="vm">__code__</span><span class="o">.</span><span class="n">co_filename</span><span class="p">)</span>     <span class="c1"># Имя файла, в котором определена функция</span>
<span class="nb">print</span><span class="p">(</span><span class="n">example_func</span><span class="o">.</span><span class="vm">__code__</span><span class="o">.</span><span class="n">co_firstlineno</span><span class="p">)</span>  <span class="c1"># Номер первой строки</span>
</pre></div></div></div>

<h3>Работа с байт-кодом</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">example_func</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span>

<span class="nb">print</span><span class="p">(</span><span class="n">example_func</span><span class="o">.</span><span class="vm">__code__</span><span class="o">.</span><span class="n">co_code</span><span class="p">)</span>  <span class="c1"># Сырые байт-коды</span>
</pre></div></div></div>

<h3>Константы, используемые в функции</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">example_func</span><span class="p">():</span>
    <span class="n">x</span> <span class="o">=</span> <span class="mi">42</span>
    <span class="k">return</span> <span class="n">x</span>

<span class="nb">print</span><span class="p">(</span><span class="n">example_func</span><span class="o">.</span><span class="vm">__code__</span><span class="o">.</span><span class="n">co_consts</span><span class="p">)</span>  <span class="c1"># (None, 42)</span>
</pre></div></div></div>

<h3>Проверка использования замыканий</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">outer_func</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">inner_func</span><span class="p">(</span><span class="n">y</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span class="n">y</span>
    <span class="k">return</span> <span class="n">inner_func</span>

<span class="n">closure_func</span> <span class="o">=</span> <span class="n">outer_func</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">closure_func</span><span class="o">.</span><span class="vm">__code__</span><span class="o">.</span><span class="n">co_freevars</span><span class="p">)</span>  <span class="c1"># (&quot;x&quot;,)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">closure_func</span><span class="o">.</span><span class="vm">__code__</span><span class="o">.</span><span class="n">co_cellvars</span><span class="p">)</span>  <span class="c1"># ()</span>
</pre></div></div></div>