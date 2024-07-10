<p>Модуль tabnanny в Python используется для проверки исходных файлов
на наличие проблем с табуляцией, которые могут вызвать синтаксические ошибки.</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>process_tokens(tokens)</td>
<td>Проверяет токены файла на проблемы с табуляцией.</td>
</tr>
<tr>
<td>NannyToken(token)</td>
<td>Конструктор класса токенов, используемый для проверки.</td>
</tr>
</tbody>
</table>
<p><strong>process_tokens(tokens)</strong> Проверяет токены файла на наличие проблем с табуляцией.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeb1f71e7d01178517624958ea6e2d1144b" onclick="copyCode(codeb1f71e7d01178517624958ea6e2d1144, codeb1f71e7d01178517624958ea6e2d1144b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeb1f71e7d01178517624958ea6e2d1144"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">tokenize</span>
<span class="kn">from</span> <span class="nn">tabnanny</span> <span class="kn">import</span> <span class="n">process_tokens</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s1">&#39;file.py&#39;</span><span class="p">,</span> <span class="s1">&#39;rb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">tokens</span> <span class="o">=</span> <span class="n">tokenize</span><span class="o">.</span><span class="n">generate_tokens</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">readline</span><span class="p">)</span>
    <span class="n">process_tokens</span><span class="p">(</span><span class="n">tokens</span><span class="p">)</span>
</pre></div></div></div>

<p><strong>NannyToken(token)</strong> Конструктор класса токенов, используемый для проверки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codee35d23fb5dc489fe4efb8c80bcf97f99b" onclick="copyCode(codee35d23fb5dc489fe4efb8c80bcf97f99, codee35d23fb5dc489fe4efb8c80bcf97f99b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codee35d23fb5dc489fe4efb8c80bcf97f99"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">tabnanny</span> <span class="kn">import</span> <span class="n">NannyToken</span>

<span class="n">token</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;    &#39;</span><span class="p">,</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span> <span class="s1">&#39;    &#39;</span><span class="p">)</span>  <span class="c1"># Пример токена с проблемой</span>
<span class="n">nanny_token</span> <span class="o">=</span> <span class="n">NannyToken</span><span class="p">(</span><span class="n">token</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">nanny_token</span><span class="p">)</span>
</pre></div></div></div>