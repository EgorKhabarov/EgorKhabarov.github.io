<h1>YAML - Ain't Markup Language</h1>
<p>Формат файлов, который используется для хранения и обмена неструктурированными и структурированными
данными. Например он популярен в файлах настройки приложений, описание конфигураций и т.д.
<code>YAML</code> использует отступы и специальные символы для обозначения структуры данных.
Он также поддерживает множество типов данных, включая строки, числа, логические значения и массивы.</p>
<div class="code_element"><div class="lang_line"><text>yaml</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-yaml"><div class="highlight"><pre><span></span><span class="nt">name</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">John Smith</span>
<span class="nt">age</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">30</span>
<span class="nt">city</span><span class="p">:</span><span class="w"> </span><span class="l l-Scalar l-Scalar-Plain">New York</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">yaml</span>  <span class="c1"># pip install yaml</span>


<span class="n">config</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;BOT&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;bot_name&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span> <span class="s2">&quot;token&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">}}</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;config.yaml&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;utf-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">yaml</span><span class="o">.</span><span class="n">safe_dump</span><span class="p">(</span><span class="n">config</span><span class="p">,</span> <span class="n">sort_keys</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">allow_unicode</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">))</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;config.yaml&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;utf-8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">config</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="n">file</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>

<span class="nb">print</span><span class="p">(</span><span class="n">config</span><span class="p">)</span>
</pre></div></div></div>