<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="n">list_of_tuples</span> <span class="o">=</span> <span class="p">[(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">),</span> <span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">)]</span>
<span class="n">result_list</span> <span class="o">=</span> <span class="p">[</span>
    <span class="n">item</span>
    <span class="k">for</span> <span class="n">tpl</span> <span class="ow">in</span> <span class="n">list_of_tuples</span>
    <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">tpl</span>
<span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result_list</span><span class="p">)</span>
<span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">]</span>
</pre></div></div>
</div>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="n">list_of_tuples</span> <span class="o">=</span> <span class="p">[(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">),</span> <span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">)]</span>
<span class="n">result_list</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">tpl</span> <span class="ow">in</span> <span class="n">list_of_tuples</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">tpl</span><span class="p">:</span>
        <span class="n">result_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">result_list</span><span class="p">)</span>
<span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">]</span>
</pre></div></div>
</div>