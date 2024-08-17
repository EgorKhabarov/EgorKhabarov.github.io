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
<div class="code-element"><div class="lang-line"><text>sql</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">SELECT</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">FROM</span><span class="w"> </span><span class="n">Table1</span>
<span class="k">FULL</span><span class="w"> </span><span class="k">OUTER</span><span class="w"> </span><span class="k">JOIN</span><span class="w"> </span><span class="n">Table2</span>
<span class="k">ON</span><span class="w"> </span><span class="n">Table1</span><span class="p">.</span><span class="n">Field1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Table2</span><span class="p">.</span><span class="n">Field1</span><span class="p">;</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>sql</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">SELECT</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">FROM</span><span class="w"> </span><span class="n">Table1</span>
<span class="k">CROSS</span><span class="w"> </span><span class="k">JOIN</span><span class="w"> </span><span class="n">Table2</span><span class="p">;</span>
</pre></div></div></div>