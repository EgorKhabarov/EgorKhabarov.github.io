<h1>Особенности</h1>
<ul>
<li><strong>Неизменяемость (immutable)</strong>: После создания строка не может быть изменена.
Все операции, которые, казалось бы, изменяют строку, возвращают новый объект <code>String</code>.</li>
<li><strong>Пул строк</strong>: При создании строк литералами Java сохраняет их в специальный пул строк, что помогает экономить память.</li>
</ul>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">;</span>
<span class="n">String</span><span class="w"> </span><span class="n">s2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">String</span><span class="p">(</span><span class="s">&quot;World&quot;</span><span class="p">);</span>
</pre></div></div></div>

<h1>Методы</h1>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>.charAt(int index)</code></td>
<td>Возвращает символ по указанному индексу</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">char</span><span class="w"> </span><span class="n">c</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">charAt</span><span class="p">(</span><span class="mi">1</span><span class="p">);</span><br><span class="c1">// &#39;e&#39;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.length()</code></td>
<td>Возвращает длину строки</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">len</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">length</span><span class="p">();</span><br><span class="c1">// 5</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.concat(String str)</code></td>
<td>Склеивает две строки, возвращает новую строку</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">concat</span><span class="p">(</span><span class="s">&quot; World&quot;</span><span class="p">);</span><br><span class="c1">// &quot;Hello World&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.contains(CharSequence)</code></td>
<td>Проверяет, содержит ли строка<br>указанную последовательность символов</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">boolean</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">contains</span><span class="p">(</span><span class="s">&quot;ll&quot;</span><span class="p">);</span><br><span class="c1">// true</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.equals(Object obj)</code></td>
<td>Проверяет строки на равенство</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">boolean</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">equals</span><span class="p">(</span><span class="s">&quot;hello&quot;</span><span class="p">);</span><br><span class="c1">// false</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.equalsIgnoreCase(String str)</code></td>
<td>Проверяет строки на равенство, игнорируя регистр символов</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">boolean</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">equalsIgnoreCase</span><span class="p">(</span><span class="s">&quot;hello&quot;</span><span class="p">);</span><br><span class="c1">// true</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.startsWith(String prefix)</code></td>
<td>Проверяет, начинается ли строка с указанного префикса</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">boolean</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">startsWith</span><span class="p">(</span><span class="s">&quot;He&quot;</span><span class="p">);</span><br><span class="c1">// true</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.endsWith(String suffix)</code></td>
<td>Проверяет, заканчивается ли строка указанным суффиксом</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">boolean</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">endsWith</span><span class="p">(</span><span class="s">&quot;lo&quot;</span><span class="p">);</span><br><span class="c1">// true</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.indexOf(String str)</code></td>
<td>Возвращает индекс первого вхождения подстроки</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">indexOf</span><span class="p">(</span><span class="s">&quot;l&quot;</span><span class="p">);</span><br><span class="c1">// 2</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.lastIndexOf(String str)</code></td>
<td>Возвращает индекс последнего вхождения подстроки</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">lastIndexOf</span><span class="p">(</span><span class="s">&quot;l&quot;</span><span class="p">);</span><br><span class="c1">// 3</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.substring</code><br>(int beginIndex)</td>
<td>Возвращает подстроку, начиная с указанного индекса</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">sub</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">substring</span><span class="p">(</span><span class="mi">2</span><span class="p">);</span><br><span class="c1">// &quot;llo&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.substring</code><br>(int beginIndex, int endIndex)</td>
<td>Возвращает подстроку с указанного<br>начала до конца (не включая)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">sub</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">substring</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">4</span><span class="p">);</span><br><span class="c1">// &quot;ell&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.toLowerCase()</code></td>
<td>Возвращает новую строку, переведенную в нижний регистр</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;HELLO&quot;</span><span class="p">.</span><span class="na">toLowerCase</span><span class="p">();</span><br><span class="c1">// &quot;hello&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.toUpperCase()</code></td>
<td>Возвращает новую строку, переведенную в верхний регистр</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;hello&quot;</span><span class="p">.</span><span class="na">toUpperCase</span><span class="p">();</span><br><span class="c1">// &quot;HELLO&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.trim()</code></td>
<td>Удаляет начальные и конечные пробелы</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;  Hello  &quot;</span><span class="p">.</span><span class="na">trim</span><span class="p">();</span><br><span class="c1">// &quot;Hello&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.replace</code><br>(char oldChar, char newChar)</td>
<td>Заменяет все вхождения одного символа на другой</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">replace</span><span class="p">(</span><span class="sc">&#39;l&#39;</span><span class="p">,</span><span class="w"> </span><span class="sc">&#39;p&#39;</span><span class="p">);</span><br><span class="c1">// &quot;Heppo&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.replace</code><br>(CharSequence target,<br>CharSequence replacement)</td>
<td>Заменяет все вхождения одной<br>последовательности символов на другую</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">replace</span><span class="p">(</span><span class="s">&quot;ll&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;yy&quot;</span><span class="p">);</span><br><span class="c1">// &quot;Heyyo&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.split(String regex)</code></td>
<td>Разделяет строку по указанному регулярному выражению</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">arr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;a,b,c&quot;</span><span class="p">.</span><span class="na">split</span><span class="p">(</span><span class="s">&quot;,&quot;</span><span class="p">);</span><br><span class="n">Arrays</span><span class="p">.</span><span class="na">toString</span><span class="p">(</span><span class="s">&quot;a,b,c&quot;</span><span class="p">.</span><span class="na">split</span><span class="p">(</span><span class="s">&quot;,&quot;</span><span class="p">))</span><br><span class="o">[</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="n">c</span><span class="o">]</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.matches(String regex)</code></td>
<td>Проверяет, соответствует ли строка регулярному выражению</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">boolean</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;abc&quot;</span><span class="p">.</span><span class="na">matches</span><span class="p">(</span><span class="s">&quot;[a-z]+&quot;</span><span class="p">);</span><br><span class="c1">// true</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.isEmpty()</code></td>
<td>Проверяет, пуста ли строка (имеет длину 0)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">boolean</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;&quot;</span><span class="p">.</span><span class="na">isEmpty</span><span class="p">();</span><br><span class="c1">// true</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.intern()</code></td>
<td>Возвращает строку из пула строк или добавляет её туда</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">intern</span><span class="p">();</span><br><span class="c1">// &quot;Hello&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.toCharArray()</code></td>
<td>Преобразует строку в массив символов</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">char</span><span class="o">[]</span><span class="w"> </span><span class="n">arr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">.</span><span class="na">toCharArray</span><span class="p">();</span><br><span class="c1">// &quot;Hello&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.compareTo(String anotherString)</code></td>
<td>Сравнивает строки лексикографически</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">cmp</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;abc&quot;</span><span class="p">.</span><span class="na">compareTo</span><span class="p">(</span><span class="s">&quot;abd&quot;</span><span class="p">);</span><br><span class="c1">// -1</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.compareToIgnoreCase(String str)</code></td>
<td>Лексикографическое сравнение<br>строк без учета регистра</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">cmp</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;abc&quot;</span><span class="p">.</span><span class="na">compareToIgnoreCase</span><span class="p">(</span><span class="s">&quot;ABC&quot;</span><span class="p">);</span><br><span class="c1">// 0</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.format(String format, Object... args)</code></td>
<td>Возвращает отформатированную<br>строку на основе переданных аргументов</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">String</span><span class="p">.</span><span class="na">format</span><span class="p">(</span><span class="s">&quot;Hello %s&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;World&quot;</span><span class="p">);</span><br><span class="c1">// &quot;Hello World&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.join</code><br>(CharSequence delimiter,<br>CharSequence... elements)</td>
<td>Объединяет элементы в строку с указанным разделителем</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">String</span><span class="p">.</span><span class="na">join</span><span class="p">(</span><span class="s">&quot;, &quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;a&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;b&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;c&quot;</span><span class="p">);</span><br><span class="c1">// &quot;a, b, c&quot;</span><br></pre></div></pre></div></div></td>
</tr>
</tbody>
</table>
<h1>Примеры использования</h1>
<ol>
<li><strong>Склеивание строк:</strong></li>
</ol>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">;</span>
<span class="n">String</span><span class="w"> </span><span class="n">s2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;World&quot;</span><span class="p">;</span>
<span class="n">String</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">s1</span><span class="p">.</span><span class="na">concat</span><span class="p">(</span><span class="s">&quot; &quot;</span><span class="p">).</span><span class="na">concat</span><span class="p">(</span><span class="n">s2</span><span class="p">);</span><span class="w">  </span><span class="c1">// &quot;Hello World&quot;</span>
</pre></div></div></div>

