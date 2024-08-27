<h1>Using axes</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>//ul/li<span class="w">                       </span><span class="c1"># ul &gt; li</span>
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
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="c1"># both the same</span>
//ul/li/a
//child::ul/child::li/child::a
</pre></div></div></div>

<p>child:: is the default axis. This makes //a/b/c work.</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="c1"># both the same</span>
<span class="c1"># this works because &#x60;child::li&#x60; is truthy, so the predicate succeeds</span>
//ul<span class="o">[</span>li<span class="o">]</span>
//ul<span class="o">[</span>child::li<span class="o">]</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="c1"># both the same</span>
//ul<span class="o">[</span>count<span class="o">(</span>li<span class="o">)</span><span class="w"> </span>&gt;<span class="w"> </span><span class="m">2</span><span class="o">]</span>
//ul<span class="o">[</span>count<span class="o">(</span>child::li<span class="o">)</span><span class="w"> </span>&gt;<span class="w"> </span><span class="m">2</span><span class="o">]</span>
</pre></div></div></div>

<h1>Descendant-or-self axis</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="c1"># both the same</span>
//div//h4
//div/descendant-or-self::h4
</pre></div></div></div>

<p>// is short for the descendant-or-self:: axis.</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="c1"># both the same</span>
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