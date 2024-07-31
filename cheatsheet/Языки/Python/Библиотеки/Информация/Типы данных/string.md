<p>Библиотека "string" в Python предоставляет набор методов для работы со строками.
Она обеспечивает функциональность для манипуляции и обработки текстовых данных.</p>
<table>
<thead>
<tr>
<th>Название метода</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>string.ascii_letters</code></td>
<td>Содержит все буквы алфавита в верхнем и нижнем регистрах.</td>
</tr>
<tr>
<td><code>string.ascii_lowercase</code></td>
<td>Содержит все буквы алфавита в нижнем регистре.</td>
</tr>
<tr>
<td><code>string.ascii_uppercase</code></td>
<td>Содержит все буквы алфавита в верхнем регистре.</td>
</tr>
<tr>
<td><code>string.digits</code></td>
<td>Содержит все цифры от 0 до 9.</td>
</tr>
<tr>
<td><code>string.hexdigits</code></td>
<td>Содержит все шестнадцатеричные цифры (от 0 до 9 и от A до F).</td>
</tr>
<tr>
<td><code>string.octdigits</code></td>
<td>Содержит все восьмеричные цифры (от 0 до 7).</td>
</tr>
<tr>
<td><code>string.punctuation</code></td>
<td>Содержит символы пунктуации.</td>
</tr>
<tr>
<td><code>string.printable</code></td>
<td>Содержит все печатные символы (буквы, цифры, символы пунктуации и пробельные символы).</td>
</tr>
<tr>
<td><code>string.whitespace</code></td>
<td>Содержит пробельные символы (пробел, табуляция, новая строка и т.д.).</td>
</tr>
</tbody>
</table>
<p><code>string.ascii_letters</code>: Возвращает все буквы алфавита в верхнем и нижнем регистрах.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code4bab015c73be6d245ed96600967feec6b"onclick="copyCode(code4bab015c73be6d245ed96600967feec6, code4bab015c73be6d245ed96600967feec6b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code4bab015c73be6d245ed96600967feec6"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">string</span>
<span class="nb">print</span><span class="p">(</span><span class="n">string</span><span class="o">.</span><span class="n">ascii_letters</span><span class="p">)</span>
</pre></div></div></div>
<p><code>string.digits</code>: Возвращает все цифры от 0 до 9.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codeb6d9f4770a58daa207d3e75f3c3bf5c3b"onclick="copyCode(codeb6d9f4770a58daa207d3e75f3c3bf5c3, codeb6d9f4770a58daa207d3e75f3c3bf5c3b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeb6d9f4770a58daa207d3e75f3c3bf5c3"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">string</span>
<span class="nb">print</span><span class="p">(</span><span class="n">string</span><span class="o">.</span><span class="n">digits</span><span class="p">)</span>
</pre></div></div></div>
<p><code>string.punctuation</code>: Возвращает символы пунктуации.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code0597a01cfa1fecf60ee9cf97ab3749acb"onclick="copyCode(code0597a01cfa1fecf60ee9cf97ab3749ac, code0597a01cfa1fecf60ee9cf97ab3749acb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code0597a01cfa1fecf60ee9cf97ab3749ac"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">string</span>
<span class="nb">print</span><span class="p">(</span><span class="n">string</span><span class="o">.</span><span class="n">punctuation</span><span class="p">)</span>
</pre></div></div></div>