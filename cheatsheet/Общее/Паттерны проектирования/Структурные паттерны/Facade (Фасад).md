<h3>Facade (Фасад)</h3>
<p>Паттерн Фасад предоставляет унифицированный интерфейс к набору интерфейсов в подсистеме, упрощая использование сложных систем.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code998f8382ef6dc981af8c194465819f43b"onclick="copyCode(code998f8382ef6dc981af8c194465819f43, code998f8382ef6dc981af8c194465819f43b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code998f8382ef6dc981af8c194465819f43"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">CPU</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">freeze</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Freezing CPU&quot;</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">jump</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">position</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Jumping to </span><span class="si">{</span><span class="n">position</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">execute</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Executing instructions&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Memory</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">load</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">position</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Loading data from </span><span class="si">{</span><span class="n">position</span><span class="si">}</span><span class="s2"> to </span><span class="si">{</span><span class="n">data</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">HardDrive</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lba</span><span class="p">,</span> <span class="n">size</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Reading </span><span class="si">{</span><span class="n">size</span><span class="si">}</span><span class="s2"> bytes from LBA </span><span class="si">{</span><span class="n">lba</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="s2">&quot;data&quot;</span>

<span class="k">class</span> <span class="nc">ComputerFacade</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cpu</span> <span class="o">=</span> <span class="n">CPU</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">memory</span> <span class="o">=</span> <span class="n">Memory</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">hard_drive</span> <span class="o">=</span> <span class="n">HardDrive</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cpu</span><span class="o">.</span><span class="n">freeze</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">memory</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">hard_drive</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="mi">1024</span><span class="p">,</span> <span class="mi">4096</span><span class="p">))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cpu</span><span class="o">.</span><span class="n">jump</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">cpu</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>

<span class="c1"># Использование</span>
<span class="n">computer</span> <span class="o">=</span> <span class="n">ComputerFacade</span><span class="p">()</span>
<span class="n">computer</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</pre></div></div></div>