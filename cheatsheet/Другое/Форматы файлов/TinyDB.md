<p>Шпаргалка по TinyDB в Python:</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code786b" onclick="copyCode(code786, code786b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code786"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>tinydb
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code787b" onclick="copyCode(code787, code787b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code787"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">tinydb</span> <span class="kn">import</span> <span class="n">TinyDB</span><span class="p">,</span> <span class="n">Query</span>

<span class="c1"># Создание базы данных</span>
<span class="n">db</span> <span class="o">=</span> <span class="n">TinyDB</span><span class="p">(</span><span class="s2">&quot;db.json&quot;</span><span class="p">)</span>

<span class="c1"># Создание таблицы с именем &quot;users&quot;</span>
<span class="n">users_table</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">table</span><span class="p">(</span><span class="s2">&quot;users&quot;</span><span class="p">)</span>

<span class="c1"># Вставка данных в таблицу &quot;users&quot;</span>
<span class="n">user_id</span> <span class="o">=</span> <span class="n">users_table</span><span class="o">.</span><span class="n">insert</span><span class="p">({</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;John&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">25</span><span class="p">})</span>

<span class="c1"># Получение всех записей из таблицы &quot;users&quot;</span>
<span class="n">all_users</span> <span class="o">=</span> <span class="n">users_table</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>

<span class="c1"># Получение записи по условию (например, по имени)</span>
<span class="n">user_query</span> <span class="o">=</span> <span class="n">Query</span><span class="p">()</span>
<span class="n">john_data</span> <span class="o">=</span> <span class="n">users_table</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">user_query</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="s2">&quot;John&quot;</span><span class="p">)</span>

<span class="c1"># Изменение данных в записи по условию (например, по имени)</span>
<span class="n">users_table</span><span class="o">.</span><span class="n">update</span><span class="p">({</span><span class="s1">&#39;age&#39;</span><span class="p">:</span> <span class="mi">26</span><span class="p">},</span> <span class="n">user_query</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="s1">&#39;John&#39;</span><span class="p">)</span>

<span class="c1"># Удаление записи по условию (например, по имени)</span>
<span class="n">users_table</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">user_query</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="s1">&#39;John&#39;</span><span class="p">)</span>
</pre></div></div></div>