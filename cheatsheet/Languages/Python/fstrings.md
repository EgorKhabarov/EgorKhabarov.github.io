<h1>F-Strings</h1>
<p><strong>F-строки</strong> - это новый способ форматирования строк в Python 3.6 и выше. 
Они позволяют встраивать выражения Python внутри строк посредством указания их в <code>{}</code> внутри строки, заключенной в <code>f</code>.</p>
<blockquote>
<p>replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"</p>
<p>field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
arg_name          ::=  [identifier | digit+]
attribute_name    ::=  identifier
element_index     ::=  digit+ | index_string
index_string      ::=  &lt;любой исходный символ, кроме "]"&gt; +</p>
<p>conversion        ::=  "r" | "s" | "a"</p>
<p>format_spec       ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill              ::=  <any character>
align             ::=  "&lt;" | "&gt;" | "=" | "^"
sign              ::=  "+" | "-" | " "
width             ::=  digit+
grouping_option   ::=  "_" | ","
precision         ::=  digit+
type              ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"</p>
</blockquote>
<h2>Field_name</h2>
<p>Выражение формы <code>".name"</code> выбирает именованный атрибут с помощью <code>getattr()</code>
Выражение формы <code>"[index]"</code> выполняет поиск по индексу с использованием <code>getitem()</code></p>
<h2>Conversion</h2>
<p>Вызывает приведение типа перед форматированием</p>
<table>
<thead>
<tr>
<th style="text-align: center;">conversion</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">!s</td>
<td>str()</td>
</tr>
<tr>
<td style="text-align: center;">!r</td>
<td>repr()</td>
</tr>
<tr>
<td style="text-align: center;">!a</td>
<td>ascii()</td>
</tr>
</tbody>
</table>
<h2>Format_spec</h2>
<p>Содержит спецификацию того, как должно быть представлено значение,
Включая такие детали, как ширина поля, выравнивание, заполнение, десятичная точность и т. д.
Каждый тип значения может определять свой собственный <strong>мини-язык форматирования</strong> или интерпретацию <code>format_spec</code>.</p>
<h3>Fill</h3>
<p>Невозможно использовать литеральную фигурную скобку <code>{</code> или <code>}</code> в качестве символа <code>fill</code>
в форматированном строковом литерале или при использовании метода <code>str.format()</code>.</p>
<details>
<summary><b>Однако можно вставить фигурную скобку с вложенным полем замены.</b></summary>


<pre><code class="language-pycon">&gt;&gt;&gt; f&quot;{1:}&gt;20}&quot;
  File &quot;&lt;stdin&gt;&quot;, line 1
    f&quot;{1:}&gt;20}&quot;
               ^
SyntaxError: f-string: single '}' is not allowed
&gt;&gt;&gt; f&quot;{1:}}&gt;20}&quot;
  File &quot;&lt;stdin&gt;&quot;, line 1
    f&quot;{1:}}&gt;20}&quot;
                ^
SyntaxError: f-string: single '}' is not allowed
&gt;&gt;&gt; f&quot;{1:{'}'}&gt;20}&quot;
&quot;}}}}}}}}}}}}}}}}}}}1&quot;
</code></pre>


