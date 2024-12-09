<h1>Pony ORM</h1>
<p><strong>Pony ORM</strong> — это объектно-реляционная модель (ORM) для Python,
которая позволяет работать с базами данных, используя генераторы выражений Python вместо SQL-запросов.
Pony ORM поддерживает такие базы данных, как <code>SQLite</code>, <code>MySQL</code>, <code>PostgreSQL</code>, <code>Oracle</code>.</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>pony
</pre></div></div></div>

<h1>Создание структуры</h1>
<p>Для работы с Pony ORM, необходимо создать объекты классов, которые будут связаны с таблицами базы данных.
Используется класс <code>Database</code> для управления подключениями и класс <code>Entity</code> для создания моделей.</p>
<h1>Пример создания</h1>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pony.orm</span> <span class="kn">import</span> <span class="n">Database</span><span class="p">,</span> <span class="n">Required</span><span class="p">,</span> <span class="n">Set</span>

<span class="n">db</span> <span class="o">=</span> <span class="n">Database</span><span class="p">()</span>

<span class="k">class</span> <span class="nc">Author</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">Entity</span><span class="p">):</span>
    <span class="n">name</span> <span class="o">=</span> <span class="n">Required</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
    <span class="n">books</span> <span class="o">=</span> <span class="n">Set</span><span class="p">(</span><span class="s2">&quot;Book&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Book</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">Entity</span><span class="p">):</span>
    <span class="n">title</span> <span class="o">=</span> <span class="n">Required</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
    <span class="n">author</span> <span class="o">=</span> <span class="n">Required</span><span class="p">(</span><span class="n">Author</span><span class="p">)</span>

<span class="n">db</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s2">&quot;sqlite&quot;</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="s2">&quot;:memory:&quot;</span><span class="p">)</span>
<span class="n">db</span><span class="o">.</span><span class="n">generate_mapping</span><span class="p">(</span><span class="n">create_tables</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div></div></div>

<h1>Взаимодействие с базой данных</h1>
<p>После создания структуры базы данных, можно добавлять, изменять, удалять и извлекать данные,
используя методы Pony ORM и генераторы выражений.</p>
<h3>Добавление данных</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pony.orm</span> <span class="kn">import</span> <span class="n">db_session</span>

<span class="k">with</span> <span class="n">db_session</span><span class="p">:</span>
    <span class="n">author</span> <span class="o">=</span> <span class="n">Author</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;J.K. Rowling&quot;</span><span class="p">)</span>
    <span class="n">book</span> <span class="o">=</span> <span class="n">Book</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;Harry Potter and the Philosopher&#39;s Stone&quot;</span><span class="p">,</span> <span class="n">author</span><span class="o">=</span><span class="n">author</span><span class="p">)</span>
</pre></div></div></div>

<h3>Извлечение данных</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">with</span> <span class="n">db_session</span><span class="p">:</span>
    <span class="n">books</span> <span class="o">=</span> <span class="n">Book</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="k">lambda</span> <span class="n">b</span><span class="p">:</span> <span class="n">b</span><span class="o">.</span><span class="n">author</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="s2">&quot;J.K. Rowling&quot;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">book</span> <span class="ow">in</span> <span class="n">books</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">book</span><span class="o">.</span><span class="n">title</span><span class="p">)</span>
</pre></div></div></div>

<h3>Обновление данных</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">with</span> <span class="n">db_session</span><span class="p">:</span>
    <span class="n">book</span> <span class="o">=</span> <span class="n">Book</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;Harry Potter and the Philosopher&#39;s Stone&quot;</span><span class="p">)</span>
    <span class="n">book</span><span class="o">.</span><span class="n">title</span> <span class="o">=</span> <span class="s2">&quot;Harry Potter and the Sorcerer&#39;s Stone&quot;</span>
</pre></div></div></div>

<h3>Удаление данных</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">with</span> <span class="n">db_session</span><span class="p">:</span>
    <span class="n">book</span> <span class="o">=</span> <span class="n">Book</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;Harry Potter and the Sorcerer&#39;s Stone&quot;</span><span class="p">)</span>
    <span class="n">book</span><span class="o">.</span><span class="n">delete</span><span class="p">()</span>
