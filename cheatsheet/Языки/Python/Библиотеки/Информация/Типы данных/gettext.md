<p>Библиотека "gettext" в Python используется для локализации и перевода текстовых сообщений в программе. </p>
<h1>Таблица методов модуля "gettext" и его подмодулей:</h1>
<h3>Методы модуля "gettext":</h3>
<p>bindtextdomain(domain, directory): устанавливает домен и директорию для поиска файлов перевода.
dgettext(domain, message): возвращает перевод сообщения из указанного домена.
dngettext(domain, singular, plural, n): возвращает перевод множественного сообщения на основе числа n.
gettext(message): возвращает перевод сообщения.
ngettext(singular, plural, n): возвращает перевод множественного сообщения на основе числа n.
textdomain(domain): устанавливает текущий домен перевода.</p>
<h3>Методы подмодуля "gettext.translation":</h3>
<p>gettext.translation(domain, localedir=None, languages=None, fallback=False): создает объект перевода на основе заданного домена и директории локализации.
gettext.translation(""): возвращает объект перевода для текущего домена.
add_fallback(translations): добавляет объект перевода в список резервных вариантов перевода.
install(domain, localedir=None, unicode=0): устанавливает объект перевода в качестве текущего.</p>
<p>Самые часто используемые методы библиотеки "gettext" вместе с их кратким описанием и примером кода:</p>
<p>gettext(message): Возвращает перевод сообщения.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code240b" onclick="copyCode(code240, code240b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code240"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">gettext</span>
<span class="n">gettext</span><span class="o">.</span><span class="n">bindtextdomain</span><span class="p">(</span><span class="s1">&#39;mydomain&#39;</span><span class="p">,</span> <span class="s1">&#39;locale/&#39;</span><span class="p">)</span>
<span class="n">gettext</span><span class="o">.</span><span class="n">textdomain</span><span class="p">(</span><span class="s1">&#39;mydomain&#39;</span><span class="p">)</span>

<span class="n">_</span> <span class="o">=</span> <span class="n">gettext</span><span class="o">.</span><span class="n">gettext</span>
<span class="nb">print</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s1">&#39;Hello, world!&#39;</span><span class="p">))</span>
</pre></div></div></div>

<p>ngettext(singular, plural, n): Возвращает перевод множественного сообщения на основе числа n.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code241b" onclick="copyCode(code241, code241b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code241"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">gettext</span>
<span class="n">gettext</span><span class="o">.</span><span class="n">bindtextdomain</span><span class="p">(</span><span class="s1">&#39;mydomain&#39;</span><span class="p">,</span> <span class="s1">&#39;locale/&#39;</span><span class="p">)</span>
<span class="n">gettext</span><span class="o">.</span><span class="n">textdomain</span><span class="p">(</span><span class="s1">&#39;mydomain&#39;</span><span class="p">)</span>

<span class="n">_</span> <span class="o">=</span> <span class="n">gettext</span><span class="o">.</span><span class="n">ngettext</span>
<span class="nb">print</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s1">&#39;</span><span class="si">%d</span><span class="s1"> apple&#39;</span><span class="p">,</span> <span class="s1">&#39;</span><span class="si">%d</span><span class="s1"> apples&#39;</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span> <span class="o">%</span> <span class="mi">5</span><span class="p">)</span>
</pre></div></div></div>

<p>dgettext(domain, message): Возвращает перевод сообщения из указанного домена.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code242b" onclick="copyCode(code242, code242b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code242"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">gettext</span>
<span class="n">gettext</span><span class="o">.</span><span class="n">bindtextdomain</span><span class="p">(</span><span class="s1">&#39;mydomain&#39;</span><span class="p">,</span> <span class="s1">&#39;locale/&#39;</span><span class="p">)</span>
<span class="n">gettext</span><span class="o">.</span><span class="n">textdomain</span><span class="p">(</span><span class="s1">&#39;mydomain&#39;</span><span class="p">)</span>

<span class="n">_</span> <span class="o">=</span> <span class="n">gettext</span><span class="o">.</span><span class="n">dgettext</span>
<span class="nb">print</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s1">&#39;mydomain&#39;</span><span class="p">,</span> <span class="s1">&#39;Hello, world!&#39;</span><span class="p">))</span>
</pre></div></div></div>