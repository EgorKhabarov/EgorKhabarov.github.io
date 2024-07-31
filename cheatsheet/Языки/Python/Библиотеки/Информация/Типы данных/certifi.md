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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codec57c66634149f5c73eca780bcd0a66b2b"onclick="copyCode(codec57c66634149f5c73eca780bcd0a66b2, codec57c66634149f5c73eca780bcd0a66b2b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codec57c66634149f5c73eca780bcd0a66b2"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">where</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
</pre></div></div></div>

<p>Функция <code>contents()</code>: возвращает содержимое файла с корневыми сертификатами в виде строки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code5c24f5dcefc2b432f73ba20bc93d5d9bb"onclick="copyCode(code5c24f5dcefc2b432f73ba20bc93d5d9b, code5c24f5dcefc2b432f73ba20bc93d5d9bb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code5c24f5dcefc2b432f73ba20bc93d5d9b"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">cert_contents</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">contents</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cert_contents</span><span class="p">)</span>
</pre></div></div></div>

<p>Функция <code>old_where()</code>: возвращает путь к предыдущей версии файла с корневыми сертификатами.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code21d599ba2c3d7c9ec0a802c86936fc9bb"onclick="copyCode(code21d599ba2c3d7c9ec0a802c86936fc9b, code21d599ba2c3d7c9ec0a802c86936fc9bb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code21d599ba2c3d7c9ec0a802c86936fc9b"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">old_file_path</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">old_where</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">old_file_path</span><span class="p">)</span>
</pre></div></div></div>

<p>Функция <code>old_contents()</code>: возвращает содержимое предыдущей версии файла с корневыми сертификатами.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code73ce910e94633ec1cdc8fcf26d1ba2d0b"onclick="copyCode(code73ce910e94633ec1cdc8fcf26d1ba2d0, code73ce910e94633ec1cdc8fcf26d1ba2d0b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code73ce910e94633ec1cdc8fcf26d1ba2d0"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">old_cert_contents</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">old_contents</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">old_cert_contents</span><span class="p">)</span>
</pre></div></div></div>

<p>Функция <code>contents_bytes()</code>: возвращает содержимое файла с корневыми сертификатами в виде байтовой строки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codebc91fbe89ea326835e82ac6dcd82f849b"onclick="copyCode(codebc91fbe89ea326835e82ac6dcd82f849, codebc91fbe89ea326835e82ac6dcd82f849b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codebc91fbe89ea326835e82ac6dcd82f849"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">certifi</span>

<span class="n">cert_bytes</span> <span class="o">=</span> <span class="n">certifi</span><span class="o">.</span><span class="n">contents_bytes</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cert_bytes</span><span class="p">)</span>
</pre></div></div></div>