</details>
<p>Это ограничение не влияет на функцию <code>format()</code>.</p>
<h3>Align</h3>
<table>
<thead>
<tr>
<th style="text-align: center;">Вариант</th>
<th>Значение</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>&lt;</strong></td>
<td>Выравнивает поле по левому краю в доступном пространстве<br><strong>По умолчанию для большинства объектов</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>&gt;</strong></td>
<td>Принудительно выравнивает поле по правому краю в доступном пространстве<br><strong>По умолчанию для чисел</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>^</strong></td>
<td>Центрирует поле в доступном пространстве</td>
</tr>
</tbody>
</table>
<h3>Sign</h3>
<p>Действителен только для числовых типов.</p>
<table>
<thead>
<tr>
<th style="text-align: center;">Вариант</th>
<th>Значение</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>+</strong></td>
<td>Указывает, что знак должен использоваться как для положительных, так и для отрицательных чисел.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>-</strong></td>
<td>Указывает, что знак следует использовать только для отрицательных чисел<br><strong>Поведение по умолчанию</strong>.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>=</strong></td>
<td>Принудительно размещает заполнение после знака (если есть), но перед цифрами.<br>Это используется для печати полей в форме <code>+000000120</code>.<br>Этот параметр выравнивания действителен только для числовых типов.<br>Он становится значением по умолчанию для чисел, когда <code>0</code> непосредственно предшествует ширине поля.</td>
</tr>
<tr>
<td style="text-align: center;"><strong><strong>Пробел</strong></strong></td>
<td>Указывает, что ведущий пробел должен использоваться на положительных числах, а знак минус на отрицательных числах.</td>
</tr>
</tbody>
</table>
<h3>&#x23;</h3>
<p><strong>#</strong> - Приводит к использованию <strong>альтернативной формы</strong> для преобразования.
    Альтернативная форма определяется по-разному для разных типов.
    Этот параметр действителен только для <strong>целых</strong>, <strong>плавающих</strong> и <strong>сложных</strong> типов.
    Для целых чисел, когда используется <strong>двоичный</strong>, <strong>восьмеричный</strong> или <strong>шестнадцатеричный</strong> вывод,
    эта опция добавляет соответствующий префикс <code>0b</code>, <code>0o</code>, <code>0x</code> или <code>0X</code> к выходному значению.<br>
    Для чисел с <strong>плавающей запятой</strong> и <strong>сложных</strong> альтернативная форма приводит к тому, что результат
    преобразования всегда содержит символ десятичной точки, <strong>даже если за ним не следуют цифры</strong>.
    Обычно символ десятичной точки появляется в результате этих преобразований только в том случае, если за ним следует цифра.
    <strong>Кроме того, для преобразований <code>g</code> и <code>G</code> конечные нули не удаляются из результата.</strong></p>
<h3>0</h3>
<p><strong>,</strong> - Сигнализирует об использовании запятой для разделителя тысяч.
    Для разделителя с учётом языкового стандарта использовать вместо него целочисленный тип представления <code>n</code>
<strong>_</strong> - Сигнализирует об использовании подчеркивания для разделителя тысяч для типов представления с плавающей запятой
    и для целочисленного типа представления <code>d</code>.
    Для целочисленных типов представления <code>b</code>, <code>o</code>, <code>x</code> и <code>X</code> символы подчеркивания вставляются каждые 4 цифры.
    Для других типов представлений указание этой опции является ошибкой.</p>
