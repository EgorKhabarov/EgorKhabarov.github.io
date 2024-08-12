<p>Библиотека "nis" в Python используется для работы с сервисом Network Information Service (NIS).
NIS предоставляет распределенную базу данных, которая используется для хранения информации о пользователях,
группах и других системных ресурсах в сети.</p>
<p>Методы модуля "nis":
nis.match(mapname, key): Возвращает значение, связанное с указанным ключом в указанной базе данных.
nis.cat(mapname): Возвращает все записи из указанной базы данных.
nis.maps(): Возвращает список доступных баз данных.
nis.getmapbyname(name): Возвращает содержимое базы данных с указанным именем.
nis.getmapbynumber(number): Возвращает содержимое базы данных с указанным номером.</p>
<p>Некоторые из самых часто используемых методов "nis" включают:
match(mapname, key): Возвращает значение, связанное с указанным ключом в указанной базе данных.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nis</span>

<span class="n">value</span> <span class="o">=</span> <span class="n">nis</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s2">&quot;passwd&quot;</span><span class="p">,</span> <span class="s2">&quot;john&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</pre></div></div>
</div>

<p>cat(mapname): Возвращает все записи из указанной базы данных.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nis</span>

<span class="n">records</span> <span class="o">=</span> <span class="n">nis</span><span class="o">.</span><span class="n">cat</span><span class="p">(</span><span class="s2">&quot;passwd&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">records</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">record</span><span class="p">)</span>
</pre></div></div>
</div>

<p>maps(): Возвращает список доступных баз данных.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nis</span>

<span class="n">map_list</span> <span class="o">=</span> <span class="n">nis</span><span class="o">.</span><span class="n">maps</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">map_list</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Это лишь некоторые из методов, доступных в библиотеке "nis".</p>