<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="n">chr_digit</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;0&quot;</span><span class="p">,</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span> <span class="s2">&quot;3&quot;</span><span class="p">,</span> <span class="s2">&quot;4&quot;</span><span class="p">,</span> <span class="s2">&quot;5&quot;</span><span class="p">,</span> <span class="s2">&quot;6&quot;</span><span class="p">,</span> <span class="s2">&quot;7&quot;</span><span class="p">,</span> <span class="s2">&quot;8&quot;</span><span class="p">,</span> <span class="s2">&quot;9&quot;</span><span class="p">]</span>


<span class="k">def</span> <span class="nf">number_to_string</span><span class="p">(</span><span class="n">number</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">number</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">&quot;0&quot;</span>
    <span class="n">sign</span> <span class="o">=</span> <span class="s2">&quot;-&quot;</span> <span class="k">if</span> <span class="n">number</span> <span class="o">&lt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="s2">&quot;&quot;</span>
    <span class="n">number</span> <span class="o">=</span> <span class="nb">abs</span><span class="p">(</span><span class="n">number</span><span class="p">)</span>
    <span class="n">digits</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">while</span> <span class="n">number</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">digit</span> <span class="o">=</span> <span class="n">number</span> <span class="o">%</span> <span class="mi">10</span>
        <span class="n">digits</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">chr_digit</span><span class="p">[</span><span class="n">digit</span><span class="p">])</span>
        <span class="n">number</span> <span class="o">//=</span> <span class="mi">10</span>
    <span class="n">digits</span><span class="o">.</span><span class="n">reverse</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">sign</span> <span class="o">+</span> <span class="s2">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">digits</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">string_to_number</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">string</span> <span class="o">==</span> <span class="s2">&quot;0&quot;</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">0</span>
    <span class="n">sign</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="k">if</span> <span class="n">string</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;-&quot;</span><span class="p">:</span>
        <span class="n">sign</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
        <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
    <span class="n">number</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">char</span> <span class="ow">in</span> <span class="n">string</span><span class="p">:</span>
        <span class="n">digit</span> <span class="o">=</span> <span class="n">chr_digit</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">char</span><span class="p">)</span>
        <span class="n">number</span> <span class="o">=</span> <span class="n">number</span> <span class="o">*</span> <span class="mi">10</span> <span class="o">+</span> <span class="n">digit</span>
    <span class="k">return</span> <span class="n">sign</span> <span class="o">*</span> <span class="n">number</span>
</pre></div></div></div>
<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="n">number_to_string</span><span class="p">(</span><span class="mi">12345</span><span class="p">))</span>
<span class="unselectable"><span class="go">&quot;12345&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="nb">print</span><span class="p">(</span><span class="n">string_to_number</span><span class="p">(</span><span class="s2">&quot;12345&quot;</span><span class="p">))</span>
<span class="unselectable"><span class="go">12345</span>
</span></pre></div></div></div>