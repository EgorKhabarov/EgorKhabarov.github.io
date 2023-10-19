<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code458b" onclick="copyCode(code458, code458b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code458"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">cached_property</span>


<span class="k">class</span> <span class="nc">Circle</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">radius</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">radius</span> <span class="o">=</span> <span class="n">radius</span>

    <span class="nd">@cached_property</span>
    <span class="k">def</span> <span class="nf">area</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="mf">3.14</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">radius</span> <span class="o">**</span> <span class="mi">2</span>


<span class="n">circle</span> <span class="o">=</span> <span class="n">Circle</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">circle</span><span class="o">.</span><span class="n">area</span><span class="p">)</span>
<span class="c1"># напечатает 314.0</span>
<span class="nb">print</span><span class="p">(</span><span class="n">circle</span><span class="o">.</span><span class="n">area</span><span class="p">)</span>
<span class="c1"># вернет кешированное значение 314.0 без вычислений</span>
</pre></div></div></div>