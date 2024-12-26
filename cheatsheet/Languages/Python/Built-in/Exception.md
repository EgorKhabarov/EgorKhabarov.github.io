<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>BaseException - базовое исключение, от которого берут начало все остальные.
 +-- SystemExit - исключение, порождаемое функцией sys.exit при выходе из программы.
 +-- KeyboardInterrupt - порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).
 +-- GeneratorExit - порождается при вызове метода close объекта generator.
 +-- Exception - а вот тут уже заканчиваются полностью системные исключения (которые лучше не трогать) и начинаются обыкновенные, с которыми можно работать.
      +-- StopIteration - порождается встроенной функцией next, если в итераторе больше нет элементов.
      +-- StopAsyncIteration -  порождается встроенной функцией anext, если в асинхронном итераторе больше нет элементов.
      +-- ArithmeticError - арифметическая ошибка.
      |    +-- FloatingPointError - порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.
      |    +-- OverflowError - возникает, когда результат арифметической операции слишком велик для представления.
      |                        Не появляется при обычной работе с целыми числами (так как python поддерживает длинные числа), но может возникать в некоторых других случаях.
      |    +-- ZeroDivisionError - деление на ноль.
      +-- AssertionError - выражение в функции assert ложно.
      +-- AttributeError - объект не имеет данного атрибута (значения или метода).
      +-- BufferError - операция, связанная с буфером, не может быть выполнена.
      +-- EOFError - функция наткнулась на конец файла и не смогла прочитать то, что хотела.
      +-- ImportError - не удалось импортирование модуля или его атрибута.
      |    +-- ModuleNotFoundError
      +-- LookupError - некорректный индекс или ключ.
      |    +-- IndexError - индекс не входит в диапазон элементов.
      |    +-- KeyError - несуществующий ключ (в словаре, множестве или другом объекте).
      +-- MemoryError - недостаточно памяти.
      +-- NameError - не найдено переменной с таким именем.
      |    +-- UnboundLocalError - сделана ссылка на локальную переменную в функции, но переменная не определена ранее.
      +-- OSError - ошибка, связанная с системой.
      |    +-- BlockingIOError - операция блокирует неблокируемый объект ввода-вывода (например, сокеты или файлы).
      |    +-- ChildProcessError - неудача при операции с дочерним процессом.
      |    +-- ConnectionError - базовый класс для исключений, связанных с подключениями.
      |    |    +-- BrokenPipeError - Возникает, когда попытка записи данных в закрытый канал или сокет завершается неудачей.
      |    |    +-- ConnectionAbortedError - Соединение неожиданно прервано до завершения.
      |    |    +-- ConnectionRefusedError - Соединение отклонено сервером (например, порт закрыт).
      |    |    +-- ConnectionResetError - Соединение сброшено другой стороной.
      |    +-- FileExistsError - попытка создания файла или директории, которая уже существует.
      |    +-- FileNotFoundError - файл или директория не существует.
      |    +-- InterruptedError - системный вызов прерван входящим сигналом.
      |    +-- IsADirectoryError - ожидался файл, но это директория.
      |    +-- NotADirectoryError - ожидалась директория, но это файл.
      |    +-- PermissionError - не хватает прав доступа.
      |    +-- ProcessLookupError - указанного процесса не существует.
      |    +-- TimeoutError - закончилось время ожидания.
      +-- ReferenceError - попытка доступа к атрибуту со слабой ссылкой.
      +-- RuntimeError - возникает, когда исключение не попадает ни под одну из других категорий.
      |    +-- NotImplementedError - возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.
      |    +-- RecursionError - вызывается при превышении максимальной глубины рекурсии, часто из-за бесконечной рекурсии.
      +-- SyntaxError - синтаксическая ошибка.
      |    +-- IndentationError - неправильные отступы.
      |         +-- TabError - смешивание в отступах табуляции и пробелов.
      +-- SystemError - внутренняя ошибка.
      +-- TypeError - операция применена к объекту несоответствующего типа.
      +-- ValueError - функция получает аргумент правильного типа, но некорректного значения.
      |    +-- UnicodeError - ошибка, связанная с кодированием / раскодированием unicode в строках.
      |         +-- UnicodeDecodeError - исключение, связанное с кодированием unicode.
      |         +-- UnicodeEncodeError - исключение, связанное с декодированием unicode.
      |         +-- UnicodeTranslateError - исключение, связанное с переводом unicode.
      +-- Warning - предупреждение.
           +-- DeprecationWarning - предупреждает о функциях, которые устарели и будут удалены в будущей версии Python.
           +-- PendingDeprecationWarning - предназначено для функций, которые планируется упразднить в далеком будущем.
           +-- RuntimeWarning - предупреждает о проблемах, которые не попадают в другие категории, но все равно заслуживают внимания во время выполнения.
           +-- SyntaxWarning - предупреждает о сомнительном синтаксисе, который может привести к неожиданному поведению.
           +-- UserWarning - общее предупреждение для пользователей, часто используемое разработчиками для обозначения некритических проблем.
           +-- FutureWarning - предупреждает об изменениях, которые произойдут в будущих версиях Python.
           +-- ImportWarning - предупреждает о проблемах во время операций импорта.
           +-- UnicodeWarning - предупреждает о проблемах с операциями, связанными с Unicode.
           +-- BytesWarning - предупреждает о проблемах с операциями с байтами или байтовыми массивами.
           +-- ResourceWarning - предупреждает об использовании ресурсов (например, о незакрытых файлах).
           +-- EncodingWarning


