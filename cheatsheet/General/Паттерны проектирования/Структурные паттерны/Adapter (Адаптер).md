<h2>Adapter (Адаптер)</h2>
<p><strong>Описание:</strong> Преобразует интерфейс одного класса в интерфейс другого, который ожидает клиент.
Позволяет классам с несовместимыми интерфейсами работать вместе.</p>
<p><strong>Когда использовать:</strong> Когда необходимо использовать существующий класс, но его интерфейс не соответствует нужному.</p>
<p><strong>Пример реализации:</strong></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Adaptee</span><span class="p">:</span>
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