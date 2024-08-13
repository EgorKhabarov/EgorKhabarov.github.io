<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>

<span class="kn">import</span> <span class="nn">requests</span>
<span class="kn">from</span> <span class="nn">requests.exceptions</span> <span class="kn">import</span> <span class="n">MissingSchema</span>


<span class="k">def</span> <span class="nf">download_emoji</span><span class="p">(</span><span class="n">emoji</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
    <span class="n">emoji_name</span> <span class="o">=</span> <span class="s2">&quot;-&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="nb">hex</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="n">c</span><span class="p">)))[</span><span class="mi">2</span><span class="p">:]</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">emoji</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">emoji_name</span><span class="p">)</span>
    <span class="n">link</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">&quot;https://web.telegram.org/a/img-apple-64/</span><span class="si">{</span><span class="n">emoji_name</span><span class="si">}</span><span class="s2">.png&quot;</span>
    <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">&quot;User-Agent&quot;</span><span class="p">:</span> <span class="p">(</span>
            <span class="s2">&quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64) &quot;</span>
            <span class="s2">&quot;AppleWebKit/537.36 (KHTML, like Gecko) &quot;</span>
            <span class="s2">&quot;Chrome/120.0.0.0 Safari/537.36 Edg/113.0.1774.42&quot;</span>
        <span class="p">)</span>
    <span class="p">}</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;emojis/</span><span class="si">{</span><span class="n">emoji_name</span><span class="si">}</span><span class="s2">.png&quot;</span><span class="p">,</span> <span class="s2">&quot;wb&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
            <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">link</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">True</span>
    <span class="k">except</span> <span class="n">MissingSchema</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">ConnectionError</span><span class="p">:</span>
        <span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">&quot;404&quot;</span><span class="p">)</span>
    <span class="k">return</span> <span class="kc">False</span>
</pre></div></div></div>