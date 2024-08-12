<p>Библиотека "xml" в Python используется для работы с XML-данными.
Она предоставляет функциональность для чтения, записи, и обработки XML-файлов.</p>
<p>Методы модуля "xml" и его подмодулей:
xml.etree.ElementTree: Позволяет работать с XML-деревом, включая чтение, запись, и обработку XML-элементов.
xml.dom: Предоставляет интерфейсы для работы с DOM (Document Object Model) XML-документов.
xml.sax: Предоставляет SAX (Simple API for XML) интерфейс для обработки XML-документов в потоковом режиме.</p>
<p>Самые часто используемые методы:
xml.etree.ElementTree.parse(file): Читает XML-файл и возвращает корневой элемент дерева.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">xml.etree.ElementTree</span> <span class="k">as</span> <span class="nn">ET</span>

<span class="n">tree</span> <span class="o">=</span> <span class="n">ET</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="s2">&quot;file.xml&quot;</span><span class="p">)</span>
<span class="n">root</span> <span class="o">=</span> <span class="n">tree</span><span class="o">.</span><span class="n">getroot</span><span class="p">()</span>
</pre></div></div>
</div>

<p>xml.etree.ElementTree.Element.findall(tag): Возвращает список элементов с указанным тегом.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">xml.etree.ElementTree</span> <span class="k">as</span> <span class="nn">ET</span>

<span class="n">tree</span> <span class="o">=</span> <span class="n">ET</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="s2">&quot;file.xml&quot;</span><span class="p">)</span>
<span class="n">root</span> <span class="o">=</span> <span class="n">tree</span><span class="o">.</span><span class="n">getroot</span><span class="p">()</span>

<span class="n">elements</span> <span class="o">=</span> <span class="n">root</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="s2">&quot;tag&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p>xml.etree.ElementTree.Element.attrib: Возвращает атрибуты элемента в виде словаря.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">xml.etree.ElementTree</span> <span class="k">as</span> <span class="nn">ET</span>

<span class="n">tree</span> <span class="o">=</span> <span class="n">ET</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="s2">&quot;file.xml&quot;</span><span class="p">)</span>
<span class="n">root</span> <span class="o">=</span> <span class="n">tree</span><span class="o">.</span><span class="n">getroot</span><span class="p">()</span>

<span class="k">for</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">root</span><span class="p">:</span>
    <span class="n">attributes</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">attrib</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">attributes</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Помните, что без доступа к конкретному XML-файлу, точные примеры кода могут быть недоступны.</p>