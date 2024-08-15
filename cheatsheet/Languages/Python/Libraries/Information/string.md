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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">string</span>
<span class="nb">print</span><span class="p">(</span><span class="n">string</span><span class="o">.</span><span class="n">ascii_letters</span><span class="p">)</span>
</pre></div></div></div>
<p><code>string.digits</code>: Возвращает все цифры от 0 до 9.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">string</span>
<span class="nb">print</span><span class="p">(</span><span class="n">string</span><span class="o">.</span><span class="n">digits</span><span class="p">)</span>
</pre></div></div></div>
<p><code>string.punctuation</code>: Возвращает символы пунктуации.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">string</span>
<span class="nb">print</span><span class="p">(</span><span class="n">string</span><span class="o">.</span><span class="n">punctuation</span><span class="p">)</span>
</pre></div></div></div>