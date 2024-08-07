<p>Библиотека "fileinput" используется для обработки текстовых файлов в Python.
Она предоставляет удобные инструменты для чтения и обработки содержимого файлов.</p>
<p>Методы модуля "fileinput" и его подмодулей:</p>
<p>input(): Возвращает итератор, который построчно читает файлы.
filename(): Возвращает текущее имя файла.
lineno(): Возвращает текущий номер строки файла.
filelineno(): Возвращает текущий номер строки относительно текущего файла.
isfirstline(): Проверяет, является ли текущая строка первой в файле.
isstdin(): Проверяет, читается ли текущая строка с stdin.
nextfile(): Переходит к следующему файлу.
close(): Закрывает файлы, открытые с помощью fileinput.</p>
<p>Некоторые из самых часто используемых методов библиотеки "fileinput" вместе с кратким описанием и примером кода:</p>
<p>input(): Возвращает итератор для построчного чтения файлов.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">fileinput</span>

<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">fileinput</span><span class="o">.</span><span class="n">input</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
</pre></div></div>
</div>

<p>filename(): Возвращает текущее имя файла.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">fileinput</span>

<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">fileinput</span><span class="o">.</span><span class="n">input</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Current file: </span><span class="si">{</span><span class="n">fileinput</span><span class="o">.</span><span class="n">filename</span><span class="p">()</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p>lineno(): Возвращает текущий номер строки файла.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">fileinput</span>

<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">fileinput</span><span class="o">.</span><span class="n">input</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Line number: </span><span class="si">{</span><span class="n">fileinput</span><span class="o">.</span><span class="n">lineno</span><span class="p">()</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div>
</div>