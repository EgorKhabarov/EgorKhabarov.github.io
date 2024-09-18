<h3>Шпаргалка по библиотеке Peewee</h3>
<p><strong>Peewee</strong> — это простая и небольшая <strong>ORM</strong> (<strong>Object-Relational Mapping</strong>) библиотека для Python,
которая позволяет взаимодействовать с базами данных через Python-классы и объекты.</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>peewee
</pre></div></div></div>

<h1>Подключение</h1>
<p>Peewee поддерживает разные базы данных: <code>SQLite</code>, <code>MySQL</code>, <code>PostgreSQL</code> и т.д.</p>
<h3>SQLite</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">peewee</span> <span class="kn">import</span> <span class="n">SqliteDatabase</span>

<span class="n">db</span> <span class="o">=</span> <span class="n">SqliteDatabase</span><span class="p">(</span><span class="s2">&quot;my_database.db&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>PostgreSQL</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">peewee</span> <span class="kn">import</span> <span class="n">PostgresqlDatabase</span>

<span class="n">db</span> <span class="o">=</span> <span class="n">PostgresqlDatabase</span><span class="p">(</span><span class="s2">&quot;my_database&quot;</span><span class="p">,</span> <span class="n">user</span><span class="o">=</span><span class="s2">&quot;username&quot;</span><span class="p">,</span> <span class="n">password</span><span class="o">=</span><span class="s2">&quot;password&quot;</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="s2">&quot;localhost&quot;</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="mi">5432</span><span class="p">)</span>
</pre></div></div></div>

<h3>MySQL</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">peewee</span> <span class="kn">import</span> <span class="n">MySQLDatabase</span>

<span class="n">db</span> <span class="o">=</span> <span class="n">MySQLDatabase</span><span class="p">(</span><span class="s2">&quot;my_database&quot;</span><span class="p">,</span> <span class="n">user</span><span class="o">=</span><span class="s2">&quot;username&quot;</span><span class="p">,</span> <span class="n">password</span><span class="o">=</span><span class="s2">&quot;password&quot;</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="s2">&quot;localhost&quot;</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="mi">3306</span><span class="p">)</span>
</pre></div></div></div>

<h1>Определение моделей</h1>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">peewee</span> <span class="kn">import</span> <span class="n">Model</span><span class="p">,</span> <span class="n">CharField</span><span class="p">,</span> <span class="n">IntegerField</span>

<span class="k">class</span> <span class="nc">BaseModel</span><span class="p">(</span><span class="n">Model</span><span class="p">):</span>
    <span class="k">class</span> <span class="nc">Meta</span><span class="p">:</span>
        <span class="n">database</span> <span class="o">=</span> <span class="n">db</span>

<span class="k">class</span> <span class="nc">User</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">username</span> <span class="o">=</span> <span class="n">CharField</span><span class="p">(</span><span class="n">unique</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">age</span> <span class="o">=</span> <span class="n">IntegerField</span><span class="p">()</span>
</pre></div></div></div>

<h1>Создание таблиц</h1>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">db</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span>
<span class="n">db</span><span class="o">.</span><span class="n">create_tables</span><span class="p">([</span><span class="n">User</span><span class="p">])</span>
</pre></div></div></div>

<h1>Добавление записей</h1>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="c1"># Создание записи</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="s2">&quot;john&quot;</span><span class="p">,</span> <span class="n">age</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>

<span class="c1"># Или создание объекта и сохранение через метод save</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">User</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="s2">&quot;doe&quot;</span><span class="p">,</span> <span class="n">age</span><span class="o">=</span><span class="mi">25</span><span class="p">)</span>
<span class="n">user</span><span class="o">.</span><span class="n">save</span><span class="p">()</span>
</pre></div></div></div>

<h1>Поиск записей</h1>
<h3>Получение всех записей</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">users</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">select</span><span class="p">()</span>
<span class="k">for</span> <span class="n">user</span> <span class="ow">in</span> <span class="n">users</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">user</span><span class="o">.</span><span class="n">username</span><span class="p">,</span> <span class="n">user</span><span class="o">.</span><span class="n">age</span><span class="p">)</span>
</pre></div></div></div>

<h3>Фильтрация записей</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">john</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">User</span><span class="o">.</span><span class="n">username</span> <span class="o">==</span> <span class="s2">&quot;john&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Фильтрация с использованием условий</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">adults</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">select</span><span class="p">()</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">User</span><span class="o">.</span><span class="n">age</span> <span class="o">&gt;=</span> <span class="mi">18</span><span class="p">)</span>
</pre></div></div></div>

<h3>Получение первой записи</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">first_user</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">select</span><span class="p">()</span><span class="o">.</span><span class="n">first</span><span class="p">()</span>
</pre></div></div></div>

<h1>Обновление записей</h1>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="c1"># Обновление записи через объект</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">User</span><span class="o">.</span><span class="n">username</span> <span class="o">==</span> <span class="s2">&quot;john&quot;</span><span class="p">)</span>
<span class="n">user</span><span class="o">.</span><span class="n">age</span> <span class="o">=</span> <span class="mi">31</span>
<span class="n">user</span><span class="o">.</span><span class="n">save</span><span class="p">()</span>

<span class="c1"># Обновление записи через метод update</span>
<span class="n">User</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">age</span><span class="o">=</span><span class="mi">32</span><span class="p">)</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">User</span><span class="o">.</span><span class="n">username</span> <span class="o">==</span> <span class="s2">&quot;john&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>
</pre></div></div></div>

<h1>Удаление записей</h1>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="c1"># Удаление записи через объект</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">User</span><span class="o">.</span><span class="n">username</span> <span class="o">==</span> <span class="s2">&quot;john&quot;</span><span class="p">)</span>
<span class="n">user</span><span class="o">.</span><span class="n">delete_instance</span><span class="p">()</span>

<span class="c1"># Удаление записи через метод delete</span>
<span class="n">User</span><span class="o">.</span><span class="n">delete</span><span class="p">()</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">User</span><span class="o">.</span><span class="n">username</span> <span class="o">==</span> <span class="s2">&quot;john&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>
</pre></div></div></div>

<h1>Связи между моделями</h1>
<h3>Один ко многим (ForeignKeyField)</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">peewee</span> <span class="kn">import</span> <span class="n">ForeignKeyField</span>

<span class="k">class</span> <span class="nc">Blog</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">title</span> <span class="o">=</span> <span class="n">CharField</span><span class="p">()</span>
    <span class="n">content</span> <span class="o">=</span> <span class="n">CharField</span><span class="p">()</span>
    <span class="n">author</span> <span class="o">=</span> <span class="n">ForeignKeyField</span><span class="p">(</span><span class="n">User</span><span class="p">,</span> <span class="n">backref</span><span class="o">=</span><span class="s2">&quot;blogs&quot;</span><span class="p">)</span>

<span class="c1"># Пример создания блога, связанного с пользователем</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">User</span><span class="o">.</span><span class="n">username</span> <span class="o">==</span> <span class="s2">&quot;doe&quot;</span><span class="p">)</span>
<span class="n">blog</span> <span class="o">=</span> <span class="n">Blog</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;My First Blog&quot;</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">,</span> <span class="n">author</span><span class="o">=</span><span class="n">user</span><span class="p">)</span>
</pre></div></div></div>

<h3>Многие ко многим</h3>
<p>Для реализации отношений «многие ко многим» создается промежуточная таблица:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Tag</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">name</span> <span class="o">=</span> <span class="n">CharField</span><span class="p">(</span><span class="n">unique</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">BlogTag</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">blog</span> <span class="o">=</span> <span class="n">ForeignKeyField</span><span class="p">(</span><span class="n">Blog</span><span class="p">)</span>
    <span class="n">tag</span> <span class="o">=</span> <span class="n">ForeignKeyField</span><span class="p">(</span><span class="n">Tag</span><span class="p">)</span>
</pre></div></div></div>

<h1>Построение запросов</h1>
<h3>Сортировка</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="c1"># Сортировка по возрасту</span>
<span class="n">users</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">select</span><span class="p">()</span><span class="o">.</span><span class="n">order_by</span><span class="p">(</span><span class="n">User</span><span class="o">.</span><span class="n">age</span><span class="o">.</span><span class="n">desc</span><span class="p">())</span>
</pre></div></div></div>

<h3>Лимит и смещение</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="c1"># Ограничение количества записей</span>
<span class="n">limited_users</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">select</span><span class="p">()</span><span class="o">.</span><span class="n">limit</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
</pre></div></div></div>

<h3>Группировка</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="c1"># Группировка и подсчет количества</span>
<span class="kn">from</span> <span class="nn">peewee</span> <span class="kn">import</span> <span class="n">fn</span>

<span class="n">user_counts</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="n">fn</span><span class="o">.</span><span class="n">COUNT</span><span class="p">(</span><span class="n">User</span><span class="o">.</span><span class="n">id</span><span class="p">))</span><span class="o">.</span><span class="n">group_by</span><span class="p">(</span><span class="n">User</span><span class="o">.</span><span class="n">age</span><span class="p">)</span>
</pre></div></div></div>

