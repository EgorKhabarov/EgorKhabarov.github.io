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
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codeb7381b53bf9556bbe4c7e4c8197ab80eb"
          onclick="copyCode(codeb7381b53bf9556bbe4c7e4c8197ab80e, codeb7381b53bf9556bbe4c7e4c8197ab80eb)">
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
<div class="code" id="codeb7381b53bf9556bbe4c7e4c8197ab80e"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">rfc3986_validator</span> <span class="kn">import</span> <span class="n">validate</span>

<span class="n">url</span> <span class="o">=</span> <span class="s2">&quot;&lt;a href=&#39;https://www.example.com&#39; target=&#39;_blank&#39;&gt;https://www.example.com&lt;/a&gt;&quot;</span>
<span class="n">is_valid</span> <span class="o">=</span> <span class="n">validate</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">is_valid</span><span class="p">)</span>  <span class="c1"># Выводит True, если URL действителен</span>
</pre></div></div>
</div>

<p>get_host(url: str) -&gt; str:
Описание: Извлекает и возвращает хост (доменное имя) из заданного URL.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codef7b19104aac0e2afd1a4694985b6eabab"
          onclick="copyCode(codef7b19104aac0e2afd1a4694985b6eaba, codef7b19104aac0e2afd1a4694985b6eabab)">
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
<div class="code" id="codef7b19104aac0e2afd1a4694985b6eaba"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">rfc3986_validator</span> <span class="kn">import</span> <span class="n">get_host</span>

<span class="n">url</span> <span class="o">=</span> <span class="s2">&quot;&lt;a href=&#39;https://www.example.com/path&#39; target=&#39;_blank&#39;&gt;https://www.example.com/path&lt;/a&gt;&quot;</span>
<span class="n">host</span> <span class="o">=</span> <span class="n">get_host</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">host</span><span class="p">)</span>  <span class="c1"># Выводит &quot;www.example.com&quot;</span>
</pre></div></div>
</div>

<p>get_path(url: str) -&gt; str:
Описание: Извлекает и возвращает путь из заданного URL.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code3119e5eb48d3d389b2b72d8075a92de5b"
          onclick="copyCode(code3119e5eb48d3d389b2b72d8075a92de5, code3119e5eb48d3d389b2b72d8075a92de5b)">
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
<div class="code" id="code3119e5eb48d3d389b2b72d8075a92de5"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">rfc3986_validator</span> <span class="kn">import</span> <span class="n">get_path</span>

<span class="n">url</span> <span class="o">=</span> <span class="s2">&quot;&lt;a href=&#39;https://www.example.com/path&#39; target=&#39;_blank&#39;&gt;https://www.example.com/path&lt;/a&gt;&quot;</span>
<span class="n">path</span> <span class="o">=</span> <span class="n">get_path</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>  <span class="c1"># Выводит &quot;/path&quot;</span>
</pre></div></div>
</div>