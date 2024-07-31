<h1>CSV - Comma Separated Values</h1>
<p>Текстовый формат файла, который используется для хранения табличных данных.
Каждая строка файла содержит одну запись, а значения в этой записи разделены запятыми.
Пример</p>
<div class="code-element">
<div class="lang-line">
  <text>csv</text>
  <button class="copy-button"
          id="code96358b76f05ee6843a293165ac60ecbdb"
          onclick="copyCode(code96358b76f05ee6843a293165ac60ecbd, code96358b76f05ee6843a293165ac60ecbdb)">
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
<div class="code" id="code96358b76f05ee6843a293165ac60ecbd"><div class="highlight"><pre><span></span><span class="n">Name</span><span class="p">,</span><span class="n">Age</span><span class="p">,</span><span class="n">City</span>
<span class="n">John</span> <span class="n">Smith</span><span class="p">,</span><span class="mi">30</span><span class="p">,</span><span class="n">New</span> <span class="n">York</span>
<span class="n">Jane</span> <span class="n">Doe</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="n">Chicago</span>
</pre></div></div>
</div>

<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codead2e1ba4617672b314e501ba8981e193b"
          onclick="copyCode(codead2e1ba4617672b314e501ba8981e193, codead2e1ba4617672b314e501ba8981e193b)">
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
<div class="code" id="codead2e1ba4617672b314e501ba8981e193"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">csv</span>
<span class="n">data</span> <span class="o">=</span> <span class="p">[[</span><span class="s2">&quot;Name&quot;</span><span class="p">,</span> <span class="s2">&quot;Age&quot;</span><span class="p">],</span> <span class="p">[</span><span class="s2">&quot;Alice&quot;</span><span class="p">,</span> <span class="mi">25</span><span class="p">],</span> <span class="p">[</span><span class="s2">&quot;Bob&quot;</span><span class="p">,</span> <span class="mi">30</span><span class="p">],</span> <span class="p">[</span><span class="s2">&quot;Charlie&quot;</span><span class="p">,</span> <span class="mi">35</span><span class="p">]]</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;data.csv&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">,</span> <span class="n">newline</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">csv</span><span class="o">.</span><span class="n">writer</span><span class="p">(</span><span class="n">file</span><span class="p">)</span><span class="o">.</span><span class="n">writerows</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;data.csv&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="p">[</span><span class="nb">print</span><span class="p">(</span><span class="n">row</span><span class="p">)</span> <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">csv</span><span class="o">.</span><span class="n">reader</span><span class="p">(</span><span class="n">file</span><span class="p">)]</span>
</pre></div></div>
</div>