<h3>Width</h3>
<p>Десятичное целое число, определяющее минимальную общую ширину поля,
включая любые префиксы, разделители и другие символы форматирования.
Если не указан, то ширина поля будет определяться содержимым.</p>
<p>Если явное выравнивание не задано, то перед полем <code>width</code> нулевым <code>0</code> символом
включается знаковое заполнение нулями для числовых типов.
Это эквивалентно <code>fill</code> символу <code>0</code> с типом alignment <code>=</code>.</p>
<p>Точность представляет собой десятичное целое число , указывающее, сколько цифр должно отображаться после десятичной 
точки для типов представления <code>f</code> и <code>F</code>, или до и после десятичной точки для типов представления <code>g</code> или <code>G</code>. 
Для типов строкового представления поле указывает максимальный размер поля, другими словами, сколько символов 
будет использовано из содержимого поля. Точность не допускается для целочисленных типов представления .</p>
<h3>Precision</h3>
<p>Десятичное число, указывающее, сколько цифр должно отображаться после десятичной точки
для значения с плавающей запятой, отформатированного с помощью <code>f</code> и <code>F</code>,
или до и после десятичной точки для значения с плавающей запятой, отформатированного с помощью <code>g</code> или <code>G</code>.
Для нечисловых типов поле указывает максимальный размер поля — другими словами,
сколько символов будет использовано из содержимого поля.
<code>precision</code> не допускается для целочисленных значений.</p>
<h3>Type</h3>
<p>Определяет, как данные должны быть представлены.</p>
<h4>1. Доступные типы представления строк:</h4>
<table>
<thead>
<tr>
<th style="text-align: center;">Тип</th>
<th>Значение</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><code>s</code></td>
<td>Формат строки. Это тип по умолчанию для строк, и его можно опустить.</td>
</tr>
<tr>
<td style="text-align: center;">None</td>
<td>То же, что <code>s</code>.</td>
</tr>
</tbody>
</table>
<h4>2. Доступные типы целочисленного представления:</h4>
<table>
<thead>
<tr>
<th style="text-align: center;">Тип</th>
<th>Значение</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>b</strong></td>
<td>Двоичный формат</td>
</tr>
<tr>
<td style="text-align: center;"><strong>c</strong></td>
<td>Преобразует целое число в соответствующий символ Юникода перед печатью</td>
</tr>
<tr>
<td style="text-align: center;"><strong>d</strong></td>
<td>Десятичное целое число</td>
</tr>
<tr>
<td style="text-align: center;"><strong>o</strong></td>
<td>Восьмеричный формат</td>
</tr>
<tr>
<td style="text-align: center;"><strong>x</strong></td>
<td>Шестнадцатеричный формат. Использует строчные буквы для цифр выше <code>9</code></td>
</tr>
<tr>
<td style="text-align: center;"><strong>X</strong></td>
<td>Шестнадцатеричный формат. Использует прописные буквы для цифр выше <code>9</code></td>
</tr>
<tr>
<td style="text-align: center;"><strong>n</strong></td>
<td>Число. Это то же самое, что и <code>d</code>, за исключением того,<br>что для вставки соответствующих символов-разделителей чисел он использует текущую настройку локали.</td>
</tr>
<tr>
<td style="text-align: center;">None</td>
<td>То же, что <code>d</code></td>
</tr>
</tbody>
</table>
<h4>3. Доступные типы представления для <code>float</code> и <code>Decimal</code> значений:</h4>
<table>
<thead>
<tr>
<th style="text-align: center;">Тип</th>
<th>Значение</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>e</strong></td>
<td>Научная нотация.<br>Для заданной точности <code>p</code> форматирует число в <strong>экспоненциальном представлении</strong> с буквой «<code>e</code>», отделяющей <strong><code>p</code> цифр коэффициента</strong> от экспоненты.<br>Коэффициент состоит из одной цифры перед и после десятичной точки, всего <code>p + 1</code> значащих цифр.<br>Если точность не указана, используется точность <strong>6 цифр</strong> после десятичной точки для <code>float</code><br>и отображаются все цифры коэффициентов для <code>Decimal</code>.<br>Если после десятичной точки нет цифр, десятичная точка также удаляется,<br>если не используется опция <code>#</code></td>
</tr>
<tr>
<td style="text-align: center;"><strong>E</strong></td>
<td>Научная нотация.<br>То же, что и <code>e</code>, за исключением того, что в качестве символа-разделителя используется заглавная буква «<code>E</code>»</td>
</tr>
<tr>
<td style="text-align: center;"><strong>f</strong></td>
<td>Запись с фиксированной точкой.<br>Для заданной точности <code>p</code> форматирует число как десятичное с точностью <code>p</code> цифр после десятичной точки.<br>Если точность не указана, используется точность <strong>6 цифр</strong> после десятичной точки для <code>float</code><br>и используется точность, достаточно большая для отображения всех цифр коэффициентов для <code>Decimal</code>.<br>Если после десятичной точки нет цифр, десятичная точка также удаляется,<br>если не используется опция <code>#</code></td>
</tr>
<tr>
<td style="text-align: center;"><strong>F</strong></td>
<td>Представление с фиксированной точкой.<br>То же, что и <code>f</code>, но преобразует <code>nan</code> в <code>NAN</code> и <code>inf</code> в <code>INF</code></td>
</tr>
<tr>
<td style="text-align: center;"><strong>g</strong></td>
<td>Общий формат.<br>Для заданной точности <code>p &gt;= 1</code> округляет число до <code>p</code> значащих цифр и затем форматирует результат либо в формате с фиксированной точкой,<br>либо в научном представлении, в зависимости от его величины.<br><br>Точные правила следующие: предположим, что результат отформатирован с типом представления <code>e</code> и <code>p-1</code> точности, будет с exp экспонентой.<br>Затем, если <code>m &lt;= exp &lt; p</code>, где <code>m</code> равно <code>-4</code> для <code>floats</code> и <code>-6</code> для <code>Decimals</code>,<br>число форматируется с типом представления <code>f</code> и точностью <code>p-1-exp</code>.<br>В противном случае номер форматируется с помощью <code>e</code> типа представления и <code>p-1</code> точности.<br>В обоих случаях из значащего удаляются незначительные конечные нули, а десятичная точка также удаляется, если после неё нет оставшихся цифр,<br>если не используется опция <code>#</code>.<br><br>Без указания точности использует точность <strong><code>6</code> значащих цифр</strong> для <code>float</code>.<br>Для <code>Decimal</code> коэффициент результата формируется из цифр коэффициента значения;<br>экспоненциальная нотация используется для значений, меньших, чем <code>1e-6</code> по абсолютной величине, и значений,<br>в которых разряд наименее значащей цифры больше 1, а в противном случае используется нотация с фиксированной точкой.<br><br>Положительные и отрицательные бесконечности, положительный и отрицательный ноль и <code>nan</code>,<br>форматируются как <code>inf</code>, <code>-inf</code>, <code>0</code>, <code>-0</code> и <code>nan</code> соответственно, независимо от точности</td>
</tr>
<tr>
<td style="text-align: center;"><strong>G</strong></td>
<td>Общий формат.<br>То же, что и <code>g</code>, за исключением переключения на <code>E</code>, если число становится слишком большим.<br>Представления бесконечности и <code>NaN</code> также в верхнем регистре.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>n</strong></td>
<td>Номер.<br>Это то же самое, что и <code>g</code>, за исключением того, что он использует текущую настройку локали<br>для вставки соответствующих символов разделителя чисел.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>%</strong></td>
<td>Процент.<br><strong>Умножает число на <code>100</code> и отображает в фиксированном <code>f</code> формате</strong>, за которым следует знак процента.</td>
</tr>
<tr>
<td style="text-align: center;"><strong>None</strong></td>
<td>Для <code>float</code> это то же самое, что и для <code>g</code>,<br>за исключением того, что когда для форматирования результата используется запись с фиксированной точкой,<br>она всегда включает как минимум одну цифру после десятичной точки.<br>Используемая точность настолько велика, насколько это необходимо для точного представления заданного значения.<br><br>Для Decimal это то же самое, что <code>g</code> или <code>G</code> в зависимости от значения <code>context.capitals</code> для текущего десятичного контекста.<br><br>Общий эффект заключается в том, чтобы соответствовать выходным данным <code>str()</code>, измененному другими модификаторами формата.</td>
</tr>
</tbody>
</table>
<p>Примеры простых форматных строк:</p>
<pre><code class="language-python">&quot;Сначала посчитай до {0}&quot;         # Ссылки на первый позиционный аргумент
&quot;Принеси мне {}&quot;                  # Неявно ссылается на первый позиционный аргумент
&quot;От {} до {}&quot;                     # То же, что &quot;От {0} до {1}&quot;
&quot;Мой квест {name}&quot;                # Ссылка на ключевой аргумент «name»
&quot;Масса в тоннах {0.weight}&quot;       # атрибут «weight» первого позиционного аргумента
&quot;Уничтожено единиц: {players[0]}&quot; # Первый элемент ключевого аргумента «players».

