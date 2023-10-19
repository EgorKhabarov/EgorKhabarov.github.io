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
<td>.</td>
<td>Один любой символ, кроме новой строки \n.</td>
</tr>
<tr>
<td>\d</td>
<td>Любая цифра</td>
</tr>
<tr>
<td>\D</td>
<td>Любой символ, кроме цифры</td>
</tr>
<tr>
<td>\s</td>
<td>Любой пробельный символ (пробел, табуляция, конец строки и т.п.)</td>
</tr>
<tr>
<td>\S</td>
<td>Любой не пробельный символ</td>
</tr>
<tr>
<td>\w</td>
<td>Любая буква (то, что может быть частью слова), а также цифры и _</td>
</tr>
<tr>
<td>\W</td>
<td>Любая не-буква, не-цифра и не подчёркивание</td>
</tr>
<tr>
<td>[..]</td>
<td>Один из символов в скобках, а также любой символ из диапазона a-b [0-9][0-9A-Fa-f]</td>
</tr>
<tr>
<td>[^..]</td>
<td>Любой символ, кроме перечисленных &lt;[^&gt;]&gt;</td>
</tr>
<tr>
<td>\d≈[0-9]</td>
<td>Буква “ё” не включается в общий диапазон букв!</td>
</tr>
<tr>
<td>\D≈[^0-9]<br>\w≈[0-9a-zA-Zа-яА-ЯёЁ]<br>\s≈[ \f\n\r\t\v]</td>
<td>Вообще говоря, в \d включается всё, что в юникоде помечено как «цифра», а в \w — как буква</td>
</tr>
<tr>
<td>[abc-], [-1]</td>
<td>Если нужен минус, его нужно указать последним или первым</td>
</tr>
<tr>
<td>[*[(+\]\t]</td>
<td>Внутри скобок нужно экранировать только ] и \</td>
</tr>
<tr>
<td>\b</td>
<td>Начало или конец слова (слева пусто или не-буква, справа буква и наоборот).<br>В отличие от предыдущих соответствует позиции, а не символу</td>
</tr>
<tr>
<td>\B</td>
<td>Не граница слова: либо и слева, и справа буквы, либо и слева, и справа НЕ буквы</td>
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
<td>{n}</td>
<td>Ровно n повторений</td>
</tr>
<tr>
<td>{m,n}</td>
<td>От m до n повторений включительно</td>
</tr>
<tr>
<td>{m,}</td>
<td>Не менее m повторений</td>
</tr>
<tr>
<td>{,n}</td>
<td>Не более n повторений</td>
</tr>
<tr>
<td>?</td>
<td>Ноль или одно вхождение, синоним {0,1}</td>
</tr>
<tr>
<td>*</td>
<td>Ноль или более, синоним {0,}</td>
</tr>
<tr>
<td>+</td>
<td>Одно или более, синоним {1,}</td>
</tr>
<tr>
<td>*?  +?  ??  {m,n}?</td>
<td>По умолчанию квантификаторы жадные — захватывают максимально возможное число символов.</td>
</tr>
<tr>
<td>{,n}?  {m,}?</td>
<td>Добавление ? делает их ленивыми, они захватывают минимально возможное число символов</td>
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
<td>^</td>
<td>Начало всего текста или начало строчки текста, если flags=re.MULTILINE</td>
</tr>
<tr>
<td>$</td>
<td>Конец всего текста или конец строчки текста, если flags=re.MULTILINE</td>
</tr>
<tr>
<td>\A</td>
<td>Строго начало всего текста</td>
</tr>
<tr>
<td>\Z</td>
<td>Строго конец всего текста</td>
</tr>
<tr>
<td>\b</td>
<td>Начало или конец слова (слева пусто или не-буква, справа буква и наоборот)</td>
</tr>
<tr>
<td>\B</td>
<td>Не граница слова: либо и слева, и справа буквы, либо и слева, и справа НЕ буквы</td>
</tr>
</tbody>
</table>
<h1>Выбор позиции</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>(?:...)</td>
<td>Позволяют локализовать часть шаблона, внутри которого происходит перечисление</td>
</tr>
<tr>
<td>(?=...)</td>
<td>Соответствует каждой позиции, сразу после которой НАЧИНАЕТСЯ соответствие шаблону ...</td>
</tr>
<tr>
<td>(?!...)</td>
<td>Соответствует каждой позиции, сразу после которой НЕ МОЖЕТ НАЧИНАТЬСЯ шаблон ...</td>
</tr>
<tr>
<td>(?&lt;=...)</td>
<td>Соответствует каждой позиции, которой может ЗАКАНЧИВАТЬСЯ шаблон ...<br>Длина шаблона должна быть фиксированной, то есть abc и a</td>
</tr>
<tr>
<td>(?&lt;!...)</td>
<td>Соответствует каждой позиции, которой НЕ МОЖЕТ ЗАКАНЧИВАТЬСЯ шаблон ...</td>
</tr>
</tbody>
</table>
<h1>Флаги</h1>
<p><a href='https://docs.python.org/3/library/re.html#flags' target='_blank'>https://docs.python.org/3/library/re.html#flags</a></p>
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
<td>re.ASCII</td>
<td>(?a)</td>
<td>По умолчанию \w, \W, \b, \B, \d, \D, \s, \S соответствуют все юникодные<br>символы с соответствующим качеством. Ускоряет работу, если все соответствия лежат внутри ASCII.</td>
</tr>
<tr>
<td>re.IGNORECASE</td>
<td>(?i)</td>
<td>Не различать заглавные и маленькие буквы. Работает медленнее, но иногда удобно</td>
</tr>
<tr>
<td>re.MULTILINE</td>
<td>(?m)</td>
<td>Специальные символы ^ и $ соответствуют началу и концу каждой строки</td>
</tr>
<tr>
<td>re.DOTALL</td>
<td>(?s)</td>
<td>По умолчанию символ \n конца строки не подходит под точку. С этим флагом точка — вообще любой символ</td>
</tr>
<tr>
<td>re.VERBOSE</td>
<td>(?x)</td>
<td>Пробелы внутри шаблона игнорируются, за исключением случаев,<br>когда они находятся в классе символов, или когда им предшествует неэкранированная<br>обратная косая черта, или внутри токенов,<br>таких как &#42;?, (?:или (?P&lt;...&gt;. Например, и не допускаются.<br><br><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre>a = re.compile(<span class="s1">r&#34;&#34;&#34;\d +  # the integral part<br>                   &#92;.    # the decimal point<br>                   \d *  # some fractional digits&#34;&#34;&#34;</span>, re.X)<br>b = re.compile(<span class="s1">r"\d+.\d*"</span>)</pre></div></div></td>
</tr>
</tbody>
</table>
<h1>Команды</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>re.search(pattern, string)</td>
<td>Найти в строке string первую строчку, подходящую под шаблон pattern</td>
</tr>
<tr>
<td>re.fullmatch(pattern, string)</td>
<td>Проверить, подходит ли строка string под шаблон pattern</td>
</tr>
<tr>
<td>re.split(pattern, string, maxsplit=0)</td>
<td>Аналог str.split(), только разделение происходит по подстрокам, подходящим под шаблон pattern</td>
</tr>
<tr>
<td>re.findall(pattern, string)</td>
<td>Найти в строке string все непересекающиеся шаблоны pattern</td>
</tr>
<tr>
<td>re.finditer(pattern, string)</td>
<td>Итератор всем непересекающимся шаблонам pattern в строке string (выдаются match-объекты)</td>
</tr>
<tr>
<td>re.sub(pattern, repl, string, count=0)</td>
<td>Заменить в строке string все непересекающиеся шаблоны pattern на repl</td>
</tr>
</tbody>
</table>
<p><br></p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code535b" onclick="copyCode(code535, code535b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code535"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">re</span> 
<span class="k">def</span> <span class="nf">repl</span><span class="p">(</span><span class="n">m</span><span class="p">):</span> 
    <span class="k">return</span> <span class="s1">&#39;&gt;censored(&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">m</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span> <span class="o">+</span> <span class="s1">&#39;)&lt;&#39;</span> 
<span class="n">text</span> <span class="o">=</span> <span class="s2">&quot;Некоторые хорошие слова подозрительны: хор, хоровод, хороводоводовед.&quot;</span> 
<span class="nb">print</span><span class="p">(</span><span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;\b[хХxX]\w*&#39;</span><span class="p">,</span> <span class="n">repl</span><span class="p">,</span> <span class="n">text</span><span class="p">))</span> 
<span class="c1"># -&gt; Некоторые &gt;censored(7)&lt; слова подозрительны: &gt;censored(3)&lt;, &gt;censored(7)&lt;, &gt;censored(15)&lt;.</span>
</pre></div></div></div>

<p>Примеры
Номер кредитки:</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code536b" onclick="copyCode(code536, code536b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code536"><div class="highlight"><pre><span></span>[0-9]{13,16}
</pre></div></div></div>

<p>ICQ:</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code537b" onclick="copyCode(code537, code537b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code537"><div class="highlight"><pre><span></span>([1-9])+(?:-?\d){4,}
</pre></div></div></div>

<p>Набор из букв и цифр (латиница):</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code538b" onclick="copyCode(code538, code538b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code538"><div class="highlight"><pre><span></span>^[a-zA-Z0-9]+$
</pre></div></div></div>

<p>Набор из букв и цифр (латиница + кириллица):</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code539b" onclick="copyCode(code539, code539b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code539"><div class="highlight"><pre><span></span>^[а-яА-ЯёЁa-zA-Z0-9]+$
</pre></div></div></div>

<p>Домен (например seo-zona.ru):</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code540b" onclick="copyCode(code540, code540b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code540"><div class="highlight"><pre><span></span>^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$
</pre></div></div></div>

<p>IPv4:</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code541b" onclick="copyCode(code541, code541b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code541"><div class="highlight"><pre><span></span>((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)
</pre></div></div></div>

<p>IPv6:</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code542b" onclick="copyCode(code542, code542b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code542"><div class="highlight"><pre><span></span>((^|:)([0-9a-fA-F]{0,4})){1,8}$
</pre></div></div></div>

<p>Имя пользователя (с ограничением 2-20 символов, 
которыми могут быть буквы и цифры, первый символ обязательно буква):</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code543b" onclick="copyCode(code543, code543b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code543"><div class="highlight"><pre><span></span>^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$
</pre></div></div></div>

<p>Дата в формате YYYY-MM-DD:</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code544b" onclick="copyCode(code544, code544b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code544"><div class="highlight"><pre><span></span>[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])
</pre></div></div></div>

<p>Дата в формате DD/MM/YYYY:</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code545b" onclick="copyCode(code545, code545b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code545"><div class="highlight"><pre><span></span>(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d
</pre></div></div></div>

<p>Целые числа и числа с плавающей точкой (разделитель точка):</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code546b" onclick="copyCode(code546, code546b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code546"><div class="highlight"><pre><span></span>\-?\d+(\.\d{0,})?
</pre></div></div></div>

<p>UUID:</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code547b" onclick="copyCode(code547, code547b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code547"><div class="highlight"><pre><span></span>^[0-9A-Fa-f]{8}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{12}$
</pre></div></div></div>

<p>Широта или долгота:</p>
<div class="code-element"><div class="lang-line"><text>regexp</text><button class="copy-button" id="code548b" onclick="copyCode(code548, code548b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code548"><div class="highlight"><pre><span></span>-?\d{1,3}\.\d+
</pre></div></div></div>