EnvironmentError
IOError
WindowsError
</pre></div></div></div>

<h1>BaseException</h1>
<p>Базовое исключение, от которого берут начало все остальные.</p>
<h2>SystemExit</h2>
<p>Исключение, порождаемое функцией sys.exit при выходе из программы.</p>
<h2>KeyboardInterrupt</h2>
<p>Порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).</p>
<h2>GeneratorExit</h2>
<p>Порождается при вызове метода close объекта generator.</p>
<h2>Exception</h2>
<p>А вот тут уже заканчиваются полностью системные исключения (которые лучше не трогать) и начинаются обыкновенные, с которыми можно работать.</p>
<h3>StopIteration</h3>
<p>Порождается встроенной функцией next, если в итераторе больше нет элементов.</p>
<h3>StopAsyncIteration</h3>
<p>Порождается встроенной функцией anext, если в асинхронном итераторе больше нет элементов.</p>
<h3>ArithmeticError</h3>
<p>Арифметическая ошибка.</p>
<h4>FloatingPointError</h4>
<p>Порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.</p>
<h4>OverflowError</h4>
<p>Возникает, когда результат арифметической операции слишком велик для представления. Не появляется при обычной работе с целыми числами (так как python поддерживает длинные числа), но может возникать в некоторых других случаях.</p>
<h4>ZeroDivisionError</h4>
<p>Деление на ноль.</p>
<h3>AssertionError</h3>
<p>Выражение в функции assert ложно.</p>
<h3>AttributeError</h3>
<p>Объект не имеет данного атрибута (значения или метода).</p>
<h3>BufferError</h3>
<p>Операция, связанная с буфером, не может быть выполнена.</p>
<h3>EOFError</h3>
<p>Функция наткнулась на конец файла и не смогла прочитать то, что хотела.</p>
<h3>ImportError</h3>
<p>Не удалось импортирование модуля или его атрибута.</p>
<h4>ModuleNotFoundError</h4>
<h3>LookupError</h3>
<p>Некорректный индекс или ключ.</p>
<h4>IndexError</h4>
<p>Индекс не входит в диапазон элементов.</p>
<h4>KeyError</h4>
<p>Несуществующий ключ (в словаре, множестве или другом объекте).</p>
<h3>MemoryError</h3>
<p>Недостаточно памяти.</p>
<h3>NameError</h3>
<p>Не найдено переменной с таким именем.</p>
<h4>UnboundLocalError</h4>
<p>Сделана ссылка на локальную переменную в функции, но переменная не определена ранее.</p>
<h3>OSError</h3>
<p>Ошибка, связанная с системой.</p>
<h4>BlockingIOError</h4>
<p>Операция блокирует неблокируемый объект ввода-вывода (например, сокеты или файлы).</p>
<h4>ChildProcessError</h4>
<p>Неудача при операции с дочерним процессом.</p>
<h4>ConnectionError</h4>
<p>Базовый класс для исключений, связанных с подключениями.</p>
<h5>BrokenPipeError</h5>
<p>Возникает, когда попытка записи данных в закрытый канал или сокет завершается неудачей.</p>
<h5>ConnectionAbortedError</h5>
<p>Соединение неожиданно прервано до завершения.</p>
<h5>ConnectionRefusedError</h5>
<p>Соединение отклонено сервером (например, порт закрыт).</p>
<h5>ConnectionResetError</h5>
<p>Соединение сброшено другой стороной.</p>
<h4>FileExistsError</h4>
<p>Попытка создания файла или директории, которая уже существует.</p>
<h4>FileNotFoundError</h4>
<p>Файл или директория не существует.</p>
<h4>InterruptedError</h4>
<p>Системный вызов прерван входящим сигналом.</p>
<h4>IsADirectoryError</h4>
<p>Ожидался файл, но это директория.</p>
<h4>NotADirectoryError</h4>
<p>Ожидалась директория, но это файл.</p>
<h4>PermissionError</h4>
<p>Не хватает прав доступа.</p>
<h4>ProcessLookupError</h4>
<p>Указанного процесса не существует.</p>
<h4>TimeoutError</h4>
<p>Закончилось время ожидания.</p>
<h3>ReferenceError</h3>
<p>Попытка доступа к атрибуту со слабой ссылкой.</p>
<h3>RuntimeError</h3>
<p>Возникает, когда исключение не попадает ни под одну из других категорий.</p>
<h4>NotImplementedError</h4>
<p>Возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.</p>
<h4>RecursionError</h4>
<p>Вызывается при превышении максимальной глубины рекурсии, часто из-за бесконечной рекурсии.</p>
<h3>SyntaxError</h3>
<p>Синтаксическая ошибка.</p>
<h4>IndentationError</h4>
<p>Неправильные отступы.</p>
<h5>TabError</h5>
<p>Смешивание в отступах табуляции и пробелов.</p>
<h3>SystemError</h3>
<p>Внутренняя ошибка.</p>
<h3>TypeError</h3>
<p>Операция применена к объекту несоответствующего типа.</p>
<h3>ValueError</h3>
<p>Функция получает аргумент правильного типа, но некорректного значения.</p>
<h4>UnicodeError</h4>
<p>Ошибка, связанная с кодированием / раскодированием unicode в строках.</p>
<h5>UnicodeDecodeError</h5>
<p>Исключение, связанное с кодированием unicode.</p>
<h5>UnicodeEncodeError</h5>
<p>Исключение, связанное с декодированием unicode.</p>
<h5>UnicodeTranslateError</h5>
<p>Исключение, связанное с переводом unicode.</p>
<h3>Warning</h3>
<p>Предупреждение.</p>
<h4>DeprecationWarning</h4>
<p>Предупреждает о функциях, которые устарели и будут удалены в будущей версии Python.</p>
<h4>PendingDeprecationWarning</h4>
<p>Предназначено для функций, которые планируется упразднить в далеком будущем.</p>
<h4>RuntimeWarning</h4>
<p>Предупреждает о проблемах, которые не попадают в другие категории, но все равно заслуживают внимания во время выполнения.</p>
<h4>SyntaxWarning</h4>
<p>Предупреждает о сомнительном синтаксисе, который может привести к неожиданному поведению.</p>
<h4>UserWarning</h4>
<p>Общее предупреждение для пользователей, часто используемое разработчиками для обозначения некритических проблем.</p>
<h4>FutureWarning</h4>
<p>Предупреждает об изменениях, которые произойдут в будущих версиях Python.</p>
<h4>ImportWarning</h4>
<p>Предупреждает о проблемах во время операций импорта.</p>
<h4>UnicodeWarning</h4>
<p>Предупреждает о проблемах с операциями, связанными с Unicode.</p>
<h4>BytesWarning</h4>
<p>Предупреждает о проблемах с операциями с байтами или байтовыми массивами.</p>
<h4>ResourceWarning</h4>
<p>Предупреждает об использовании ресурсов (например, о незакрытых файлах).</p>
<h4>EncodingWarning</h4>
<p>EnvironmentError
IOError
WindowsError</p>
<h1>Методы Exception</h1>
<p><a href="?Languages/Python/Methods/Magic%20attributes.md#exception">Подробнее про магические атрибуты исключений</a></p>
<table>
<thead>
<tr>
<th>Метод/Атрибут</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>add_note</code></td>
<td>Добавляет примечание к исключению</td>
<td><code>e.add_note("Доп. информация")</code></td>
</tr>
<tr>
<td><code>args</code></td>
<td>Кортеж аргументов, переданных при создании исключения</td>
<td><code>print(e.args)</code></td>
</tr>
<tr>
<td><code>with_traceback</code></td>
<td>Привязывает traceback (информацию о стеке вызовов) к исключению</td>
<td><code>new_exc = e.with_traceback(tb)</code><br><code>raise e.with_traceback(tb)</code></td>
</tr>
</tbody>
</table>
<h1>Методы ExceptionGroup</h1>
<p>Конструктор</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">ExceptionGroup</span><span class="p">(</span><span class="n">message</span><span class="p">,</span> <span class="n">exceptions</span><span class="p">)</span>
</pre></div></div></div>