&quot;Гарольд умный {0!s}&quot;             # Сначала вызывает str() для первого аргумента
&quot;Принесите святую {name!r}&quot;       # Сначала вызывает repr() для первого аргумента
&quot;Больше {!a}&quot;                     # Сначала вызывает ascii() для первого аргумента
</code></pre>
<p>Доступ к аргументам по позиции:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; &quot;{0}, {1}, {2}&quot;.format(&quot;a&quot;, &quot;b&quot;, &quot;c&quot;)
&quot;a, b, c&quot;
&gt;&gt;&gt; &quot;{}, {}, {}&quot;.format(&quot;a&quot;, &quot;b&quot;, &quot;c&quot;)  # 3.1+ python version only
&quot;a, b, c&quot;
&gt;&gt;&gt; &quot;{2}, {1}, {0}&quot;.format(&quot;a&quot;, &quot;b&quot;, &quot;c&quot;)
&quot;c, b, a&quot;
&gt;&gt;&gt; &quot;{2}, {1}, {0}&quot;.format(*&quot;abc&quot;)      # unpacking argument sequence
&quot;c, b, a&quot;
&gt;&gt;&gt; &quot;{0}{1}{0}&quot;.format(&quot;abra&quot;, &quot;cad&quot;)   # arguments indices can be repeated
&quot;abracadabra&quot;
</code></pre>
<p>Доступ к аргументам по имени:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; &quot;Coordinates: {latitude}, {longitude}&quot;.format(latitude=&quot;37.24N&quot;, longitude=&quot;-115.81W&quot;)
&quot;Coordinates: 37.24N, -115.81W&quot;
&gt;&gt;&gt; coord = {&quot;latitude&quot;: &quot;37.24N&quot;, &quot;longitude&quot;: &quot;-115.81W&quot;}
&gt;&gt;&gt; &quot;Coordinates: {latitude}, {longitude}&quot;.format(**coord)
&quot;Coordinates: 37.24N, -115.81W&quot;
</code></pre>
<p>Доступ к атрибутам аргументов:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; c = 3-5j
&gt;&gt;&gt; (
...     &quot;The complex number {0} is formed from the real part {0.real} &quot;
...     &quot;and the imaginary part {0.imag}.&quot;
... ).format(c)
&quot;The complex number 3-5j is formed from the real part 3.0 and the imaginary part -5.0.&quot;
</code></pre>
<pre><code class="language-pycon">&gt;&gt;&gt; class Point:
...     def __init__(self, x, y):
...         self.x, self.y = x, y
...     def __str__(self):
...         return &quot;Point({self.x}, {self.y})&quot;.format(self=self)
...
&gt;&gt;&gt; str(Point(4, 2))
&quot;Point(4, 2)&quot;
</code></pre>
<p>Доступ к элементам аргументов:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; &quot;X: {0[0]};  Y: {0[1]}&quot;.format((3, 5))
&quot;X: 3;  Y: 5&quot;
</code></pre>
<p>Замена <code>%s</code> и <code>%r</code>:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; &quot;repr() shows quotes: {!r}; str() doesn't: {!s}&quot;.format(&quot;test1&quot;, &quot;test2&quot;)
&quot;repr() shows quotes: 'test1'; str() doesn't: test2&quot;
</code></pre>
<p>Выравнивание текста и указание ширины:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; &quot;{:&lt;30}&quot;.format(&quot;left aligned&quot;)
&quot;left aligned                  &quot;
&gt;&gt;&gt; &quot;{:&gt;30}&quot;.format(&quot;right aligned&quot;)
&quot;                 right aligned&quot;
&gt;&gt;&gt; &quot;{:^30}&quot;.format(&quot;centered&quot;)
&quot;           centered           &quot;
&gt;&gt;&gt; &quot;{:*^30}&quot;.format(&quot;centered&quot;)  # use &quot;*&quot; as a fill char
&quot;***********centered***********&quot;
</code></pre>
<p>Замена <code>%+f</code>, <code>%-f</code>, и и указание знака: <code>%</code> <code>f</code></p>
<pre><code class="language-pycon">&gt;&gt;&gt; &quot;{:+f}; {:+f}&quot;.format(3.14, -3.14)  # show it always
&quot;+3.140000; -3.140000&quot;
&gt;&gt;&gt; &quot;{: f}; {: f}&quot;.format(3.14, -3.14)  # show a space for positive numbers
&quot; 3.140000; -3.140000&quot;
&gt;&gt;&gt; &quot;{:-f}; {:-f}&quot;.format(3.14, -3.14)  # show only the minus -- same as &quot;{:f}; {:f}&quot;
&quot;3.140000; -3.140000&quot;
&gt;&gt;&gt; 
&gt;&gt;&gt; &quot;{:-.2f}; {:-.2f}&quot;.format(3.14, -3.14)
&quot;3.14; -3.14&quot;
</code></pre>
<p>Замена <code>%x</code> и <code>%o</code> преобразование значения в разные базы:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; # format also supports binary numbers
&gt;&gt;&gt; &quot;int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}&quot;.format(42)
&quot;int: 42;  hex: 2a;  oct: 52;  bin: 101010&quot;
&gt;&gt;&gt; # with 0x, 0o, or 0b as prefix:
&gt;&gt;&gt; &quot;int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}&quot;.format(42)
&quot;int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010&quot;
</code></pre>
<p>Использование запятой или подчёркивания в качестве разделителя тысяч:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; &quot;{:,}&quot;.format(1234567890)
&quot;1,234,567,890&quot;
&gt;&gt;&gt; &quot;{:_}&quot;.format(1234567890)
&quot;1_234_567_890&quot;
</code></pre>
<p>Выражение процента:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; points, total = 19, 22
&gt;&gt;&gt; &quot;Correct answers: {:.2%}&quot;.format(points/total)
&quot;Correct answers: 86.36%&quot;
</code></pre>
<p>Использование форматирования для конкретного типа:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; from datetime import datetime
&gt;&gt;&gt; &quot;{:%Y-%m-%d %H:%M:%S}&quot;.format(datetime(2010, 7, 4, 12, 15, 58))
&quot;2010-07-04 12:15:58&quot;
</code></pre>
<p>Вложенные аргументы и более сложные примеры:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; for align, text in zip(&quot;&lt;^&gt;&quot;, [&quot;left&quot;, &quot;center&quot;, &quot;right&quot;]):
...    &quot;{0:{fill}{align}16}&quot;.format(text, fill=align, align=align)
...
&quot;left&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&quot;
&quot;^^^^^center^^^^^&quot;
&quot;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;right&quot;
&gt;&gt;&gt; octets = [192, 168, 0, 1]
&gt;&gt;&gt; &quot;{:02X}{:02X}{:02X}{:02X}&quot;.format(*octets)
&quot;C0A80001&quot;
&gt;&gt;&gt; int(_, 16)
3232235521
&gt;&gt;&gt; width = 5
&gt;&gt;&gt; for num in range(5,12): 
...     for base in &quot;dXob&quot;:
...         print(&quot;{0:{width}{base}}&quot;.format(num, base=base, width=width), end=&quot; &quot;)
...     print()
... 
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8     8    10  1000
    9     9    11  1001
   10     A    12  1010
   11     B    13  1011
