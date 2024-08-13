<h1>Using axes</h1>
<pre><code class="language-bash">//ul/li                       # ul &gt; li
//ul/child::li                # ul &gt; li (same)
//ul/following-sibling::li    # ul ~ li
//ul/descendant-or-self::li   # ul li
//ul/ancestor-or-self::li     # $('ul').closest('li')
</code></pre>
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
<pre><code class="language-bash"># both the same
//ul/li/a
//child::ul/child::li/child::a
</code></pre>
<p>child:: is the default axis. This makes //a/b/c work.</p>
<pre><code class="language-bash"># both the same
# this works because `child::li` is truthy, so the predicate succeeds
//ul[li]
//ul[child::li]
</code></pre>
<pre><code class="language-bash"># both the same
//ul[count(li) &gt; 2]
//ul[count(child::li) &gt; 2]
</code></pre>
<h1>Descendant-or-self axis</h1>
<pre><code class="language-bash"># both the same
//div//h4
//div/descendant-or-self::h4
</code></pre>
<p>// is short for the descendant-or-self:: axis.</p>
<pre><code class="language-bash"># both the same
//ul//[last()]
//ul/descendant-or-self::[last()]
</code></pre>
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