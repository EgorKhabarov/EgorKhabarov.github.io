<p>F-строки - это новый способ форматирования строк в Python 3.6 и выше. 
Они позволяют встраивать выражения Python внутри строк посредством указания их в {} внутри строки, заключенной в f.</p>
<p>replacement_field ::=  "{" [field_name] ["!" преобразование] [":" спецификация формата] "}"
field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
arg_name          ::=  [identifier | digit+]
attribute_name    ::=  identifier
element_index     ::=  digit+ | index_string
index_string      ::=  &lt;любой исходный символ, кроме "]"&gt; +
conversion        ::=  "r" | "s" | "a"
format_spec       ::=  &lt;описано в следующем разделе&gt;</p>
<p>За field_name может следовать поле преобразования , которому предшествует восклицательный знак "!", 
и format_spec , которому предшествует двоеточие ":". 
Они определяют нестандартный формат для замещающего значения.</p>
<p>В настоящее время поддерживаются три флага преобразования: "!s" который вызывает str() значение, "!r" который вызывает repr() и "!a" который вызывает ascii().</p>
<p>Некоторые примеры:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeb5f0496a3dbbc053509a25d975c3ffb1b" onclick="copyCode(codeb5f0496a3dbbc053509a25d975c3ffb1, codeb5f0496a3dbbc053509a25d975c3ffb1b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeb5f0496a3dbbc053509a25d975c3ffb1"><div class="highlight"><pre><span></span><span class="s2">&quot;Harold&#39;s a clever </span><span class="si">{0!s}</span><span class="s2">&quot;</span>        <span class="c1"># Calls str() on the argument first</span>
<span class="s2">&quot;Bring out the holy </span><span class="si">{name!r}</span><span class="s2">&quot;</span>    <span class="c1"># Calls repr() on the argument first</span>
<span class="s2">&quot;More </span><span class="si">{!a}</span><span class="s2">&quot;</span>                      <span class="c1"># Calls ascii() on the argument first</span>
</pre></div></div></div>

<p>format_spec     ::= [[ fill] align][ sign][z][#][0][ width][ grouping_option][. precision][ type]
заполнить       ::= &lt;любой символ&gt;
выровнять       ::= "&lt;" | "&gt;" | "=" | "^"
знак            ::= "+" | "-" | " "
ширина          ::= digit+
grouping_option ::= "_" | ","
точность        ::= digit+
тип             ::= "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"</p>
<p>Вариант Значение
"<code>&lt;</code>"     Принудительно выравнивает поле по левому краю в доступном пространстве 
        (это значение по умолчанию для большинства объектов).
"<code>&gt;</code>"     Принудительно выравнивает поле по правому краю в доступном пространстве (это значение по умолчанию для чисел).
"<code>=</code>"     Принудительно размещает заполнение после знака (если есть), но перед цифрами. 
        Это используется для печати полей в форме «+000000120». 
        Этот параметр выравнивания действителен только для числовых типов. 
        Он становится значением по умолчанию для чисел, когда «0» непосредственно предшествует ширине поля.
"<code>^</code>"     Центрирует поле в доступном пространстве.
Параметр знака действителен только для числовых типов и может быть одним из следующих:</p>
<p>Вариант Значение</p>
<p>"<code>+</code>"     указывает, что знак должен использоваться как для положительных, так и для отрицательных чисел.
"<code>-</code>"     указывает, что знак следует использовать только для отрицательных чисел (это поведение по умолчанию).
spase   указывает, что перед положительными числами следует использовать начальный пробел, а перед отрицательными — знак минус.</p>
<p>Параметр "<code>z</code>" приводит отрицательные нулевые значения с плавающей запятой к положительным нулям после округления до точности формата. 
Этот параметр действителен только для типов представления с плавающей запятой.</p>
<p>Опция "<code>#</code>" приводит к использованию «альтернативной формы» для преобразования. 
          Альтернативная форма определяется по-разному для разных типов. 
          Этот параметр действителен только для целых, плавающих и сложных типов. 
          Для целых чисел, когда используется двоичный, восьмеричный или шестнадцатеричный вывод, 
          эта опция добавляет соответствующий префикс "<code>0b</code>", "<code>0o</code>", "<code>0x</code>" или "<code>0X</code>" к выходному значению. 
          Для чисел с плавающей запятой и сложных альтернативная форма приводит к тому, что результат 
          преобразования всегда содержит символ десятичной точки, даже если за ним не следуют цифры. 
          Обычно символ десятичной точки появляется в результате этих преобразований только в том случае, 
          если за ним следует цифра. Кроме того, для преобразований "<code>g</code>" и "<code>G</code>" конечные нули не удаляются из результата.
Опция "<code>,</code>" сигнализирует об использовании запятой для разделителя тысяч. 
         Для разделителя, учитывающего локаль, "<code>n</code>" вместо этого используйте целочисленный тип представления.
Опция "<code>_</code>" сигнализирует об использовании подчеркивания для разделителя тысяч для типов представления с плавающей 
         запятой и для целочисленного типа представления "<code>d</code>". 
         Для целочисленных типов представления "<code>b</code>", "<code>o</code>", "<code>x</code>"и "<code>X</code>" символы подчеркивания будут вставлены 
         через каждые 4 цифры. Для других типов презентаций указание этой опции является ошибкой.
ширина — десятичное целое число, определяющее минимальную общую ширину поля, включая все префиксы, 
         разделители и другие символы форматирования. Если не указано, то ширина поля будет определяться содержимым.
Если явное выравнивание не задано, перед полем ширины "<code>0</code>" ставится нулевой символ ( ), 
         что позволяет использовать заполнение нулями с учетом знака для числовых типов. 
         Это эквивалентно символу заполнения "<code>0</code>" с типом выравнивания "<code>=</code>" .
установка перед полем ширины "<code>0</code>" больше не влияет на выравнивание строк по умолчанию.</p>
<p>Точность представляет собой десятичное целое число , указывающее, сколько цифр должно отображаться после десятичной 
точки для типов представления "<code>f</code>" и "<code>F</code>", или до и после десятичной точки для типов представления "<code>g</code>" или "<code>G</code>". 
Для типов строкового представления поле указывает максимальный размер поля, другими словами, сколько символов 
будет использовано из содержимого поля. Точность не допускается для целочисленных типов представления .</p>
<p>Доступные типы представления строк:</p>
<p>Тип    Значение
"<code>s</code>"    Формат строки. Это тип по умолчанию для строк, и его можно опустить.
None   То же, что "<code>s</code>".</p>
<p>Доступные типы целочисленного представления:</p>
<p>Тип   Значение
"<code>b</code>"   Двоичный формат. Выводит число по основанию <code>2</code>.
"<code>c</code>"   Характер. Преобразует целое число в соответствующий символ Юникода перед печатью.
"<code>d</code>"   Десятичное целое. Выводит число в базе <code>10</code>.
"<code>o</code>"   Восьмеричный формат. Выводит число по основанию <code>8</code>.
"<code>x</code>"   Шестнадцатеричный формат. Выводит число по основанию <code>16</code>, используя строчные буквы для цифр выше <code>9</code>.
"<code>X</code>"   Шестнадцатеричный формат. Выводит число по основанию <code>16</code>, используя прописные буквы для цифр выше <code>9</code>. Если "#" указано, префикс "<code>0x</code>" также будет прописным "<code>0X</code>".
"<code>n</code>"   Число. Это то же самое "<code>d</code>", что и , за исключением того, что он использует текущую настройку локали для вставки соответствующих символов-разделителей чисел.
None  То же, что ' </p>
<p>Доступные типы представления для <code>float</code> и <code>Decimal</code> значений:</p>
<p>Тип    Значение
"<code>e</code>"    Научная нотация. Для заданной точности <code>p</code> форматирует число в экспоненте с буквой «<code>e</code>», отделяющей коэффициент от показателя степени. 
       Коэффициент имеет одну цифру до и <code>p</code> цифры после запятой, всего значащих цифр. 
       Без заданной точности использует точность цифр после запятой для и показывает все цифры коэффициента для. 
       Если за десятичной точкой не следуют цифры, десятичная точка также удаляется, если не используется этот параметр. p + 16 float Decimal
"<code>E</code>"    Научная нотация. То же, что и "<code>e</code>" за исключением того, что в качестве символа-разделителя используется заглавная буква «E».
"<code>f</code>"    Обозначение с фиксированной точкой. Для заданной точности <code>p</code> форматирует число как десятичное число, 
       в котором <code>p</code> после запятой следуют только цифры. 
       Без заданной точности использует точность 6цифр после запятой для <code>float</code> и использует точность, 
       достаточную для отображения всех цифр коэффициента для <code>Decimal</code>. 
       Если за десятичной точкой не следуют цифры, десятичная точка также удаляется, если не используется этот параметр.
"<code>F</code>"    Обозначение с фиксированной точкой. То же , что и "<code>f</code>", но преобразуется <code>nan</code> в <code>NAN</code> и <code>inf</code> в <code>INF</code>.
"<code>g</code>"    Общий формат. Для заданной точности это округляет число до значащих цифр, а затем форматирует результат 
       либо в формате с фиксированной запятой, либо в экспоненциальном представлении, в зависимости от его величины. 
       Точность рассматривается как эквивалентная точности .p &gt;= 1p01
Точные правила таковы: предположим, что результат, отформатированный с типом представления "<code>e</code>" и точностью p-1, 
будет иметь показатель степени exp. Затем, если , где -4 для чисел с плавающей запятой и -6 для , число форматируется с типом представления и точностью. 
В противном случае число форматируется с типом представления и точностью . В обоих случаях из мантиссы удаляются незначащие конечные нули, а также 
удаляется десятичная точка, если за ней не следуют оставшиеся цифры, если не используется опция.m &lt;= exp &lt; pmDecimals "<code>f</code>" p-1-exp "e" p-1 "#"
Без заданной точности использует точность 6 значащих цифр для float. При Decimal коэффициент результата формируется из цифр коэффициента значения; 
научное обозначение используется для значений, меньших 1e-6абсолютного значения, и значений, 
в которых разрядное значение младшей значащей цифры больше 1, а в противном случае используется обозначение с фиксированной запятой.
Положительная и отрицательная бесконечность, положительные и отрицательные нули и нан с форматируются и <code>inf</code> соответственно <code>-inf</code>, 0независимо от точности. -0 nan
"<code>G</code>"    Общий формат. То же, что и "<code>g</code>" за исключением переключения, "<code>E</code>" если число становится слишком большим. Представления бесконечности и NaN также в верхнем регистре.
"<code>n</code>"    Число. Это то же самое "<code>g</code>", что и , за исключением того, что он использует текущую настройку локали для вставки соответствующих символов-разделителей чисел.
"<code>%</code>"    Процент. Умножает число на 100 и отображает в фиксированном ("<code>f</code>") формате, за которым следует знак процента.
Никто  Поскольку float это то же самое "<code>g</code>", что и , за исключением того, что когда для форматирования результата используется запись с 
фиксированной точкой, он всегда включает по крайней мере одну цифру после десятичной точки. Используемая точность настолько велика, насколько это необходимо для точного представления заданного значения.
Для Decimal это то же самое, что "<code>g</code>" или "<code>G</code>" в зависимости от значения <code>context.capitals</code> для текущего десятичного контекста. 
Общий эффект заключается в том, чтобы соответствовать выходным данным <code>str()</code> , измененным другими модификаторами формата.</p>
<p>Доступ к аргументам по позиции:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code3b06033b9ac1c1a2da4d18cec207a1deb" onclick="copyCode(code3b06033b9ac1c1a2da4d18cec207a1de, code3b06033b9ac1c1a2da4d18cec207a1deb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code3b06033b9ac1c1a2da4d18cec207a1de"><div class="highlight"><pre><span></span><span class="s2">&quot;</span><span class="si">{0}</span><span class="s2">, </span><span class="si">{1}</span><span class="s2">, </span><span class="si">{2}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;a&quot;</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">,</span> <span class="s2">&quot;c&quot;</span><span class="p">)</span>
<span class="s2">&quot;a, b, c&quot;</span>
<span class="s2">&quot;</span><span class="si">{}</span><span class="s2">, </span><span class="si">{}</span><span class="s2">, </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;a&quot;</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">,</span> <span class="s2">&quot;c&quot;</span><span class="p">)</span>  <span class="c1"># 3.1+ only</span>
<span class="s2">&quot;a, b, c&quot;</span>
<span class="s2">&quot;</span><span class="si">{2}</span><span class="s2">, </span><span class="si">{1}</span><span class="s2">, </span><span class="si">{0}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;a&quot;</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">,</span> <span class="s2">&quot;c&quot;</span><span class="p">)</span>
<span class="s2">&quot;c, b, a&quot;</span>
<span class="s2">&quot;</span><span class="si">{2}</span><span class="s2">, </span><span class="si">{1}</span><span class="s2">, </span><span class="si">{0}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">*</span><span class="s2">&quot;abc&quot;</span><span class="p">)</span>      <span class="c1"># unpacking argument sequence</span>
<span class="s2">&quot;c, b, a&quot;</span>
<span class="s2">&quot;</span><span class="si">{0}{1}{0}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;abra&quot;</span><span class="p">,</span> <span class="s2">&quot;cad&quot;</span><span class="p">)</span>   <span class="c1"># arguments indices can be repeated</span>
<span class="s2">&quot;abracadabra&quot;</span>
</pre></div></div></div>

<p>Доступ к аргументам по имени:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code5f94ea38e36c3bd017dec7b22ad9c807b" onclick="copyCode(code5f94ea38e36c3bd017dec7b22ad9c807, code5f94ea38e36c3bd017dec7b22ad9c807b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code5f94ea38e36c3bd017dec7b22ad9c807"><div class="highlight"><pre><span></span><span class="s2">&quot;Coordinates: </span><span class="si">{latitude}</span><span class="s2">, </span><span class="si">{longitude}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">latitude</span><span class="o">=</span><span class="s2">&quot;37.24N&quot;</span><span class="p">,</span> <span class="n">longitude</span><span class="o">=</span><span class="s2">&quot;-115.81W&quot;</span><span class="p">)</span>
<span class="s2">&quot;Coordinates: 37.24N, -115.81W&quot;</span>
<span class="n">coord</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;latitude&quot;</span><span class="p">:</span> <span class="s2">&quot;37.24N&quot;</span><span class="p">,</span> <span class="s2">&quot;longitude&quot;</span><span class="p">:</span> <span class="s2">&quot;-115.81W&quot;</span><span class="p">}</span>
<span class="s2">&quot;Coordinates: </span><span class="si">{latitude}</span><span class="s2">, </span><span class="si">{longitude}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">coord</span><span class="p">)</span>
<span class="s2">&quot;Coordinates: 37.24N, -115.81W&quot;</span>
</pre></div></div></div>

