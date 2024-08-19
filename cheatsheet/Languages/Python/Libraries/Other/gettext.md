<p>Библиотека "gettext" в Python используется для локализации и перевода текстовых сообщений в программе.</p>
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
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">gettext</span>
<span class="n">gettext</span><span class="o">.</span><span class="n">bindtextdomain</span><span class="p">(</span><span class="s2">&quot;mydomain&quot;</span><span class="p">,</span> <span class="s2">&quot;locale/&quot;</span><span class="p">)</span>
<span class="n">gettext</span><span class="o">.</span><span class="n">textdomain</span><span class="p">(</span><span class="s2">&quot;mydomain&quot;</span><span class="p">)</span>

<span class="n">_</span> <span class="o">=</span> <span class="n">gettext</span><span class="o">.</span><span class="n">gettext</span>
<span class="nb">print</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">))</span>
</pre></div></div></div>

<p>ngettext(singular, plural, n): Возвращает перевод множественного сообщения на основе числа n.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">gettext</span>
<span class="n">gettext</span><span class="o">.</span><span class="n">bindtextdomain</span><span class="p">(</span><span class="s2">&quot;mydomain&quot;</span><span class="p">,</span> <span class="s2">&quot;locale/&quot;</span><span class="p">)</span>
<span class="n">gettext</span><span class="o">.</span><span class="n">textdomain</span><span class="p">(</span><span class="s2">&quot;mydomain&quot;</span><span class="p">)</span>

<span class="n">_</span> <span class="o">=</span> <span class="n">gettext</span><span class="o">.</span><span class="n">ngettext</span>
<span class="nb">print</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s2">&quot;</span><span class="si">%d</span><span class="s2"> apple&quot;</span><span class="p">,</span> <span class="s2">&quot;</span><span class="si">%d</span><span class="s2"> apples&quot;</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span> <span class="o">%</span> <span class="mi">5</span><span class="p">)</span>
</pre></div></div></div>

<p>dgettext(domain, message): Возвращает перевод сообщения из указанного домена.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">gettext</span>
<span class="n">gettext</span><span class="o">.</span><span class="n">bindtextdomain</span><span class="p">(</span><span class="s2">&quot;mydomain&quot;</span><span class="p">,</span> <span class="s2">&quot;locale/&quot;</span><span class="p">)</span>
<span class="n">gettext</span><span class="o">.</span><span class="n">textdomain</span><span class="p">(</span><span class="s2">&quot;mydomain&quot;</span><span class="p">)</span>

<span class="n">_</span> <span class="o">=</span> <span class="n">gettext</span><span class="o">.</span><span class="n">dgettext</span>
<span class="nb">print</span><span class="p">(</span><span class="n">_</span><span class="p">(</span><span class="s2">&quot;mydomain&quot;</span><span class="p">,</span> <span class="s2">&quot;Hello, world!&quot;</span><span class="p">))</span>
</pre></div></div></div>