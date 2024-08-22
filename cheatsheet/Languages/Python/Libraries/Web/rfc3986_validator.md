<p>Название библиотеки: "rfc3986_validator"</p>
<p>Описание: Библиотека "rfc3986_validator" используется для проверки и валидации URL-адресов согласно стандарту RFC 3986.
Она обеспечивает функционал для проверки правильности формата URL и его различных компонентов, таких как схема, хост, путь и другие.</p>
<p>Методы модуля и их описание:</p>
<p>Модуль: rfc3986_validator
validate(url: str) -&gt; bool: Проверяет, соответствует ли заданный URL формату RFC 3986. Возвращает True, если URL действительный, и False в противном случае.
get_scheme(url: str) -&gt; str: Извлекает и возвращает схему (протокол) из заданного URL.
get_host(url: str) -&gt; str: Извлекает и возвращает хост (доменное имя) из заданного URL.
get_path(url: str) -&gt; str: Извлекает и возвращает путь из заданного URL.
get_query(url: str) -&gt; str: Извлекает и возвращает параметры запроса из заданного URL.
get_fragment(url: str) -&gt; str: Извлекает и возвращает фрагмент из заданного URL.</p>
<p>Список самых часто используемых методов, их описание и</p>
<p>validate(url: str) -&gt; bool:
Описание: Проверяет, является ли заданный URL действительным согласно стандарту RFC 3986.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">rfc3986_validator</span> <span class="kn">import</span> <span class="n">validate</span>

<span class="n">url</span> <span class="o">=</span> <span class="s2">&quot;https://www.example.com&quot;</span>
<span class="n">is_valid</span> <span class="o">=</span> <span class="n">validate</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">is_valid</span><span class="p">)</span>  <span class="c1"># Выводит True, если URL действителен</span>
</pre></div></div></div>

<p>get_host(url: str) -&gt; str:
Описание: Извлекает и возвращает хост (доменное имя) из заданного URL.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">rfc3986_validator</span> <span class="kn">import</span> <span class="n">get_host</span>

<span class="n">url</span> <span class="o">=</span> <span class="s2">&quot;https://www.example.com/path&quot;</span>
<span class="n">host</span> <span class="o">=</span> <span class="n">get_host</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">host</span><span class="p">)</span>  <span class="c1"># Выводит &quot;www.example.com&quot;</span>
</pre></div></div></div>

<p>get_path(url: str) -&gt; str:
Описание: Извлекает и возвращает путь из заданного URL.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">rfc3986_validator</span> <span class="kn">import</span> <span class="n">get_path</span>

<span class="n">url</span> <span class="o">=</span> <span class="s2">&quot;https://www.example.com/path&quot;</span>
<span class="n">path</span> <span class="o">=</span> <span class="n">get_path</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>  <span class="c1"># Выводит &quot;/path&quot;</span>
</pre></div></div></div>