<h1>Транзакции</h1>
<p>Транзакции в Peewee позволяют выполнять несколько запросов к базе данных как одну атомарную операцию.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">with</span> <span class="n">db</span><span class="o">.</span><span class="n">atomic</span><span class="p">():</span>
    <span class="n">User</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="s2">&quot;alice&quot;</span><span class="p">,</span> <span class="n">age</span><span class="o">=</span><span class="mi">23</span><span class="p">)</span>
    <span class="n">User</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="s2">&quot;bob&quot;</span><span class="p">,</span> <span class="n">age</span><span class="o">=</span><span class="mi">35</span><span class="p">)</span>
</pre></div></div></div>

<h3>Пример построения структуры базы данных</h3>
<p>Допустим, мы создаем блог-платформу, где пользователи могут публиковать посты, комментировать и добавлять теги.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">datetime</span>
<span class="kn">from</span> <span class="nn">peewee</span> <span class="kn">import</span> <span class="n">Model</span><span class="p">,</span> <span class="n">CharField</span><span class="p">,</span> <span class="n">TextField</span><span class="p">,</span> <span class="n">ForeignKeyField</span><span class="p">,</span> <span class="n">DateTimeField</span><span class="p">,</span> <span class="n">SqliteDatabase</span>

<span class="n">db</span> <span class="o">=</span> <span class="n">SqliteDatabase</span><span class="p">(</span><span class="s2">&quot;blog.db&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">BaseModel</span><span class="p">(</span><span class="n">Model</span><span class="p">):</span>
    <span class="k">class</span> <span class="nc">Meta</span><span class="p">:</span>
        <span class="n">database</span> <span class="o">=</span> <span class="n">db</span>

<span class="k">class</span> <span class="nc">User</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">username</span> <span class="o">=</span> <span class="n">CharField</span><span class="p">(</span><span class="n">unique</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">password</span> <span class="o">=</span> <span class="n">CharField</span><span class="p">()</span>

<span class="k">class</span> <span class="nc">Blog</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">title</span> <span class="o">=</span> <span class="n">CharField</span><span class="p">()</span>
    <span class="n">content</span> <span class="o">=</span> <span class="n">TextField</span><span class="p">()</span>
    <span class="n">pub_date</span> <span class="o">=</span> <span class="n">DateTimeField</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">)</span>
    <span class="n">author</span> <span class="o">=</span> <span class="n">ForeignKeyField</span><span class="p">(</span><span class="n">User</span><span class="p">,</span> <span class="n">backref</span><span class="o">=</span><span class="s2">&quot;blogs&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Comment</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">blog</span> <span class="o">=</span> <span class="n">ForeignKeyField</span><span class="p">(</span><span class="n">Blog</span><span class="p">,</span> <span class="n">backref</span><span class="o">=</span><span class="s2">&quot;comments&quot;</span><span class="p">)</span>
    <span class="n">user</span> <span class="o">=</span> <span class="n">ForeignKeyField</span><span class="p">(</span><span class="n">User</span><span class="p">,</span> <span class="n">backref</span><span class="o">=</span><span class="s2">&quot;comments&quot;</span><span class="p">)</span>
    <span class="n">content</span> <span class="o">=</span> <span class="n">TextField</span><span class="p">()</span>
    <span class="n">pub_date</span> <span class="o">=</span> <span class="n">DateTimeField</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Tag</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">name</span> <span class="o">=</span> <span class="n">CharField</span><span class="p">(</span><span class="n">unique</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">BlogTag</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">blog</span> <span class="o">=</span> <span class="n">ForeignKeyField</span><span class="p">(</span><span class="n">Blog</span><span class="p">,</span> <span class="n">backref</span><span class="o">=</span><span class="s2">&quot;tags&quot;</span><span class="p">)</span>
    <span class="n">tag</span> <span class="o">=</span> <span class="n">ForeignKeyField</span><span class="p">(</span><span class="n">Tag</span><span class="p">,</span> <span class="n">backref</span><span class="o">=</span><span class="s2">&quot;blogs&quot;</span><span class="p">)</span>

<span class="c1"># Создание таблиц</span>
<span class="n">db</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span>
<span class="n">db</span><span class="o">.</span><span class="n">create_tables</span><span class="p">([</span><span class="n">User</span><span class="p">,</span> <span class="n">Blog</span><span class="p">,</span> <span class="n">Comment</span><span class="p">,</span> <span class="n">Tag</span><span class="p">,</span> <span class="n">BlogTag</span><span class="p">])</span>

<span class="c1"># Пример создания записи</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="s2">&quot;john_doe&quot;</span><span class="p">,</span> <span class="n">password</span><span class="o">=</span><span class="s2">&quot;password123&quot;</span><span class="p">)</span>
<span class="n">blog</span> <span class="o">=</span> <span class="n">Blog</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;My Blog Post&quot;</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="s2">&quot;This is my first post&quot;</span><span class="p">,</span> <span class="n">author</span><span class="o">=</span><span class="n">user</span><span class="p">)</span>
<span class="n">comment</span> <span class="o">=</span> <span class="n">Comment</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">blog</span><span class="o">=</span><span class="n">blog</span><span class="p">,</span> <span class="n">user</span><span class="o">=</span><span class="n">user</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="s2">&quot;Nice post!&quot;</span><span class="p">)</span>
<span class="n">tag</span> <span class="o">=</span> <span class="n">Tag</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Python&quot;</span><span class="p">)</span>
<span class="n">BlogTag</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">blog</span><span class="o">=</span><span class="n">blog</span><span class="p">,</span> <span class="n">tag</span><span class="o">=</span><span class="n">tag</span><span class="p">)</span>
</pre></div></div></div>

