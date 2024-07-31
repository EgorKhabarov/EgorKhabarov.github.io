<p>Библиотека "enum" в Python используется для создания и использования перечислений,
которые представляют собой набор именованных значений.
Она облегчает работу с ограниченным набором значений, обеспечивая их типизацию и удобный доступ.</p>
<p>Методы модуля "enum" и его подмодулей:</p>
<p>Модуль "enum":
Enum: Базовый класс для создания перечислений.
auto: Декоратор, который автоматически присваивает значения перечисления.</p>
<p>Подмодуль "Enum":
name: Возвращает имя элемента перечисления.
value: Возвращает значение элемента перечисления.</p>
<p>Подмодуль "IntEnum":
IntEnum: Базовый класс для создания перечислений с целочисленными значениями.</p>
<p>Подмодуль "Flag":
Flag: Базовый класс для создания перечислений с битовыми флагами.
auto: Декоратор, который автоматически присваивает значения флагов.</p>
<p>Некоторые из самых часто используемых методов "enum" и их описание:</p>
<p>Enum.name: Возвращает имя элемента перечисления.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code7c8c534f353d16bd5e3627a439c8ae6db"onclick="copyCode(code7c8c534f353d16bd5e3627a439c8ae6d, code7c8c534f353d16bd5e3627a439c8ae6db)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code7c8c534f353d16bd5e3627a439c8ae6d"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>

<span class="k">class</span> <span class="nc">Color</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">RED</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">GREEN</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="n">BLUE</span> <span class="o">=</span> <span class="mi">3</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="o">.</span><span class="n">RED</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>  <span class="c1"># Выводит &quot;RED&quot;</span>
</pre></div></div></div>

<p>Enum.value: Возвращает значение элемента перечисления.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codedf51f5e2f3a3ffdc465a22fa5f8acb9fb"onclick="copyCode(codedf51f5e2f3a3ffdc465a22fa5f8acb9f, codedf51f5e2f3a3ffdc465a22fa5f8acb9fb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codedf51f5e2f3a3ffdc465a22fa5f8acb9f"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>

<span class="k">class</span> <span class="nc">Color</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">RED</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">GREEN</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="n">BLUE</span> <span class="o">=</span> <span class="mi">3</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="o">.</span><span class="n">RED</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>  <span class="c1"># Выводит 1</span>
</pre></div></div></div>

<p>Flag: Базовый класс для создания перечислений с битовыми флагами.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code7ca16d91379bf96b8bf1f1225db1aefcb"onclick="copyCode(code7ca16d91379bf96b8bf1f1225db1aefc, code7ca16d91379bf96b8bf1f1225db1aefcb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code7ca16d91379bf96b8bf1f1225db1aefc"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Flag</span><span class="p">,</span> <span class="n">auto</span>

<span class="k">class</span> <span class="nc">Permissions</span><span class="p">(</span><span class="n">Flag</span><span class="p">):</span>
    <span class="n">READ</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
    <span class="n">WRITE</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
    <span class="n">EXECUTE</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>

<span class="n">user_permissions</span> <span class="o">=</span> <span class="n">Permissions</span><span class="o">.</span><span class="n">READ</span> <span class="o">|</span> <span class="n">Permissions</span><span class="o">.</span><span class="n">WRITE</span>
<span class="nb">print</span><span class="p">(</span><span class="n">user_permissions</span><span class="p">)</span>  <span class="c1"># Выводит &lt;Permissions.READ|WRITE: 3&gt;</span>
</pre></div></div></div>