</pre></div></div></div>

<h3>Генераторы выражений (Query Expressions)</h3>
<p>Pony ORM позволяет использовать Python выражения для фильтрации, сортировки и выборки данных.
Это делает код более читабельным и легким в написании.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">with</span> <span class="n">db_session</span><span class="p">:</span>
    <span class="n">books</span> <span class="o">=</span> <span class="n">select</span><span class="p">(</span><span class="n">b</span> <span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="n">Book</span> <span class="k">if</span> <span class="s2">&quot;Harry Potter&quot;</span> <span class="ow">in</span> <span class="n">b</span><span class="o">.</span><span class="n">title</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">book</span> <span class="ow">in</span> <span class="n">books</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">book</span><span class="o">.</span><span class="n">title</span><span class="p">)</span>
</pre></div></div></div>

<h1>Отношения между сущностями</h1>
<p>Pony ORM поддерживает различные типы отношений между сущностями</p>
<h3><strong>Один-ко-многим (One-to-Many)</strong>:</h3>
<p>Пример был показан выше, где один автор может написать несколько книг (отношение <code>Author -&gt; Book</code>).</p>
<h3><strong>Многие-ко-многим (Many-to-Many)</strong>:</h3>
<p>Пример создания связи между студентами и курсами, которые они могут посещать.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Student</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">Entity</span><span class="p">):</span>
    <span class="n">name</span> <span class="o">=</span> <span class="n">Required</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
    <span class="n">courses</span> <span class="o">=</span> <span class="n">Set</span><span class="p">(</span><span class="s2">&quot;Course&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Course</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">Entity</span><span class="p">):</span>
    <span class="n">name</span> <span class="o">=</span> <span class="n">Required</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
    <span class="n">students</span> <span class="o">=</span> <span class="n">Set</span><span class="p">(</span><span class="n">Student</span><span class="p">)</span>
</pre></div></div></div>

<h3><strong>Один-к-одному (One-to-One)</strong></h3>
<p>Связь между студентом и его личным профилем.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Profile</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">Entity</span><span class="p">):</span>
    <span class="n">student</span> <span class="o">=</span> <span class="n">Required</span><span class="p">(</span><span class="s2">&quot;Student&quot;</span><span class="p">)</span>
    <span class="n">bio</span> <span class="o">=</span> <span class="n">Required</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Student</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">Entity</span><span class="p">):</span>
    <span class="n">name</span> <span class="o">=</span> <span class="n">Required</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
    <span class="n">profile</span> <span class="o">=</span> <span class="n">Required</span><span class="p">(</span><span class="n">Profile</span><span class="p">)</span>
</pre></div></div></div>

<h1>Транзакции</h1>
<p>Pony ORM автоматически управляет транзакциями через контекстный менеджер <code>db_session</code>.
Все операции, выполняемые в рамках <code>db_session</code>, происходят в одной транзакции.
Pony ORM автоматически коммитит или откатывает транзакцию в зависимости от результата выполнения.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pony.orm</span> <span class="kn">import</span> <span class="n">db_session</span>

<span class="k">with</span> <span class="n">db_session</span><span class="p">:</span>
    <span class="n">author</span> <span class="o">=</span> <span class="n">Author</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;George Orwell&quot;</span><span class="p">)</span>
    <span class="n">book</span> <span class="o">=</span> <span class="n">Book</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;1984&quot;</span><span class="p">,</span> <span class="n">author</span><span class="o">=</span><span class="n">author</span><span class="p">)</span>
</pre></div></div></div>

<h1>Кэширование</h1>
<p>Pony ORM кэширует объекты в рамках одной сессии <code>db_session</code>.
Это значит, что повторные запросы за одним и тем же объектом
в рамках одной сессии не будут обращаться к базе данных.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">with</span> <span class="n">db_session</span><span class="p">:</span>
    <span class="n">author1</span> <span class="o">=</span> <span class="n">Author</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;George Orwell&quot;</span><span class="p">)</span>
    <span class="n">author2</span> <span class="o">=</span> <span class="n">Author</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;George Orwell&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">author1</span> <span class="ow">is</span> <span class="n">author2</span><span class="p">)</span>  <span class="c1"># True</span>
