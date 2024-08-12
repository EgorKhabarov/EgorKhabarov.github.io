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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">sqrt</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">p</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">):</span>
    <span class="k">return</span> <span class="nb">pow</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="p">(</span><span class="mi">1</span> <span class="o">/</span> <span class="n">p</span><span class="p">))</span>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">rgb_to_hex</span><span class="p">(</span><span class="n">r</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">g</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">b</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">return</span> <span class="s2">&quot;#</span><span class="si">{:02x}{:02x}{:02x}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">r</span><span class="p">,</span> <span class="n">g</span><span class="p">,</span> <span class="n">b</span><span class="p">)</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">hex_to_rgb</span><span class="p">(</span><span class="n">h</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]:</span>
    <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">h</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="s2">&quot;#&quot;</span><span class="p">)[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span> <span class="o">+</span> <span class="mi">2</span><span class="p">],</span> <span class="mi">16</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">))</span>
</pre></div></div>
</div>
<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">rgb_to_hex</span><span class="p">(</span><span class="mi">164</span><span class="p">,</span> <span class="mi">73</span><span class="p">,</span> <span class="mi">211</span><span class="p">)</span>
<span class="unselectable"><span class="go">&quot;#A449D3&quot;</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">hex_to_rgb</span><span class="p">(</span><span class="s2">&quot;#A449D3&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">(164, 73, 211)</span>
</span></pre></div></div>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">html_escape</span><span class="p">(</span><span class="n">text</span><span class="p">):</span>
    <span class="k">return</span> <span class="s2">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;&amp;#</span><span class="si">{</span><span class="nb">ord</span><span class="p">(</span><span class="n">char</span><span class="p">)</span><span class="si">}</span><span class="s2">;&quot;</span> <span class="k">for</span> <span class="n">char</span> <span class="ow">in</span> <span class="n">text</span><span class="p">)</span>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">tg_color</span><span class="p">(</span><span class="n">chat_id</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
<span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    0x6FB9F0 Синий</span>
<span class="sd">    0xFFD67E Оранжевый</span>
<span class="sd">    0xCB86DB Фиолетовый</span>
<span class="sd">    0x8EEE98 Зелёный</span>
<span class="sd">    0xFF93B2 Розовый</span>
<span class="sd">    0xFB6F5F Красный</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">return</span> <span class="p">{</span><span class="mi">0</span><span class="p">:</span> <span class="s2">&quot;К&quot;</span><span class="p">,</span> <span class="mi">1</span><span class="p">:</span> <span class="s2">&quot;О&quot;</span><span class="p">,</span> <span class="mi">2</span><span class="p">:</span> <span class="s2">&quot;Ф&quot;</span><span class="p">,</span> <span class="mi">3</span><span class="p">:</span> <span class="s2">&quot;З&quot;</span><span class="p">,</span> <span class="mi">4</span><span class="p">:</span> <span class="s2">&quot;Г&quot;</span><span class="p">,</span> <span class="mi">5</span><span class="p">:</span> <span class="s2">&quot;С&quot;</span><span class="p">,</span> <span class="mi">6</span><span class="p">:</span> <span class="s2">&quot;Р&quot;</span><span class="p">}[</span><span class="nb">abs</span><span class="p">(</span><span class="n">chat_id</span><span class="p">)</span> <span class="o">%</span> <span class="mi">7</span><span class="p">]</span>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">unicode</span><span class="p">(</span><span class="n">text</span><span class="p">):</span>
    <span class="k">return</span> <span class="s2">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="sa">fr</span><span class="s2">&quot;\U</span><span class="si">{</span><span class="nb">ord</span><span class="p">(</span><span class="n">char</span><span class="p">)</span><span class="si">:</span><span class="s2">0&gt;8x</span><span class="si">}</span><span class="s2">&quot;</span> <span class="k">for</span> <span class="n">char</span> <span class="ow">in</span> <span class="n">text</span><span class="p">)</span>
</pre></div></div>
</div>