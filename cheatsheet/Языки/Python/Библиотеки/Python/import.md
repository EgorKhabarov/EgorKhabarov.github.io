<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-button" id="code5b0859c2e7b8e88b84f29c50d7e5de50b" onclick="copyCode(code5b0859c2e7b8e88b84f29c50d7e5de50, code5b0859c2e7b8e88b84f29c50d7e5de50b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code5b0859c2e7b8e88b84f29c50d7e5de50"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">def</span> <span class="nf">im</span><span class="p">():</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="kn">import</span> <span class="nn">math</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">math</span>
<span class="unselectable"><span class="gt">Traceback (most recent call last):</span></span>
<span class="unselectable">  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span></span>
<span class="unselectable"><span class="gr">NameError</span>: <span class="n">name &#39;math&#39; is not defined</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">im</span><span class="p">()</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">math</span>
<span class="unselectable"><span class="gt">Traceback (most recent call last):</span></span>
<span class="unselectable">  File <span class="nb">&quot;&lt;stdin&gt;&quot;</span>, line <span class="m">1</span>, in <span class="n">&lt;module&gt;</span></span>
<span class="unselectable"><span class="gr">NameError</span>: <span class="n">name &#39;math&#39; is not defined</span></span>
<span class="unselectable"></pre></div></span></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code801beed0075836aa1a043f68a986eacfb" onclick="copyCode(code801beed0075836aa1a043f68a986eacf, code801beed0075836aa1a043f68a986eacfb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code801beed0075836aa1a043f68a986eacf"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">importlib</span>

<span class="n">importlib</span><span class="o">.</span><span class="n">reload</span><span class="p">(</span><span class="n">my_module</span><span class="p">)</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codea904572390984dd020cfe0a2c5625ca7b" onclick="copyCode(codea904572390984dd020cfe0a2c5625ca7, codea904572390984dd020cfe0a2c5625ca7b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codea904572390984dd020cfe0a2c5625ca7"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>
<span class="kn">import</span> <span class="nn">importlib</span>

<span class="n">library_name</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Введите название библиотеки, которую вы хотите установить: &quot;</span><span class="p">)</span>

<span class="c1"># проверяем, установлена ли библиотека</span>
<span class="k">try</span><span class="p">:</span>
    <span class="n">importlib</span><span class="o">.</span><span class="n">import_module</span><span class="p">(</span><span class="n">library_name</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Библиотека </span><span class="si">{</span><span class="n">library_name</span><span class="si">}</span><span class="s2"> уже установлена.&quot;</span><span class="p">)</span>
<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
    <span class="c1"># устанавливаем библиотеку</span>
    <span class="n">subprocess</span><span class="o">.</span><span class="n">call</span><span class="p">([</span><span class="s2">&quot;pip&quot;</span><span class="p">,</span> <span class="s2">&quot;install&quot;</span><span class="p">,</span> <span class="n">library_name</span><span class="p">])</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Библиотека </span><span class="si">{</span><span class="n">library_name</span><span class="si">}</span><span class="s2"> установлена успешно.&quot;</span><span class="p">)</span>
</pre></div></div></div>