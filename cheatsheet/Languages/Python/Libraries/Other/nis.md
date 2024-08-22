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
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nis</span>

<span class="n">value</span> <span class="o">=</span> <span class="n">nis</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s2">&quot;passwd&quot;</span><span class="p">,</span> <span class="s2">&quot;john&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</pre></div></div></div>

<p>cat(mapname): Возвращает все записи из указанной базы данных.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nis</span>

<span class="n">records</span> <span class="o">=</span> <span class="n">nis</span><span class="o">.</span><span class="n">cat</span><span class="p">(</span><span class="s2">&quot;passwd&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">records</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">record</span><span class="p">)</span>
</pre></div></div></div>

<p>maps(): Возвращает список доступных баз данных.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nis</span>

<span class="n">map_list</span> <span class="o">=</span> <span class="n">nis</span><span class="o">.</span><span class="n">maps</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">map_list</span><span class="p">)</span>
</pre></div></div></div>

<p>Это лишь некоторые из методов, доступных в библиотеке "nis".</p>