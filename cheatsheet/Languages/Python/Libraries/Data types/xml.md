<p>Библиотека "xml" в Python используется для работы с XML-данными.
Она предоставляет функциональность для чтения, записи, и обработки XML-файлов.</p>
<p>Методы модуля "xml" и его подмодулей:
xml.etree.ElementTree: Позволяет работать с XML-деревом, включая чтение, запись, и обработку XML-элементов.
xml.dom: Предоставляет интерфейсы для работы с DOM (Document Object Model) XML-документов.
xml.sax: Предоставляет SAX (Simple API for XML) интерфейс для обработки XML-документов в потоковом режиме.</p>
<p>Самые часто используемые методы:
xml.etree.ElementTree.parse(file): Читает XML-файл и возвращает корневой элемент дерева.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">xml.etree.ElementTree</span> <span class="k">as</span> <span class="nn">ET</span>

<span class="n">tree</span> <span class="o">=</span> <span class="n">ET</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="s2">&quot;file.xml&quot;</span><span class="p">)</span>
<span class="n">root</span> <span class="o">=</span> <span class="n">tree</span><span class="o">.</span><span class="n">getroot</span><span class="p">()</span>
</pre></div></div></div>

<p>xml.etree.ElementTree.Element.findall(tag): Возвращает список элементов с указанным тегом.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">xml.etree.ElementTree</span> <span class="k">as</span> <span class="nn">ET</span>

<span class="n">tree</span> <span class="o">=</span> <span class="n">ET</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="s2">&quot;file.xml&quot;</span><span class="p">)</span>
<span class="n">root</span> <span class="o">=</span> <span class="n">tree</span><span class="o">.</span><span class="n">getroot</span><span class="p">()</span>

<span class="n">elements</span> <span class="o">=</span> <span class="n">root</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="s2">&quot;tag&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>xml.etree.ElementTree.Element.attrib: Возвращает атрибуты элемента в виде словаря.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">xml.etree.ElementTree</span> <span class="k">as</span> <span class="nn">ET</span>

<span class="n">tree</span> <span class="o">=</span> <span class="n">ET</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="s2">&quot;file.xml&quot;</span><span class="p">)</span>
<span class="n">root</span> <span class="o">=</span> <span class="n">tree</span><span class="o">.</span><span class="n">getroot</span><span class="p">()</span>

<span class="k">for</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">root</span><span class="p">:</span>
    <span class="n">attributes</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">attrib</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">attributes</span><span class="p">)</span>
</pre></div></div></div>

<p>Помните, что без доступа к конкретному XML-файлу, точные примеры кода могут быть недоступны.</p>