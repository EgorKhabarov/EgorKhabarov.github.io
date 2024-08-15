<h1>Steps and axes</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>//</td>
<td>ul</td>
<td>/</td>
<td>a[@id='link']</td>
</tr>
<tr>
<td>Axis</td>
<td>Step</td>
<td>Axis</td>
<td>Step</td>
</tr>
</tbody>
</table>
<h1>Prefixes</h1>
<table>
<thead>
<tr>
<th>Prefix</th>
<th>Example</th>
<th>What</th>
</tr>
</thead>
<tbody>
<tr>
<td>//</td>
<td>//hr[@class='edge']</td>
<td>Anywhere</td>
</tr>
<tr>
<td>./</td>
<td>./a</td>
<td>Relative</td>
</tr>
<tr>
<td>/</td>
<td>/html/body/div</td>
<td>Root</td>
</tr>
</tbody>
</table>
<p>Begin your expression with any of these.</p>
<h1>Axes</h1>
<table>
<thead>
<tr>
<th>Axis</th>
<th>Example</th>
<th>What</th>
</tr>
</thead>
<tbody>
<tr>
<td>/</td>
<td>//ul/li/a</td>
<td>Child</td>
</tr>
<tr>
<td>//</td>
<td>//[@id="list"]//a</td>
<td>Descendant</td>
</tr>
</tbody>
</table>
<p>Separate your steps with /. Use two (//) if you don’t want to select direct children.</p>
<h1>Steps</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span>//div
//div<span class="o">[</span>@name<span class="o">=</span><span class="s1">&#39;box&#39;</span><span class="o">]</span>
//<span class="o">[</span>@id<span class="o">=</span><span class="s1">&#39;link&#39;</span><span class="o">]</span>
</pre></div></div></div>

<p>A step may have an element name (div) and predicates ([...]). Both are optional. They can also be these other things:</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span>//a/text<span class="o">()</span><span class="w">     </span><span class="c1">#=&gt; &quot;Go home&quot;</span>
//a/@href<span class="w">      </span><span class="c1">#=&gt; &quot;index.html&quot;</span>
//a/*<span class="w">          </span><span class="c1">#=&gt; All a&#39;s child elements</span>
</pre></div></div></div>