<h1>TOML - Tom's Obvious, Minimal Language</h1>
<p>формат конфигурационных файлов, который был разработан
для использования в проектах, написанных на языке программирования <code>Rust</code>.</p>
<p>TOML файлы имеют структуру ключ-значение, где ключи и значения
разделены знаком <code>=</code>, и используют синтаксис, похожий на язык программирования <code>INI</code>.</p>
<div class="code-element"><div class="lang-line"><text>toml</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">[package]</span>
<span class="n">name</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;example&quot;</span>
<span class="n">version</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;1.0.0&quot;</span>
<span class="n">authors</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="s2">&quot;John Doe &lt;john@example.com&gt;&quot;</span><span class="p">]</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">toml</span>  <span class="c1"># pip install toml</span>


<span class="n">config</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;BOT&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;bot_name&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span> <span class="s2">&quot;token&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">}}</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;config.toml&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">toml</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">config</span><span class="p">))</span>
    <span class="c1"># toml.dump(config, file)</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;config.toml&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">config</span> <span class="o">=</span> <span class="n">toml</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="c1"># config = toml.loads(file.read())</span>

<span class="nb">print</span><span class="p">(</span><span class="n">config</span><span class="p">)</span>
</pre></div></div></div>