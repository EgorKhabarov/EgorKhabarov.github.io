<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code179b" onclick="copyCode(code179, code179b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code179"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Student</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_score</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">score</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_score</span>

    <span class="nd">@score</span><span class="o">.</span><span class="n">setter</span>
    <span class="k">def</span> <span class="nf">score</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">s</span><span class="p">):</span>
        <span class="k">if</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">s</span> <span class="o">&lt;=</span> <span class="mi">100</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_score</span> <span class="o">=</span> <span class="n">s</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span>

<span class="n">user1</span> <span class="o">=</span> <span class="n">Student</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">user1</span><span class="o">.</span><span class="n">score</span><span class="p">)</span> <span class="c1"># 0</span>
<span class="n">user1</span><span class="o">.</span><span class="n">score</span> <span class="o">=</span> <span class="mi">1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">user1</span><span class="o">.</span><span class="n">score</span><span class="p">)</span> <span class="c1"># 1</span>
<span class="n">user1</span><span class="o">.</span><span class="n">_score</span> <span class="o">=</span> <span class="mi">999</span>
<span class="nb">print</span><span class="p">(</span><span class="n">user1</span><span class="o">.</span><span class="n">score</span><span class="p">)</span> <span class="c1"># 999</span>
<span class="n">user1</span><span class="o">.</span><span class="n">score</span> <span class="o">=</span> <span class="mi">999</span>
<span class="nb">print</span><span class="p">(</span><span class="n">user1</span><span class="o">.</span><span class="n">score</span><span class="p">)</span> <span class="c1"># ValueError</span>
</pre></div></div></div>