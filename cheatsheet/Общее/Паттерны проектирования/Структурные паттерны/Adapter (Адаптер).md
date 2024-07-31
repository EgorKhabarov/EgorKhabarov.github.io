<h2>Adapter (Адаптер)</h2>
<p><strong>Описание:</strong> Преобразует интерфейс одного класса в интерфейс другого, который ожидает клиент.
Позволяет классам с несовместимыми интерфейсами работать вместе.</p>
<p><strong>Когда использовать:</strong> Когда необходимо использовать существующий класс, но его интерфейс не соответствует нужному.</p>
<p><strong>Пример реализации:</strong></p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codebfc54a0446b99eeb2b2b0dde73745ab0b" onclick="copyCode(codebfc54a0446b99eeb2b2b0dde73745ab0, codebfc54a0446b99eeb2b2b0dde73745ab0b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codebfc54a0446b99eeb2b2b0dde73745ab0"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Adaptee</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">specific_request</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;specific request&quot;</span>

<span class="k">class</span> <span class="nc">Target</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">request</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">Adapter</span><span class="p">(</span><span class="n">Target</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">adaptee</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_adaptee</span> <span class="o">=</span> <span class="n">adaptee</span>

    <span class="k">def</span> <span class="nf">request</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;Adapter: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_adaptee</span><span class="o">.</span><span class="n">specific_request</span><span class="p">()</span><span class="si">}</span><span class="s2">&quot;</span>

<span class="n">adaptee</span> <span class="o">=</span> <span class="n">Adaptee</span><span class="p">()</span>
<span class="n">adapter</span> <span class="o">=</span> <span class="n">Adapter</span><span class="p">(</span><span class="n">adaptee</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">adapter</span><span class="o">.</span><span class="n">request</span><span class="p">())</span>  <span class="c1"># Вывод: &quot;Adapter: specific request&quot;</span>
</pre></div></div></div>