<div class="code-element"><div class="lang-line"><text>python-console</text><button class="copy-button" id="code487b" onclick="copyCode(code487, code487b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code487"><div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="k">def</span> <span class="nf">im</span><span class="p">():</span> <span class="kn">import</span> <span class="nn">math</span>
<span class="o">...</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">math</span>
<span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
  <span class="n">File</span> <span class="s2">&quot;&lt;stdin&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
<span class="ne">NameError</span><span class="p">:</span> <span class="n">name</span> <span class="s1">&#39;math&#39;</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">defined</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">im</span><span class="p">()</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">math</span>
<span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
  <span class="n">File</span> <span class="s2">&quot;&lt;stdin&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
<span class="ne">NameError</span><span class="p">:</span> <span class="n">name</span> <span class="s1">&#39;math&#39;</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">defined</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code488b" onclick="copyCode(code488, code488b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code488"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">importlib</span>

<span class="n">importlib</span><span class="o">.</span><span class="n">reload</span><span class="p">(</span><span class="n">my_module</span><span class="p">)</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code489b" onclick="copyCode(code489, code489b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code489"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>
<span class="kn">import</span> <span class="nn">importlib</span>

<span class="n">library_name</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Введите название библиотеки, которую вы хотите установить: &quot;</span><span class="p">)</span>

<span class="c1"># проверяем, установлена ли библиотека</span>
<span class="k">try</span><span class="p">:</span>
    <span class="n">importlib</span><span class="o">.</span><span class="n">import_module</span><span class="p">(</span><span class="n">library_name</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Библиотека </span><span class="si">{</span><span class="n">library_name</span><span class="si">}</span><span class="s2"> уже установлена.&quot;</span><span class="p">)</span>
<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
    <span class="c1"># устанавливаем библиотеку</span>
    <span class="n">subprocess</span><span class="o">.</span><span class="n">call</span><span class="p">([</span><span class="s1">&#39;pip&#39;</span><span class="p">,</span> <span class="s1">&#39;install&#39;</span><span class="p">,</span> <span class="n">library_name</span><span class="p">])</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Библиотека </span><span class="si">{</span><span class="n">library_name</span><span class="si">}</span><span class="s2"> установлена успешно.&quot;</span><span class="p">)</span>
</pre></div></div></div>