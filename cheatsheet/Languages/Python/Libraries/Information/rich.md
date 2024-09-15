<p>Библиотека <code>Rich</code> — это мощный инструмент для форматирования текста, вывода в терминал с использованием стилей,
цветов, таблиц, прогресс-баров и других элементов пользовательского интерфейса.
Она облегчает создание красивого и информативного вывода в консоли.
Библиотека также поддерживает рендеринг логов и трассировок ошибок.</p>
<h1>Основные возможности</h1>
<ol>
<li><strong>Цветной и стилизованный текст</strong></li>
<li><strong>Отображение таблиц</strong></li>
<li><strong>Прогресс-бары</strong></li>
<li><strong>Логи и трассировки ошибок</strong></li>
<li><strong>Отображение деревьев</strong></li>
<li><strong>Поддержка разметки Markdown</strong></li>
</ol>
<h1>Установка</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>rich
</pre></div></div></div>

<h3>Пример простого форматированного текста</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">rich</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="s2">&quot;[bold magenta]Hello, [italic]Rich[/italic]!&quot;</span><span class="p">)</span>
</pre></div></div></div>
<blockquote>
<p><span style="color:magenta"><span style="font-weight:700">Hello, <span style="font-style:italic">Rich</span>!</span></span></p>
</blockquote>
<h2>Основные функции и примеры</h2>
<h3>Форматирование текста</h3>
<p>В <code>Rich</code> используется синтаксис разметки для стилизации текста. Стили можно комбинировать.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">rich</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="s2">&quot;[bold red]Ошибка:[/] неверный ввод!&quot;</span><span class="p">)</span>
</pre></div></div></div>
<blockquote>
<p><span style="font-weight:700;color:red">Ошибка:</span> неверный ввод!</p>
</blockquote>
<p>Возможные стили: <code>bold</code>, <code>italic</code>, <code>underline</code>, <code>strikethrough</code>,
а также цветовые схемы (<code>red</code>, <code>green</code>, <code>blue</code> и другие).</p>
<h2>Таблицы</h2>
<p>Вы можете создавать и выводить таблицы с помощью класса <code>Table</code>.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">rich.table</span> <span class="kn">import</span> <span class="n">Table</span>
<span class="kn">from</span> <span class="nn">rich.console</span> <span class="kn">import</span> <span class="n">Console</span>


<span class="n">console</span> <span class="o">=</span> <span class="n">Console</span><span class="p">()</span>

<span class="n">table</span> <span class="o">=</span> <span class="n">Table</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;Таблица Пользователей&quot;</span><span class="p">)</span>

