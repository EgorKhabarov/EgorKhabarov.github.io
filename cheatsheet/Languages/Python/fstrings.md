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
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="mi">1</span><span class="si">:}</span><span class="s2">&gt;20</span><span class="si">}</span><span class="s2">&quot;</span>
<span class="unselectable">  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span></span>
<span class="unselectable"><span class="w">    </span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="mi">1</span><span class="si">:}</span><span class="s2">&gt;20</span><span class="si">}</span><span class="s2">&quot;</span></span>
<span class="unselectable"><span class="w">               </span><span class="pm">^</span></span>
<span class="unselectable"><span class="gr">SyntaxError</span>: <span class="n">f-string: single &#39;}&#39; is not allowed</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="mi">1</span><span class="si">:</span><span class="se">}}</span><span class="s2">&gt;20</span><span class="si">}</span><span class="s2">&quot;</span>
<span class="unselectable">  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span></span>
<span class="unselectable"><span class="w">    </span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="mi">1</span><span class="si">:</span><span class="se">}}</span><span class="s2">&gt;20</span><span class="si">}</span><span class="s2">&quot;</span></span>
<span class="unselectable"><span class="w">                </span><span class="pm">^</span></span>
<span class="unselectable"><span class="gr">SyntaxError</span>: <span class="n">f-string: single &#39;}&#39; is not allowed</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="mi">1</span><span class="si">:{</span><span class="s1">&#39;}&#39;</span><span class="si">}</span><span class="s2">&gt;20</span><span class="si">}</span><span class="s2">&quot;</span>
<span class="unselectable"><span class="go">&quot;}}}}}}}}}}}}}}}}}}}1&quot;</span>
</span></pre></div></div></div>
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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="s2">&quot;Сначала посчитай до </span><span class="si">{0}</span><span class="s2">&quot;</span>         <span class="c1"># Ссылки на первый позиционный аргумент</span>
<span class="s2">&quot;Принеси мне </span><span class="si">{}</span><span class="s2">&quot;</span>                  <span class="c1"># Неявно ссылается на первый позиционный аргумент</span>
<span class="s2">&quot;От </span><span class="si">{}</span><span class="s2"> до </span><span class="si">{}</span><span class="s2">&quot;</span>                     <span class="c1"># То же, что &quot;От {0} до {1}&quot;</span>
<span class="s2">&quot;Мой квест </span><span class="si">{name}</span><span class="s2">&quot;</span>                <span class="c1"># Ссылка на ключевой аргумент «name»</span>
<span class="s2">&quot;Масса в тоннах </span><span class="si">{0.weight}</span><span class="s2">&quot;</span>       <span class="c1"># атрибут «weight» первого позиционного аргумента</span>
<span class="s2">&quot;Уничтожено единиц: </span><span class="si">{players[0]}</span><span class="s2">&quot;</span> <span class="c1"># Первый элемент ключевого аргумента «players».</span>

<span class="s2">&quot;Гарольд умный </span><span class="si">{0!s}</span><span class="s2">&quot;</span>             <span class="c1"># Сначала вызывает str() для первого аргумента</span>
<span class="s2">&quot;Принесите святую </span><span class="si">{name!r}</span><span class="s2">&quot;</span>       <span class="c1"># Сначала вызывает repr() для первого аргумента</span>
<span class="s2">&quot;Больше </span><span class="si">{!a}</span><span class="s2">&quot;</span>                     <span class="c1"># Сначала вызывает ascii() для первого аргумента</span>
</pre></div></div></div>

<p>Доступ к аргументам по позиции:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;</span><span class="si">{0}</span><span class="s2">, </span><span class="si">{1}</span><span class="s2">, </span><span class="si">{2}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;a&quot;</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">,</span> <span class="s2">&quot;c&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;a, b, c&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="s2">&quot;</span><span class="si">{}</span><span class="s2">, </span><span class="si">{}</span><span class="s2">, </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;a&quot;</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">,</span> <span class="s2">&quot;c&quot;</span><span class="p">)</span>  <span class="c1"># 3.1+ python version only</span>
<span class="unselectable"><span class="go">&quot;a, b, c&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="s2">&quot;</span><span class="si">{2}</span><span class="s2">, </span><span class="si">{1}</span><span class="s2">, </span><span class="si">{0}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;a&quot;</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">,</span> <span class="s2">&quot;c&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;c, b, a&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="s2">&quot;</span><span class="si">{2}</span><span class="s2">, </span><span class="si">{1}</span><span class="s2">, </span><span class="si">{0}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">*</span><span class="s2">&quot;abc&quot;</span><span class="p">)</span>      <span class="c1"># unpacking argument sequence</span>
<span class="unselectable"><span class="go">&quot;c, b, a&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="s2">&quot;</span><span class="si">{0}{1}{0}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;abra&quot;</span><span class="p">,</span> <span class="s2">&quot;cad&quot;</span><span class="p">)</span>   <span class="c1"># arguments indices can be repeated</span>
<span class="unselectable"><span class="go">&quot;abracadabra&quot;</span>
</span></pre></div></div></div>