<ol>
<li><strong>Получение подстроки:</strong></li>
</ol>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello World&quot;</span><span class="p">;</span>
<span class="n">String</span><span class="w"> </span><span class="n">sub</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">s</span><span class="p">.</span><span class="na">substring</span><span class="p">(</span><span class="mi">6</span><span class="p">);</span><span class="w">  </span><span class="c1">// &quot;World&quot;</span>
</pre></div></div></div>

<ol>
<li><strong>Замена символов:</strong></li>
</ol>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;apple&quot;</span><span class="p">;</span>
<span class="n">String</span><span class="w"> </span><span class="n">replaced</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">s</span><span class="p">.</span><span class="na">replace</span><span class="p">(</span><span class="sc">&#39;p&#39;</span><span class="p">,</span><span class="w"> </span><span class="sc">&#39;b&#39;</span><span class="p">);</span><span class="w">  </span><span class="c1">// &quot;abble&quot;</span>
</pre></div></div></div>

<ol>
<li><strong>Разделение строки:</strong></li>
</ol>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;a,b,c&quot;</span><span class="p">;</span>
<span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">parts</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">s</span><span class="p">.</span><span class="na">split</span><span class="p">(</span><span class="s">&quot;,&quot;</span><span class="p">);</span><span class="w">  </span><span class="c1">// [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;]</span>
</pre></div></div></div>

<ol>
<li><strong>Проверка содержания строки:</strong></li>
</ol>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;Hello&quot;</span><span class="p">;</span>
<span class="kt">boolean</span><span class="w"> </span><span class="n">contains</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">s</span><span class="p">.</span><span class="na">contains</span><span class="p">(</span><span class="s">&quot;ell&quot;</span><span class="p">);</span><span class="w">  </span><span class="c1">// true</span>
</pre></div></div></div>

<ol>
<li><strong>Форматирование строки:</strong></li>
</ol>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">formatted</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">String</span><span class="p">.</span><span class="na">format</span><span class="p">(</span><span class="s">&quot;Name: %s, Age: %d&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;Alice&quot;</span><span class="p">,</span><span class="w"> </span><span class="mi">30</span><span class="p">);</span>
<span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">formatted</span><span class="p">);</span><span class="w">  </span><span class="c1">// &quot;Name: Alice, Age: 30&quot;</span>
</pre></div></div></div>