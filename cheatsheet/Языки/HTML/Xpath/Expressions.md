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
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code610b" onclick="copyCode(code610, code610b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code610"><div class="highlight"><pre><span></span>//div
//div<span class="o">[</span>@name<span class="o">=</span><span class="s1">&#39;box&#39;</span><span class="o">]</span>
//<span class="o">[</span>@id<span class="o">=</span><span class="s1">&#39;link&#39;</span><span class="o">]</span>
</pre></div></div></div>

<p>A step may have an element name (div) and predicates ([...]). Both are optional. They can also be these other things:</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code611b" onclick="copyCode(code611, code611b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code611"><div class="highlight"><pre><span></span>//a/text<span class="o">()</span><span class="w">     </span><span class="c1">#=&gt; &quot;Go home&quot;</span>
//a/@href<span class="w">      </span><span class="c1">#=&gt; &quot;index.html&quot;</span>
//a/*<span class="w">          </span><span class="c1">#=&gt; All a&#39;s child elements</span>
</pre></div></div></div>