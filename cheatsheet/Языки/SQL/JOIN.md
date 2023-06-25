<ul>
<li>
<p>JOIN
    Используется для соединения двух таблиц в одну.
    Существует ряд различных видов JOIN, каждый из которых имеет свои особенности
    и применяется в зависимости от ситуации.
    INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN,
    CROSS JOIN, NATURAL JOIN, UNION JOIN, STRAIGHT_JOIN, OUTER APPLY, CROSS APPLY</p>
</li>
<li>
<p>INNER JOIN - это самый распространенный вид JOIN
    Соединяет две таблицы по совпадающим значениям определенных полей.
    Результатом является таблица, содержащая только те строки,
    которые совпадают по заданным полям.</p>
</li>
<li>
<p>LEFT JOIN аналогичен INNER JOIN
    Результирующая таблица содержит все строки из левой (первой) таблицы,
    даже если они не совпадают по заданным полям со второй таблицей.
    Несовпадающие строки заполняются нулевыми значениями</p>
</li>
<li>
<p>RIGHT JOIN аналог LEFT JOIN
    Результирующая таблица содержит все строки из правой (второй) таблицы,
    даже если они не совпадают по заданным полям с первой таблицей.
    Несовпадающие строки заполняются нулевыми значениями.</p>
</li>
<li>
<p>FULL OUTER JOIN комбинация LEFT JOIN и RIGHT JOIN.
    Результирующая таблица содержит все строки из обоих таблиц,
    даже если они не совпадают по заданным полям.
    Несовпадающие строки заполняются нулевыми значениями.</p>
</li>
</ul>
<div class="code-element">
    <div class="lang-line">sql<button class="copy-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="k">SELECT</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">FROM</span><span class="w"> </span><span class="n">Table1</span>
<span class="k">FULL</span><span class="w"> </span><span class="k">OUTER</span><span class="w"> </span><span class="k">JOIN</span><span class="w"> </span><span class="n">Table2</span>
<span class="k">ON</span><span class="w"> </span><span class="n">Table1</span><span class="p">.</span><span class="n">Field1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Table2</span><span class="p">.</span><span class="n">Field1</span><span class="p">;</span>
</pre></div></div>
</div>

<ul>
<li>CROSS JOIN
    соединяет все строки из первой таблицы со всеми строками из второй таблицы,
    создавая картежи, удовлетворяющие условию соединения.
    Таким образом, CROSS JOIN не учитывает совпадающие
    значения в таблицах и создает все возможные картежи.</li>
</ul>
<div class="code-element">
    <div class="lang-line">sql<button class="copy-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="k">SELECT</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">FROM</span><span class="w"> </span><span class="n">Table1</span>
<span class="k">CROSS</span><span class="w"> </span><span class="k">JOIN</span><span class="w"> </span><span class="n">Table2</span><span class="p">;</span>
</pre></div></div>
</div>