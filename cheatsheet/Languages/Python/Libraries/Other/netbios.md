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
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">netbios</span> <span class="k">as</span> <span class="nn">nb</span>

<span class="n">name</span> <span class="o">=</span> <span class="n">nb</span><span class="o">.</span><span class="n">getnetbiosname</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
</pre></div></div></div>

<p>nbt.getwinsaddrs(): Возвращает список IP-адресов машин, знающих сведения о NetBIOS-именах.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">netbios</span> <span class="k">as</span> <span class="nn">nb</span>

<span class="n">wins_addrs</span> <span class="o">=</span> <span class="n">nb</span><span class="o">.</span><span class="n">getwinsaddrs</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">wins_addrs</span><span class="p">)</span>
</pre></div></div></div>

<p>nbt.getnodetype(): Возвращает тип узла в сети.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">netbios</span> <span class="k">as</span> <span class="nn">nb</span>

<span class="n">node_type</span> <span class="o">=</span> <span class="n">nb</span><span class="o">.</span><span class="n">getnodetype</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">node_type</span><span class="p">)</span>
</pre></div></div></div>