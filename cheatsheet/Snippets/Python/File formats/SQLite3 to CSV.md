<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sqlite3</span>
<span class="kn">import</span> <span class="nn">csv</span>

<span class="k">def</span> <span class="nf">SQL</span><span class="p">(</span><span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="nb">tuple</span> <span class="o">|</span> <span class="nb">dict</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">commit</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">column_names</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
<span class="w">    </span><span class="sd">&quot;&quot;&quot;Выполняет SQL запрос&quot;&quot;&quot;</span>
    <span class="k">with</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;database.sqlite&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">connection</span><span class="p">:</span>
        <span class="n">cursor</span> <span class="o">=</span> <span class="n">connection</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span>
        <span class="n">cursor</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">params</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">commit</span><span class="p">:</span> <span class="n">connection</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">cursor</span><span class="o">.</span><span class="n">fetchall</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">column_names</span> <span class="ow">and</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">cursor</span><span class="p">,</span> <span class="s2">&quot;description&quot;</span><span class="p">):</span>
            <span class="n">column_names_data</span> <span class="o">=</span> <span class="p">[</span><span class="n">column</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">column</span> <span class="ow">in</span> <span class="n">cursor</span><span class="o">.</span><span class="n">description</span><span class="p">]</span> <span class="ow">or</span> <span class="kc">None</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">column_names_data</span> <span class="o">+</span> <span class="n">result</span>
    <span class="k">return</span> <span class="n">result</span>

<span class="n">data</span> <span class="o">=</span> <span class="n">SQL</span><span class="p">(</span><span class="s2">&quot;SELECT * FROM table_name;&quot;</span><span class="p">)</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;data.csv&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">,</span> <span class="n">newline</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">writer</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">writer</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="n">writer</span><span class="o">.</span><span class="n">writerows</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;data.csv&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">reader</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">reader</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="n">column_names</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span><span class="n">reader</span><span class="p">)</span>
    <span class="n">SQL</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">&quot;&quot;&quot;</span>
<span class="s2">CREATE TABLE table_name (</span>
<span class="s2">    </span><span class="si">{</span><span class="s2">&quot;, &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">column</span><span class="si">}</span><span class="s2"> TEXT&quot;</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">column</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">column_names</span><span class="p">])</span><span class="si">}</span>
<span class="s2">);</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
        <span class="n">commit</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">reader</span><span class="p">:</span>
        <span class="n">SQL</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">&quot;&quot;&quot;</span>
<span class="s2">INSERT INTO table_name (</span>
<span class="s2">    </span><span class="si">{</span><span class="s2">&quot;, &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">column_names</span><span class="p">)</span><span class="si">}</span>
<span class="s2">)</span>
<span class="s2">VALUES (</span>
<span class="s2">    </span><span class="si">{</span><span class="s2">&quot;, &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;&quot;</span><span class="si">{</span><span class="n">column</span><span class="si">}</span><span class="s1">&quot;&#39;</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">column</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">row</span><span class="p">])</span><span class="si">}</span>
<span class="s2">)</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
            <span class="n">commit</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">);</span>
</pre></div></div></div>