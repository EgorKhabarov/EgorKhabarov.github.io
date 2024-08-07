<p>Библиотека "pymsgbox" используется для создания простых диалоговых окон с сообщениями, предупреждениями и запросами пользователю в Python.</p>
<p>Таблица методов модуля "pymsgbox" и их краткое описание:
<code>alert</code>: Отображает диалоговое окно с сообщением для пользователя.
<code>confirm</code>: Отображает диалоговое окно с вопросом для пользователя с двумя вариантами ответа (Да/Нет).
<code>prompt</code>: Отображает диалоговое окно с запросом пользователю на ввод текста.
<code>password</code>: Отображает диалоговое окно с запросом пользователю на ввод пароля (текста, скрытого звездочками).
<code>textbox</code>: Отображает диалоговое окно с возможностью ввода и редактирования текста пользователем.</p>
<p>Список самых частых методов "pymsgbox", их краткое описание и примерный код для демонстрации:</p>
<p><code>alert(message, title=""):</code>
Описание: Отображает диалоговое окно с сообщением для пользователя.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pymsgbox</span>

<span class="n">pymsgbox</span><span class="o">.</span><span class="n">alert</span><span class="p">(</span><span class="s2">&quot;Привет, пользователь!&quot;</span><span class="p">,</span> <span class="s2">&quot;Информация&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p><code>confirm(text, title="", buttons=["Да", "Нет"]):</code>
Описание: Отображает диалоговое окно с вопросом для пользователя с двумя вариантами ответа.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pymsgbox</span>

<span class="n">response</span> <span class="o">=</span> <span class="n">pymsgbox</span><span class="o">.</span><span class="n">confirm</span><span class="p">(</span><span class="s2">&quot;Вы уверены, что хотите продолжить?&quot;</span><span class="p">,</span> <span class="s2">&quot;Подтверждение&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">response</span> <span class="o">==</span> <span class="s2">&quot;Да&quot;</span><span class="p">:</span>
    <span class="c1"># Действия при выборе &quot;Да&quot;</span>
    <span class="k">pass</span>
<span class="k">else</span><span class="p">:</span>
    <span class="c1"># Действия при выборе &quot;Нет&quot;</span>
    <span class="k">pass</span>
</pre></div></div>
</div>

<p><code>prompt(text, title="", default=""):</code>
Описание: Отображает диалоговое окно с запросом пользователю на ввод текста.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pymsgbox</span>

<span class="n">username</span> <span class="o">=</span> <span class="n">pymsgbox</span><span class="o">.</span><span class="n">prompt</span><span class="p">(</span><span class="s2">&quot;Введите ваше имя:&quot;</span><span class="p">,</span> <span class="s2">&quot;Ввод данных&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p><code>password(text, title=""):</code>
Описание: Отображает диалоговое окно с запросом пользователю на ввод пароля (скрытого звездочками).</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pymsgbox</span>

<span class="n">password</span> <span class="o">=</span> <span class="n">pymsgbox</span><span class="o">.</span><span class="n">password</span><span class="p">(</span><span class="s2">&quot;Введите пароль:&quot;</span><span class="p">,</span> <span class="s2">&quot;Подтверждение&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p><code>textbox(text="", title="", default="", multiline=False):</code>
Описание: Отображает диалоговое окно с возможностью ввода и редактирования текста пользователем.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pymsgbox</span>

<span class="n">text</span> <span class="o">=</span> <span class="n">pymsgbox</span><span class="o">.</span><span class="n">textbox</span><span class="p">(</span><span class="s2">&quot;Введите текст:&quot;</span><span class="p">,</span> <span class="s2">&quot;Редактирование текста&quot;</span><span class="p">)</span>
</pre></div></div>
</div>