<p>Доступ к аргументам по имени:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;Coordinates: </span><span class="si">{latitude}</span><span class="s2">, </span><span class="si">{longitude}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">latitude</span><span class="o">=</span><span class="s2">&quot;37.24N&quot;</span><span class="p">,</span> <span class="n">longitude</span><span class="o">=</span><span class="s2">&quot;-115.81W&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;Coordinates: 37.24N, -115.81W&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">coord</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;latitude&quot;</span><span class="p">:</span> <span class="s2">&quot;37.24N&quot;</span><span class="p">,</span> <span class="s2">&quot;longitude&quot;</span><span class="p">:</span> <span class="s2">&quot;-115.81W&quot;</span><span class="p">}</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;Coordinates: </span><span class="si">{latitude}</span><span class="s2">, </span><span class="si">{longitude}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">coord</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;Coordinates: 37.24N, -115.81W&quot;</span>
</span></pre></div></div></div>

<p>Доступ к атрибутам аргументов:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">c</span> <span class="o">=</span> <span class="mi">3</span><span class="o">-</span><span class="mi">5</span><span class="n">j</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="p">(</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="s2">&quot;The complex number </span><span class="si">{0}</span><span class="s2"> is formed from the real part </span><span class="si">{0.real}</span><span class="s2"> &quot;</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="s2">&quot;and the imaginary part </span><span class="si">{0.imag}</span><span class="s2">.&quot;</span>
<span class="unselectable"><span class="o">...</span> </span><span class="p">)</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;The complex number 3-5j is formed from the real part 3.0 and the imaginary part -5.0.&quot;</span>
</span></pre></div></div></div>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">class</span> <span class="nc">Point</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="bp">self</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">y</span> <span class="o">=</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="k">return</span> <span class="s2">&quot;Point(</span><span class="si">{self.x}</span><span class="s2">, </span><span class="si">{self.y}</span><span class="s2">)&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="o">=</span><span class="bp">self</span><span class="p">)</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">str</span><span class="p">(</span><span class="n">Point</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
<span class="unselectable"><span class="go">&quot;Point(4, 2)&quot;</span>
</span></pre></div></div></div>

<p>Доступ к элементам аргументов:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;X: </span><span class="si">{0[0]}</span><span class="s2">;  Y: </span><span class="si">{0[1]}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">((</span><span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">))</span>
<span class="unselectable"><span class="go">&quot;X: 3;  Y: 5&quot;</span>
</span></pre></div></div></div>
<p>Замена <code>%s</code> и <code>%r</code>:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;repr() shows quotes: </span><span class="si">{!r}</span><span class="s2">; str() doesn&#39;t: </span><span class="si">{!s}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;test1&quot;</span><span class="p">,</span> <span class="s2">&quot;test2&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;repr() shows quotes: &#39;test1&#39;; str() doesn&#39;t: test2&quot;</span>
</span></pre></div></div></div>

<p>Выравнивание текста и указание ширины:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;</span><span class="si">{:&lt;30}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;left aligned&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;left aligned                  &quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="s2">&quot;</span><span class="si">{:&gt;30}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;right aligned&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;                 right aligned&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="s2">&quot;</span><span class="si">{:^30}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;centered&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;           centered           &quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="s2">&quot;</span><span class="si">{:*^30}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;centered&quot;</span><span class="p">)</span>  <span class="c1"># use &quot;*&quot; as a fill char</span>
<span class="unselectable"><span class="go">&quot;***********centered***********&quot;</span>
</span></pre></div></div></div>

