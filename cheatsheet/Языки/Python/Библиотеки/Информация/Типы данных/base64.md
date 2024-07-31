<p>Библиотека "base64" в Python используется для кодирования и декодирования данных в формате base64.
Base64 является способом представления двоичных данных в виде текста, что удобно для передачи и хранения данных,
которые не могут быть безопасно переданы в обычном двоичном формате.</p>
<p>Методы модуля "base64" и его подмодулей:</p>
<p>Модуль "base64":
b64encode(data): Кодирует данные в формате base64.
b64decode(data): Декодирует данные из формата base64.
b64encodebytes(data): Кодирует данные в формате base64 и возвращает байтовую строку.
b64decodebytes(data): Декодирует байтовую строку из формата base64 и возвращает декодированные данные.</p>
<p>Подмодуль "base64.urlsafe":
urlsafe_b64encode(data): Кодирует данные в формате base64 для URL без использования символов, которые могут вызывать проблемы в URL.
urlsafe_b64decode(data): Декодирует данные из формата base64 для URL.</p>
<p>Некоторые из самых часто используемых методов "base64" и их краткое описание:</p>
<p>b64encode(data): Кодирует данные в формате base64.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codee4cb029e9b01f4273f74dcb71d03e093b"onclick="copyCode(codee4cb029e9b01f4273f74dcb71d03e093, codee4cb029e9b01f4273f74dcb71d03e093b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codee4cb029e9b01f4273f74dcb71d03e093"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">base64</span>

<span class="n">data</span> <span class="o">=</span> <span class="sa">b</span><span class="s2">&quot;Hello, World!&quot;</span>
<span class="n">encoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64encode</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">encoded_data</span><span class="p">)</span>
</pre></div></div></div>

<p>b64decode(data): Декодирует данные из формата base64.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code78761d679334660dc55e25ad6bb4440cb"onclick="copyCode(code78761d679334660dc55e25ad6bb4440c, code78761d679334660dc55e25ad6bb4440cb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code78761d679334660dc55e25ad6bb4440c"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">base64</span>

<span class="n">encoded_data</span> <span class="o">=</span> <span class="sa">b</span><span class="s2">&quot;SGVsbG8sIFdvcmxkIQ==&quot;</span>
<span class="n">decoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64decode</span><span class="p">(</span><span class="n">encoded_data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">decoded_data</span><span class="p">)</span>
</pre></div></div></div>

<p>urlsafe_b64encode(data): Кодирует данные в формате base64 для URL без использования символов, которые могут вызывать проблемы в URL.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code60a70ea81059aaa04ed1105e9aadbbfbb"onclick="copyCode(code60a70ea81059aaa04ed1105e9aadbbfb, code60a70ea81059aaa04ed1105e9aadbbfbb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code60a70ea81059aaa04ed1105e9aadbbfb"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">base64</span>

<span class="n">data</span> <span class="o">=</span> <span class="sa">b</span><span class="s2">&quot;Hello, World!&quot;</span>
<span class="n">encoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">urlsafe_b64encode</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">encoded_data</span><span class="p">)</span>
</pre></div></div></div>

<p>urlsafe_b64decode(data): Декодирует данные из формата base64 для URL.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codeaef341430c072d7a8368da8c48f168b9b"onclick="copyCode(codeaef341430c072d7a8368da8c48f168b9, codeaef341430c072d7a8368da8c48f168b9b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeaef341430c072d7a8368da8c48f168b9"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">base64</span>

<span class="n">encoded_data</span> <span class="o">=</span> <span class="sa">b</span><span class="s2">&quot;SGVsbG8sIFdvcmxkIQ==&quot;</span>
<span class="n">decoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">urlsafe_b64decode</span><span class="p">(</span><span class="n">encoded_data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">decoded_data</span><span class="p">)</span>
</pre></div></div></div>