<h1>Observer (Наблюдатель)</h1>
<p><strong>Описание</strong>: Определяет зависимость один ко многим между объектами,
так что при изменении состояния одного объекта все зависимые объекты уведомляются и обновляются автоматически.</p>
<p><strong>Когда использовать</strong>: Когда изменение состояния одного объекта требует обновления других объектов,
и вы не хотите, чтобы объекты были жестко связаны.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Observer</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">ConcreteObserver</span><span class="p">(</span><span class="n">Observer</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Received message: </span><span class="si">{</span><span class="n">message</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Subject</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_observers</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span> <span class="nf">add_observer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">observer</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_observers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">observer</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">remove_observer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">observer</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_observers</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">observer</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">notify_observers</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">observer</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_observers</span><span class="p">:</span>
            <span class="n">observer</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>


<span class="n">subject</span> <span class="o">=</span> <span class="n">Subject</span><span class="p">()</span>
<span class="n">subject</span><span class="o">.</span><span class="n">add_observer</span><span class="p">(</span><span class="n">ConcreteObserver</span><span class="p">())</span>
<span class="n">subject</span><span class="o">.</span><span class="n">add_observer</span><span class="p">(</span><span class="n">ConcreteObserver</span><span class="p">())</span>
<span class="n">subject</span><span class="o">.</span><span class="n">notify_observers</span><span class="p">(</span><span class="s2">&quot;Hello Observers!&quot;</span><span class="p">)</span>
<span class="c1"># Received message: Hello Observers!</span>
<span class="c1"># Received message: Hello Observers!</span>
</pre></div></div></div>