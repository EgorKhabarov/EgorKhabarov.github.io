<h3>Builder (Строитель)</h3>
<p>Паттерн Строитель используется для пошагового создания сложных объектов.
Он отделяет конструирование объекта от его представления,
так что один и тот же процесс создания может создавать разные представления.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">House</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">walls</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">roof</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">doors</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;Walls: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="si">}</span><span class="s2">, Roof: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">roof</span><span class="si">}</span><span class="s2">, Doors: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">doors</span><span class="si">}</span><span class="s2">&quot;</span>

<span class="k">class</span> <span class="nc">HouseBuilder</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">house</span> <span class="o">=</span> <span class="n">House</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">build_walls</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">walls</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">house</span><span class="o">.</span><span class="n">walls</span> <span class="o">=</span> <span class="n">walls</span>
        <span class="k">return</span> <span class="bp">self</span>

    <span class="k">def</span> <span class="nf">build_roof</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">roof</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">house</span><span class="o">.</span><span class="n">roof</span> <span class="o">=</span> <span class="n">roof</span>
        <span class="k">return</span> <span class="bp">self</span>

    <span class="k">def</span> <span class="nf">build_doors</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doors</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">house</span><span class="o">.</span><span class="n">doors</span> <span class="o">=</span> <span class="n">doors</span>
        <span class="k">return</span> <span class="bp">self</span>

    <span class="k">def</span> <span class="nf">get_house</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">house</span>

<span class="c1"># Использование</span>
<span class="n">builder</span> <span class="o">=</span> <span class="n">HouseBuilder</span><span class="p">()</span>
<span class="n">house</span> <span class="o">=</span> <span class="n">builder</span><span class="o">.</span><span class="n">build_walls</span><span class="p">(</span><span class="s2">&quot;Brick walls&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">build_roof</span><span class="p">(</span><span class="s2">&quot;Tile roof&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">build_doors</span><span class="p">(</span><span class="s2">&quot;Wooden doors&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">get_house</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">house</span><span class="p">)</span>
</pre></div></div>
</div>