</pre></div></div></div>

<h3>Пример полной работы с базой данных</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pony.orm</span> <span class="kn">import</span> <span class="n">Database</span><span class="p">,</span> <span class="n">Required</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">db_session</span><span class="p">,</span> <span class="n">select</span>

<span class="n">db</span> <span class="o">=</span> <span class="n">Database</span><span class="p">()</span>

<span class="k">class</span> <span class="nc">Author</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">Entity</span><span class="p">):</span>
    <span class="n">name</span> <span class="o">=</span> <span class="n">Required</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
    <span class="n">books</span> <span class="o">=</span> <span class="n">Set</span><span class="p">(</span><span class="s2">&quot;Book&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Book</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">Entity</span><span class="p">):</span>
    <span class="n">title</span> <span class="o">=</span> <span class="n">Required</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
    <span class="n">author</span> <span class="o">=</span> <span class="n">Required</span><span class="p">(</span><span class="n">Author</span><span class="p">)</span>

<span class="c1"># Привязка базы данных к SQLite</span>
<span class="n">db</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s2">&quot;sqlite&quot;</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="s2">&quot;library.sqlite&quot;</span><span class="p">,</span> <span class="n">create_db</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">db</span><span class="o">.</span><span class="n">generate_mapping</span><span class="p">(</span><span class="n">create_tables</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="c1"># Добавление данных</span>
<span class="k">with</span> <span class="n">db_session</span><span class="p">:</span>
    <span class="n">author</span> <span class="o">=</span> <span class="n">Author</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;George Orwell&quot;</span><span class="p">)</span>
    <span class="n">book1</span> <span class="o">=</span> <span class="n">Book</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;1984&quot;</span><span class="p">,</span> <span class="n">author</span><span class="o">=</span><span class="n">author</span><span class="p">)</span>
    <span class="n">book2</span> <span class="o">=</span> <span class="n">Book</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;Animal Farm&quot;</span><span class="p">,</span> <span class="n">author</span><span class="o">=</span><span class="n">author</span><span class="p">)</span>

<span class="c1"># Извлечение данных</span>
<span class="k">with</span> <span class="n">db_session</span><span class="p">:</span>
    <span class="n">books</span> <span class="o">=</span> <span class="n">select</span><span class="p">(</span><span class="n">b</span> <span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="n">Book</span> <span class="k">if</span> <span class="n">b</span><span class="o">.</span><span class="n">author</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="s2">&quot;George Orwell&quot;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">book</span> <span class="ow">in</span> <span class="n">books</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">book</span><span class="o">.</span><span class="n">title</span><span class="si">}</span><span class="s2"> by </span><span class="si">{</span><span class="n">book</span><span class="o">.</span><span class="n">author</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="c1"># Обновление данных</span>
<span class="k">with</span> <span class="n">db_session</span><span class="p">:</span>
    <span class="n">book</span> <span class="o">=</span> <span class="n">Book</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;1984&quot;</span><span class="p">)</span>
    <span class="n">book</span><span class="o">.</span><span class="n">title</span> <span class="o">=</span> <span class="s2">&quot;Nineteen Eighty-Four&quot;</span>

<span class="c1"># Удаление данных</span>
<span class="k">with</span> <span class="n">db_session</span><span class="p">:</span>
    <span class="n">book</span> <span class="o">=</span> <span class="n">Book</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;Animal Farm&quot;</span><span class="p">)</span>
    <span class="n">book</span><span class="o">.</span><span class="n">delete</span><span class="p">()</span>
</pre></div></div></div>

<h1>Особенности работы с Pony ORM</h1>
<ul>
<li><strong>Ленивая загрузка</strong>: Pony ORM автоматически загружает связанные данные только тогда, когда они необходимы.</li>
<li><strong>Оптимизация запросов</strong>: Генераторы выражений оптимизируются в SQL-запросы, что обеспечивает производительность.</li>
<li><strong>Поддержка сложных запросов</strong>: Можно выполнять сложные SQL-запросы с использованием привычных Python-выражений.</li>
</ul>