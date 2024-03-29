<table>
<thead>
<tr>
<th style="text-align: left;">Метод</th>
<th style="text-align: left;">Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">str.capitalize()</td>
<td style="text-align: left;">Переводит первую букву в верхний, а остальные в нижний регистр.</td>
</tr>
<tr>
<td style="text-align: left;">str.casefold()</td>
<td style="text-align: left;">Переводит все символы в нижний регистр</td>
</tr>
<tr>
<td style="text-align: left;">str.center(width[, fillvalue])</td>
<td style="text-align: left;">Обрамляет значениями fillvalue строку, пока длина не станет width</td>
</tr>
<tr>
<td style="text-align: left;">str.count(str[, start][, end]</td>
<td style="text-align: left;">Считает количество подстрок str в выбранном промежутке строки</td>
</tr>
<tr>
<td style="text-align: left;">str.encode(encoding, errors)</td>
<td style="text-align: left;">Меняет кодировку строки</td>
</tr>
<tr>
<td style="text-align: left;">str.endswith(suffix[, start][, end])</td>
<td style="text-align: left;">Возвращает True если строка заканчивается на suffix, иначе False</td>
</tr>
<tr>
<td style="text-align: left;">str.expandtabs(tabsize=8)</td>
<td style="text-align: left;">Увеличивает размер символов табуляции до tabsize пробелов</td>
</tr>
<tr>
<td style="text-align: left;">str.find(str[, start][, end])</td>
<td style="text-align: left;">Возвращает индекс начала первой подстроки str в выбранном промежутке или -1, если она не найдена</td>
</tr>
<tr>
<td style="text-align: left;">str.format(args, *kwargs)</td>
<td style="text-align: left;">Последовательно заменяет {} в строке на свои аргументы</td>
</tr>
<tr>
<td style="text-align: left;">str.format_map(dict)</td>
<td style="text-align: left;">Заменяет {<val>} в строке на dict[<val>]</td>
</tr>
<tr>
<td style="text-align: left;">str.index(str[, start][, end])</td>
<td style="text-align: left;">Возвращает индекс начала первой подстроки str в выбранном промежутке или ValueError, если она не найдена</td>
</tr>
<tr>
<td style="text-align: left;">str.isalnum()</td>
<td style="text-align: left;">Возвращает True, если строка состоит только из букв и цифр, иначе False</td>
</tr>
<tr>
<td style="text-align: left;">str.isalpha()</td>
<td style="text-align: left;">Возвращает True, если строка состоит только из букв, иначе False</td>
</tr>
<tr>
<td style="text-align: left;">str.isdecimal()</td>
<td style="text-align: left;">Возвращает True, если строка состоит только из цифр, иначе False [1]</td>
</tr>
<tr>
<td style="text-align: left;">str.isdigit()</td>
<td style="text-align: left;">Возвращает True, если строка состоит только из цифр, иначе False [1]</td>
</tr>
<tr>
<td style="text-align: left;">str.isidentifier()</td>
<td style="text-align: left;">Возвращает True, если строка является идентификатором (if, class, assert), иначе False</td>
</tr>
<tr>
<td style="text-align: left;">str.islower()</td>
<td style="text-align: left;">Возвращает True, если вся строка в нижнем регистре, иначе False</td>
</tr>
<tr>
<td style="text-align: left;">str.isnumeric()</td>
<td style="text-align: left;">Возвращает True, если строка состоит только из цифр, иначе False [1]</td>
</tr>
<tr>
<td style="text-align: left;">str.isprintable()</td>
<td style="text-align: left;">Возвращает True, если все символы строки отображаются, иначе False (например, \n, \t)</td>
</tr>
<tr>
<td style="text-align: left;">str.isspace()</td>
<td style="text-align: left;">Возвращает True, если строка состоит из пробелов, иначе False</td>
</tr>
<tr>
<td style="text-align: left;">str.istitle()</td>
<td style="text-align: left;">Возвращает True, если строка начинается с заглавной буквы, а остальные — строчные, иначе False</td>
</tr>
<tr>
<td style="text-align: left;">str.isupper()</td>
<td style="text-align: left;">Возвращает True, если строка в верхнем регистре, иначе False</td>
</tr>
<tr>
<td style="text-align: left;">str.join(iter)</td>
<td style="text-align: left;">Склеивает элементы последовательности iter в одну строку с разделителем s</td>
</tr>
<tr>
<td style="text-align: left;">str.ljust(width, fillchar=' ')</td>
<td style="text-align: left;">Добавляет в конец строки символ fillchar, пока длина не станет width</td>
</tr>
<tr>
<td style="text-align: left;">str.lower()</td>
<td style="text-align: left;">Переводит символы строки в нижний регистр</td>
</tr>
<tr>
<td style="text-align: left;">str.lstrip([chars])</td>
<td style="text-align: left;">Возвращает строку без пробельных символов или chars в начале</td>
</tr>
<tr>
<td style="text-align: left;">str.maketrans(*args)</td>
<td style="text-align: left;">Возвращает таблицу перевода для s.translate</td>
</tr>
<tr>
<td style="text-align: left;">str.partition(sep)</td>
<td style="text-align: left;">Разделяет строку на три части по первому разделителю sep: [начало, sep, конец]</td>
</tr>
<tr>
<td style="text-align: left;">str.replace(old, new)</td>
<td style="text-align: left;">Заменяет все подстроки old на new</td>
</tr>
<tr>
<td style="text-align: left;">str.rfind(str[, start][, end])</td>
<td style="text-align: left;">Возвращает индекс начала последней подстроки str в выбранном промежутке или -1, если она не найдена</td>
</tr>
<tr>
<td style="text-align: left;">str.rindex(str[, start][, end])</td>
<td style="text-align: left;">Возвращает индекс начала последней подстроки str в выбранном промежутке или ValueError, если она не найдена</td>
</tr>
<tr>
<td style="text-align: left;">str.rjust(width, fillchar=' ')</td>
<td style="text-align: left;">Добавляет в начало строки символ fillchar, пока длина не станет width</td>
</tr>
<tr>
<td style="text-align: left;">str.rpartition()</td>
<td style="text-align: left;">Разделяет строку на три части по последнему разделителю sep: [начало, sep, конец]</td>
</tr>
<tr>
<td style="text-align: left;">str.rsplit(sep=' ', maxsplit=-1)</td>
<td style="text-align: left;">Возвращает список подстрок, разделенных по sep до maxsplit раз (с конца)</td>
</tr>
<tr>
<td style="text-align: left;">str.rstrip([chars])</td>
<td style="text-align: left;">Возвращает строку без пробельных символов или chars в конце</td>
</tr>
<tr>
<td style="text-align: left;">str.split((sep=' ', maxsplit=-1))</td>
<td style="text-align: left;">Возвращает список подстрок, разделенных по sep до maxsplit раз</td>
</tr>
<tr>
<td style="text-align: left;">str.splitlines(keepends=False)</td>
<td style="text-align: left;">Разделяет строку по \n. Не удаляет разделители, если keepends=True.</td>
</tr>
<tr>
<td style="text-align: left;">str.startswith(prefix[, start][, end])</td>
<td style="text-align: left;">Возвращает True если строка начинается с prefix, иначе False</td>
</tr>
<tr>
<td style="text-align: left;">str.strip([chars])</td>
<td style="text-align: left;">Возвращает строку без пробельных символов или chars в начале и конце</td>
</tr>
<tr>
<td style="text-align: left;">str.swapcase()</td>
<td style="text-align: left;">Меняет регистр всех символов на противоположный</td>
</tr>
<tr>
<td style="text-align: left;">str.title()</td>
<td style="text-align: left;">Возвращает строку, где все слова начинаются с заглавной буквы, а продолжаются строчными</td>
</tr>
<tr>
<td style="text-align: left;">str.translate(table)</td>
<td style="text-align: left;">Заменяет все символы строки согласно таблице перевода</td>
</tr>
<tr>
<td style="text-align: left;">str.upper()</td>
<td style="text-align: left;">Возвращает копию строки в верхнем регистре</td>
</tr>
<tr>
<td style="text-align: left;">str.zfill(width)</td>
<td style="text-align: left;">Заполняет строку указанным числом нулей в начале</td>
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
<td style="text-align: left;">\n</td>
<td style="text-align: left;">Перевод строки</td>
<td style="text-align: left;">'ab\ncd'</td>
<td style="text-align: left;">ab</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">cd</td>
</tr>
<tr>
<td style="text-align: left;">\</td>
<td style="text-align: left;">Экранирование</td>
<td style="text-align: left;">'ab\ncd'</td>
<td style="text-align: left;">ab\ncd</td>
</tr>
<tr>
<td style="text-align: left;">\a</td>
<td style="text-align: left;">Звонок</td>
<td style="text-align: left;">'a\aa'</td>
<td style="text-align: left;">a[BEL]a</td>
</tr>
<tr>
<td style="text-align: left;">\b</td>
<td style="text-align: left;">Забой</td>
<td style="text-align: left;">'ab\ba'</td>
<td style="text-align: left;">ac</td>
</tr>
<tr>
<td style="text-align: left;">\f</td>
<td style="text-align: left;">Перевод страницы</td>
<td style="text-align: left;">'a\fa'</td>
<td style="text-align: left;">a[FF]a</td>
</tr>
<tr>
<td style="text-align: left;">\r</td>
<td style="text-align: left;">Возврат каретки</td>
<td style="text-align: left;">'ab\rcd'</td>
<td style="text-align: left;">cd</td>
</tr>
<tr>
<td style="text-align: left;">\t</td>
<td style="text-align: left;">Горизонтальная табуляция</td>
<td style="text-align: left;">'a\ta'</td>
<td style="text-align: left;">a a</td>
</tr>
<tr>
<td style="text-align: left;">\v</td>
<td style="text-align: left;">Вертикальная табуляция</td>
<td style="text-align: left;">'a\va'</td>
<td style="text-align: left;">a[VT]a</td>
</tr>
<tr>
<td style="text-align: left;">\N{id}</td>
<td style="text-align: left;">Символ Юникода по id</td>
<td style="text-align: left;">'\N{Degree Sign}'</td>
<td style="text-align: left;">°</td>
</tr>
<tr>
<td style="text-align: left;">\uhhhh</td>
<td style="text-align: left;">16-ричный символ Юникода</td>
<td style="text-align: left;">'\u2030'</td>
<td style="text-align: left;">‰</td>
</tr>
<tr>
<td style="text-align: left;">\Uhhhh</td>
<td style="text-align: left;">32-ичный символ Юникода</td>
<td style="text-align: left;">'\U00000394'</td>
<td style="text-align: left;">Δ</td>
</tr>
<tr>
<td style="text-align: left;">\xhh</td>
<td style="text-align: left;">16-ричное значение символа</td>
<td style="text-align: left;">'\x2A'</td>
<td style="text-align: left;">*</td>
</tr>
<tr>
<td style="text-align: left;">\ooo</td>
<td style="text-align: left;">восьмеричное значение символа</td>
<td style="text-align: left;">'/275'</td>
<td style="text-align: left;">½</td>
</tr>
<tr>
<td style="text-align: left;">\0</td>
<td style="text-align: left;">символ Null</td>
<td style="text-align: left;">'\0'</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">\u00A0</td>
<td style="text-align: left;">символ неразнывного пробела</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>