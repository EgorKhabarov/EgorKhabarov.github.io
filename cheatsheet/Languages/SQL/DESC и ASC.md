<p><strong><code>DESC</code></strong> и <strong><code>ASC</code></strong> — это ключевые слова, используемые для
указания порядка сортировки данных в запросах SQL в команде <code>ORDER BY</code></p>
<h1>Ключевые моменты</h1>
<h3><code>ASC</code> указывает сортировку по возрастанию <em>(по умолчанию)</em></h3>
<ul>
<li>"Ascending" — по возрастанию</li>
<li>Сортирует данные от меньшего к большему</li>
<li>Для чисел: от минимального значения к максимальному</li>
<li>Для строк: от A до Z (в алфавитном порядке)</li>
<li>Для дат: от самой ранней к самой поздней</li>
<li><div class="code_element"><div class="lang_line"><text>sql</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-sql"><div class="highlight"><pre><span></span><span class="k">SELECT</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">FROM</span><span class="w"> </span><span class="n">employees</span>
<span class="k">ORDER</span><span class="w"> </span><span class="k">BY</span><span class="w"> </span><span class="n">name</span><span class="p">;</span>
<span class="c1">-- Эквивалентно ORDER BY name ASC;</span>
</pre></div></div></div></li>
</ul>
<h3><code>DESC</code> указывает сортировку по убыванию</h3>
<ul>
<li>"Descending" — по убыванию</li>
<li>Сортирует данные от большего к меньшему</li>
<li>Для чисел: от максимального значения к минимальному</li>
<li>Для строк: от Z до A (в обратном алфавитном порядке)</li>
<li>Для дат: от самой поздней к самой ранней</li>
<li><div class="code_element"><div class="lang_line"><text>sql</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-sql"><div class="highlight"><pre><span></span><span class="k">SELECT</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">FROM</span><span class="w"> </span><span class="n">employees</span>
<span class="k">ORDER</span><span class="w"> </span><span class="k">BY</span><span class="w"> </span><span class="n">salary</span><span class="w"> </span><span class="k">DESC</span><span class="p">;</span>
</pre></div></div></div></li>
</ul>
<h3>Комбинированная сортировка</h3>
<p>Можно задавать разные порядки сортировки для нескольких столбцов</p>
<div class="code_element"><div class="lang_line"><text>sql</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-sql"><div class="highlight"><pre><span></span><span class="k">SELECT</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">FROM</span><span class="w"> </span><span class="n">employees</span>
<span class="k">ORDER</span><span class="w"> </span><span class="k">BY</span><span class="w"> </span><span class="n">department</span><span class="w"> </span><span class="k">ASC</span><span class="p">,</span>
<span class="w">         </span><span class="n">salary</span><span class="w"> </span><span class="k">DESC</span><span class="p">;</span>
</pre></div></div></div>
<p>Сначала сортирует по отделу в алфавитном порядке, затем внутри отдела по убыванию зарплаты</p>