<span class="n">table</span><span class="o">.</span><span class="n">add_column</span><span class="p">(</span><span class="s2">&quot;Имя&quot;</span><span class="p">,</span> <span class="n">justify</span><span class="o">=</span><span class="s2">&quot;right&quot;</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="s2">&quot;cyan&quot;</span><span class="p">,</span> <span class="n">no_wrap</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">table</span><span class="o">.</span><span class="n">add_column</span><span class="p">(</span><span class="s2">&quot;Возраст&quot;</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="s2">&quot;magenta&quot;</span><span class="p">)</span>
<span class="n">table</span><span class="o">.</span><span class="n">add_column</span><span class="p">(</span><span class="s2">&quot;Профессия&quot;</span><span class="p">,</span> <span class="n">justify</span><span class="o">=</span><span class="s2">&quot;right&quot;</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="s2">&quot;green&quot;</span><span class="p">)</span>

<span class="n">table</span><span class="o">.</span><span class="n">add_row</span><span class="p">(</span><span class="s2">&quot;Иван&quot;</span><span class="p">,</span> <span class="s2">&quot;32&quot;</span><span class="p">,</span> <span class="s2">&quot;Инженер&quot;</span><span class="p">)</span>
<span class="n">table</span><span class="o">.</span><span class="n">add_row</span><span class="p">(</span><span class="s2">&quot;Анна&quot;</span><span class="p">,</span> <span class="s2">&quot;28&quot;</span><span class="p">,</span> <span class="s2">&quot;Дизайнер&quot;</span><span class="p">)</span>
<span class="n">table</span><span class="o">.</span><span class="n">add_row</span><span class="p">(</span><span class="s2">&quot;Петр&quot;</span><span class="p">,</span> <span class="s2">&quot;40&quot;</span><span class="p">,</span> <span class="s2">&quot;Менеджер&quot;</span><span class="p">)</span>

<span class="n">console</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">table</span><span class="p">)</span>
</pre></div></div></div>
<blockquote>
<p>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-style:italic">Таблица Пользователей</span>
┏━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━┓
┃  Имя ┃ Возраст ┃ Профессия ┃
┡━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━┩
│ <span style="color:cyan">Иван</span> │ <span style="color:magenta">32</span>      │   <span style="color:green">Инженер</span> │
│ <span style="color:cyan">Анна</span> │ <span style="color:magenta">28</span>      │  <span style="color:green">Дизайнер</span> │
│ <span style="color:cyan">Петр</span> │ <span style="color:magenta">40</span>      │  <span style="color:green">Менеджер</span> │
└──────┴─────────┴───────────┘</p>
</blockquote>
<p>Этот код создаст таблицу с тремя столбцами, которая будет выведена в консоль с цветами и выравниванием.</p>
<h3>Прогресс-бары</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">time</span>
<span class="kn">from</span> <span class="nn">rich.progress</span> <span class="kn">import</span> <span class="n">Progress</span>


<span class="k">with</span> <span class="n">Progress</span><span class="p">()</span> <span class="k">as</span> <span class="n">progress</span><span class="p">:</span>
    <span class="n">task</span> <span class="o">=</span> <span class="n">progress</span><span class="o">.</span><span class="n">add_task</span><span class="p">(</span><span class="s2">&quot;Обработка...&quot;</span><span class="p">,</span> <span class="n">total</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
    <span class="k">while</span> <span class="ow">not</span> <span class="n">progress</span><span class="o">.</span><span class="n">finished</span><span class="p">:</span>
        <span class="n">progress</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">task</span><span class="p">,</span> <span class="n">advance</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.1</span><span class="p">)</span>
</pre></div></div></div>

<p>Прогресс-бар будет обновляться в реальном времени, показывая прогресс задачи.</p>
<h3>Логи</h3>
<p><code>Rich</code> интегрируется с модулем <code>logging</code>, позволяя выводить цветные и более информативные логи.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>
<span class="kn">from</span> <span class="nn">rich.logging</span> <span class="kn">import</span> <span class="n">RichHandler</span>


<span class="n">logging</span><span class="o">.</span><span class="n">basicConfig</span><span class="p">(</span><span class="n">level</span><span class="o">=</span><span class="s2">&quot;NOTSET&quot;</span><span class="p">,</span> <span class="n">handlers</span><span class="o">=</span><span class="p">[</span><span class="n">RichHandler</span><span class="p">()])</span>
<span class="n">log</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="s2">&quot;rich&quot;</span><span class="p">)</span>

<span class="n">log</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">&quot;Это информационное сообщение&quot;</span><span class="p">)</span>
<span class="n">log</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">&quot;Это ошибка&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Трассировки ошибок</h3>
<p><code>Rich</code> может красиво отображать трассировки ошибок, улучшая их читаемость.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">rich.console</span> <span class="kn">import</span> <span class="n">Console</span>


<span class="n">console</span> <span class="o">=</span> <span class="n">Console</span><span class="p">()</span>

<span class="k">try</span><span class="p">:</span>
    <span class="mi">1</span> <span class="o">/</span> <span class="mi">0</span>
<span class="k">except</span> <span class="ne">ZeroDivisionError</span><span class="p">:</span>
    <span class="n">console</span><span class="o">.</span><span class="n">print_exception</span><span class="p">()</span>
</pre></div></div></div>

<h3>Деревья</h3>
<p>С помощью <code>Tree</code> можно отображать данные в виде иерархических деревьев.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">rich.tree</span> <span class="kn">import</span> <span class="n">Tree</span>
<span class="kn">from</span> <span class="nn">rich.console</span> <span class="kn">import</span> <span class="n">Console</span>


<span class="n">console</span> <span class="o">=</span> <span class="n">Console</span><span class="p">()</span>

<span class="n">tree</span> <span class="o">=</span> <span class="n">Tree</span><span class="p">(</span><span class="s2">&quot;Файловая система&quot;</span><span class="p">)</span>
<span class="n">tree</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="s2">&quot;Папка 1&quot;</span><span class="p">)</span>
<span class="n">tree</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="s2">&quot;Папка 2&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="s2">&quot;Файл 1&quot;</span><span class="p">)</span>

<span class="n">console</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">tree</span><span class="p">)</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">Файловая система</span>
<span class="sd">├── Папка 1</span>
<span class="sd">└── Папка 2</span>
<span class="sd">    └── Файл 1</span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div></div></div>

<h3>Markdown</h3>
<p><code>Rich</code> поддерживает рендеринг разметки Markdown.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">rich.console</span> <span class="kn">import</span> <span class="n">Console</span>
<span class="kn">from</span> <span class="nn">rich.markdown</span> <span class="kn">import</span> <span class="n">Markdown</span>


<span class="n">console</span> <span class="o">=</span> <span class="n">Console</span><span class="p">()</span>
<span class="n">md</span> <span class="o">=</span> <span class="n">Markdown</span><span class="p">(</span>
<span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
<span class="sd"># Заголовок</span>

<span class="sd">* Пункт 1</span>
<span class="sd">* Пункт 2</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="p">)</span>
<span class="n">console</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">md</span><span class="p">)</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓</span>
<span class="sd">┃                Заголовок                 ┃</span>
<span class="sd">┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛</span>

<span class="sd"> • Пункт 1</span>
<span class="sd"> • Пункт 2</span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div></div></div>

<h1>Дополнительные возможности</h1>
<ul>
<li><strong>Списки</strong>: Создание стилизованных списков.</li>
<li><strong>JSON</strong>: Вывод <code>JSON</code> данных в цвете.</li>
<li><strong>Ограничение по ширине</strong>: Вывод данных с ограничением по ширине консоли.</li>
</ul>