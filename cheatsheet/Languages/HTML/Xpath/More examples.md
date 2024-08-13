<h1>Examples</h1>
<pre><code class="language-bash">//*                 # all elements
count(//*)          # count all elements
(//h1)[1]/text()    # text of the first h1 heading
//li[span]          # find a &lt;li&gt; with an &lt;span&gt; inside it
                    # ...expands to //li[child::span]
//ul/li/..          # use .. to select a parent
</code></pre>
<h1>Find a parent</h1>
<pre><code class="language-bash">//section[h1[@id='section-name']]
</code></pre>
<p>Finds a &lt;section&gt; that directly contains h1#section-name</p>
<pre><code class="language-bash">//section[//h1[@id='section-name']]
</code></pre>
<p>Finds a &lt;section&gt; that contains h1#section-name.
(Same as above, but uses descendant-or-self instead of child)</p>
<h1>Closest</h1>
<pre><code class="language-bash">./ancestor-or-self::[@class=&quot;box&quot;]
</code></pre>
<p>Works like jQuery’s $().closest('.box').</p>
<h1>Attributes</h1>
<pre><code class="language-bash">//item[@price &gt; 2*@discount]
</code></pre>
<p>Finds &lt;item&gt; and check its attributes</p>