<p>Доступ к атрибутам аргументов:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code4075c31b4b7a25c9a10b04c3e7b395ebb" onclick="copyCode(code4075c31b4b7a25c9a10b04c3e7b395eb, code4075c31b4b7a25c9a10b04c3e7b395ebb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code4075c31b4b7a25c9a10b04c3e7b395eb"><div class="highlight"><pre><span></span><span class="n">c</span> <span class="o">=</span> <span class="mi">3</span><span class="o">-</span><span class="mi">5</span><span class="n">j</span>
<span class="p">(</span><span class="s2">&quot;The complex number </span><span class="si">{0}</span><span class="s2"> is formed from the real part </span><span class="si">{0.real}</span><span class="s2"> &quot;</span>
 <span class="s2">&quot;and the imaginary part </span><span class="si">{0.imag}</span><span class="s2">.&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>
<span class="s2">&quot;The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.&quot;</span>
<span class="k">class</span> <span class="nc">Point</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">y</span> <span class="o">=</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span>
    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;Point(</span><span class="si">{self.x}</span><span class="s2">, </span><span class="si">{self.y}</span><span class="s2">)&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="o">=</span><span class="bp">self</span><span class="p">)</span>

<span class="nb">str</span><span class="p">(</span><span class="n">Point</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
<span class="s2">&quot;Point(4, 2)&quot;</span>
</pre></div></div></div>

<p>Доступ к элементам аргументов:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code99358a3291f28e558e568f23839fbd38b" onclick="copyCode(code99358a3291f28e558e568f23839fbd38, code99358a3291f28e558e568f23839fbd38b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code99358a3291f28e558e568f23839fbd38"><div class="highlight"><pre><span></span><span class="n">coord</span> <span class="o">=</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
<span class="s2">&quot;X: </span><span class="si">{0[0]}</span><span class="s2">;  Y: </span><span class="si">{0[1]}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">coord</span><span class="p">)</span>
<span class="s2">&quot;X: 3;  Y: 5&quot;</span>

<span class="n">Замена</span> <span class="err">`</span><span class="o">%</span><span class="n">s</span><span class="err">`</span> <span class="n">и</span> <span class="err">`</span><span class="o">%</span><span class="n">r</span><span class="err">`</span><span class="p">:</span>
<span class="s2">&quot;repr() shows quotes: </span><span class="si">{!r}</span><span class="s2">; str() doesn&#39;t: </span><span class="si">{!s}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;test1&quot;</span><span class="p">,</span> <span class="s2">&quot;test2&quot;</span><span class="p">)</span>
<span class="s2">&quot;repr() shows quotes: &#39;test1&#39;; str() doesn&#39;t: test2&quot;</span>
</pre></div></div></div>

<p>Выравнивание текста и указание ширины:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codef2a7f9522916d695b07d07b6a0cee519b" onclick="copyCode(codef2a7f9522916d695b07d07b6a0cee519, codef2a7f9522916d695b07d07b6a0cee519b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codef2a7f9522916d695b07d07b6a0cee519"><div class="highlight"><pre><span></span><span class="s2">&quot;</span><span class="si">{:&lt;30}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;left aligned&quot;</span><span class="p">)</span>
<span class="s2">&quot;left aligned                  &quot;</span>
<span class="s2">&quot;</span><span class="si">{:&gt;30}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;right aligned&quot;</span><span class="p">)</span>
<span class="s2">&quot;                 right aligned&quot;</span>
<span class="s2">&quot;</span><span class="si">{:^30}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;centered&quot;</span><span class="p">)</span>
<span class="s2">&quot;           centered           &quot;</span>
<span class="s2">&quot;</span><span class="si">{:*^30}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;centered&quot;</span><span class="p">)</span>  <span class="c1"># use &quot;*&quot; as a fill char</span>
<span class="s2">&quot;***********centered***********&quot;</span>
</pre></div></div></div>

<p>Замена %+f, %-f, и и указание знака:% f</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeeb948facea3093943b060e18304886e1b" onclick="copyCode(codeeb948facea3093943b060e18304886e1, codeeb948facea3093943b060e18304886e1b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeeb948facea3093943b060e18304886e1"><div class="highlight"><pre><span></span><span class="s2">&quot;</span><span class="si">{:+f}</span><span class="s2">; </span><span class="si">{:+f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mf">3.14</span><span class="p">,</span> <span class="o">-</span><span class="mf">3.14</span><span class="p">)</span>  <span class="c1"># show it always</span>
<span class="s2">&quot;+3.140000; -3.140000&quot;</span>
<span class="s2">&quot;</span><span class="si">{: f}</span><span class="s2">; </span><span class="si">{: f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mf">3.14</span><span class="p">,</span> <span class="o">-</span><span class="mf">3.14</span><span class="p">)</span>  <span class="c1"># show a space for positive numbers</span>
<span class="s2">&quot; 3.140000; -3.140000&quot;</span>
<span class="s2">&quot;</span><span class="si">{:-f}</span><span class="s2">; </span><span class="si">{:-f}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mf">3.14</span><span class="p">,</span> <span class="o">-</span><span class="mf">3.14</span><span class="p">)</span>  <span class="c1"># show only the minus -- same as &quot;{:f}; {:f}&quot;</span>
<span class="s2">&quot;3.140000; -3.140000&quot;</span>
</pre></div></div></div>

<p>Замена <code>%x</code> и <code>%o</code> преобразование значения в разные базы:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code05b5939c971e388ed1a670200a327e5fb" onclick="copyCode(code05b5939c971e388ed1a670200a327e5f, code05b5939c971e388ed1a670200a327e5fb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code05b5939c971e388ed1a670200a327e5f"><div class="highlight"><pre><span></span><span class="c1"># format also supports binary numbers</span>
<span class="s2">&quot;int: </span><span class="si">{0:d}</span><span class="s2">;  hex: </span><span class="si">{0:x}</span><span class="s2">;  oct: </span><span class="si">{0:o}</span><span class="s2">;  bin: </span><span class="si">{0:b}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>
<span class="s2">&quot;int: 42;  hex: 2a;  oct: 52;  bin: 101010&quot;</span>
<span class="c1"># with 0x, 0o, or 0b as prefix:</span>
<span class="s2">&quot;int: </span><span class="si">{0:d}</span><span class="s2">;  hex: </span><span class="si">{0:#x}</span><span class="s2">;  oct: </span><span class="si">{0:#o}</span><span class="s2">;  bin: </span><span class="si">{0:#b}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>
<span class="s2">&quot;int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010&quot;</span>
</pre></div></div></div>

<p>Использование запятой в качестве разделителя тысяч:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code7a205b325a283ea30319e13b596540cfb" onclick="copyCode(code7a205b325a283ea30319e13b596540cf, code7a205b325a283ea30319e13b596540cfb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code7a205b325a283ea30319e13b596540cf"><div class="highlight"><pre><span></span><span class="s2">&quot;</span><span class="si">{:,}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mi">1234567890</span><span class="p">)</span>
<span class="s2">&quot;1,234,567,890&quot;</span>
</pre></div></div></div>

<p>Выражение процента:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeab02dafe2d3488432535e345e96dd3b0b" onclick="copyCode(codeab02dafe2d3488432535e345e96dd3b0, codeab02dafe2d3488432535e345e96dd3b0b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeab02dafe2d3488432535e345e96dd3b0"><div class="highlight"><pre><span></span><span class="n">points</span> <span class="o">=</span> <span class="mi">19</span>
<span class="n">total</span> <span class="o">=</span> <span class="mi">22</span>
<span class="s2">&quot;Correct answers: </span><span class="si">{:.2%}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">points</span><span class="o">/</span><span class="n">total</span><span class="p">)</span>
<span class="s2">&quot;Correct answers: 86.36%&quot;</span>
</pre></div></div></div>

<p>Использование форматирования для конкретного типа:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code95fff9a3fb8cb366c5ab65abdc7b48f8b" onclick="copyCode(code95fff9a3fb8cb366c5ab65abdc7b48f8, code95fff9a3fb8cb366c5ab65abdc7b48f8b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code95fff9a3fb8cb366c5ab65abdc7b48f8"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">datetime</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2010</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">12</span><span class="p">,</span> <span class="mi">15</span><span class="p">,</span> <span class="mi">58</span><span class="p">)</span>
<span class="s2">&quot;{:%Y-%m-</span><span class="si">%d</span><span class="s2"> %H:%M:%S}&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>
<span class="s2">&quot;2010-07-04 12:15:58&quot;</span>
</pre></div></div></div>

<p>Вложенные аргументы и более сложные примеры:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code6c496ff4d8e9f808de8e4798d11df3b3b" onclick="copyCode(code6c496ff4d8e9f808de8e4798d11df3b3, code6c496ff4d8e9f808de8e4798d11df3b3b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code6c496ff4d8e9f808de8e4798d11df3b3"><div class="highlight"><pre><span></span><span class="k">for</span> <span class="n">align</span><span class="p">,</span> <span class="n">text</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="s2">&quot;&lt;^&gt;&quot;</span><span class="p">,</span> <span class="p">[</span><span class="s2">&quot;left&quot;</span><span class="p">,</span> <span class="s2">&quot;center&quot;</span><span class="p">,</span> <span class="s2">&quot;right&quot;</span><span class="p">]):</span>
    <span class="s2">&quot;{0:</span><span class="si">{fill}{align}</span><span class="s2">16}&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">fill</span><span class="o">=</span><span class="n">align</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="n">align</span><span class="p">)</span>

<span class="s2">&quot;left&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&quot;</span>
<span class="s2">&quot;^^^^^center^^^^^&quot;</span>
<span class="s2">&quot;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;right&quot;</span>
<span class="n">octets</span> <span class="o">=</span> <span class="p">[</span><span class="mi">192</span><span class="p">,</span> <span class="mi">168</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span>
<span class="s2">&quot;</span><span class="si">{:02X}{:02X}{:02X}{:02X}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">*</span><span class="n">octets</span><span class="p">)</span>
<span class="s2">&quot;C0A80001&quot;</span>
<span class="nb">int</span><span class="p">(</span><span class="n">_</span><span class="p">,</span> <span class="mi">16</span><span class="p">)</span>
<span class="mi">3232235521</span>
<span class="n">width</span> <span class="o">=</span> <span class="mi">5</span>
<span class="k">for</span> <span class="n">num</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">12</span><span class="p">):</span> 
    <span class="k">for</span> <span class="n">base</span> <span class="ow">in</span> <span class="s2">&quot;dXob&quot;</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;{0:</span><span class="si">{width}{base}</span><span class="s2">}&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">num</span><span class="p">,</span> <span class="n">base</span><span class="o">=</span><span class="n">base</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">),</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">()</span>

<span class="c1">#    5     5     5   101</span>
<span class="c1">#    6     6     6   110</span>
<span class="c1">#    7     7     7   111</span>
<span class="c1">#    8     8    10  1000</span>
<span class="c1">#    9     9    11  1001</span>
<span class="c1">#   10     A    12  1010</span>
<span class="c1">#   11     B    13  1011</span>
</pre></div></div></div>

<p>Форматирование чисел:
Для вывода количества знаков после запятой можно использовать флаг f:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codecf4591cffe2a98c0f1c117c64f0475a3b" onclick="copyCode(codecf4591cffe2a98c0f1c117c64f0475a3, codecf4591cffe2a98c0f1c117c64f0475a3b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codecf4591cffe2a98c0f1c117c64f0475a3"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;pi </span><span class="si">{</span><span class="mi">22</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">7</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Форматирование строк:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code38aa5af28a75b6126eff48613625b712b" onclick="copyCode(code38aa5af28a75b6126eff48613625b712, code38aa5af28a75b6126eff48613625b712b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code38aa5af28a75b6126eff48613625b712"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">:</span><span class="s2">&lt;10</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># выравнивается в лево на 10 символов</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">:</span><span class="s2">&gt;10</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># выравнивается в право на 10 символов</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">:</span><span class="s2">^10</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># выравнивается по центру шириной 10 символов</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="mi">22</span><span class="o">/</span><span class="mi">7</span><span class="si">:</span><span class="s2">&gt;10.2f</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>       <span class="c1"># выравнивает в право на 10 и оставляет два знака после точки</span>
</pre></div></div></div>

<p>Форматирование строк может быть улучшено с помощью флагов:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codead9cffdf70b936f90885129c6e632865b" onclick="copyCode(codead9cffdf70b936f90885129c6e632865, codead9cffdf70b936f90885129c6e632865b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codead9cffdf70b936f90885129c6e632865"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">:</span><span class="s2">=^10</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># CENTERED WITH 10 CHARACTERS WIDTH AND FILLED WITH &quot;=&quot;</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeba5e1b657a715c99b694d30a2d2bf839b" onclick="copyCode(codeba5e1b657a715c99b694d30a2d2bf839, codeba5e1b657a715c99b694d30a2d2bf839b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeba5e1b657a715c99b694d30a2d2bf839"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Person</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__format__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">format_spec</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;Person Object&quot;</span>

<span class="n">p</span> <span class="o">=</span> <span class="n">Person</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">p</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># Person Object</span>
</pre></div></div></div>