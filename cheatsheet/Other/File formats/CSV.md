<h1>CSV - Comma Separated Values</h1>
<p>Текстовый формат файла, который используется для хранения табличных данных.
Каждая строка файла содержит одну запись, а значения в этой записи разделены запятыми.</p>
<div class="code-element"><div class="lang-line"><text>csv</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="n">Name</span><span class="p">,</span><span class="n">Age</span><span class="p">,</span><span class="n">City</span>
<span class="n">John</span> <span class="n">Smith</span><span class="p">,</span><span class="mi">30</span><span class="p">,</span><span class="n">New</span> <span class="n">York</span>
<span class="n">Jane</span> <span class="n">Doe</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="n">Chicago</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">csv</span>


<span class="n">data</span> <span class="o">=</span> <span class="p">[</span>
    <span class="p">(</span><span class="s2">&quot;Name&quot;</span><span class="p">,</span> <span class="s2">&quot;Age&quot;</span><span class="p">),</span>
    <span class="p">(</span><span class="s2">&quot;Alice&quot;</span><span class="p">,</span> <span class="mi">25</span><span class="p">),</span>
    <span class="p">(</span><span class="s2">&quot;Bob&quot;</span><span class="p">,</span> <span class="mi">30</span><span class="p">),</span>
    <span class="p">(</span><span class="s2">&quot;Charlie&quot;</span><span class="p">,</span> <span class="mi">35</span><span class="p">),</span>
<span class="p">]</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;data.csv&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">,</span> <span class="n">newline</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">csv</span><span class="o">.</span><span class="n">writer</span><span class="p">(</span><span class="n">file</span><span class="p">)</span><span class="o">.</span><span class="n">writerows</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;data.csv&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">csv</span><span class="o">.</span><span class="n">reader</span><span class="p">(</span><span class="n">file</span><span class="p">)))</span>
</pre></div></div></div>