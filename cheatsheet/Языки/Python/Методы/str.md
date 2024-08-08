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
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;capitalize&quot;</span><span class="o">.</span><span class="n">capitalize</span><span class="p">()</span><br><span class="unselectable"><span class="s2">&quot;Capitalize&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.casefold()</td>
<td style="text-align: left;">Переводит все символы в нижний регистр</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;CaSeFoLd&quot;</span><span class="o">.</span><span class="n">casefold</span><span class="p">()</span><br><span class="unselectable"><span class="s2">&quot;casefold&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.lower()</td>
<td style="text-align: left;">Переводит символы строки в нижний регистр</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;lOwEr&quot;</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span><br><span class="unselectable"><span class="s2">&quot;lower&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.upper()</td>
<td style="text-align: left;">Возвращает копию строки в верхнем регистре</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;upper&quot;</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span><br><span class="unselectable"><span class="s2">&quot;UPPER&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.swapcase()</td>
<td style="text-align: left;">Меняет регистр всех символов на противоположный</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;sWaPcAsE&quot;</span><span class="o">.</span><span class="n">swapcase</span><span class="p">()</span><br><span class="unselectable"><span class="s2">&quot;SwApCaSe&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.title()</td>
<td style="text-align: left;">Возвращает строку, где все слова начинаются с заглавной буквы,<br>а продолжаются строчными</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;title title&quot;</span><span class="o">.</span><span class="n">title</span><span class="p">()</span><br><span class="unselectable"><span class="s2">&quot;Title Title&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.isupper()</td>
<td style="text-align: left;"><code>True</code>, если строка в верхнем регистре</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;A&quot;</span><span class="o">.</span><span class="n">isupper</span><span class="p">()</span><br><span class="unselectable"><span class="kc">True</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;a&quot;</span><span class="o">.</span><span class="n">isupper</span><span class="p">()</span><br><span class="unselectable"><span class="kc">False</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.islower()</td>
<td style="text-align: left;"><code>True</code>, если вся строка в нижнем регистре</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;a&quot;</span><span class="o">.</span><span class="n">islower</span><span class="p">()</span><br><span class="unselectable"><span class="kc">True</span></span><br><span class="unselectable"><span class="s2">&quot;A&quot;</span><span class="o">.</span><span class="n">islower</span><span class="p">()</span></span><br><span class="unselectable"><span class="kc">False</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.center(width[, fillvalue])</td>
<td style="text-align: left;">Обрамляет значениями <code>fillvalue</code> строку,<br>пока длина не станет <code>width</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;0&quot;</span><span class="o">.</span><span class="n">center</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="s2">&quot;_&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="s2">&quot;__0__&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.ljust(width, fillchar=" ")</td>
<td style="text-align: left;">Добавляет в конец строки символ <code>fillchar</code>,<br>пока длина не станет <code>width</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1&quot;</span><span class="o">.</span><span class="n">ljust</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="s2">&quot;_&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="s2">&quot;1____&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.rjust(width, fillchar=" ")</td>
<td style="text-align: left;">Добавляет в начало строки символ <code>fillchar</code>,<br>пока длина не станет <code>width</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1&quot;</span><span class="o">.</span><span class="n">rjust</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="s2">&quot;_&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="s2">&quot;____1&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.count(str[, start][, end]</td>
<td style="text-align: left;">Считает количество подстрок <code>str</code> в выбранном промежутке строки</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;12123412&quot;</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s2">&quot;12&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="mi">3</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.encode(encoding, errors)</td>
<td style="text-align: left;">Меняет кодировку строки</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;qwerty123&quot;</span><span class="o">.</span><span class="n">encode</span><span class="p">()</span><br><span class="unselectable"><span class="sa">b</span><span class="s2">&quot;qwerty123&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.startswith(prefix[, start[, end]])</td>
<td style="text-align: left;"><code>True</code> если строка начинается с <code>prefix</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1234&quot;</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">&quot;34&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="kc">False</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1234&quot;</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">&quot;12&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="kc">True</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1234&quot;</span><span class="o">.</span><span class="n">startswith</span><span class="p">((</span><span class="s2">&quot;12&quot;</span><span class="p">,</span> <span class="s2">&quot;89&quot;</span><span class="p">))</span><br><span class="unselectable"><span class="kc">True</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.endswith(suffix[, start[, end]])</td>
<td style="text-align: left;"><code>True</code> если строка заканчивается на <code>suffix</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1234&quot;</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">&quot;12&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="kc">False</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1234&quot;</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">&quot;34&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="kc">True</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1234&quot;</span><span class="o">.</span><span class="n">endswith</span><span class="p">((</span><span class="s2">&quot;34&quot;</span><span class="p">,</span> <span class="s2">&quot;56&quot;</span><span class="p">))</span><br><span class="unselectable"><span class="kc">True</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.removeprefix(prefix: str)</td>
<td style="text-align: left;">Возвращает строку без прификса <code>prefix</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;123&quot;</span><span class="o">.</span><span class="n">removeprefix</span><span class="p">(</span><span class="s2">&quot;1&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="s2">&quot;23&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.removesuffix(suffix: str)</td>
<td style="text-align: left;">Возвращает строку без суффикса <code>suffix</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;123&quot;</span><span class="o">.</span><span class="n">removesuffix</span><span class="p">(</span><span class="s2">&quot;3&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="s2">&quot;12&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.expandtabs(tabsize=8)</td>
<td style="text-align: left;">Увеличивает размер символов табуляции до <code>tabsize</code> пробелов</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot; &quot;</span><span class="o">.</span><span class="n">expandtabs</span><span class="p">(</span><span class="mi">8</span><span class="p">)</span><br><span class="unselectable"><span class="s2">&quot;        &quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.index(str[, start[, end]])</td>
<td style="text-align: left;">Возвращает индекс начала первой подстроки <code>str</code><br>в выбранном промежутке или <code>ValueError</code>, если она не найдена</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1234&quot;</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s2">&quot;2&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="mi">1</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.rindex(str[, start[, end]])</td>
<td style="text-align: left;">Возвращает индекс начала последней подстроки <code>str</code><br>в выбранном промежутке или <code>ValueError</code>, если она не найдена</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;123427&quot;</span><span class="o">.</span><span class="n">rindex</span><span class="p">(</span><span class="s2">&quot;2&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="mi">4</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.find(str[, start[, end]])</td>
<td style="text-align: left;">Возвращает индекс начала первой подстроки <code>str</code><br>в выбранном промежутке или <code>-1</code>, если она не найдена</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1234&quot;</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s2">&quot;2&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="mi">1</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.rfind(str[, start[, end]])</td>
<td style="text-align: left;">Возвращает индекс начала последней подстроки <code>str</code><br>в выбранном промежутке или <code>-1</code>, если она не найдена</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;123427&quot;</span><span class="o">.</span><span class="n">rfind</span><span class="p">(</span><span class="s2">&quot;2&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="mi">4</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.format(args, *kwargs)</td>
<td style="text-align: left;">Последовательно заменяет <code>{}</code> в строке на свои аргументы</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;</span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s2">&quot;1&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="s2">&quot;1&quot;</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;</span><span class="si">{a}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">a</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="s2">&quot;1&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.format_map(dict)</td>
<td style="text-align: left;">Заменяет <code>{&lt;val&gt;}</code> в строке на <code>dict[&lt;val&gt;]</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;</span><span class="si">{x}</span><span class="s2"> </span><span class="si">{y}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format_map</span><span class="p">(</span><br><span class="unselectable"><span class="o">...</span> </span><span class="p">{</span><span class="s2">&quot;x&quot;</span><span class="p">:</span> <span class="mi">4</span><span class="p">,</span> <span class="s2">&quot;y&quot;</span><span class="p">:</span> <span class="o">-</span><span class="mi">5</span><span class="p">}</span><br><span class="unselectable"><span class="o">...</span> </span><span class="p">)</span><br><span class="unselectable"><span class="s2">&quot;4 -5&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.join(iter)</td>
<td style="text-align: left;">Склеивает элементы последовательности <code>iter</code><br>в одну строку с разделителем <code>str</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot; &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">((</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;2&quot;</span><span class="p">))</span><br><span class="unselectable"><span class="s2">&quot;1 2&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.strip([chars])</td>
<td style="text-align: left;">Возвращает строку без пробельных символов<br>или <code>chars</code> в начале и конце</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;   1 3   &quot;</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><br><span class="unselectable"><span class="s2">&quot;1 3&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.lstrip([chars])</td>
<td style="text-align: left;">Возвращает строку без пробельных символов или <code>chars</code> в начале</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;   1 3   &quot;</span><span class="o">.</span><span class="n">lstrip</span><span class="p">()</span><br><span class="unselectable"><span class="s2">&quot;1 3    &quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.rstrip([chars])</td>
<td style="text-align: left;">Возвращает строку без пробельных символов или <code>chars</code> в конце</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;   1 3   &quot;</span><span class="o">.</span><span class="n">rstrip</span><span class="p">()</span><br><span class="unselectable"><span class="s2">&quot;   1 3&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.replace(old, new)</td>
<td style="text-align: left;">Заменяет все подстроки <code>old</code> на <code>new</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1231&quot;</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;_&quot;</span><span class="p">)</span><br><span class="unselectable"><span class="s2">&quot;_23_&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.split((sep=" ", maxsplit=-1))</td>
<td style="text-align: left;">Возвращает список подстрок,<br>разделенных по <code>sep</code> до <code>maxsplit</code> раз</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1 3&quot;</span><span class="o">.</span><span class="n">split</span><span class="p">()</span><br><span class="unselectable"><span class="p">[</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;3&quot;</span><span class="p">]</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.splitlines(keepends=False)</td>
<td style="text-align: left;">Разделяет строку по <code>\n</code>.<br>Не удаляет разделители, если <code>keepends=True</code>.</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1 3</span><span class="se">\n</span><span class="s2">4&quot;</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()</span><br><span class="unselectable"><span class="p">[</span><span class="s2">&quot;1 3&quot;</span><span class="p">,</span> <span class="s2">&quot;4&quot;</span><span class="p">]</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.rsplit(sep=" ", maxsplit=-1)</td>
<td style="text-align: left;">Возвращает список подстрок,<br>разделенных по sep до <code>maxsplit</code> раз (с конца)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1 3&quot;</span><span class="o">.</span><span class="n">split</span><span class="p">()</span><br><span class="unselectable"><span class="p">[</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;3&quot;</span><span class="p">]</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.zfill(width)</td>
<td style="text-align: left;">Заполняет строку указанным числом нулей в начале</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;1&quot;</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span><br><span class="unselectable"><span class="s2">&quot;00001&quot;</span></span><br></pre></div></pre></div></div></td>
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
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;     &quot;</span><span class="o">.</span><span class="n">isspace</span><span class="p">()</span><br><span class="unselectable"><span class="kc">True</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;a&quot;</span><span class="o">.</span><span class="n">isspace</span><span class="p">()</span><br><span class="unselectable"><span class="kc">False</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.istitle()</td>
<td style="text-align: left;"><code>True</code>, если строка начинается с заглавной буквы,<br>а остальные — строчные</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;Aa&quot;</span><span class="o">.</span><span class="n">istitle</span><span class="p">()</span><br><span class="unselectable"><span class="kc">True</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;aA&quot;</span><span class="o">.</span><span class="n">istitle</span><span class="p">()</span><br><span class="unselectable"><span class="kc">False</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;Aa1 &quot;</span><span class="o">.</span><span class="n">istitle</span><span class="p">()</span><br><span class="unselectable"><span class="kc">True</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.isascii()</td>
<td style="text-align: left;">Проверяет, состоит ли строка только из ASCII символов</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Состоит только из ASCII</span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;Hello, World!&quot;</span><span class="o">.</span><span class="n">isascii</span><span class="p">()</span><br><span class="unselectable"><span class="kc">True</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Состоит не из ASCII</span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;Привет, мир!&quot;</span><span class="o">.</span><span class="n">isascii</span><span class="p">()</span><br><span class="unselectable"><span class="kc">False</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Не содержит не-ASCII</span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;&quot;</span><span class="o">.</span><span class="n">isascii</span><span class="p">()</span><br><span class="unselectable"><span class="kc">True</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">str.isdigit()</td>
<td style="text-align: left;">Проверяет, состоит ли строка только из цифр (0-9)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;12345&quot;</span><span class="o">.</span><span class="n">isdigit</span><span class="p">()</span><br><span class="unselectable"><span class="kc">True</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;abc123&quot;</span><span class="o">.</span><span class="n">isdigit</span><span class="p">()</span><br><span class="unselectable"><span class="kc">False</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;123 456&quot;</span><span class="o">.</span><span class="n">isdigit</span><span class="p">()</span><br><span class="unselectable"><span class="kc">False</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;123.45&quot;</span><span class="o">.</span><span class="n">isdigit</span><span class="p">()</span><br><span class="unselectable"><span class="kc">False</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;+123&quot;</span><span class="o">.</span><span class="n">isdigit</span><span class="p">()</span><br><span class="unselectable"><span class="kc">False</span></span><br><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="s2">&quot;-123&quot;</span><span class="o">.</span><span class="n">isdigit</span><span class="p">()</span><br><span class="unselectable"><span class="kc">False</span></span><br></pre></div></pre></div></div></td>
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