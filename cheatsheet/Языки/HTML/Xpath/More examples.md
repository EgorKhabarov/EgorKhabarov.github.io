<h1>Examples</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code639b" onclick="copyCode(code639, code639b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code639"><div class="highlight"><pre><span></span>//*<span class="w">                 </span><span class="c1"># all elements</span>
count<span class="o">(</span>//*<span class="o">)</span><span class="w">          </span><span class="c1"># count all elements</span>
<span class="o">(</span>//h1<span class="o">)[</span><span class="m">1</span><span class="o">]</span>/text<span class="o">()</span><span class="w">    </span><span class="c1"># text of the first h1 heading</span>
//li<span class="o">[</span>span<span class="o">]</span><span class="w">          </span><span class="c1"># find a &lt;li&gt; with an &lt;span&gt; inside it</span>
<span class="w">                    </span><span class="c1"># ...expands to //li[child::span]</span>
//ul/li/..<span class="w">          </span><span class="c1"># use .. to select a parent</span>
</pre></div></div></div>

<h1>Find a parent</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code640b" onclick="copyCode(code640, code640b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code640"><div class="highlight"><pre><span></span>//section<span class="o">[</span>h1<span class="o">[</span>@id<span class="o">=</span><span class="s1">&#39;section-name&#39;</span><span class="o">]]</span>
</pre></div></div></div>

<p>Finds a &lt;section&gt; that directly contains h1#section-name</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code641b" onclick="copyCode(code641, code641b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code641"><div class="highlight"><pre><span></span>//section<span class="o">[</span>//h1<span class="o">[</span>@id<span class="o">=</span><span class="s1">&#39;section-name&#39;</span><span class="o">]]</span>
</pre></div></div></div>

<p>Finds a &lt;section&gt; that contains h1#section-name.
(Same as above, but uses descendant-or-self instead of child)</p>
<h1>Closest</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code642b" onclick="copyCode(code642, code642b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code642"><div class="highlight"><pre><span></span>./ancestor-or-self::<span class="o">[</span>@class<span class="o">=</span><span class="s2">&quot;box&quot;</span><span class="o">]</span>
</pre></div></div></div>

<p>Works like jQuery’s $().closest('.box').</p>
<h1>Attributes</h1>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" id="code643b" onclick="copyCode(code643, code643b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code643"><div class="highlight"><pre><span></span>//item<span class="o">[</span>@price<span class="w"> </span>&gt;<span class="w"> </span><span class="m">2</span>*@discount<span class="o">]</span>
</pre></div></div></div>

<p>Finds &lt;item&gt; and check its attributes</p>