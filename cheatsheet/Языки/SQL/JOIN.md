<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>JOIN</td>
<td>Используется для соединения двух таблиц в одну.<br>Существует ряд различных видов JOIN, каждый из которых имеет свои особенности<br>и применяется в зависимости от ситуации.<br>INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN,<br>CROSS JOIN, NATURAL JOIN, UNION JOIN, STRAIGHT_JOIN, OUTER APPLY, CROSS APPLY</td>
</tr>
<tr>
<td>INNER JOIN - это самый распространенный вид JOIN</td>
<td>Соединяет две таблицы по совпадающим значениям определенных полей.<br>Результатом является таблица, содержащая только те строки,<br>которые совпадают по заданным полям.</td>
</tr>
<tr>
<td>LEFT JOIN аналогичен INNER JOIN</td>
<td>Результирующая таблица содержит все строки из левой (первой) таблицы,<br>даже если они не совпадают по заданным полям со второй таблицей.<br>Несовпадающие строки заполняются нулевыми значениями</td>
</tr>
<tr>
<td>RIGHT JOIN аналог LEFT JOIN</td>
<td>Результирующая таблица содержит все строки из правой (второй) таблицы,<br>даже если они не совпадают по заданным полям с первой таблицей.<br>Несовпадающие строки заполняются нулевыми значениями.</td>
</tr>
<tr>
<td>FULL OUTER JOIN комбинация LEFT JOIN и RIGHT JOIN.</td>
<td>Результирующая таблица содержит все строки из обоих таблиц,<br>даже если они не совпадают по заданным полям.<br>Несовпадающие строки заполняются нулевыми значениями.</td>
</tr>
<tr>
<td>CROSS JOIN</td>
<td>Cоединяет все строки из первой таблицы со всеми строками из второй таблицы,<br>создавая картежи, удовлетворяющие условию соединения.<br>Таким образом, CROSS JOIN не учитывает совпадающие<br>значения в таблицах и создает все возможные картежи.</td>
</tr>
</tbody>
</table>
<div class="code-element"><div class="lang-line"><text>sql</text><button class="copy-button" id="code550b" onclick="copyCode(code550, code550b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code550"><div class="highlight"><pre><span></span><span class="k">SELECT</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">FROM</span><span class="w"> </span><span class="n">Table1</span>
<span class="k">FULL</span><span class="w"> </span><span class="k">OUTER</span><span class="w"> </span><span class="k">JOIN</span><span class="w"> </span><span class="n">Table2</span>
<span class="k">ON</span><span class="w"> </span><span class="n">Table1</span><span class="p">.</span><span class="n">Field1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Table2</span><span class="p">.</span><span class="n">Field1</span><span class="p">;</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>sql</text><button class="copy-button" id="code551b" onclick="copyCode(code551, code551b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code551"><div class="highlight"><pre><span></span><span class="k">SELECT</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">FROM</span><span class="w"> </span><span class="n">Table1</span>
<span class="k">CROSS</span><span class="w"> </span><span class="k">JOIN</span><span class="w"> </span><span class="n">Table2</span><span class="p">;</span>
</pre></div></div></div>