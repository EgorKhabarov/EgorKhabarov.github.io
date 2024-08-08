<p>Me:</p>
<blockquote>
<p>Можешь переписать этот код на C++?</p>
<p><div class="code-element">
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
</button></p>
</blockquote>
<div class="codehilite"><pre><span></span><code><span class="nt">&lt;/div&gt;</span>
<span class="nt">&lt;div</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;code&quot;</span><span class="nt">&gt;&lt;div</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;highlight&quot;</span><span class="nt">&gt;&lt;pre&gt;&lt;span&gt;&lt;/span&gt;&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;n&quot;</span><span class="nt">&gt;</span>a<span class="nt">&lt;/span&gt;</span><span class="w"> </span><span class="nt">&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;o&quot;</span><span class="nt">&gt;</span>=<span class="nt">&lt;/span&gt;</span><span class="w"> </span><span class="nt">&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;p&quot;</span><span class="nt">&gt;</span>[<span class="nt">&lt;/span&gt;&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;mi&quot;</span><span class="nt">&gt;</span>0<span class="nt">&lt;/span&gt;&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;p&quot;</span><span class="nt">&gt;</span>,<span class="nt">&lt;/span&gt;</span><span class="w"> </span><span class="nt">&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;mi&quot;</span><span class="nt">&gt;</span>1<span class="nt">&lt;/span&gt;&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;p&quot;</span><span class="nt">&gt;</span>,<span class="nt">&lt;/span&gt;</span><span class="w"> </span><span class="nt">&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;s2&quot;</span><span class="nt">&gt;</span><span class="ni">&amp;quot;</span>привет<span class="ni">&amp;quot;</span><span class="nt">&lt;/span&gt;&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;p&quot;</span><span class="nt">&gt;</span>,<span class="nt">&lt;/span&gt;</span><span class="w"> </span><span class="nt">&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;s2&quot;</span><span class="nt">&gt;</span><span class="ni">&amp;quot;</span>мир<span class="ni">&amp;quot;</span><span class="nt">&lt;/span&gt;&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;p&quot;</span><span class="nt">&gt;</span>]<span class="nt">&lt;/span&gt;</span>
</code></pre></div>

<p><span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span> <span class="n">a</span><span class="p">[</span><span class="mi">3</span><span class="p">])</span>
</pre></div></div>
</div></p>
<hr />
<p>ChatGPT:</p>
<blockquote>
<p>Да, я могу переписать этот код на C++:</p>
<p><div class="code-element">
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
</button></p>
</blockquote>
<div class="codehilite"><pre><span></span><code><span class="nt">&lt;/div&gt;</span>
<span class="nt">&lt;div</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;code&quot;</span><span class="nt">&gt;&lt;div</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;highlight&quot;</span><span class="nt">&gt;&lt;pre&gt;&lt;span&gt;&lt;/span&gt;&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;cp&quot;</span><span class="nt">&gt;</span>#include<span class="nt">&lt;/span&gt;&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;w&quot;</span><span class="nt">&gt;</span><span class="w"> </span><span class="nt">&lt;/span&gt;&lt;span</span><span class="w"> </span><span class="na">class=</span><span class="s">&quot;cpf&quot;</span><span class="nt">&gt;</span><span class="ni">&amp;lt;</span>iostream<span class="ni">&amp;gt;</span><span class="nt">&lt;/span&gt;</span>
</code></pre></div>

<p><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>
<span class="w"> </span>
<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="o">&gt;</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="s">&quot;0&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;1&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;привет&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;мир&quot;</span><span class="w"> </span><span class="p">};</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">a</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">a</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div></div>
</div></p>
<blockquote>
<p>Здесь я использовал std::vector, чтобы создать массив строк, 
поскольку C++ не поддерживает нетипизированные массивы.</p>
</blockquote>