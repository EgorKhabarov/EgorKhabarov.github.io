<p>Библиотека "certifi" в Python используется для работы с сертификатами в криптографии.
Она предоставляет набор корневых сертификатов, которые могут быть использованы
для проверки подлинности SSL-соединений при выполнении запросов HTTP.</p>
<p>Методы и подмодули "certifi":
Подмодуль "cacertifi": содержит корневые сертификаты, предназначенные для проверки SSL-соединений.
Функция <code>where()</code>: возвращает путь к файлу с набором корневых сертификатов.
Функция <code>contents()</code>: возвращает содержимое файла с корневыми сертификатами в виде строки.
Функция <code>old_where()</code>: возвращает путь к предыдущей версии файла с корневыми сертификатами.
Функция <code>old_contents()</code>: возвращает содержимое предыдущей версии файла с корневыми сертификатами.
Функция <code>contents_bytes()</code>: возвращает содержимое файла с корневыми сертификатами в виде байтовой строки.</p>
<p>Некоторые часто используемые методы "certifi":
Функция <code>where()</code>: возвращает путь к файлу с набором корневых сертификатов.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">where</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
</pre></div></div></div>

<p>Функция <code>contents()</code>: возвращает содержимое файла с корневыми сертификатами в виде строки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">cert_contents</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">contents</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cert_contents</span><span class="p">)</span>
</pre></div></div></div>

<p>Функция <code>old_where()</code>: возвращает путь к предыдущей версии файла с корневыми сертификатами.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">old_file_path</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">old_where</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">old_file_path</span><span class="p">)</span>
</pre></div></div></div>

<p>Функция <code>old_contents()</code>: возвращает содержимое предыдущей версии файла с корневыми сертификатами.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">old_cert_contents</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">old_contents</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">old_cert_contents</span><span class="p">)</span>
</pre></div></div></div>

<p>Функция <code>contents_bytes()</code>: возвращает содержимое файла с корневыми сертификатами в виде байтовой строки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">cert_bytes</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">contents_bytes</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cert_bytes</span><span class="p">)</span>
</pre></div></div></div>