</code></pre>
<p>Форматирование чисел:
Для вывода количества знаков после запятой можно использовать флаг f:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; f&quot;pi {22 / 7:.2f}&quot;
&quot;pi 3.14&quot;
</code></pre>
<p>Форматирование строк:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; name = &quot;Name&quot;
&gt;&gt;&gt; f&quot;{name.upper():&lt;10}&quot;  # выравнивается в лево на 10 символов
&quot;NAME      &quot;
&gt;&gt;&gt; f&quot;{name.upper():&gt;10}&quot;  # выравнивается в право на 10 символов
&quot;      NAME&quot;
&gt;&gt;&gt; f&quot;{name.upper():^10}&quot;  # выравнивается по центру шириной 10 символов
&quot;   NAME   &quot;
&gt;&gt;&gt; f&quot;{22 / 7:&gt;10.2f}&quot;     # выравнивает в право на 10 и оставляет два знака после точки
&quot;      3.14&quot;
</code></pre>
<p>Форматирование строк может быть улучшено с помощью флагов:</p>
<pre><code class="language-pycon">&gt;&gt;&gt; f&quot;{name.upper():=^10}&quot;  # centered with 10 characters width and filled with &quot;=&quot;
&quot;===NAME===&quot;
</code></pre>
<pre><code class="language-python">&gt;&gt;&gt; class Person:
...     def __format__(self, format_spec):
...         return &quot;Person Object&quot;
... 
&gt;&gt;&gt; p = Person()
&gt;&gt;&gt; print(f&quot;{p}&quot;)
Person Object
</code></pre>
<pre><code class="language-pycon">&gt;&gt;&gt; import string
&gt;&gt;&gt; class PluralFormatter(string.Formatter):
...     def format_field(self, value, format_spec):
...         if format_spec.startswith(&quot;plural,&quot;):
...             words = format_spec.split(&quot;,&quot;)
...             if value == 1:
...                 return words[1]
...             else:
...                 return words[2]
...         else:
...             return super().format_field(value, format_spec)
...
&gt;&gt;&gt; fmt = PluralFormatter()
&gt;&gt;&gt; msg = &quot;{0} {0:plural,bottle,bottles} on the wall&quot;
&gt;&gt;&gt; for bottle_count in (99, 3, 2, 1, 0):
...     print(fmt.format(msg, bottle_count))
... 
99 bottles on the wall
3 bottles on the wall
2 bottles on the wall
1 bottle on the wall
0 bottles on the wall
</code></pre>
<p>Взято из <a href="https://digitology.tech/docs/python_3/library/string.html">https://digitology.tech/docs/python_3/library/string.html</a></p>
<h1>% strings</h1>
<table>
<thead>
<tr>
<th style="text-align: center;"></th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">%s</td>
<td style="text-align: left;">Строковое представление.</td>
</tr>
<tr>
<td style="text-align: center;">%d</td>
<td style="text-align: left;">Целое число.</td>
</tr>
<tr>
<td style="text-align: center;">%f</td>
<td style="text-align: left;">Число с плавающей точкой.</td>
</tr>
<tr>
<td style="text-align: center;">%x</td>
<td style="text-align: left;">Шестнадцатеричное представление целого числа.</td>
</tr>
<tr>
<td style="text-align: center;">%o</td>
<td style="text-align: left;">Восьмеричное представление целого числа.</td>
</tr>
</tbody>
</table>