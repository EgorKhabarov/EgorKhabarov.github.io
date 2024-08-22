<p>Регуля́рные выраже́ния — формальный язык, используемый в компьютерных программах, 
работающих с текстом, для поиска и осуществления манипуляций с подстроками в тексте, 
основанный на использовании метасимволов. 
Для поиска используется строка-образец, состоящая из символов и 
метасимволов и задающая правило поиска.</p>
<h1>Обозначения</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>.</code></td>
<td>Один любой символ, кроме новой строки <code>\n</code>.</td>
</tr>
<tr>
<td><code>\d</code></td>
<td>Любая цифра</td>
</tr>
<tr>
<td><code>\D</code></td>
<td>Любой символ, кроме цифры</td>
</tr>
<tr>
<td><code>\s</code></td>
<td>Любой пробельный символ (пробел, табуляция, конец строки и т.п.)</td>
</tr>
<tr>
<td><code>\S</code></td>
<td>Любой не пробельный символ</td>
</tr>
<tr>
<td><code>\w</code></td>
<td>Любая буква (то, что может быть частью слова), а также цифры и <code>_</code></td>
</tr>
<tr>
<td><code>\W</code></td>
<td>Любая не-буква, не-цифра и не подчёркивание</td>
</tr>
<tr>
<td><code>[..]</code></td>
<td>Один из символов в скобках, а также любой символ из диапазона <code>a-b</code> <code>[0-9]</code> <code>[0-9A-Fa-f]</code></td>
</tr>
<tr>
<td><code>[^..]</code></td>
<td>Любой символ, кроме перечисленных <code>[^&gt;]</code></td>
</tr>
<tr>
<td><code>\d</code>≈<code>[0-9]</code><br><code>\D</code>≈<code>[^0-9]</code><br><code>\w</code>≈<code>[0-9a-zA-Zа-яА-ЯёЁ]</code><br><code>\s</code>≈<code>[ \f\n\r\t\v]</code></td>
<td>Буква <code>ё</code> не включается в общий диапазон букв!<br>Вообще говоря, в <code>\d</code> включается всё, что в юникоде помечено как «цифра», а в <code>\w</code> — как буква</td>
</tr>
<tr>
<td><code>[abc-], [-1]</code></td>
<td>Если нужен минус, его нужно указать последним или первым</td>
</tr>
<tr>
<td><code>[*[(+\\\]\t]</code></td>
<td>Внутри скобок нужно экранировать только <code>]</code> и <code>\</code></td>
</tr>
<tr>
<td><code>\b</code></td>
<td>Начало или конец слова (слева пусто или не-буква, справа буква и наоборот).<br>В отличие от предыдущих соответствует позиции, а не символу</td>
</tr>
<tr>
<td><code>\B</code></td>
<td>Не граница слова: либо и слева, и справа буквы, либо и слева, и справа <strong>НЕ</strong> буквы</td>
</tr>
</tbody>
</table>
<h1>Повторения</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>{n}</code></td>
<td>Ровно n повторений</td>
</tr>
<tr>
<td><code>{m,n}</code></td>
<td>От m до n повторений включительно</td>
</tr>
<tr>
<td><code>{m,}</code></td>
<td>Не менее m повторений</td>
</tr>
<tr>
<td><code>{,n}</code></td>
<td>Не более n повторений</td>
</tr>
<tr>
<td><code>?</code></td>
<td>Ноль или одно вхождение, синоним <code>{0,1}</code></td>
</tr>
<tr>
<td><code>*</code></td>
<td>Ноль или более, синоним <code>{0,}</code></td>
</tr>
<tr>
<td><code>+</code></td>
<td>Одно или более, синоним <code>{1,}</code></td>
</tr>
<tr>
<td><code>*?</code> <code>+?</code> <code>??</code> <code>{m,n}?</code><br><code>{,n}?</code> <code>{m,}?</code></td>
<td>По умолчанию квантификаторы жадные — захватывают максимально возможное число символов.<br>Добавление <code>?</code> делает их ленивыми, они захватывают минимально возможное число символов.</td>
</tr>
</tbody>
</table>
<h1>Начало &amp; конец</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>^</code></td>
<td>Начало всего текста или начало строчки текста, если <code>flags=re.MULTILINE</code></td>
</tr>
<tr>
<td><code>$</code></td>
<td>Конец всего текста или конец строчки текста, если <code>flags=re.MULTILINE</code></td>
</tr>
<tr>
<td><code>\A</code></td>
<td>Строго начало всего текста</td>
</tr>
<tr>
<td><code>\Z</code></td>
<td>Строго конец всего текста</td>
</tr>
<tr>
<td><code>\b</code></td>
<td>Начало или конец слова (слева пусто или не-буква, справа буква и наоборот)</td>
</tr>
<tr>
<td><code>\B</code></td>
<td>Не граница слова: либо и слева, и справа буквы, либо и слева, и справа НЕ буквы</td>
</tr>
</tbody>
</table>
<h1>Условные выражения</h1>
<table>
<thead>
<tr>
<th>Условное выражение</th>
<th></th>
<th>Регулярка</th>
<th>Соответствие</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>(?=.)</code></td>
<td>Позитивный просмотр вперёд</td>
<td><code>Людовик(?=XVI)</code></td>
<td>ЛюдовикXV, <span style="background-color: #999999; color: #FFFFFF">Людовик</span>XVI, <span style="background-color: #999999; color: #FFFFFF">Людовик</span>XVIII, ЛюдовикLXVII, ЛюдовикXXL</td>
</tr>
<tr>
<td><code>(?!.)</code></td>
<td>Негативный просмотр вперёд</td>
<td><code>Людовик(?!XVI)</code></td>
<td><span style="background-color: #999999; color: #FFFFFF">Людовик</span>XV, ЛюдовикXVI, ЛюдовикXVIII, <span style="background-color: #999999; color: #FFFFFF">Людовик</span>LXVII, <span style="background-color: #999999; color: #FFFFFF">Людовик</span>XXL</td>
</tr>
<tr>
<td><code>(?&lt;=.)</code></td>
<td>Позитивный просмотр назад<br>Длина шаблона должна быть фиксированной</td>
<td><code>(?&lt;=Сергей )Иванов</code></td>
<td>Сергей <span style="background-color: #999999; color: #FFFFFF">Иванов</span>, Игорь Иванов</td>
</tr>
<tr>
<td><code>(?&lt;!.)</code></td>
<td>Негативный просмотр назад</td>
<td><code>(?&lt;!Сергей )Иванов</code></td>
<td>Сергей Иванов, Игорь <span style="background-color: #999999; color: #FFFFFF">Иванов</span></td>
</tr>
</tbody>
</table>
<h1>Группы захвата</h1>
<table>
<thead>
<tr>
<th>Группа захвата</th>
<th>Название</th>
<th>Регулярка</th>
<th>Соответствие</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>(?:pattern)</code></td>
<td>Незахватывающая группа</td>
<td><code>(?:abc|def)</code></td>
<td>123 <span style="background-color: #999999; color: #FFFFFF">abc</span> 456</td>
</tr>
<tr>
<td><code>(?P&lt;name&gt;pattern)</code></td>
<td>Именованная группа захвата</td>
<td><code>My name is (?P&lt;name&gt;\w+)</code></td>
<td>My name is <span style="background-color: #999999; color: #FFFFFF">John</span><br><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;My name is (?P&lt;name&gt;\w+)&quot;</span><span class="p">)</span><br><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s2">&quot;My name is John&quot;</span><span class="p">)</span><br><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">)</span><br><span class="c1"># John</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>(?P=name)</code></td>
<td>Именованная обратная ссылка<br>Позволяет ссылаться на ранее захваченные группы по имени</td>
<td><code>(?P&lt;word&gt;\w+)\s+(?P=word)</code></td>
<td><span style="background-color: #999999; color: #FFFFFF">hello hello</span></td>
</tr>
</tbody>
</table>
<h1>Другое</h1>
<table>
<thead>
<tr>
<th>Паттерн</th>
<th>Название</th>
<th>Регулярка</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>(?&gt;pattern)</code></td>
<td>Атомарная группа<br>Захватывает подстроку<br>и запрещает бэктрекинг*<br>внутри этой группы,<br>если остальная часть<br>шаблона не совпала.</td>
<td><code>(?&gt;\d{3})\d</code><br>Эта конструкция сначала пытается<br>сопоставить <code>\d{3}</code>, а затем <code>\d</code>.<br>Если первое выражение не совпадает,<br>оно не пытается вернуться назад.</td>
<td><span style="background-color: #999999; color: #FFFFFF">1234</span></td>
</tr>
<tr>
<td><code>(?R)</code> или <code>(?0)</code></td>
<td>Рекурсивный шаблон<br>Вставляет текущее регулярное<br>выражение внутрь самого себя.</td>
<td><code>\((?:[^()]+|(?R))*\)</code><br>Это регулярное выражение<br>сопоставляет сбалансированные скобки.<br><code>re.error: unknown extension ?R at position 13</code></td>
<td><span style="background-color: #999999; color: #FFFFFF">(a(b)c)</span></td>
</tr>
<tr>
<td><code>(?P&lt;name1&gt;pattern1|(?P&lt;name2&gt;pattern2))</code></td>
<td>Условные выражения<br>с именованными группами</td>
<td></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span>    <span class="sa">r</span><span class="s2">&quot;(?P&lt;name1&gt;pattern1|&quot;</span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span>    <span class="sa">r</span><span class="s2">&quot;(?P&lt;name2&gt;pattern2))&quot;</span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="p">)</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span>    <span class="s2">&quot;pattern2&quot;</span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="p">)</span><span class="o">.</span><span class="n">groupdict</span><span class="p">()</span><br><span class="unselectable"><span class="p">{</span></span><br><span class="unselectable">    <span class="s2">&quot;name1&quot;</span><span class="p">:</span> <span class="s2">&quot;pattern2&quot;</span><span class="p">,</span></span><br><span class="unselectable">    <span class="s2">&quot;name2&quot;</span><span class="p">:</span> <span class="s2">&quot;pattern2&quot;</span><span class="p">,</span></span><br><span class="unselectable"><span class="p">}</span></span><br></pre></div></pre></div></div></td>
</tr>
</tbody>
</table>
<h1>Флаги</h1>
<p><a href="https://docs.python.org/3/library/re.html#flags">https://docs.python.org/3/library/re.html#flags</a></p>
<table>
<thead>
<tr>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>re.A</code><br><code>re.ASCII</code></td>
<td><code>(?a)</code></td>
<td>По умолчанию <code>\w</code>, <code>\W</code>, <code>\b</code>, <code>\B</code>, <code>\d</code>, <code>\D</code>, <code>\s</code>, <code>\S</code> соответствуют все юникодные<br>символы с соответствующим качеством. Ускоряет работу, если все соответствия лежат внутри ASCII.</td>
</tr>
<tr>
<td><code>re.I</code><br><code>re.IGNORECASE</code></td>
<td><code>(?i)</code></td>
<td>Не различать заглавные и маленькие буквы. Работает медленнее, но иногда удобно</td>
</tr>
<tr>
<td><code>re.M</code><br><code>re.MULTILINE</code></td>
<td><code>(?m)</code></td>
<td>Специальные символы <code>^</code> и <code>$</code> соответствуют началу и концу каждой строки</td>
</tr>
<tr>
<td><code>re.S</code><br><code>re.DOTALL</code></td>
<td><code>(?s)</code></td>
<td>По умолчанию символ <code>\n</code> конца строки не подходит под точку. С этим флагом точка — вообще любой символ</td>
</tr>
<tr>
<td><code>re.X</code><br><code>re.VERBOSE</code></td>
<td><code>(?x)</code></td>
<td>Пробелы внутри шаблона игнорируются, за исключением случаев,<br>когда они находятся в классе символов, или когда им предшествует неэкранированная<br>обратная косая черта, или внутри токенов,<br>таких как <code>*?</code>, <code>(?:</code> или <code>(?P&lt;...&gt;</code>. Например, и не допускаются.<br><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><br><span class="w">   </span><span class="sa">r</span><span class="sd">&quot;&quot;&quot;</span><br><span class="sd">\d +  # the integral part</span><br><span class="sd">\.    # the decimal point</span><br><span class="sd">\d *  # some fractional digits</span><br><span class="sd">&quot;&quot;&quot;</span><span class="p">,</span><br>   <span class="n">re</span><span class="o">.</span><span class="n">X</span><span class="p">,</span><br><span class="p">)</span><br><span class="n">b</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;\d+.\d*&quot;</span><span class="p">)</span><br><br><span class="c1"># Wrong!</span><br><span class="n">c</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><br><span class="w">   </span><span class="sa">r</span><span class="sd">&quot;&quot;&quot;(?s)</span><br><span class="sd">\d +  # the integral part</span><br><span class="sd">\.    # the decimal point</span><br><span class="sd">\d *  # some fractional digits</span><br><span class="sd">&quot;&quot;&quot;</span><br><span class="p">)</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>re.L</code><br><code>re.LOCALE</code></td>
<td><code>(?L)</code></td>
<td>Сделать <code>\w</code>, <code>\W</code>, <code>\b</code>, \Bи соответствие без учета регистра зависимым от текущей локали.<br>Этот флаг можно использовать только с шаблонами байтов.</td>
</tr>
<tr>
<td><code>re.U</code><br><code>re.UNICODE</code></td>
<td></td>
<td>В Python 3 символы Unicode сопоставляются по умолчанию для <code>str</code> шаблонов.<br>Поэтому этот флаг является избыточным, <strong>не имеет никакого эффекта</strong><br>и сохраняется только для обратной совместимости.</td>
</tr>
<tr>
<td><code>re.DEBUG</code></td>
<td></td>
<td>Отображение отладочной информации о скомпилированном выражении.</td>
</tr>
<tr>
<td><code>re.NOFLAG</code></td>
<td></td>
<td>С версии 3.11.</td>
</tr>
</tbody>
</table>
<p>Группы-модификаторы можно объединять в одну группу: <code>(?i-sm)</code>.
Такая группа включает режим <code>i</code> и выключает режимы <code>s</code> и <code>m</code>.
Если использование модификаторов требуется только в пределах группы, то нужный шаблон
указывается внутри группы после модификаторов и после двоеточия.
Например, <b><code>(?-i)(?i:tv)set</code></b> найдёт <b><code>TVset</code></b>, но не <b><code>TVSET</code></b>.</p>
<h1>Команды</h1>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>re.match(    <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int | RegexFlag = 0                             <br>) -&gt; Match[str] | None</td>
<td>Ищет совпадение в начале строки.</td>
</tr>
<tr>
<td>re.search(   <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int | RegexFlag = 0                             <br>) -&gt; Match[str] | None</td>
<td>Ищет первое совпадение в строке.</td>
</tr>
<tr>
<td>re.findall(  <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int | RegexFlag = 0                             <br>) -&gt; list</td>
<td>Возвращает список всех непересекающихся совпадений в строке.</td>
</tr>
<tr>
<td>re.finditer( <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int | RegexFlag = 0                             <br>) -&gt; Iterator[Match[str]]</td>
<td>Возвращает итератор по всем совпадениям в строке.</td>
</tr>
<tr>
<td>re.sub(      <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;repl: str | (Match[str]) -&gt; str, <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str, count: int = 0, flags: int | RegexFlag = 0<br>) -&gt; str</td>
<td>Заменяет совпадения в строке на указанный текст.</td>
</tr>
<tr>
<td>re.subn(     <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;repl: str | (Match[str]) -&gt; str, <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str, count: int = 0, flags: int | RegexFlag = 0<br>) -&gt; tuple[str, int]</td>
<td>То же, что и <code>re.sub()</code>, но также возвращает количество замен.</td>
</tr>
<tr>
<td>re.split(    <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;maxsplit: int = 0, flags: int | RegexFlag = 0          <br>) -&gt; list[str]</td>
<td>Разбивает строку по шаблону и возвращает список строк.</td>
</tr>
<tr>
<td>re.fullmatch(<br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int | RegexFlag = 0                             <br>) -&gt; Match[str] | None</td>
<td>Проверяет, полностью ли строка соответствует шаблону.</td>
</tr>
<tr>
<td>re.compile(  <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int | RegexFlag = 0       <br>) -&gt; Pattern[AnyStr]</td>
<td>Компилирует регулярное выражение в объект регулярного выражения.</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>re.compile(...).match(    <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int | RegexFlag = 0                             <br>) -&gt; Match[str] | None</td>
<td>Ищет совпадение в начале строки.</td>
</tr>
<tr>
<td>re.compile(...).search(   <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int | RegexFlag = 0                             <br>) -&gt; Match[str] | None</td>
<td>Ищет первое совпадение в строке.</td>
</tr>
<tr>
<td>re.compile(...).findall(  <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int | RegexFlag = 0                             <br>) -&gt; list</td>
<td>Возвращает список всех непересекающихся совпадений в строке.</td>
</tr>
<tr>
<td>re.compile(...).finditer( <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int | RegexFlag = 0                             <br>) -&gt; Iterator[Match[str]]</td>
<td>Возвращает итератор по всем совпадениям в строке.</td>
</tr>
<tr>
<td>re.compile(...).sub(      <br>&nbsp;&nbsp;&nbsp;&nbsp;repl: str | (Match[str]) -&gt; str, <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str, count: int = 0, flags: int | RegexFlag = 0<br>) -&gt; str</td>
<td>Заменяет совпадения в строке на указанный текст.</td>
</tr>
<tr>
<td>re.compile(...).subn(     <br>&nbsp;&nbsp;&nbsp;&nbsp;repl: str | (Match[str]) -&gt; str, <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str, count: int = 0, flags: int | RegexFlag = 0<br>) -&gt; tuple[str, int]</td>
<td>То же, что и <code>re.compile(...).sub()</code>, но также возвращает количество замен.</td>
</tr>
<tr>
<td>re.compile(...).split(    <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;maxsplit: int = 0, flags: int | RegexFlag = 0          <br>) -&gt; list[str]</td>
<td>Разбивает строку по шаблону и возвращает список строк.</td>
</tr>
<tr>
<td>re.compile(...).fullmatch(<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int | RegexFlag = 0                             <br>) -&gt; Match[str] | None</td>
<td>Проверяет, полностью ли строка соответствует шаблону.</td>
</tr>
</tbody>
</table>
<p><br></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">import</span> <span class="nn">re</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">def</span> <span class="nf">func</span><span class="p">(</span><span class="n">m</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;[censored(</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">m</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span><span class="si">}</span><span class="s2">)]&quot;</span>
<span class="unselectable"><span class="o">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">text</span> <span class="o">=</span> <span class="s2">&quot;Некоторые хорошие слова подозрительны: хор, хоровод, хороводоводовед.&quot;</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;\b[хХxX]\w*&quot;</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="n">text</span><span class="p">))</span>
<span class="unselectable"><span class="n">Некоторые</span> <span class="p">[</span><span class="n">censored</span><span class="p">(</span><span class="mi">7</span><span class="p">)]</span> <span class="n">слова</span> <span class="n">подозрительны</span><span class="p">:</span> <span class="p">[</span><span class="n">censored</span><span class="p">(</span><span class="mi">3</span><span class="p">)],</span> <span class="p">[</span><span class="n">censored</span><span class="p">(</span><span class="mi">7</span><span class="p">)],</span> <span class="p">[</span><span class="n">censored</span><span class="p">(</span><span class="mi">15</span><span class="p">)]</span><span class="o">.</span></span>
</pre></div></div></div>

<h1>Примеры</h1>
<h3>Номер кредитки:</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>[0-9]{13,16}
</pre></div></div></div>

<h3>ICQ:</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>([1-9])+(?:-?\d){4,}
</pre></div></div></div>

<h3>Набор из букв и цифр (латиница):</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>^[a-zA-Z0-9]+$
</pre></div></div></div>

<h3>Набор из букв и цифр (латиница + кириллица):</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>^[а-яА-ЯёЁa-zA-Z0-9]+$
</pre></div></div></div>

<h3>Домен (например seo-zona.ru):</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$
</pre></div></div></div>

<h3>IPv4:</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)
</pre></div></div></div>

<h3>IPv6:</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>((^|:)([0-9a-fA-F]{0,4})){1,8}$
</pre></div></div></div>

<h3>Имя пользователя (с ограничением 2-20 символов,<br>которыми могут быть буквы и цифры, первый символ обязательно буква):</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$
</pre></div></div></div>

<h3>Дата в формате YYYY-MM-DD:</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])
</pre></div></div></div>

<h3>Дата в формате <code>DD/MM/YYYY</code>:</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d
</pre></div></div></div>

<h3>Целые числа и числа с плавающей точкой (разделитель точка):</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>\-?\d+(\.\d{0,})?
</pre></div></div></div>

<h3>UUID:</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>^[0-9A-Fa-f]{8}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{12}$
</pre></div></div></div>

<h3>Широта или долгота:</h3>
<div class="code_element"><div class="lang_line"><text>regexp</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>-?\d{1,3}\.\d+
</pre></div></div></div>

<h2>Пример атомарной группы</h2>
<p>Возьмем выражение <code>(?&gt;a|ab)c</code> и строку <code>abc</code>:</p>
<ol>
<li>Сначала регулярное выражение пытается сопоставить <code>a</code> внутри атомарной группы <code>(?&gt;a|ab)</code>.</li>
<li>После успешного совпадения с <code>a</code>, атомарная группа блокируется, и больше не возвращается назад, даже если дальнейшие совпадения не удаются.</li>
<li>Затем выражение пытается сопоставить <code>c</code>, что не удается, потому что следующий символ <code>b</code>.</li>
<li>В обычной группе регулярное выражение вернулось бы назад, чтобы попробовать сопоставить <code>ab</code> вместо <code>a</code>.<br>Но так как группа атомарная, бэктрекинг не происходит, и регулярное выражение не находит совпадения.</li>
</ol>
<h3>Пример кода</h3>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">import</span> <span class="nn">re</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">simple_group</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;(a|ab)c&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">atomic_group</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;(?&gt;a|ab)c&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="n">simple_group</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="s2">&quot;abc&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">group</span><span class="p">())</span>  <span class="c1"># Обычная группа</span>
<span class="unselectable"><span class="go">abc</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="nb">print</span><span class="p">(</span><span class="n">atomic_group</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="s2">&quot;abc&quot;</span><span class="p">))</span>  <span class="c1"># Атомарная группа</span>
<span class="unselectable"><span class="go">None</span>
</span></pre></div></div></div>

