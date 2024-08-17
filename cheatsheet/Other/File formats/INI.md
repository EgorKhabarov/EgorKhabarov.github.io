<h1>INI (Initialization)</h1>
<p>формат конфигурационных файлов, который используется 
для хранения настроек приложений и операционных систем. 
Он был разработан в <code>Windows</code> и стал широко используемым 
форматом для хранения конфигурационных данных в различных программных продуктах.</p>
<div class="code-element"><div class="lang-line"><text>ini</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">[Section1]</span>
<span class="na">key1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">value1</span>
<span class="na">key2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">value2</span>

<span class="k">[Section2]</span>
<span class="na">key3</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">value3</span>
<span class="na">key4</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">value4</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="c1"># config = configparser.ConfigParser()</span>
<span class="c1"># config[&quot;BOT&quot;] = {&quot;bot_name&quot;: &quot;&quot;, &quot;token&quot;: &quot;&quot;}</span>

<span class="kn">import</span> <span class="nn">configparser</span>


<span class="n">config</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;BOT&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;bot_name&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span> <span class="s2">&quot;token&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">}}</span>
<span class="n">config_ini</span> <span class="o">=</span> <span class="n">configparser</span><span class="o">.</span><span class="n">ConfigParser</span><span class="p">()</span>

<span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">config</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
    <span class="n">config_ini</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;config.ini&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">config_ini</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

<span class="n">config_ini</span> <span class="o">=</span> <span class="n">configparser</span><span class="o">.</span><span class="n">ConfigParser</span><span class="p">()</span>
<span class="n">config_ini</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="s2">&quot;config.ini&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">config</span><span class="p">)</span>
</pre></div></div></div>