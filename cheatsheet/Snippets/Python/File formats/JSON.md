<h1>JSON - JavaScript Object Notation</h1>
<p>Tекстовый формат обмена данными, который основан на синтаксисе JavaScript.
Он используется для хранения и обмена структурированными данными и часто используется
в веб-приложениях для обмена данными между клиентом и сервером.</p>
<div class="code_element"><div class="lang_line"><text>json</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-json"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">    </span><span class="nt">&quot;name&quot;</span><span class="p">:</span><span class="w"> </span><span class="s2">&quot;John Smith&quot;</span><span class="p">,</span>
<span class="w">    </span><span class="nt">&quot;age&quot;</span><span class="p">:</span><span class="w"> </span><span class="mi">30</span><span class="p">,</span>
<span class="w">    </span><span class="nt">&quot;city&quot;</span><span class="p">:</span><span class="w"> </span><span class="s2">&quot;New York&quot;</span>
<span class="p">}</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">json</span>


<span class="n">config</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;BOT&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;bot_name&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span> <span class="s2">&quot;token&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">}}</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;config.json&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">config</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="o">=</span><span class="kc">False</span><span class="p">))</span>
    <span class="c1"># json.dump(config, file, indent=4, ensure_ascii=False)</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;config.json&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">config</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="c1"># config = json.loads(file.read())</span>

<span class="nb">print</span><span class="p">(</span><span class="n">config</span><span class="p">)</span>
</pre></div></div></div>

<h1>JSONL</h1>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Alice Jones&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">25</span><span class="p">,</span> <span class="s2">&quot;city&quot;</span><span class="p">:</span> <span class="s2">&quot;Los Angeles&quot;</span><span class="p">}</span>
<span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;John Smith&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">30</span><span class="p">,</span> <span class="s2">&quot;city&quot;</span><span class="p">:</span> <span class="s2">&quot;New York&quot;</span><span class="p">}</span>
<span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Bob Johnson&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">40</span><span class="p">,</span> <span class="s2">&quot;city&quot;</span><span class="p">:</span> <span class="s2">&quot;Chicago&quot;</span><span class="p">}</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">json</span>


<span class="n">config</span> <span class="o">=</span> <span class="p">[</span>
    <span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Alice Jones&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">25</span><span class="p">,</span> <span class="s2">&quot;city&quot;</span><span class="p">:</span> <span class="s2">&quot;Los Angeles&quot;</span><span class="p">},</span>
    <span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;John Smith&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">30</span><span class="p">,</span> <span class="s2">&quot;city&quot;</span><span class="p">:</span> <span class="s2">&quot;New York&quot;</span><span class="p">},</span>
    <span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Bob Johnson&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">40</span><span class="p">,</span> <span class="s2">&quot;city&quot;</span><span class="p">:</span> <span class="s2">&quot;Chicago&quot;</span><span class="p">},</span>
<span class="p">]</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;test.jsonl&quot;</span><span class="p">,</span> <span class="s2">&quot;a&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">file</span><span class="o">.</span><span class="n">writelines</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">line</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">config</span><span class="p">])</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;config.jsonl&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;UTF-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">file</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">line</span><span class="p">))</span>
</pre></div></div></div>

<p><a target="_self" href="?Snippets/Python/File formats/TinyDB (json).md" class="wikilink">TinyDB (json)</a></p>