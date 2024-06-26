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
<p>За field_name может следовать поле преобразования , которому предшествует восклицательный знак '!', 
и format_spec , которому предшествует двоеточие ':'. 
Они определяют нестандартный формат для замещающего значения.</p>
<p>В настоящее время поддерживаются три флага преобразования: '!s'который вызывает str() значение, '!r'который вызывает repr() и '!a'который вызывает ascii().</p>
<p>Некоторые примеры:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code481b" onclick="copyCode(code481, code481b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code481"><div class="highlight"><pre><span></span><span class="s2">&quot;Harold&#39;s a clever </span><span class="si">{0!s}</span><span class="s2">&quot;</span>        <span class="c1"># Calls str() on the argument first</span>
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
'<code>&lt;</code>'     Принудительно выравнивает поле по левому краю в доступном пространстве 
        (это значение по умолчанию для большинства объектов).
'<code>&gt;</code>'     Принудительно выравнивает поле по правому краю в доступном пространстве (это значение по умолчанию для чисел).
'<code>=</code>'     Принудительно размещает заполнение после знака (если есть), но перед цифрами. 
        Это используется для печати полей в форме «+000000120». 
        Этот параметр выравнивания действителен только для числовых типов. 
        Он становится значением по умолчанию для чисел, когда «0» непосредственно предшествует ширине поля.
'<code>^</code>'     Центрирует поле в доступном пространстве.
Параметр знака действителен только для числовых типов и может быть одним из следующих:</p>
<p>Вариант Значение</p>
<p>'<code>+</code>'     указывает, что знак должен использоваться как для положительных, так и для отрицательных чисел.
'<code>-</code>'     указывает, что знак следует использовать только для отрицательных чисел (это поведение по умолчанию).
spase   указывает, что перед положительными числами следует использовать начальный пробел, а перед отрицательными — знак минус.</p>
<p>Параметр '<code>z</code>' приводит отрицательные нулевые значения с плавающей запятой к положительным нулям после округления до точности формата. 
Этот параметр действителен только для типов представления с плавающей запятой.</p>
<p>Опция '<code>#</code>' приводит к использованию «альтернативной формы» для преобразования. 
          Альтернативная форма определяется по-разному для разных типов. 
          Этот параметр действителен только для целых, плавающих и сложных типов. 
          Для целых чисел, когда используется двоичный, восьмеричный или шестнадцатеричный вывод, 
          эта опция добавляет соответствующий префикс '<code>0b</code>', '<code>0o</code>', '<code>0x</code>'или '<code>0X</code>'к выходному значению. 
          Для чисел с плавающей запятой и сложных альтернативная форма приводит к тому, что результат 
          преобразования всегда содержит символ десятичной точки, даже если за ним не следуют цифры. 
          Обычно символ десятичной точки появляется в результате этих преобразований только в том случае, 
          если за ним следует цифра. Кроме того, для преобразований '<code>g</code>'и '<code>G</code>' конечные нули не удаляются из результата.
Опция '<code>,</code>'сигнализирует об использовании запятой для разделителя тысяч. 
         Для разделителя, учитывающего локаль, '<code>n</code>' вместо этого используйте целочисленный тип представления.
Опция '<code>_</code>'сигнализирует об использовании подчеркивания для разделителя тысяч для типов представления с плавающей 
         запятой и для целочисленного типа представления '<code>d</code>'. 
         Для целочисленных типов представления '<code>b</code>', '<code>o</code>', '<code>x</code>'и '<code>X</code>'символы подчеркивания будут вставлены 
         через каждые 4 цифры. Для других типов презентаций указание этой опции является ошибкой.
ширина — десятичное целое число, определяющее минимальную общую ширину поля, включая все префиксы, 
         разделители и другие символы форматирования. Если не указано, то ширина поля будет определяться содержимым.
Если явное выравнивание не задано, перед полем ширины'<code>0</code>' ставится нулевой символ ( ), 
         что позволяет использовать заполнение нулями с учетом знака для числовых типов. 
         Это эквивалентно символу заполнения'<code>0</code>' с типом выравнивания'<code>=</code>' .
установка перед полем ширины '<code>0</code>' больше не влияет на выравнивание строк по умолчанию.</p>
<p>Точность представляет собой десятичное целое число , указывающее, сколько цифр должно отображаться после десятичной 
точки для типов представления '<code>f</code>'и '<code>F</code>', или до и после десятичной точки для типов представления '<code>g</code>'или '<code>G</code>'. 
Для типов строкового представления поле указывает максимальный размер поля, другими словами, сколько символов 
будет использовано из содержимого поля. Точность не допускается для целочисленных типов представления .</p>
<p>Доступные типы представления строк:</p>
<p>Тип    Значение
'<code>s</code>'    Формат строки. Это тип по умолчанию для строк, и его можно опустить.
None   То же, что '<code>s</code>'.</p>
<p>Доступные типы целочисленного представления:</p>
<p>Тип   Значение
'<code>b</code>'   Двоичный формат. Выводит число по основанию 2.
'<code>c</code>'   Характер. Преобразует целое число в соответствующий символ Юникода перед печатью.
'<code>d</code>'   Десятичное целое. Выводит число в базе 10.
'<code>o</code>'   Восьмеричный формат. Выводит число по основанию 8.
'<code>x</code>'   Шестнадцатеричный формат. Выводит число по основанию 16, используя строчные буквы для цифр выше 9.
'<code>X</code>'   Шестнадцатеричный формат. Выводит число по основанию 16, используя прописные буквы для цифр выше 9. Если '#' указано, префикс '0x' также будет прописным '0X'.
'<code>n</code>'   Число. Это то же самое '<code>d</code>', что и , за исключением того, что он использует текущую настройку локали для вставки соответствующих символов-разделителей чисел.
None  То же, что ' </p>
<p>Доступные типы представления для floatи Decimalзначений:</p>
<p>Тип    Значение
'<code>e</code>'    Научная нотация. Для заданной точности pформатирует число в экспоненте с буквой «e», отделяющей коэффициент от показателя степени. 
       Коэффициент имеет одну цифру до и pцифры после запятой, всего значащих цифр. 
       Без заданной точности использует точность цифр после запятой для и показывает все цифры коэффициента для. 
       Если за десятичной точкой не следуют цифры, десятичная точка также удаляется, если не используется этот параметр.p + 16floatDecimal#
'<code>E</code>'    Научная нотация. То же, что и '<code>e</code>' за исключением того, что в качестве символа-разделителя используется заглавная буква «E».
'<code>f</code>'    Обозначение с фиксированной точкой. Для заданной точности pформатирует число как десятичное число, 
       в котором pпосле запятой следуют только цифры. 
       Без заданной точности использует точность 6цифр после запятой для floatи использует точность, 
       достаточную для отображения всех цифр коэффициента для Decimal. 
       Если за десятичной точкой не следуют цифры, десятичная точка также удаляется, если не #используется этот параметр.
'<code>F</code>'    Обозначение с фиксированной точкой. То же , что и '<code>f</code>', но преобразуется nanв NANи infв INF.
'<code>g</code>'    Общий формат. Для заданной точности это округляет число до значащих цифр, а затем форматирует результат 
       либо в формате с фиксированной запятой, либо в экспоненциальном представлении, в зависимости от его величины. 
       Точность рассматривается как эквивалентная точности .p &gt;= 1p01
Точные правила таковы: предположим, что результат, отформатированный с типом представления '<code>e</code>' и точностью p-1, 
будет иметь показатель степени exp. Затем, если , где -4 для чисел с плавающей запятой и -6 для , число форматируется с типом представления и точностью . 
В противном случае число форматируется с типом представления и точностью . В обоих случаях из мантиссы удаляются незначащие конечные нули, а также 
удаляется десятичная точка, если за ней не следуют оставшиеся цифры, если не используется опция.m &lt;= exp &lt; pmDecimals 'f' p-1-exp 'e' p-1 '#'
Без заданной точности использует точность 6 значащих цифр для float. При Decimalкоэффициент результата формируется из цифр коэффициента значения; 
научное обозначение используется для значений, меньших 1e-6абсолютного значения, и значений, 
в которых разрядное значение младшей значащей цифры больше 1, а в противном случае используется обозначение с фиксированной запятой.
Положительная и отрицательная бесконечность, положительные и отрицательные нули и нанс форматируются как , , и infсоответственно -inf, 0независимо от точности.-0nan
'<code>G</code>'    Общий формат. То же, что и '<code>g</code>' за исключением переключения, '<code>E</code>' если число становится слишком большим. Представления бесконечности и NaN также в верхнем регистре.
'<code>n</code>'    Число. Это то же самое '<code>g</code>', что и , за исключением того, что он использует текущую настройку локали для вставки соответствующих символов-разделителей чисел.
'<code>%</code>'    Процент. Умножает число на 100 и отображает в фиксированном ('<code>f</code>') формате, за которым следует знак процента.
Никто  Поскольку floatэто то же самое '<code>g</code>', что и , за исключением того, что когда для форматирования результата используется запись с 
фиксированной точкой, он всегда включает по крайней мере одну цифру после десятичной точки. Используемая точность настолько велика, насколько это необходимо для точного представления заданного значения.
Для Decimalэто то же самое, что '<code>g</code>' или '<code>G</code>' в зависимости от значения context.capitalsдля текущего десятичного контекста. 
Общий эффект заключается в том, чтобы соответствовать выходным данным str() , измененным другими модификаторами формата.</p>
<p>Доступ к аргументам по позиции:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code482b" onclick="copyCode(code482, code482b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code482"><div class="highlight"><pre><span></span><span class="s1">&#39;</span><span class="si">{0}</span><span class="s1">, </span><span class="si">{1}</span><span class="s1">, </span><span class="si">{2}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">)</span>
<span class="s1">&#39;a, b, c&#39;</span>
<span class="s1">&#39;</span><span class="si">{}</span><span class="s1">, </span><span class="si">{}</span><span class="s1">, </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">)</span>  <span class="c1"># 3.1+ only</span>
<span class="s1">&#39;a, b, c&#39;</span>
<span class="s1">&#39;</span><span class="si">{2}</span><span class="s1">, </span><span class="si">{1}</span><span class="s1">, </span><span class="si">{0}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">)</span>
<span class="s1">&#39;c, b, a&#39;</span>
<span class="s1">&#39;</span><span class="si">{2}</span><span class="s1">, </span><span class="si">{1}</span><span class="s1">, </span><span class="si">{0}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">*</span><span class="s1">&#39;abc&#39;</span><span class="p">)</span>      <span class="c1"># unpacking argument sequence</span>
<span class="s1">&#39;c, b, a&#39;</span>
<span class="s1">&#39;</span><span class="si">{0}{1}{0}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39;abra&#39;</span><span class="p">,</span> <span class="s1">&#39;cad&#39;</span><span class="p">)</span>   <span class="c1"># arguments&#39; indices can be repeated</span>
<span class="s1">&#39;abracadabra&#39;</span>
</pre></div></div></div>

<p>Доступ к аргументам по имени:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code483b" onclick="copyCode(code483, code483b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code483"><div class="highlight"><pre><span></span><span class="s1">&#39;Coordinates: </span><span class="si">{latitude}</span><span class="s1">, </span><span class="si">{longitude}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">latitude</span><span class="o">=</span><span class="s1">&#39;37.24N&#39;</span><span class="p">,</span> <span class="n">longitude</span><span class="o">=</span><span class="s1">&#39;-115.81W&#39;</span><span class="p">)</span>
<span class="s1">&#39;Coordinates: 37.24N, -115.81W&#39;</span>
<span class="n">coord</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;latitude&#39;</span><span class="p">:</span> <span class="s1">&#39;37.24N&#39;</span><span class="p">,</span> <span class="s1">&#39;longitude&#39;</span><span class="p">:</span> <span class="s1">&#39;-115.81W&#39;</span><span class="p">}</span>
<span class="s1">&#39;Coordinates: </span><span class="si">{latitude}</span><span class="s1">, </span><span class="si">{longitude}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">coord</span><span class="p">)</span>
<span class="s1">&#39;Coordinates: 37.24N, -115.81W&#39;</span>
</pre></div></div></div>

<p>Доступ к атрибутам аргументов:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code484b" onclick="copyCode(code484, code484b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code484"><div class="highlight"><pre><span></span><span class="n">c</span> <span class="o">=</span> <span class="mi">3</span><span class="o">-</span><span class="mi">5</span><span class="n">j</span>
<span class="p">(</span><span class="s1">&#39;The complex number </span><span class="si">{0}</span><span class="s1"> is formed from the real part </span><span class="si">{0.real}</span><span class="s1"> &#39;</span>
 <span class="s1">&#39;and the imaginary part </span><span class="si">{0.imag}</span><span class="s1">.&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>
<span class="s1">&#39;The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.&#39;</span>
<span class="k">class</span> <span class="nc">Point</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">y</span> <span class="o">=</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span>
    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s1">&#39;Point(</span><span class="si">{self.x}</span><span class="s1">, </span><span class="si">{self.y}</span><span class="s1">)&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="o">=</span><span class="bp">self</span><span class="p">)</span>

<span class="nb">str</span><span class="p">(</span><span class="n">Point</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
<span class="s1">&#39;Point(4, 2)&#39;</span>
</pre></div></div></div>

<p>Доступ к элементам аргументов:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code485b" onclick="copyCode(code485, code485b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code485"><div class="highlight"><pre><span></span><span class="n">coord</span> <span class="o">=</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
<span class="s1">&#39;X: </span><span class="si">{0[0]}</span><span class="s1">;  Y: </span><span class="si">{0[1]}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">coord</span><span class="p">)</span>
<span class="s1">&#39;X: 3;  Y: 5&#39;</span>

<span class="n">Замена</span> <span class="o">%</span><span class="n">sи</span> <span class="o">%</span><span class="n">r</span><span class="p">:</span>
<span class="s2">&quot;repr() shows quotes: </span><span class="si">{!r}</span><span class="s2">; str() doesn&#39;t: </span><span class="si">{!s}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39;test1&#39;</span><span class="p">,</span> <span class="s1">&#39;test2&#39;</span><span class="p">)</span>
<span class="s2">&quot;repr() shows quotes: &#39;test1&#39;; str() doesn&#39;t: test2&quot;</span>
</pre></div></div></div>

<p>Выравнивание текста и указание ширины:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code486b" onclick="copyCode(code486, code486b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code486"><div class="highlight"><pre><span></span><span class="s1">&#39;</span><span class="si">{:&lt;30}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39;left aligned&#39;</span><span class="p">)</span>
<span class="s1">&#39;left aligned                  &#39;</span>
<span class="s1">&#39;</span><span class="si">{:&gt;30}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39;right aligned&#39;</span><span class="p">)</span>
<span class="s1">&#39;                 right aligned&#39;</span>
<span class="s1">&#39;</span><span class="si">{:^30}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39;centered&#39;</span><span class="p">)</span>
<span class="s1">&#39;           centered           &#39;</span>
<span class="s1">&#39;</span><span class="si">{:*^30}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39;centered&#39;</span><span class="p">)</span>  <span class="c1"># use &#39;*&#39; as a fill char</span>
<span class="s1">&#39;***********centered***********&#39;</span>
</pre></div></div></div>

<p>Замена %+f, %-f, и и указание знака:% f</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code487b" onclick="copyCode(code487, code487b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code487"><div class="highlight"><pre><span></span><span class="s1">&#39;</span><span class="si">{:+f}</span><span class="s1">; </span><span class="si">{:+f}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mf">3.14</span><span class="p">,</span> <span class="o">-</span><span class="mf">3.14</span><span class="p">)</span>  <span class="c1"># show it always</span>
<span class="s1">&#39;+3.140000; -3.140000&#39;</span>
<span class="s1">&#39;</span><span class="si">{: f}</span><span class="s1">; </span><span class="si">{: f}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mf">3.14</span><span class="p">,</span> <span class="o">-</span><span class="mf">3.14</span><span class="p">)</span>  <span class="c1"># show a space for positive numbers</span>
<span class="s1">&#39; 3.140000; -3.140000&#39;</span>
<span class="s1">&#39;</span><span class="si">{:-f}</span><span class="s1">; </span><span class="si">{:-f}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mf">3.14</span><span class="p">,</span> <span class="o">-</span><span class="mf">3.14</span><span class="p">)</span>  <span class="c1"># show only the minus -- same as &#39;{:f}; {:f}&#39;</span>
<span class="s1">&#39;3.140000; -3.140000&#39;</span>
</pre></div></div></div>

<p>Замена %xи %oпреобразование значения в разные базы:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code488b" onclick="copyCode(code488, code488b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code488"><div class="highlight"><pre><span></span><span class="c1"># format also supports binary numbers</span>
<span class="s2">&quot;int: </span><span class="si">{0:d}</span><span class="s2">;  hex: </span><span class="si">{0:x}</span><span class="s2">;  oct: </span><span class="si">{0:o}</span><span class="s2">;  bin: </span><span class="si">{0:b}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>
<span class="s1">&#39;int: 42;  hex: 2a;  oct: 52;  bin: 101010&#39;</span>
<span class="c1"># with 0x, 0o, or 0b as prefix:</span>
<span class="s2">&quot;int: </span><span class="si">{0:d}</span><span class="s2">;  hex: </span><span class="si">{0:#x}</span><span class="s2">;  oct: </span><span class="si">{0:#o}</span><span class="s2">;  bin: </span><span class="si">{0:#b}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>
<span class="s1">&#39;int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010&#39;</span>
</pre></div></div></div>

<p>Использование запятой в качестве разделителя тысяч:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code489b" onclick="copyCode(code489, code489b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code489"><div class="highlight"><pre><span></span><span class="s1">&#39;</span><span class="si">{:,}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mi">1234567890</span><span class="p">)</span>
<span class="s1">&#39;1,234,567,890&#39;</span>
</pre></div></div></div>

<p>Выражение процента:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code490b" onclick="copyCode(code490, code490b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code490"><div class="highlight"><pre><span></span><span class="n">points</span> <span class="o">=</span> <span class="mi">19</span>
<span class="n">total</span> <span class="o">=</span> <span class="mi">22</span>
<span class="s1">&#39;Correct answers: </span><span class="si">{:.2%}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">points</span><span class="o">/</span><span class="n">total</span><span class="p">)</span>
<span class="s1">&#39;Correct answers: 86.36%&#39;</span>
</pre></div></div></div>

<p>Использование форматирования для конкретного типа:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code491b" onclick="copyCode(code491, code491b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code491"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">datetime</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2010</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">12</span><span class="p">,</span> <span class="mi">15</span><span class="p">,</span> <span class="mi">58</span><span class="p">)</span>
<span class="s1">&#39;{:%Y-%m-</span><span class="si">%d</span><span class="s1"> %H:%M:%S}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>
<span class="s1">&#39;2010-07-04 12:15:58&#39;</span>
</pre></div></div></div>

<p>Вложенные аргументы и более сложные примеры:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code492b" onclick="copyCode(code492, code492b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code492"><div class="highlight"><pre><span></span><span class="k">for</span> <span class="n">align</span><span class="p">,</span> <span class="n">text</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="s1">&#39;&lt;^&gt;&#39;</span><span class="p">,</span> <span class="p">[</span><span class="s1">&#39;left&#39;</span><span class="p">,</span> <span class="s1">&#39;center&#39;</span><span class="p">,</span> <span class="s1">&#39;right&#39;</span><span class="p">]):</span>
    <span class="s1">&#39;{0:</span><span class="si">{fill}{align}</span><span class="s1">16}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">fill</span><span class="o">=</span><span class="n">align</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="n">align</span><span class="p">)</span>

<span class="s1">&#39;left&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&#39;</span>
<span class="s1">&#39;^^^^^center^^^^^&#39;</span>
<span class="s1">&#39;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;right&#39;</span>
<span class="n">octets</span> <span class="o">=</span> <span class="p">[</span><span class="mi">192</span><span class="p">,</span> <span class="mi">168</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span>
<span class="s1">&#39;</span><span class="si">{:02X}{:02X}{:02X}{:02X}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">*</span><span class="n">octets</span><span class="p">)</span>
<span class="s1">&#39;C0A80001&#39;</span>
<span class="nb">int</span><span class="p">(</span><span class="n">_</span><span class="p">,</span> <span class="mi">16</span><span class="p">)</span>
<span class="mi">3232235521</span>
<span class="n">width</span> <span class="o">=</span> <span class="mi">5</span>
<span class="k">for</span> <span class="n">num</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">12</span><span class="p">):</span> 
    <span class="k">for</span> <span class="n">base</span> <span class="ow">in</span> <span class="s1">&#39;dXob&#39;</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;{0:</span><span class="si">{width}{base}</span><span class="s1">}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">num</span><span class="p">,</span> <span class="n">base</span><span class="o">=</span><span class="n">base</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">),</span> <span class="n">end</span><span class="o">=</span><span class="s1">&#39; &#39;</span><span class="p">)</span>
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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code493b" onclick="copyCode(code493, code493b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code493"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;pi </span><span class="si">{</span><span class="mi">22</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">7</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Форматирование строк:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code494b" onclick="copyCode(code494, code494b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code494"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">:</span><span class="s2">&lt;10</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span> <span class="c1"># выравнивается в лево на 10 символов</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">:</span><span class="s2">&gt;10</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span> <span class="c1"># выравнивается в право на 10 символов</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">:</span><span class="s2">^10</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span> <span class="c1"># выравнивается по центру шириной 10 символов</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="mi">22</span><span class="o">/</span><span class="mi">7</span><span class="si">:</span><span class="s2">&gt;10.2f</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>      <span class="c1"># выравнивает в право на 10 и оставляет два знака после точки</span>
</pre></div></div></div>

<p>Форматирование строк может быть улучшено с помощью флагов:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code495b" onclick="copyCode(code495, code495b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code495"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><span class="si">:</span><span class="s2">=^10</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span> <span class="c1"># CENTERED WITH 10 CHARACTERS WIDTH AND FILLED WITH &quot;=&quot;</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code496b" onclick="copyCode(code496, code496b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code496"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Person</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__format__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">format_spec</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;Person Object&quot;</span>

<span class="n">p</span> <span class="o">=</span> <span class="n">Person</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">p</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span> <span class="c1"># Person Object</span>
</pre></div></div></div>