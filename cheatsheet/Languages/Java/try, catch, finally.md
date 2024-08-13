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
    <div class="code"><div class="highlight"><pre><span></span><span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">ExceptionExample</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">try</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="kt">int</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">10</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w">  </span><span class="c1">// Это вызовет ArithmeticException</span>
<span class="w">        </span><span class="p">}</span><span class="w"> </span><span class="k">catch</span><span class="w"> </span><span class="p">(</span><span class="n">ArithmeticException</span><span class="w"> </span><span class="n">e</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Ошибка деления на ноль: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">e</span><span class="p">.</span><span class="na">getMessage</span><span class="p">());</span>
<span class="w">        </span><span class="p">}</span><span class="w"> </span><span class="k">finally</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Блок finally выполняется всегда.&quot;</span><span class="p">);</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div>
</div>

<h1>try-with-resources</h1>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">try</span><span class="w"> </span><span class="p">(</span><span class="n">BufferedReader</span><span class="w"> </span><span class="n">reader</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">BufferedReader</span><span class="p">(</span><span class="k">new</span><span class="w"> </span><span class="n">FileReader</span><span class="p">(</span><span class="s">&quot;file.txt&quot;</span><span class="p">)))</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">String</span><span class="w"> </span><span class="n">line</span><span class="p">;</span>
<span class="w">    </span><span class="k">while</span><span class="w"> </span><span class="p">((</span><span class="n">line</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">reader</span><span class="p">.</span><span class="na">readLine</span><span class="p">())</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="kc">null</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">line</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span><span class="w"> </span><span class="k">catch</span><span class="w"> </span><span class="p">(</span><span class="n">IOException</span><span class="w"> </span><span class="n">e</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">e</span><span class="p">.</span><span class="na">printStackTrace</span><span class="p">();</span>
<span class="p">}</span>
</pre></div></div>
</div>

<h2>Без круглых скобочек</h2>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="n">BufferedReader</span><span class="w"> </span><span class="n">reader</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="kc">null</span><span class="p">;</span>
<span class="k">try</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">reader</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">BufferedReader</span><span class="p">(</span><span class="k">new</span><span class="w"> </span><span class="n">FileReader</span><span class="p">(</span><span class="s">&quot;file.txt&quot;</span><span class="p">));</span>
<span class="w">    </span><span class="n">String</span><span class="w"> </span><span class="n">line</span><span class="p">;</span>
<span class="w">    </span><span class="k">while</span><span class="w"> </span><span class="p">((</span><span class="n">line</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">reader</span><span class="p">.</span><span class="na">readLine</span><span class="p">())</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="kc">null</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">line</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span><span class="w"> </span><span class="k">catch</span><span class="w"> </span><span class="p">(</span><span class="n">IOException</span><span class="w"> </span><span class="n">e</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">e</span><span class="p">.</span><span class="na">printStackTrace</span><span class="p">();</span>
<span class="p">}</span><span class="w"> </span><span class="k">finally</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">reader</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="kc">null</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">try</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">reader</span><span class="p">.</span><span class="na">close</span><span class="p">();</span>
<span class="w">        </span><span class="p">}</span><span class="w"> </span><span class="k">catch</span><span class="w"> </span><span class="p">(</span><span class="n">IOException</span><span class="w"> </span><span class="n">e</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">e</span><span class="p">.</span><span class="na">printStackTrace</span><span class="p">();</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div>
</div>