<table>
<thead>
<tr>
<th>Метод/Атрибут</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>add_note</code></td>
<td>Добавляет примечание для всей группы исключений</td>
<td><code>eg.add_note("Доп. информация")</code></td>
</tr>
<tr>
<td><code>args</code></td>
<td>Возвращает кортеж с описанием группы и списком исключений</td>
<td><code>print(eg.args)</code></td>
</tr>
<tr>
<td><code>derive</code></td>
<td>Создает новую группу исключений из подмножества текущей группы</td>
<td><code>derived_group = eg.derive([ValueError("Ошибка")])</code></td>
</tr>
<tr>
<td><code>exceptions</code></td>
<td>Список всех исключений, входящих в группу</td>
<td><code>for e in eg.exceptions: print(e)</code></td>
</tr>
<tr>
<td><code>message</code></td>
<td>Описание группы исключений</td>
<td><code>print(eg.message)</code></td>
</tr>
<tr>
<td><code>split</code></td>
<td>Разделяет группу на две: исключения, удовлетворяющие условию, и остальные</td>
<td><code>match, rest = eg.split(lambda e: isinstance(e, ValueError))</code></td>
</tr>
<tr>
<td><code>subgroup</code></td>
<td>Возвращает подгруппу исключений, удовлетворяющих условию</td>
<td><code>subgroup = eg.subgroup(lambda e: isinstance(e, KeyError))</code></td>
</tr>
<tr>
<td><code>with_traceback</code></td>
<td>Привязывает traceback (информацию о стеке вызовов) ко всей группе исключений</td>
<td><code>new_group = eg.with_traceback(tb)</code></td>
</tr>
</tbody>
</table>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">e</span> <span class="o">=</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Ошибка&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">e</span><span class="o">.</span><span class="n">add_note</span><span class="p">(</span><span class="s2">&quot;Дополнительная информация о причине ошибки&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">__notes__</span><span class="p">)</span>
<span class="unselectable"><span class="go">[&#39;Дополнительная информация о причине ошибки.&#39;]</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="k">raise</span> <span class="n">e</span>
<span class="unselectable"><span class="gt">Traceback (most recent call last):</span></span>
<span class="unselectable">  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span></span>
<span class="unselectable"><span class="gr">ValueError</span>: <span class="n">Ошибка</span></span>
<span class="unselectable"><span class="x">Дополнительная информация о причине ошибки</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">e</span><span class="o">.</span><span class="n">args</span>
<span class="unselectable"><span class="go">(&#39;Ошибка&#39;,)</span>
</span></pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">try</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">raise</span> <span class="n">ExceptionGroup</span><span class="p">(</span><span class="s2">&quot;Ошибки обработки данных&quot;</span><span class="p">,</span> <span class="p">[</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Некорректное значение&quot;</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="ne">TypeError</span><span class="p">(</span><span class="s2">&quot;Несовместимый тип&quot;</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="ne">KeyError</span><span class="p">(</span><span class="s2">&quot;Ключ не найден&quot;</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="p">])</span>
<span class="unselectable"><span class="o">...</span> </span><span class="k">except</span> <span class="n">ExceptionGroup</span> <span class="k">as</span> <span class="n">eg</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Сообщение группы: </span><span class="si">{</span><span class="n">eg</span><span class="o">.</span><span class="n">message</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Исключения в группе:&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">eg</span><span class="o">.</span><span class="n">exceptions</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;- </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">e</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;---&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="c1"># Разделяем на ValueError и остальные</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">match</span><span class="p">,</span> <span class="n">rest</span> <span class="o">=</span> <span class="n">eg</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="k">lambda</span> <span class="n">e</span><span class="p">:</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="ne">ValueError</span><span class="p">))</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Ошибки ValueError:&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">match</span><span class="o">.</span><span class="n">exceptions</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="nb">print</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Остальные ошибки:&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">rest</span><span class="o">.</span><span class="n">exceptions</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="nb">print</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="go">Сообщение группы: Ошибки обработки данных</span>
<span class="go">Исключения в группе:</span>
<span class="go">- ValueError: Некорректное значение</span>
<span class="go">- TypeError: Несовместимый тип</span>
<span class="go">- KeyError: &#39;Ключ не найден&#39;</span>
<span class="go">---</span>
<span class="go">Ошибки ValueError:</span>
<span class="go">Некорректное значение</span>
<span class="go">Остальные ошибки:</span>
<span class="go">Несовместимый тип</span>
<span class="go">&#39;Ключ не найден&#39;</span>
</span></pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">try</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">raise</span> <span class="n">ExceptionGroup</span><span class="p">(</span><span class="s2">&quot;Группа ошибок&quot;</span><span class="p">,</span> <span class="p">[</span><span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Ошибка 1&quot;</span><span class="p">),</span> <span class="ne">KeyError</span><span class="p">(</span><span class="s2">&quot;Ошибка 2&quot;</span><span class="p">)])</span>
<span class="unselectable"><span class="o">...</span> </span><span class="k">except</span> <span class="n">ExceptionGroup</span> <span class="k">as</span> <span class="n">eg</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">derived_group</span> <span class="o">=</span> <span class="n">eg</span><span class="o">.</span><span class="n">derive</span><span class="p">([</span><span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Ошибка 3&quot;</span><span class="p">)])</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">derived_group</span><span class="o">.</span><span class="n">exceptions</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="nb">print</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="go">(&#39;Ошибка 3&#39;,)</span>
</span></pre></div></div></div>