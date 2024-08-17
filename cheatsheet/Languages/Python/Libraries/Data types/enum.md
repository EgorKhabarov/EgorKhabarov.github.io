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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>

<span class="k">class</span> <span class="nc">Color</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">RED</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">GREEN</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="n">BLUE</span> <span class="o">=</span> <span class="mi">3</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="o">.</span><span class="n">RED</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>  <span class="c1"># Выводит &quot;RED&quot;</span>
</pre></div></div></div>

<p>Enum.value: Возвращает значение элемента перечисления.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>

<span class="k">class</span> <span class="nc">Color</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">RED</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">GREEN</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="n">BLUE</span> <span class="o">=</span> <span class="mi">3</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="o">.</span><span class="n">RED</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>  <span class="c1"># Выводит 1</span>
</pre></div></div></div>

<p>Flag: Базовый класс для создания перечислений с битовыми флагами.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Flag</span><span class="p">,</span> <span class="n">auto</span>

<span class="k">class</span> <span class="nc">Permissions</span><span class="p">(</span><span class="n">Flag</span><span class="p">):</span>
    <span class="n">READ</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
    <span class="n">WRITE</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
    <span class="n">EXECUTE</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>

<span class="n">user_permissions</span> <span class="o">=</span> <span class="n">Permissions</span><span class="o">.</span><span class="n">READ</span> <span class="o">|</span> <span class="n">Permissions</span><span class="o">.</span><span class="n">WRITE</span>
<span class="nb">print</span><span class="p">(</span><span class="n">user_permissions</span><span class="p">)</span>  <span class="c1"># Выводит &lt;Permissions.READ|WRITE: 3&gt;</span>
</pre></div></div></div>