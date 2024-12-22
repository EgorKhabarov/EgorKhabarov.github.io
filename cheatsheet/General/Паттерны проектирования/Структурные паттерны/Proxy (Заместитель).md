<h1>Proxy (Заместитель)</h1>
<p><strong>Описание</strong>: Представляет собой объект-заместитель, который контролирует доступ к другому объекту.</p>
<p><strong>Когда использовать</strong>: Когда нужно управлять доступом к объекту, например, для ленивой инициализации, контроля доступа или логирования.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">RealSubject</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">request</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;RealSubject: Handling request.&quot;</span>

<span class="k">class</span> <span class="nc">Proxy</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">real_subject</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_real_subject</span> <span class="o">=</span> <span class="n">real_subject</span>

    <span class="k">def</span> <span class="nf">request</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Proxy: Checking access before forwarding request.&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_subject</span><span class="o">.</span><span class="n">request</span><span class="p">()</span>

<span class="n">real_subject</span> <span class="o">=</span> <span class="n">RealSubject</span><span class="p">()</span>
<span class="n">proxy</span> <span class="o">=</span> <span class="n">Proxy</span><span class="p">(</span><span class="n">real_subject</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">proxy</span><span class="o">.</span><span class="n">request</span><span class="p">())</span>
<span class="c1"># Proxy: Checking access before forwarding request.</span>
<span class="c1"># RealSubject: Handling request.</span>
</pre></div></div></div>