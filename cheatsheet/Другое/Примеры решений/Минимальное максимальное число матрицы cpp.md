<div class="code-element">
    <div class="lang-line">
        <text>cpp</text>
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
        <button class="copy-button-2"
        onclick="DownloadCode(this, 'maxminmatrix.cpp')">
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
    <text>Download code</text>
</button>
    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;time.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iomanip&gt;</span>

<span class="k">using</span><span class="w"> </span><span class="k">namespace</span><span class="w"> </span><span class="nn">std</span><span class="p">;</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">rows</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">3</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">cols</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">4</span><span class="p">;</span>
<span class="w">    </span><span class="n">srand</span><span class="p">(</span><span class="n">time</span><span class="p">(</span><span class="nb">NULL</span><span class="p">));</span>
<span class="w">    </span><span class="n">vector</span><span class="o">&lt;</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;&gt;</span><span class="w"> </span><span class="n">matrix</span><span class="p">(</span><span class="n">rows</span><span class="p">,</span><span class="w"> </span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="n">cols</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">rows</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;|&quot;</span><span class="p">;</span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">cols</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">j</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="kt">int</span><span class="w"> </span><span class="n">number</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">rand</span><span class="p">()</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="mi">999</span><span class="p">;</span>
<span class="w">            </span><span class="n">matrix</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">number</span><span class="p">;</span>
<span class="w">            </span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">setw</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">setfill</span><span class="p">(</span><span class="s">&quot; &quot;</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">number</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; |&quot;</span><span class="p">;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">max</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">min</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">999</span><span class="p">;</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="k">auto</span><span class="w"> </span><span class="n">r</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">matrix</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="k">auto</span><span class="w"> </span><span class="n">c</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">r</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">c</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="n">max</span><span class="p">)</span><span class="w"> </span><span class="n">max</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">c</span><span class="p">;</span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">c</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">min</span><span class="p">)</span><span class="w"> </span><span class="n">min</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">c</span><span class="p">;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;max = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">max</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;min = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">min</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">;</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div></div>
</div>