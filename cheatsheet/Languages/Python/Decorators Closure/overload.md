<p><code>@overload</code> - это декоратор в Python, который используется для определения перегрузки метода внутри класса. 
Перегрузка метода - это механизм, позволяющий определить несколько версий метода с разными параметрами. 
При вызове метода, интерпретатор Python выберет версию метода, которая соответствует переданным аргументам.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">overload</span>

<span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="nd">@overload</span>
    <span class="k">def</span> <span class="nf">my_method</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg1</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="nd">@overload</span>
    <span class="k">def</span> <span class="nf">my_method</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg1</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">my_method</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg1</span><span class="p">):</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg1</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">arg1</span> <span class="o">*</span> <span class="mi">2</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg1</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">arg1</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>


<span class="n">obj</span> <span class="o">=</span> <span class="n">MyClass</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="n">my_method</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>        <span class="c1"># 4</span>
<span class="nb">print</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="n">my_method</span><span class="p">(</span><span class="s2">&quot;hello&quot;</span><span class="p">))</span>  <span class="c1"># HELLO</span>
</pre></div></div></div>