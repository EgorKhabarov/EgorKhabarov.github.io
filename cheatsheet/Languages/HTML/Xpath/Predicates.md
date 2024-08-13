<h1>Predicates</h1>
<pre><code class="language-bash">//div[true()]
//div[@class=&quot;head&quot;]
//div[@class=&quot;head&quot;][@id=&quot;top&quot;]
</code></pre>
<p>Restricts a nodeset only if some condition is true. They can be chained.</p>
<h1>Operators</h1>
<pre><code class="language-bash"># Comparison
//a[@id = &quot;xyz&quot;]
//a[@id != &quot;xyz&quot;]
//a[@price &gt; 25]
</code></pre>
<pre><code class="language-bash"># Logic (and/or)
//div[@id=&quot;head&quot; and position()=2]
//div[(x and y) or not(z)]
</code></pre>
<p>Use comparison and logic operators to make conditionals.</p>
<h1>Using nodes</h1>
<pre><code class="language-bash"># Use them inside functions
//ul[count(li) &gt; 2]
//ul[count(li[@class='hide']) &gt; 0]
</code></pre>
<pre><code class="language-bash"># This returns `&lt;ul&gt;` that has a `&lt;li&gt;` child
//ul[li]
</code></pre>
<p>You can use nodes inside predicates.</p>
<h1>Indexing</h1>
<pre><code class="language-bash">//a[1]                  # first &lt;a&gt;
//a[last()]             # last &lt;a&gt;
//ol/li[2]              # second &lt;li&gt;
//ol/li[position()=2]   # same as above
//ol/li[position()&gt;1]   # :not(:first-of-type)
</code></pre>
<p>Use [] with a number, or last() or position().</p>
<h1>Chaining order</h1>
<pre><code class="language-bash">a[1][@href='/']
a[@href='/'][1]
</code></pre>
<p>Order is significant, these two are different.</p>
<h1>Nesting predicates</h1>
<pre><code class="language-bash">//section[.//h1[@id='hi']]
</code></pre>
<p>This returns &lt;section&gt; if it has an &lt;h1&gt; descendant with id='hi'.</p>