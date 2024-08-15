<h1>Predicates</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span>//div<span class="o">[</span>true<span class="o">()]</span>
//div<span class="o">[</span>@class<span class="o">=</span><span class="s2">&quot;head&quot;</span><span class="o">]</span>
//div<span class="o">[</span>@class<span class="o">=</span><span class="s2">&quot;head&quot;</span><span class="o">][</span>@id<span class="o">=</span><span class="s2">&quot;top&quot;</span><span class="o">]</span>
</pre></div></div></div>

<p>Restricts a nodeset only if some condition is true. They can be chained.</p>
<h1>Operators</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="c1"># Comparison</span>
//a<span class="o">[</span>@id<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;xyz&quot;</span><span class="o">]</span>
//a<span class="o">[</span>@id<span class="w"> </span>!<span class="o">=</span><span class="w"> </span><span class="s2">&quot;xyz&quot;</span><span class="o">]</span>
//a<span class="o">[</span>@price<span class="w"> </span>&gt;<span class="w"> </span><span class="m">25</span><span class="o">]</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="c1"># Logic (and/or)</span>
//div<span class="o">[</span>@id<span class="o">=</span><span class="s2">&quot;head&quot;</span><span class="w"> </span>and<span class="w"> </span>position<span class="o">()=</span><span class="m">2</span><span class="o">]</span>
//div<span class="o">[(</span>x<span class="w"> </span>and<span class="w"> </span>y<span class="o">)</span><span class="w"> </span>or<span class="w"> </span>not<span class="o">(</span>z<span class="o">)]</span>
</pre></div></div></div>

<p>Use comparison and logic operators to make conditionals.</p>
<h1>Using nodes</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="c1"># Use them inside functions</span>
//ul<span class="o">[</span>count<span class="o">(</span>li<span class="o">)</span><span class="w"> </span>&gt;<span class="w"> </span><span class="m">2</span><span class="o">]</span>
//ul<span class="o">[</span>count<span class="o">(</span>li<span class="o">[</span>@class<span class="o">=</span><span class="s1">&#39;hide&#39;</span><span class="o">])</span><span class="w"> </span>&gt;<span class="w"> </span><span class="m">0</span><span class="o">]</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="c1"># This returns `&lt;ul&gt;` that has a `&lt;li&gt;` child</span>
//ul<span class="o">[</span>li<span class="o">]</span>
</pre></div></div></div>

<p>You can use nodes inside predicates.</p>
<h1>Indexing</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span>//a<span class="o">[</span><span class="m">1</span><span class="o">]</span><span class="w">                  </span><span class="c1"># first &lt;a&gt;</span>
//a<span class="o">[</span>last<span class="o">()]</span><span class="w">             </span><span class="c1"># last &lt;a&gt;</span>
//ol/li<span class="o">[</span><span class="m">2</span><span class="o">]</span><span class="w">              </span><span class="c1"># second &lt;li&gt;</span>
//ol/li<span class="o">[</span>position<span class="o">()=</span><span class="m">2</span><span class="o">]</span><span class="w">   </span><span class="c1"># same as above</span>
//ol/li<span class="o">[</span>position<span class="o">()</span>&gt;1<span class="o">]</span><span class="w">   </span><span class="c1"># :not(:first-of-type)</span>
</pre></div></div></div>

<p>Use [] with a number, or last() or position().</p>
<h1>Chaining order</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span>a<span class="o">[</span><span class="m">1</span><span class="o">][</span>@href<span class="o">=</span><span class="s1">&#39;/&#39;</span><span class="o">]</span>
a<span class="o">[</span>@href<span class="o">=</span><span class="s1">&#39;/&#39;</span><span class="o">][</span><span class="m">1</span><span class="o">]</span>
</pre></div></div></div>

<p>Order is significant, these two are different.</p>
<h1>Nesting predicates</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span>//section<span class="o">[</span>.//h1<span class="o">[</span>@id<span class="o">=</span><span class="s1">&#39;hi&#39;</span><span class="o">]]</span>
</pre></div></div></div>
<p>This returns &lt;section&gt; if it has an &lt;h1&gt; descendant with id='hi'.</p>