<p>Замена <code>%+f</code>, <code>%-f</code>, и и указание знака: <code>%</code> <code>f</code></p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;</span><span class="si">{:+f}</span><span class="s2">; </span><span class="si">{:+f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mf">3.14</span><span class="p">,</span> <span class="o">-</span><span class="mf">3.14</span><span class="p">)</span>  <span class="c1"># show it always</span>
<span class="unselectable"><span class="go">&quot;+3.140000; -3.140000&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="s2">&quot;</span><span class="si">{: f}</span><span class="s2">; </span><span class="si">{: f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mf">3.14</span><span class="p">,</span> <span class="o">-</span><span class="mf">3.14</span><span class="p">)</span>  <span class="c1"># show a space for positive numbers</span>
<span class="unselectable"><span class="go">&quot; 3.140000; -3.140000&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="s2">&quot;</span><span class="si">{:-f}</span><span class="s2">; </span><span class="si">{:-f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mf">3.14</span><span class="p">,</span> <span class="o">-</span><span class="mf">3.14</span><span class="p">)</span>  <span class="c1"># show only the minus -- same as &quot;{:f}; {:f}&quot;</span>
<span class="unselectable"><span class="go">&quot;3.140000; -3.140000&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;</span><span class="si">{:-.2f}</span><span class="s2">; </span><span class="si">{:-.2f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mf">3.14</span><span class="p">,</span> <span class="o">-</span><span class="mf">3.14</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;3.14; -3.14&quot;</span>
</span></pre></div></div></div>

<p>Замена <code>%x</code> и <code>%o</code> преобразование значения в разные базы:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># format also supports binary numbers</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;int: </span><span class="si">{0:d}</span><span class="s2">;  hex: </span><span class="si">{0:x}</span><span class="s2">;  oct: </span><span class="si">{0:o}</span><span class="s2">;  bin: </span><span class="si">{0:b}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;int: 42;  hex: 2a;  oct: 52;  bin: 101010&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="c1"># with 0x, 0o, or 0b as prefix:</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;int: </span><span class="si">{0:d}</span><span class="s2">;  hex: </span><span class="si">{0:#x}</span><span class="s2">;  oct: </span><span class="si">{0:#o}</span><span class="s2">;  bin: </span><span class="si">{0:#b}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010&quot;</span>
</span></pre></div></div></div>

<p>Использование запятой или подчёркивания в качестве разделителя тысяч:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;</span><span class="si">{:,}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mi">1234567890</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;1,234,567,890&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="s2">&quot;{:_}&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mi">1234567890</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;1_234_567_890&quot;</span>
</span></pre></div></div></div>

<p>Выражение процента:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">points</span><span class="p">,</span> <span class="n">total</span> <span class="o">=</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">22</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;Correct answers: </span><span class="si">{:.2%}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">points</span><span class="o">/</span><span class="n">total</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;Correct answers: 86.36%&quot;</span>
</span></pre></div></div></div>

<p>Использование форматирования для конкретного типа:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">datetime</span> <span class="kn">import</span> <span class="n">datetime</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;{:%Y-%m-</span><span class="si">%d</span><span class="s2"> %H:%M:%S}&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2010</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">12</span><span class="p">,</span> <span class="mi">15</span><span class="p">,</span> <span class="mi">58</span><span class="p">))</span>
<span class="unselectable"><span class="go">&quot;2010-07-04 12:15:58&quot;</span>
</span></pre></div></div></div>

<p>Вложенные аргументы и более сложные примеры:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">for</span> <span class="n">align</span><span class="p">,</span> <span class="n">text</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="s2">&quot;&lt;^&gt;&quot;</span><span class="p">,</span> <span class="p">[</span><span class="s2">&quot;left&quot;</span><span class="p">,</span> <span class="s2">&quot;center&quot;</span><span class="p">,</span> <span class="s2">&quot;right&quot;</span><span class="p">]):</span>
<span class="unselectable"><span class="o">...</span> </span>   <span class="s2">&quot;{0:</span><span class="si">{fill}{align}</span><span class="s2">16}&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">fill</span><span class="o">=</span><span class="n">align</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="n">align</span><span class="p">)</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="go">&quot;left&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&quot;</span>
<span class="go">&quot;^^^^^center^^^^^&quot;</span>
<span class="go">&quot;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;right&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">octets</span> <span class="o">=</span> <span class="p">[</span><span class="mi">192</span><span class="p">,</span> <span class="mi">168</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;</span><span class="si">{:02X}{:02X}{:02X}{:02X}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">*</span><span class="n">octets</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;C0A80001&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="nb">int</span><span class="p">(</span><span class="n">_</span><span class="p">,</span> <span class="mi">16</span><span class="p">)</span>
<span class="unselectable"><span class="go">3232235521</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">width</span> <span class="o">=</span> <span class="mi">5</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">for</span> <span class="n">num</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">12</span><span class="p">):</span> 
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">for</span> <span class="n">base</span> <span class="ow">in</span> <span class="s2">&quot;dXob&quot;</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;{0:</span><span class="si">{width}{base}</span><span class="s2">}&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">num</span><span class="p">,</span> <span class="n">base</span><span class="o">=</span><span class="n">base</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">),</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">()</span>
<span class="unselectable"><span class="o">...</span> </span>
<span class="unselectable"><span class="go">    5     5     5   101</span>
<span class="go">    6     6     6   110</span>
<span class="go">    7     7     7   111</span>
<span class="go">    8     8    10  1000</span>
<span class="go">    9     9    11  1001</span>
<span class="go">   10     A    12  1010</span>
<span class="go">   11     B    13  1011</span>
</span></pre></div></div></div>

<p>Форматирование чисел:
Для вывода количества знаков после запятой можно использовать флаг f:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="sa">f</span><span class="s2">&quot;pi </span><span class="si">{</span><span class="mi">22</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">7</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">&quot;</span>
<span class="unselectable"><span class="go">&quot;pi 3.14&quot;</span>
</span></pre></div></div></div>

<p>Форматирование строк:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;Name&quot;</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">:</span><span class="s2">&lt;10</span><span class="si">}</span><span class="s2">&quot;</span>  <span class="c1"># выравнивается в лево на 10 символов</span>
<span class="unselectable"><span class="go">&quot;NAME      &quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">:</span><span class="s2">&gt;10</span><span class="si">}</span><span class="s2">&quot;</span>  <span class="c1"># выравнивается в право на 10 символов</span>
<span class="unselectable"><span class="go">&quot;      NAME&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">:</span><span class="s2">^10</span><span class="si">}</span><span class="s2">&quot;</span>  <span class="c1"># выравнивается по центру шириной 10 символов</span>
<span class="unselectable"><span class="go">&quot;   NAME   &quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="mi">22</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">7</span><span class="si">:</span><span class="s2">&gt;10.2f</span><span class="si">}</span><span class="s2">&quot;</span>     <span class="c1"># выравнивает в право на 10 и оставляет два знака после точки</span>
<span class="unselectable"><span class="go">&quot;      3.14&quot;</span>
</span></pre></div></div></div>

<p>Форматирование строк может быть улучшено с помощью флагов:</p>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">:</span><span class="s2">=^10</span><span class="si">}</span><span class="s2">&quot;</span>  <span class="c1"># centered with 10 characters width and filled with &quot;=&quot;</span>
<span class="unselectable"><span class="go">&quot;===NAME===&quot;</span>
</span></pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">class</span> <span class="nc">Person</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">def</span> <span class="fm">__format__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">format_spec</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="k">return</span> <span class="s2">&quot;Person Object&quot;</span>
<span class="unselectable"><span class="o">...</span> </span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">p</span> <span class="o">=</span> <span class="n">Person</span><span class="p">()</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">p</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="n">Person</span> <span class="n">Object</span></span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">import</span> <span class="nn">string</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">class</span> <span class="nc">PluralFormatter</span><span class="p">(</span><span class="n">string</span><span class="o">.</span><span class="n">Formatter</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">def</span> <span class="nf">format_field</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">format_spec</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="k">if</span> <span class="n">format_spec</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">&quot;plural,&quot;</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>            <span class="n">words</span> <span class="o">=</span> <span class="n">format_spec</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;,&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>            <span class="k">if</span> <span class="n">value</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>                <span class="k">return</span> <span class="n">words</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
<span class="unselectable"><span class="o">...</span> </span>            <span class="k">else</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>                <span class="k">return</span> <span class="n">words</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="k">else</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>            <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">format_field</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">format_spec</span><span class="p">)</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">fmt</span> <span class="o">=</span> <span class="n">PluralFormatter</span><span class="p">()</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">msg</span> <span class="o">=</span> <span class="s2">&quot;</span><span class="si">{0}</span><span class="s2"> {0:plural,bottle,bottles} on the wall&quot;</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">for</span> <span class="n">bottle_count</span> <span class="ow">in</span> <span class="p">(</span><span class="mi">99</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">(</span><span class="n">fmt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">msg</span><span class="p">,</span> <span class="n">bottle_count</span><span class="p">))</span>
<span class="unselectable"><span class="o">...</span> </span>
<span class="unselectable"><span class="go">99 bottles on the wall</span>
<span class="go">3 bottles on the wall</span>
<span class="go">2 bottles on the wall</span>
<span class="go">1 bottle on the wall</span>
<span class="go">0 bottles on the wall</span>
</span></pre></div></div></div>

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