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
<pre><code class="language-bash">//div
//div[@name='box']
//[@id='link']
</code></pre>
<p>A step may have an element name (div) and predicates ([...]). Both are optional. They can also be these other things:</p>
<pre><code class="language-bash">//a/text()     #=&gt; &quot;Go home&quot;
//a/@href      #=&gt; &quot;index.html&quot;
//a/*          #=&gt; All a's child elements
</code></pre>