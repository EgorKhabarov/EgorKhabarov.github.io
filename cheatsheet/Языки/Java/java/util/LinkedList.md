<div class="code-element">
    <div class="lang-line">
        <text>java</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">java.util.LinkedList</span><span class="p">;</span>

<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">LinkedListExample</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">LinkedList</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span><span class="w"> </span><span class="n">list</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">LinkedList</span><span class="o">&lt;&gt;</span><span class="p">();</span>
<span class="w">        </span><span class="n">list</span><span class="p">.</span><span class="na">add</span><span class="p">(</span><span class="s">&quot;Red&quot;</span><span class="p">);</span>
<span class="w">        </span><span class="n">list</span><span class="p">.</span><span class="na">add</span><span class="p">(</span><span class="s">&quot;Green&quot;</span><span class="p">);</span>
<span class="w">        </span><span class="n">list</span><span class="p">.</span><span class="na">add</span><span class="p">(</span><span class="s">&quot;Blue&quot;</span><span class="p">);</span>
<span class="w">        </span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">String</span><span class="w"> </span><span class="n">color</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">list</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">color</span><span class="p">);</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div>
</div>