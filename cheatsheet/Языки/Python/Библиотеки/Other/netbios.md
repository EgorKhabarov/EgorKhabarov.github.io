<p>"netbios" - это библиотека в Python, которая предоставляет функциональность
для работы с протоколом NetBIOS (Network Basic Input/Output System).</p>
<p>Таблица методов модуля "netbios" и их краткого описания:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>nbt.getnetbiosname()</td>
<td>Получает NetBIOS-имя компьютера, на котором выполняется код.</td>
</tr>
<tr>
<td>nbt.getwinsaddrs()</td>
<td>Возвращает список IP-адресов машин, знающих сведения о NetBIOS-именах.</td>
</tr>
<tr>
<td>nbt.getnodetype()</td>
<td>Возвращает тип узла в сети.</td>
</tr>
<tr>
<td>nbt.gethostbyname()</td>
<td>Возвращает IP-адреса, связанные с указанным NetBIOS-именем.</td>
</tr>
<tr>
<td>nbt.getbcastaddrs()</td>
<td>Возвращает список широковещательных адресов, связанных с NetBIOS-именами.</td>
</tr>
</tbody>
</table>
<p>Список самых часто используемых методов, их краткого описания и</p>
<p>nbt.getnetbiosname(): Возвращает NetBIOS-имя компьютера.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">netbios</span> <span class="k">as</span> <span class="nn">nb</span>

<span class="n">name</span> <span class="o">=</span> <span class="n">nb</span><span class="o">.</span><span class="n">getnetbiosname</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
</pre></div></div>
</div>

<p>nbt.getwinsaddrs(): Возвращает список IP-адресов машин, знающих сведения о NetBIOS-именах.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">netbios</span> <span class="k">as</span> <span class="nn">nb</span>

<span class="n">wins_addrs</span> <span class="o">=</span> <span class="n">nb</span><span class="o">.</span><span class="n">getwinsaddrs</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">wins_addrs</span><span class="p">)</span>
</pre></div></div>
</div>

<p>nbt.getnodetype(): Возвращает тип узла в сети.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">netbios</span> <span class="k">as</span> <span class="nn">nb</span>

<span class="n">node_type</span> <span class="o">=</span> <span class="n">nb</span><span class="o">.</span><span class="n">getnodetype</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">node_type</span><span class="p">)</span>
</pre></div></div>
</div>