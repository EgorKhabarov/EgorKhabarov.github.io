<h1>INI (Initialization)</h1>
<p>формат конфигурационных файлов, который используется 
для хранения настроек приложений и операционных систем. 
Он был разработан в Windows и стал широко используемым 
форматом для хранения конфигурационных данных в различных программных продуктах.
Пример</p>
<div class="code-element"><div class="lang-line"><text>ini</text><button class="copy-button" id="code776b" onclick="copyCode(code776, code776b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code776"><div class="highlight"><pre><span></span><span class="k">[Section1]</span>
<span class="na">key1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">value1</span>
<span class="na">key2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">value2</span>

<span class="k">[Section2]</span>
<span class="na">key3</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">value3</span>
<span class="na">key4</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">value4</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code777b" onclick="copyCode(code777, code777b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code777"><div class="highlight"><pre><span></span><span class="c1"># config = configparser.ConfigParser()</span>
<span class="c1"># config[&quot;BOT&quot;] = {&quot;bot_name&quot;: &quot;&quot;, &quot;token&quot;: &quot;&quot;}</span>

<span class="kn">import</span> <span class="nn">configparser</span>
<span class="n">config</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;BOT&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;bot_name&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span> <span class="s2">&quot;token&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">}}</span>
<span class="n">config_ini</span> <span class="o">=</span> <span class="n">configparser</span><span class="o">.</span><span class="n">ConfigParser</span><span class="p">()</span>
<span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">config</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
    <span class="n">config_ini</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;config.ini&quot;</span><span class="p">,</span> <span class="s1">&#39;w&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">config_ini</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

<span class="n">config_ini</span> <span class="o">=</span> <span class="n">configparser</span><span class="o">.</span><span class="n">ConfigParser</span><span class="p">()</span>
<span class="n">config_ini</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="s2">&quot;config.ini&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">config</span><span class="p">)</span>
</pre></div></div></div>