<p>Библиотека "wheel" в Python используется для упрощения установки пакетов и их распространения.
Она представляет собой формат пакета, который содержит предварительно
скомпилированные бинарные файлы, что позволяет ускорить процесс установки.</p>
<h3>Методы модуля "wheel"</h3>
<p><code>convert</code>: используется для преобразования исходных файлов пакета в формат wheel.
<code>install</code>: позволяет установить пакет из wheel-файла.
<code>unpack</code>: распаковывает содержимое wheel-файла.
<code>pack</code>: упаковывает исходные файлы пакета в wheel-файл.</p>
<h3>Подмодули</h3>
<p><code>metadata</code>: содержит методы для работы с метаданными пакета, такими как версия, автор и описание.
<code>tags</code>: предоставляет информацию о поддерживаемых платформах и интерпретаторах.
<code>signatures</code>: позволяет работать с подписями wheel-файлов.
<code>pep425tags</code>: предоставляет методы для работы с тегами PEP 425,
которые описывают совместимость пакетов с определенными версиями Python и операционных систем.</p>
<h3>convert</h3>
<p>Преобразует исходные файлы пакета в формат wheel.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">wheel</span> <span class="kn">import</span> <span class="n">convert</span>

<span class="n">convert</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s2">&quot;path/to/source/package&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>install</h3>
<p>Устанавливает пакет из wheel-файла.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">wheel</span> <span class="kn">import</span> <span class="n">install</span>

<span class="n">install</span><span class="o">.</span><span class="n">install</span><span class="p">(</span><span class="s2">&quot;path/to/wheel/file.whl&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>unpack</h3>
<p>Распаковывает содержимое wheel-файла.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">wheel</span> <span class="kn">import</span> <span class="n">unpack</span>

<span class="n">unpack</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s2">&quot;path/to/wheel/file.whl&quot;</span><span class="p">,</span> <span class="s2">&quot;path/to/destination&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>pack</h3></h3>
<p>Упаковывает исходные файлы пакета в wheel-файл.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">wheel</span> <span class="kn">import</span> <span class="n">pack</span>

<span class="n">pack</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s2">&quot;path/to/source/package&quot;</span><span class="p">,</span> <span class="s2">&quot;path/to/destination/file.whl&quot;</span><span class="p">)</span>
</pre></div></div></div>