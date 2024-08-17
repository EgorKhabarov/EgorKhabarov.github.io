<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">def</span> <span class="nf">im</span><span class="p">():</span>
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
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">importlib</span>

<span class="n">importlib</span><span class="o">.</span><span class="n">reload</span><span class="p">(</span><span class="n">my_module</span><span class="p">)</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>
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