<h1>Пагинация</h1>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">paginate</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">page</span><span class="p">,</span> <span class="n">page_size</span><span class="o">=</span><span class="mi">10</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">query</span><span class="o">.</span><span class="n">paginate</span><span class="p">(</span><span class="n">page</span><span class="p">,</span> <span class="n">page_size</span><span class="p">)</span>

<span class="c1"># Получение первой страницы с 10 записями</span>
<span class="n">first_page</span> <span class="o">=</span> <span class="n">paginate</span><span class="p">(</span><span class="n">User</span><span class="o">.</span><span class="n">select</span><span class="p">(),</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">10</span><span class="p">)</span>
</pre></div></div></div>

<h1>Миграции</h1>
<p>Для изменения структуры базы данных рекомендуется использовать миграции.
В Peewee для этого есть библиотека <code>playhouse.migrate</code></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">playhouse.migrate</span> <span class="kn">import</span> <span class="o">*</span>

<span class="n">migrator</span> <span class="o">=</span> <span class="n">SqliteMigrator</span><span class="p">(</span><span class="n">db</span><span class="p">)</span>

<span class="c1"># Добавление нового поля в таблицу User</span>
<span class="n">migrate</span><span class="p">(</span><span class="n">migrator</span><span class="o">.</span><span class="n">add_column</span><span class="p">(</span><span class="s2">&quot;user&quot;</span><span class="p">,</span> <span class="s2">&quot;email&quot;</span><span class="p">,</span> <span class="n">CharField</span><span class="p">(</span><span class="n">null</span><span class="o">=</span><span class="kc">True</span><span class="p">)))</span>
</pre></div></div></div>