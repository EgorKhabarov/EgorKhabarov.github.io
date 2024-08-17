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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">base64</span>

<span class="n">data</span> <span class="o">=</span> <span class="sa">b</span><span class="s2">&quot;Hello, World!&quot;</span>
<span class="n">encoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64encode</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">encoded_data</span><span class="p">)</span>
</pre></div></div></div>

<p>b64decode(data): Декодирует данные из формата base64.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">base64</span>

<span class="n">encoded_data</span> <span class="o">=</span> <span class="sa">b</span><span class="s2">&quot;SGVsbG8sIFdvcmxkIQ==&quot;</span>
<span class="n">decoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64decode</span><span class="p">(</span><span class="n">encoded_data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">decoded_data</span><span class="p">)</span>
</pre></div></div></div>

<p>urlsafe_b64encode(data): Кодирует данные в формате base64 для URL без использования символов, которые могут вызывать проблемы в URL.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">base64</span>

<span class="n">data</span> <span class="o">=</span> <span class="sa">b</span><span class="s2">&quot;Hello, World!&quot;</span>
<span class="n">encoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">urlsafe_b64encode</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">encoded_data</span><span class="p">)</span>
</pre></div></div></div>

<p>urlsafe_b64decode(data): Декодирует данные из формата base64 для URL.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">base64</span>

<span class="n">encoded_data</span> <span class="o">=</span> <span class="sa">b</span><span class="s2">&quot;SGVsbG8sIFdvcmxkIQ==&quot;</span>
<span class="n">decoded_data</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">urlsafe_b64decode</span><span class="p">(</span><span class="n">encoded_data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">decoded_data</span><span class="p">)</span>
</pre></div></div></div>