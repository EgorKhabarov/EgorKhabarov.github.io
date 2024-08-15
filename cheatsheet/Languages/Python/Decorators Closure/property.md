<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Student</span><span class="p">:</span>
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
<span class="nb">print</span><span class="p">(</span><span class="n">user1</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>  <span class="c1"># 0</span>
<span class="n">user1</span><span class="o">.</span><span class="n">score</span> <span class="o">=</span> <span class="mi">1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">user1</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>  <span class="c1"># 1</span>
<span class="n">user1</span><span class="o">.</span><span class="n">_score</span> <span class="o">=</span> <span class="mi">999</span>
<span class="nb">print</span><span class="p">(</span><span class="n">user1</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>  <span class="c1"># 999</span>
<span class="n">user1</span><span class="o">.</span><span class="n">score</span> <span class="o">=</span> <span class="mi">999</span>
<span class="nb">print</span><span class="p">(</span><span class="n">user1</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>  <span class="c1"># ValueError</span>
</pre></div></div></div>