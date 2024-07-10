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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code0c3daafb9557cc1f40c1aafb5f765742b" onclick="copyCode(code0c3daafb9557cc1f40c1aafb5f765742, code0c3daafb9557cc1f40c1aafb5f765742b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code0c3daafb9557cc1f40c1aafb5f765742"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">base64</span>

<span class="n">data</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;Hello, World!&#39;</span>
<span class="n">encoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64encode</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">encoded_data</span><span class="p">)</span>
</pre></div></div></div>

<p>b64decode(data): Декодирует данные из формата base64.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code3c3a967df6c71d6bb06b688656425412b" onclick="copyCode(code3c3a967df6c71d6bb06b688656425412, code3c3a967df6c71d6bb06b688656425412b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code3c3a967df6c71d6bb06b688656425412"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">base64</span>

<span class="n">encoded_data</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;SGVsbG8sIFdvcmxkIQ==&#39;</span>
<span class="n">decoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64decode</span><span class="p">(</span><span class="n">encoded_data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">decoded_data</span><span class="p">)</span>
</pre></div></div></div>

<p>urlsafe_b64encode(data): Кодирует данные в формате base64 для URL без использования символов, которые могут вызывать проблемы в URL.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code09ec12a5b401fd24b7bc19f7a63b1688b" onclick="copyCode(code09ec12a5b401fd24b7bc19f7a63b1688, code09ec12a5b401fd24b7bc19f7a63b1688b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code09ec12a5b401fd24b7bc19f7a63b1688"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">base64</span>

<span class="n">data</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;Hello, World!&#39;</span>
<span class="n">encoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">urlsafe_b64encode</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">encoded_data</span><span class="p">)</span>
</pre></div></div></div>

<p>urlsafe_b64decode(data): Декодирует данные из формата base64 для URL.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code4104e5e3ddedae7930814180fb161cb8b" onclick="copyCode(code4104e5e3ddedae7930814180fb161cb8, code4104e5e3ddedae7930814180fb161cb8b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code4104e5e3ddedae7930814180fb161cb8"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">base64</span>

<span class="n">encoded_data</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;SGVsbG8sIFdvcmxkIQ==&#39;</span>
<span class="n">decoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">urlsafe_b64decode</span><span class="p">(</span><span class="n">encoded_data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">decoded_data</span><span class="p">)</span>
</pre></div></div></div>