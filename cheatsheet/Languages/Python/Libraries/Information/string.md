<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ascii_letters</code></td>
<td>Содержит все буквы алфавита в верхнем и нижнем регистрах</td>
</tr>
<tr>
<td><code>ascii_lowercase</code></td>
<td>Содержит все буквы алфавита в нижнем регистре</td>
</tr>
<tr>
<td><code>ascii_uppercase</code></td>
<td>Содержит все буквы алфавита в верхнем регистре</td>
</tr>
<tr>
<td><code>capwords</code></td>
<td></td>
</tr>
<tr>
<td><code>digits</code></td>
<td>Содержит все цифры от 0 до 9</td>
</tr>
<tr>
<td><code>hexdigits</code></td>
<td>Содержит все шестнадцатеричные цифры (от 0 до 9 и от A до F)</td>
</tr>
<tr>
<td><code>octdigits</code></td>
<td>Содержит все восьмеричные цифры (от 0 до 7)</td>
</tr>
<tr>
<td><code>printable</code></td>
<td>Содержит все печатные символы (буквы, цифры, символы пунктуации и пробельные символы)</td>
</tr>
<tr>
<td><code>punctuation</code></td>
<td>Содержит символы пунктуации</td>
</tr>
<tr>
<td><code>whitespace</code></td>
<td>Содержит пробельные символы (пробел, табуляция, новая строка и т.д.)</td>
</tr>
<tr>
<td><code>Formatter</code></td>
<td></td>
</tr>
<tr>
<td><code>Template</code></td>
<td>A string class for supporting $-substitutions</td>
</tr>
</tbody>
</table>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">string</span><span class="o">.</span><span class="n">ascii_lowercase</span>
<span class="unselectable"><span class="go">&quot;abcdefghijklmnopqrstuvwxyz&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">string</span><span class="o">.</span><span class="n">ascii_uppercase</span>
<span class="unselectable"><span class="go">&quot;ABCDEFGHIJKLMNOPQRSTUVWXYZ&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">string</span><span class="o">.</span><span class="n">ascii_letters</span>  <span class="c1"># ascii_lowercase + ascii_uppercase</span>
<span class="unselectable"><span class="go">&quot;abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">string</span><span class="o">.</span><span class="n">capwords</span><span class="p">(</span><span class="s2">&quot;text text text&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;Text Text Text&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">string</span><span class="o">.</span><span class="n">digits</span>
<span class="unselectable"><span class="go">&quot;0123456789&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">string</span><span class="o">.</span><span class="n">hexdigits</span>
<span class="unselectable"><span class="go">digits + &quot;abcdef&quot; + &quot;ABCDEF&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">string</span><span class="o">.</span><span class="n">octdigits</span>
<span class="unselectable"><span class="go">&quot;01234567&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">string</span><span class="o">.</span><span class="n">printable</span>  <span class="c1"># digits + ascii_letters + punctuation + whitespace</span>
<span class="unselectable"><span class="go">&quot;0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!&quot;#$%&amp;\&#39;()*+,-./:;&lt;=&gt;?@[\\]^_&#x60;{|}~ \t\n\r\x0b\x0c&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">string</span><span class="o">.</span><span class="n">punctuation</span>
<span class="unselectable"><span class="go">&quot;!\&quot;#$%&amp;&#39;()*+,-./:;&lt;=&gt;?@[\\]^_&#x60;{|}~&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">string</span><span class="o">.</span><span class="n">whitespace</span>  <span class="c1"># &quot; \t\n\r\v\f&quot;</span>
<span class="unselectable"><span class="go">&quot; \t\n\r\x0b\x0c&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">string</span><span class="o">.</span><span class="n">Formatter</span>
<span class="unselectable"><span class="go">&lt;class &#39;string.Formatter&#39;&gt;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">string</span><span class="o">.</span><span class="n">Template</span>
<span class="unselectable"><span class="go">&lt;class &#39;string.Template&#39;&gt;</span>
</span></pre></div></div></div>