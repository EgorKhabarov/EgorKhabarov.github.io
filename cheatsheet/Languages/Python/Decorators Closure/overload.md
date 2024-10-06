<h1>@overload</h1>
<p>Декоратор <code>@overload</code> позволяет описывать разные варианты вызова функций с конкретными типами параметров,
но его следует использовать вместе с одной фактической реализацией функции.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">overload</span>

<span class="k">class</span> <span class="nc">Calculator</span><span class="p">:</span>
    <span class="nd">@overload</span>
    <span class="k">def</span> <span class="nf">operate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">a</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span> <span class="nf">operate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">a</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span> <span class="o">...</span>

    <span class="k">def</span> <span class="nf">operate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">a</span><span class="p">):</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">a</span> <span class="o">*</span> <span class="mi">2</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">a</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>

<span class="n">calc</span> <span class="o">=</span> <span class="n">Calculator</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">calc</span><span class="o">.</span><span class="n">operate</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>    <span class="c1"># 20</span>
<span class="nb">print</span><span class="p">(</span><span class="n">calc</span><span class="o">.</span><span class="n">operate</span><span class="p">(</span><span class="s2">&quot;abc&quot;</span><span class="p">))</span> <span class="c1"># ABC</span>
</pre></div></div></div>

<h2>__init__</h2>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">overload</span>

<span class="k">class</span> <span class="nc">Person</span><span class="p">:</span>
    <span class="nd">@overload</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">age</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span> <span class="o">...</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg</span><span class="p">):</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">arg</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">age</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">age</span> <span class="o">=</span> <span class="n">arg</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="kc">None</span>

<span class="n">p1</span> <span class="o">=</span> <span class="n">Person</span><span class="p">(</span><span class="s2">&quot;Alice&quot;</span><span class="p">)</span>
<span class="n">p2</span> <span class="o">=</span> <span class="n">Person</span><span class="p">(</span><span class="mi">30</span><span class="p">)</span>
</pre></div></div></div>