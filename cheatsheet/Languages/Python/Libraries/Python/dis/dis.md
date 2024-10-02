<p>Библиотека <code>dis</code> в Python предоставляет функции для дизассемблирования байт-кода
Она используется для анализа низкоуровневого байт-кода Python
и может быть полезна для отладки, оптимизации производительности и исследования внутренней работы интерпретатора</p>
<p>Вот шпаргалка по библиотеке <strong><code>dis</code></strong>, включающая ключевые функции и классы</p>
<h3>Основные функции <code>dis</code></h3>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>dis.dis(obj)</code></td>
<td>Дизассемблирует функцию, метод, класс,<br>модуль или объект и выводит байт-код в читабельном виде</td>
<td><code>import dis; dis.dis(some_function)</code></td>
</tr>
<tr>
<td><code>dis.code_info(obj)</code></td>
<td>Выводит подробную информацию о коде функции,<br>метода или объекта в виде строки<br>(имя, аргументы, количество инструкций и т.д.)</td>
<td><code>import dis; print(dis.code_info(some_function))</code></td>
</tr>
<tr>
<td><code>dis.show_code(obj)</code></td>
<td>Показывает информацию о коде объекта,<br>включая аргументы и размеры</td>
<td><code>dis.show_code(some_function)</code></td>
</tr>
<tr>
<td><code>dis.get_instructions(obj)</code></td>
<td>Возвращает итератор инструкций байт-кода для объекта<br>(функции, метода или класса)</td>
<td><code>instructions = list(dis.get_instructions(some_function))</code></td>
</tr>
<tr>
<td><code>dis.Bytecode(obj)</code></td>
<td>Возвращает объект <code>Bytecode</code>, представляющий<br>инструкции байт-кода для объекта.<br>Можно использовать для итерации по инструкциям</td>
<td><code>bytecode = dis.Bytecode(some_function)</code><br><code>for instr in bytecode: print(instr.opname, instr.argval)</code></td>
</tr>
<tr>
<td><code>dis.distb([tb])</code></td>
<td>Дизассемблирует байт-код последней трассировки (traceback)<br>или переданного объекта трассировки,<br>полезно для анализа ошибок в стек-трейсах</td>
<td><code>try: 1/0; except ZeroDivisionError: dis.distb()</code></td>
</tr>
<tr>
<td><code>dis.disassemble(code)</code></td>
<td>Дизассемблирует объект кода (code object) и возвращает его инструкции</td>
<td><code>code = some_function.__code__</code><br><code>dis.disassemble(code)</code></td>
</tr>
</tbody>
</table>
<h3>Классы в библиотеке <code>dis</code></h3>
<table>
<thead>
<tr>
<th>Класс</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>dis.Bytecode</code></td>
<td>Представляет последовательность инструкций байт-кода для объекта.<br>Можно итерировать по объектам этого класса для анализа байт-кода</td>
<td><code>bytecode = dis.Bytecode(some_function)</code><br><code>for instr in bytecode:</code><br><code>print(instr.opname, instr.argval)</code></td>
</tr>
<tr>
<td><code>dis.Instruction</code></td>
<td>Описывает одну инструкцию байт-кода, содержит такие поля как<br><code>opcode</code>, <code>opname</code>, <code>arg</code>, <code>argval</code>, <code>starts_line</code> и т.д</td>
<td><code>for instr in dis.get_instructions(some_function):</code><br><code>print(instr.opname, instr.argval)</code></td>
</tr>
</tbody>
</table>
<h3>Поля класса <code>dis.Instruction</code></h3>
<table>
<thead>
<tr>
<th>Поле</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>opcode</code></td>
<td>Числовое значение кода операции (инструкции байт-кода)</td>
</tr>
<tr>
<td><code>opname</code></td>
<td>Имя инструкции (например, <code>LOAD_CONST</code>, <code>RETURN_VALUE</code>)</td>
</tr>
<tr>
<td><code>arg</code></td>
<td>Аргумент инструкции (может быть None, если у инструкции нет аргументов)</td>
</tr>
<tr>
<td><code>argval</code></td>
<td>Значение аргумента инструкции (например, константа, которая загружается инструкцией <code>LOAD_CONST</code>)</td>
</tr>
<tr>
<td><code>argrepr</code></td>
<td>Представление аргумента в виде строки (удобное для чтения описание)</td>
</tr>
<tr>
<td><code>offset</code></td>
<td>Смещение инструкции относительно начала байт-кода (в байтах)</td>
</tr>
<tr>
<td><code>starts_line</code></td>
<td>Номер строки Python-кода, с которой начинается выполнение инструкции (или None, если инструкция не начинается с новой строки)</td>
</tr>
<tr>
<td><code>is_jump_target</code></td>
<td>Булево значение, указывающее, является ли инструкция целью перехода</td>
</tr>
</tbody>
</table>
<h3>Дизассемблирование кода</h3>
<p>Пример дизассемблирования функции</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">dis</span>

