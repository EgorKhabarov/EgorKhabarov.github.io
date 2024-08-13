<table>
<thead>
<tr>
<th style="text-align: left;">Метод</th>
<th style="text-align: left;">Описание</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">str.capitalize()</td>
<td style="text-align: left;">Переводит первую букву в верхний, а остальные в нижний регистр.</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "capitalize".capitalize()<br>"Capitalize"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.casefold()</td>
<td style="text-align: left;">Переводит все символы в нижний регистр</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "CaSeFoLd".casefold()<br>"casefold"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.lower()</td>
<td style="text-align: left;">Переводит символы строки в нижний регистр</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "lOwEr".lower()<br>"lower"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.upper()</td>
<td style="text-align: left;">Возвращает копию строки в верхнем регистре</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "upper".upper()<br>"UPPER"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.swapcase()</td>
<td style="text-align: left;">Меняет регистр всех символов на противоположный</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "sWaPcAsE".swapcase()<br>"SwApCaSe"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.title()</td>
<td style="text-align: left;">Возвращает строку, где все слова начинаются с заглавной буквы,<br>а продолжаются строчными</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "title title".title()<br>"Title Title"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.isupper()</td>
<td style="text-align: left;"><code>True</code>, если строка в верхнем регистре</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "A".isupper()<br>True<br>&gt;&gt;&gt; "a".isupper()<br>False</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.islower()</td>
<td style="text-align: left;"><code>True</code>, если вся строка в нижнем регистре</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "a".islower()<br>True<br>"A".islower()<br>False</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.center(width[, fillvalue])</td>
<td style="text-align: left;">Обрамляет значениями <code>fillvalue</code> строку,<br>пока длина не станет <code>width</code></td>
<td><pre><code class="language-python">&gt;&gt;&gt; "0".center(5, "_")<br>"__0__"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.ljust(width, fillchar=" ")</td>
<td style="text-align: left;">Добавляет в конец строки символ <code>fillchar</code>,<br>пока длина не станет <code>width</code></td>
<td><pre><code class="language-python">&gt;&gt;&gt; "1".ljust(5, "_")<br>"1____"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.rjust(width, fillchar=" ")</td>
<td style="text-align: left;">Добавляет в начало строки символ <code>fillchar</code>,<br>пока длина не станет <code>width</code></td>
<td><pre><code class="language-python">&gt;&gt;&gt; "1".rjust(5, "_")<br>"____1"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.count(str[, start][, end]</td>
<td style="text-align: left;">Считает количество подстрок <code>str</code> в выбранном промежутке строки</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "12123412".count("12")<br>3</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.encode(encoding, errors)</td>
<td style="text-align: left;">Меняет кодировку строки</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "qwerty123".encode()<br>b"qwerty123"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.startswith(prefix[, start[, end]])</td>
<td style="text-align: left;"><code>True</code> если строка начинается с <code>prefix</code></td>
<td><pre><code class="language-python">&gt;&gt;&gt; "1234".startswith("34")<br>False<br>&gt;&gt;&gt; "1234".startswith("12")<br>True<br>&gt;&gt;&gt; "1234".startswith(("12", "89"))<br>True</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.endswith(suffix[, start[, end]])</td>
<td style="text-align: left;"><code>True</code> если строка заканчивается на <code>suffix</code></td>
<td><pre><code class="language-python">&gt;&gt;&gt; "1234".endswith("12")<br>False<br>&gt;&gt;&gt; "1234".endswith("34")<br>True<br>&gt;&gt;&gt; "1234".endswith(("34", "56"))<br>True</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.removeprefix(prefix: str)</td>
<td style="text-align: left;">Возвращает строку без прификса <code>prefix</code></td>
<td><pre><code class="language-python">&gt;&gt;&gt; "123".removeprefix("1")<br>"23"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.removesuffix(suffix: str)</td>
<td style="text-align: left;">Возвращает строку без суффикса <code>suffix</code></td>
<td><pre><code class="language-python">&gt;&gt;&gt; "123".removesuffix("3")<br>"12"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.expandtabs(tabsize=8)</td>
<td style="text-align: left;">Увеличивает размер символов табуляции до <code>tabsize</code> пробелов</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "    ".expandtabs(8)<br>"        "</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.index(str[, start[, end]])</td>
<td style="text-align: left;">Возвращает индекс начала первой подстроки <code>str</code><br>в выбранном промежутке или <code>ValueError</code>, если она не найдена</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "1234".index("2")<br>1</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.rindex(str[, start[, end]])</td>
<td style="text-align: left;">Возвращает индекс начала последней подстроки <code>str</code><br>в выбранном промежутке или <code>ValueError</code>, если она не найдена</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "123427".rindex("2")<br>4</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.find(str[, start[, end]])</td>
<td style="text-align: left;">Возвращает индекс начала первой подстроки <code>str</code><br>в выбранном промежутке или <code>-1</code>, если она не найдена</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "1234".find("2")<br>1</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.rfind(str[, start[, end]])</td>
<td style="text-align: left;">Возвращает индекс начала последней подстроки <code>str</code><br>в выбранном промежутке или <code>-1</code>, если она не найдена</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "123427".rfind("2")<br>4</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.format(args, *kwargs)</td>
<td style="text-align: left;">Последовательно заменяет <code>{}</code> в строке на свои аргументы</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "{}".format("1")<br>"1"<br>&gt;&gt;&gt; "{a}".format(a="1")<br>"1"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.format_map(dict)</td>
<td style="text-align: left;">Заменяет <code>{&lt;val&gt;}</code> в строке на <code>dict[&lt;val&gt;]</code></td>
<td><pre><code class="language-python">&gt;&gt;&gt; "{x} {y}".format_map(<br>...     {"x": 4, "y": -5}<br>... )<br>"4 -5"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.join(iter)</td>
<td style="text-align: left;">Склеивает элементы последовательности <code>iter</code><br>в одну строку с разделителем <code>str</code></td>
<td><pre><code class="language-python">&gt;&gt;&gt; " ".join(("1", "2"))<br>"1 2"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.strip([chars])</td>
<td style="text-align: left;">Возвращает строку без пробельных символов<br>или <code>chars</code> в начале и конце</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "   1 3  ".strip()<br>"1 3"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.lstrip([chars])</td>
<td style="text-align: left;">Возвращает строку без пробельных символов или <code>chars</code> в начале</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "   1 3  ".lstrip()<br>"1 3  "</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.rstrip([chars])</td>
<td style="text-align: left;">Возвращает строку без пробельных символов или <code>chars</code> в конце</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "   1 3  ".rstrip()<br>"   1 3"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.replace(old, new)</td>
<td style="text-align: left;">Заменяет все подстроки <code>old</code> на <code>new</code></td>
<td><pre><code class="language-python">&gt;&gt;&gt; "1231".replace("1", "_")<br>"_23_"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.split((sep=" ", maxsplit=-1))</td>
<td style="text-align: left;">Возвращает список подстрок,<br>разделенных по <code>sep</code> до <code>maxsplit</code> раз</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "1 3".split()<br>["1", "3"]</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.splitlines(keepends=False)</td>
<td style="text-align: left;">Разделяет строку по <code>\n</code>.<br>Не удаляет разделители, если <code>keepends=True</code>.</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "1 3\n4".splitlines()<br>["1 3", "4"]</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.rsplit(sep=" ", maxsplit=-1)</td>
<td style="text-align: left;">Возвращает список подстрок,<br>разделенных по sep до <code>maxsplit</code> раз (с конца)</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "1 3".split()<br>["1", "3"]</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.zfill(width)</td>
<td style="text-align: left;">Заполняет строку указанным числом нулей в начале</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "1".zfill(5)<br>"00001"</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.maketrans(*args)</td>
<td style="text-align: left;">Возвращает таблицу перевода для <code>s.translate</code></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">str.translate(table)</td>
<td style="text-align: left;">Заменяет все символы строки согласно таблице перевода</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">str.partition(sep)</td>
<td style="text-align: left;">Разделяет строку на три части по первому разделителю <code>sep</code>:<br>[начало, sep, конец]</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">str.rpartition()</td>
<td style="text-align: left;">Разделяет строку на три части по последнему разделителю <code>sep</code>:<br>[начало, sep, конец]</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">str.isalnum()</td>
<td style="text-align: left;"><code>True</code>, если строка состоит только из букв и цифр</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">str.isalpha()</td>
<td style="text-align: left;"><code>True</code>, если строка состоит только из букв</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">str.isdecimal()</td>
<td style="text-align: left;"><code>True</code>, если строка состоит только из цифр</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">str.isidentifier()</td>
<td style="text-align: left;"><code>True</code>, если строка является идентификатором<br>(<code>if</code>, <code>class</code>, <code>assert</code>)</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">str.isnumeric()</td>
<td style="text-align: left;"><code>True</code>, если строка состоит только из цифр</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">str.isprintable()</td>
<td style="text-align: left;"><code>True</code>, если все символы строки отображаются<br>(например, <code>\n</code>, <code>\t</code>)</td>
<td></td>
</tr>
<tr>
<td style="text-align: left;">str.isspace()</td>
<td style="text-align: left;"><code>True</code>, если строка состоит из пробелов</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "    ".isspace()<br>True<br>&gt;&gt;&gt; "a".isspace()<br>False</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.istitle()</td>
<td style="text-align: left;"><code>True</code>, если строка начинается с заглавной буквы,<br>а остальные — строчные</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "Aa".istitle()<br>True<br>&gt;&gt;&gt; "aA".istitle()<br>False<br>&gt;&gt;&gt; "Aa1 ".istitle()<br>True</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.isascii()</td>
<td style="text-align: left;">Проверяет, состоит ли строка только из ASCII символов</td>
<td><pre><code class="language-python">&gt;&gt;&gt; # Состоит только из ASCII<br>&gt;&gt;&gt; "Hello, World!".isascii()<br>True<br>&gt;&gt;&gt; # Состоит не из ASCII<br>&gt;&gt;&gt; "Привет, мир!".isascii()<br>False<br>&gt;&gt;&gt; # Не содержит не-ASCII<br>&gt;&gt;&gt; "".isascii()<br>True</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">str.isdigit()</td>
<td style="text-align: left;">Проверяет, состоит ли строка только из цифр (0-9)</td>
<td><pre><code class="language-python">&gt;&gt;&gt; "12345".isdigit()<br>True<br>&gt;&gt;&gt; "abc123".isdigit()<br>False<br>&gt;&gt;&gt; "123 456".isdigit()<br>False<br>&gt;&gt;&gt; "123.45".isdigit()<br>False<br>&gt;&gt;&gt; "+123".isdigit()<br>False<br>&gt;&gt;&gt; "-123".isdigit()<br>False</code></pre></td>
</tr>
</tbody>
</table>
<p><strong>Символы</strong></p>
<table>
<thead>
<tr>
<th style="text-align: left;">Символ</th>
<th style="text-align: left;">Назначение</th>
<th style="text-align: left;">Пример</th>
<th style="text-align: left;">Результат</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><code>\n</code></td>
<td style="text-align: left;">Перевод строки</td>
<td style="text-align: left;"><code>"ab\ncd"</code></td>
<td style="text-align: left;">ab<br>cd</td>
</tr>
<tr>
<td style="text-align: left;"><code>\</code></td>
<td style="text-align: left;">Экранирование</td>
<td style="text-align: left;"><code>"ab\ncd"</code></td>
<td style="text-align: left;">ab\ncd</td>
</tr>
<tr>
<td style="text-align: left;"><code>\a</code></td>
<td style="text-align: left;">Звонок</td>
<td style="text-align: left;"><code>"a\aa"</code></td>
<td style="text-align: left;">a[BEL]a</td>
</tr>
<tr>
<td style="text-align: left;"><code>\b</code></td>
<td style="text-align: left;">Забой</td>
<td style="text-align: left;"><code>"ab\ba"</code></td>
<td style="text-align: left;">ac</td>
</tr>
<tr>
<td style="text-align: left;"><code>\f</code></td>
<td style="text-align: left;">Перевод страницы</td>
<td style="text-align: left;"><code>"a\fa"</code></td>
<td style="text-align: left;">a[FF]a</td>
</tr>
<tr>
<td style="text-align: left;"><code>\r</code></td>
<td style="text-align: left;">Возврат каретки</td>
<td style="text-align: left;"><code>"ab\rcd"</code></td>
<td style="text-align: left;">cd</td>
</tr>
<tr>
<td style="text-align: left;"><code>\t</code></td>
<td style="text-align: left;">Горизонтальная табуляция</td>
<td style="text-align: left;"><code>"a\ta"</code></td>
<td style="text-align: left;">a a</td>
</tr>
<tr>
<td style="text-align: left;"><code>\v</code></td>
<td style="text-align: left;">Вертикальная табуляция</td>
<td style="text-align: left;"><code>"a\va"</code></td>
<td style="text-align: left;">a[VT]a</td>
</tr>
<tr>
<td style="text-align: left;"><code>\N{id}</code></td>
<td style="text-align: left;">Символ Юникода по id</td>
<td style="text-align: left;"><code>"\N{Degree Sign}"</code></td>
<td style="text-align: left;">°</td>
</tr>
<tr>
<td style="text-align: left;"><code>\uhhhh</code></td>
<td style="text-align: left;">16-ричный символ Юникода</td>
<td style="text-align: left;"><code>"\u2030"</code></td>
<td style="text-align: left;">‰</td>
</tr>
<tr>
<td style="text-align: left;"><code>\Uhhhh</code></td>
<td style="text-align: left;">32-ичный символ Юникода</td>
<td style="text-align: left;"><code>"\U00000394"</code></td>
<td style="text-align: left;">Δ</td>
</tr>
<tr>
<td style="text-align: left;"><code>\xhh</code></td>
<td style="text-align: left;">16-ричное значение символа</td>
<td style="text-align: left;"><code>"\x2A"</code></td>
<td style="text-align: left;">*</td>
</tr>
<tr>
<td style="text-align: left;"><code>\ooo</code></td>
<td style="text-align: left;">восьмеричное значение символа</td>
<td style="text-align: left;"><code>"\275"</code></td>
<td style="text-align: left;">½</td>
</tr>
<tr>
<td style="text-align: left;"><code>\0</code></td>
<td style="text-align: left;">символ Null</td>
<td style="text-align: left;"><code>"\0"</code></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><code>\u00A0</code></td>
<td style="text-align: left;">символ неразнывного пробела</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>