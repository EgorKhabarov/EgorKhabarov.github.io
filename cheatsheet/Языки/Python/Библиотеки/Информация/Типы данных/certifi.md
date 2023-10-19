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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code89b" onclick="copyCode(code89, code89b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code89"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">where</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
</pre></div></div></div>

<p>Функция <code>contents()</code>: возвращает содержимое файла с корневыми сертификатами в виде строки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code90b" onclick="copyCode(code90, code90b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code90"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">cert_contents</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">contents</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cert_contents</span><span class="p">)</span>
</pre></div></div></div>

<p>Функция <code>old_where()</code>: возвращает путь к предыдущей версии файла с корневыми сертификатами.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code91b" onclick="copyCode(code91, code91b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code91"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">old_file_path</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">old_where</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">old_file_path</span><span class="p">)</span>
</pre></div></div></div>

<p>Функция <code>old_contents()</code>: возвращает содержимое предыдущей версии файла с корневыми сертификатами.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code92b" onclick="copyCode(code92, code92b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code92"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">old_cert_contents</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">old_contents</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">old_cert_contents</span><span class="p">)</span>
</pre></div></div></div>

<p>Функция <code>contents_bytes()</code>: возвращает содержимое файла с корневыми сертификатами в виде байтовой строки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code93b" onclick="copyCode(code93, code93b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code93"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">cert_bytes</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">contents_bytes</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cert_bytes</span><span class="p">)</span>
</pre></div></div></div>