<span class="k">def</span> <span class="nf">example</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span>

<span class="n">dis</span><span class="o">.</span><span class="n">dis</span><span class="p">(</span><span class="n">example</span><span class="p">)</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>2           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
</pre></div></div></div>

<h3>Разбор объектов с помощью <code>dis.get_instructions</code></h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">dis</span>

<span class="k">def</span> <span class="nf">example</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span>

<span class="k">for</span> <span class="n">instr</span> <span class="ow">in</span> <span class="n">dis</span><span class="o">.</span><span class="n">get_instructions</span><span class="p">(</span><span class="n">example</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">instr</span><span class="o">.</span><span class="n">opname</span><span class="p">,</span> <span class="n">instr</span><span class="o">.</span><span class="n">argval</span><span class="p">)</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>LOAD_FAST a
LOAD_FAST b
BINARY_ADD None
RETURN_VALUE None
</pre></div></div></div>

<h3>Примеры других функций</h3>
<p><strong><code>dis.code_info()</code></strong> для получения информации о функции</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">dis</span>

<span class="k">def</span> <span class="nf">example</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
  <span class="k">return</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span>

<span class="nb">print</span><span class="p">(</span><span class="n">dis</span><span class="o">.</span><span class="n">code_info</span><span class="p">(</span><span class="n">example</span><span class="p">))</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>Name:              example
Argument count:    2
Positional-only arguments: 0
Kw-only arguments: 0
Number of locals:  2
Stack size:        2
Flags:             OPTIMIZED, NEWLOCALS, NOFREE
</pre></div></div></div>

<h3><code>dis.Bytecode</code></h3>
<p>Использование <code>Bytecode</code> для итерации по инструкциям</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">dis</span>

<span class="k">def</span> <span class="nf">example</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span>

<span class="n">bytecode</span> <span class="o">=</span> <span class="n">dis</span><span class="o">.</span><span class="n">Bytecode</span><span class="p">(</span><span class="n">example</span><span class="p">)</span>

<span class="k">for</span> <span class="n">instr</span> <span class="ow">in</span> <span class="n">bytecode</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">instr</span><span class="o">.</span><span class="n">opname</span><span class="p">,</span> <span class="n">instr</span><span class="o">.</span><span class="n">argval</span><span class="p">)</span>
</pre></div></div></div>

<h3>Полезные функции для анализа исключений</h3>
<p><strong><code>dis.distb()</code></strong>: используется для дизассемблирования байт-кода по последней трассировке (traceback)</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">try</span><span class="p">:</span>
  <span class="mi">1</span> <span class="o">/</span> <span class="mi">0</span>
<span class="k">except</span> <span class="ne">ZeroDivisionError</span><span class="p">:</span>
  <span class="kn">import</span> <span class="nn">dis</span>
  <span class="n">dis</span><span class="o">.</span><span class="n">distb</span><span class="p">()</span>
</pre></div></div></div>

<h3>Использование с модулями и классами</h3>
<p>Можно дизассемблировать не только функции, но и модули целиком</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">dis</span>

<span class="n">module_code</span> <span class="o">=</span> <span class="nb">compile</span><span class="p">(</span><span class="s2">&quot;a = 10</span><span class="se">\n</span><span class="s2">b = 20</span><span class="se">\n</span><span class="s2">c = a + b&quot;</span><span class="p">,</span> <span class="s2">&quot;&lt;string&gt;&quot;</span><span class="p">,</span> <span class="s2">&quot;exec&quot;</span><span class="p">)</span>
<span class="n">dis</span><span class="o">.</span><span class="n">dis</span><span class="p">(</span><span class="n">module_code</span><span class="p">)</span>
</pre></div></div></div>

<p>Это покажет инструкции для выполнения кода всего модуля.</p>