<h1>Бэктрекинг</h1>
<p><strong>Бэктрекинг (backtracking)</strong> — это процесс возврата назад по строке для поиска альтернативных путей совпадения,
если текущий путь не приводит к успешному совпадению.
Регулярные выражения могут исследовать разные комбинации символов и паттернов, чтобы найти подходящее совпадение.</p>
<h2>Пример бэктрекинга</h2>
<p>Рассмотрим регулярное выражение <code>a(b|c)*d</code> и строку <code>abbbd</code>:</p>
<ol>
<li>Начало сопоставления с <code>a</code> — успех.</li>
<li>Далее идет <code>(b|c)*</code>, которое может захватить любое количество <code>b</code> или <code>c</code>. Сначала регулярное выражение захватывает все <code>b</code>: <code>abbb</code>.</li>
<li>Теперь шаблон пытается сопоставить <code>d</code> после <code>abbb</code>. Строка заканчивается на <code>d</code>, и совпадение успешно завершается.</li>
</ol>
<p>Теперь возьмем строку <code>abbcd</code>:</p>
<ol>
<li>Начало сопоставления с <code>a</code> — успех.</li>
<li>Далее идет <code>(b|c)*</code>, которое снова захватывает все <code>b</code>: <code>abb</code>.</li>
<li>Теперь шаблон пытается сопоставить <code>d</code> после <code>abb</code>. Это неудача, потому что следующий символ <code>c</code>.</li>
<li>Регулярное выражение возвращается (бэктрекинг) к последнему совпавшему <code>b</code>, теперь пробует совпадение с <code>c</code>: <code>abbc</code>.</li>
<li>Теперь шаблон пытается сопоставить <code>d</code> после <code>abbc</code>. Строка заканчивается на <code>d</code>, и совпадение успешно завершается.</li>
</ol>
<h1>Особенности в разных языках</h1>
<h2>Java</h2>
<h3>&amp;&amp; ^</h3>
<p><code>[\w&amp;&amp;[^_]]</code> - Любой символ, подходящий под <code>\w</code>, кроме <code>_</code>.</p>