<h1>Using axes</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code610b" onclick="copyCode(code610, code610b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code610"><div class="highlight"><pre><span></span>//ul/li<span class="w">                       </span><span class="c1"># ul &gt; li</span>
//ul/child::li<span class="w">                </span><span class="c1"># ul &gt; li (same)</span>
//ul/following-sibling::li<span class="w">    </span><span class="c1"># ul ~ li</span>
//ul/descendant-or-self::li<span class="w">   </span><span class="c1"># ul li</span>
//ul/ancestor-or-self::li<span class="w">     </span><span class="c1"># $(&#39;ul&#39;).closest(&#39;li&#39;)</span>
</pre></div></div></div>

<p>Steps of an expression are separated by /, usually used to pick child nodes.
That’s not always true: you can specify a different “axis” with ::.</p>
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
<td>/child::</td>
<td>li</td>
</tr>
<tr>
<td>Axis</td>
<td>Step</td>
<td>Axis</td>
<td>Step</td>
</tr>
</tbody>
</table>
<h1>Child axis</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code611b" onclick="copyCode(code611, code611b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code611"><div class="highlight"><pre><span></span><span class="c1"># both the same</span>
//ul/li/a
//child::ul/child::li/child::a
</pre></div></div></div>

<p>child:: is the default axis. This makes //a/b/c work.</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code612b" onclick="copyCode(code612, code612b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code612"><div class="highlight"><pre><span></span><span class="c1"># both the same</span>
<span class="c1"># this works because `child::li` is truthy, so the predicate succeeds</span>
//ul<span class="o">[</span>li<span class="o">]</span>
//ul<span class="o">[</span>child::li<span class="o">]</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code613b" onclick="copyCode(code613, code613b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code613"><div class="highlight"><pre><span></span><span class="c1"># both the same</span>
//ul<span class="o">[</span>count<span class="o">(</span>li<span class="o">)</span><span class="w"> </span>&gt;<span class="w"> </span><span class="m">2</span><span class="o">]</span>
//ul<span class="o">[</span>count<span class="o">(</span>child::li<span class="o">)</span><span class="w"> </span>&gt;<span class="w"> </span><span class="m">2</span><span class="o">]</span>
</pre></div></div></div>

<h1>Descendant-or-self axis</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code614b" onclick="copyCode(code614, code614b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code614"><div class="highlight"><pre><span></span><span class="c1"># both the same</span>
//div//h4
//div/descendant-or-self::h4
</pre></div></div></div>

<p>// is short for the descendant-or-self:: axis.</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code615b" onclick="copyCode(code615, code615b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code615"><div class="highlight"><pre><span></span><span class="c1"># both the same</span>
//ul//<span class="o">[</span>last<span class="o">()]</span>
//ul/descendant-or-self::<span class="o">[</span>last<span class="o">()]</span>
</pre></div></div></div>

<h1>Other axes</h1>
<table>
<thead>
<tr>
<th>Axis</th>
<th>Abbrev</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>ancestor</td>
<td></td>
<td></td>
</tr>
<tr>
<td>ancestor-or-self</td>
<td></td>
<td></td>
</tr>
<tr>
<td>attribute</td>
<td>@</td>
<td>@href is short for attribute::href</td>
</tr>
<tr>
<td>child</td>
<td></td>
<td>div is short for child::div</td>
</tr>
<tr>
<td>descendant</td>
<td></td>
<td></td>
</tr>
<tr>
<td>descendant-or-self</td>
<td>//</td>
<td>// is short for /descendant-or-self::node()/</td>
</tr>
<tr>
<td>namespace</td>
<td></td>
<td></td>
</tr>
<tr>
<td>self</td>
<td>.</td>
<td>. is short for self::node()</td>
</tr>
<tr>
<td>parent</td>
<td>..</td>
<td>.. is short for parent::node()</td>
</tr>
<tr>
<td>following</td>
<td></td>
<td></td>
</tr>
<tr>
<td>following-sibling</td>
<td></td>
<td></td>
</tr>
<tr>
<td>preceding</td>
<td></td>
<td></td>
</tr>
<tr>
<td>preceding-sibling</td>
<td></td>
<td></td>
</tr>
<tr>
<td>There are other axes you can use.</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h1>Unions</h1>
<p>//a | //span
Use | to join two expressions.</p>