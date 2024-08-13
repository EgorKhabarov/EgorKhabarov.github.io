<h2>Observer (Наблюдатель)</h2>
<p><strong>Описание:</strong> Определяет зависимость <strong>один-ко-многим</strong> между объектами таким образом,
что при <strong>изменении состояния одного объекта все зависимые объекты уведомляются и обновляются автоматически</strong>.</p>
<p><strong>Когда использовать:</strong> Когда изменение состояния одного объекта должно привести к изменению состояния других объектов,
например, в системах событий или уведомлений.</p>
<p><strong>Пример реализации:</strong></p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Subject</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_observers</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span> <span class="nf">attach</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">observer</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_observers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">observer</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">detach</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">observer</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_observers</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">observer</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">notify</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">observer</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_observers</span><span class="p">:</span>
            <span class="n">observer</span><span class="o">.</span><span class="n">update</span><span class="p">()</span>

<span class="k">class</span> <span class="nc">ConcreteObserver</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">update</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Observer updated&quot;</span><span class="p">)</span>

<span class="n">subject</span> <span class="o">=</span> <span class="n">Subject</span><span class="p">()</span>
<span class="n">observer</span> <span class="o">=</span> <span class="n">ConcreteObserver</span><span class="p">()</span>
<span class="n">subject</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="n">observer</span><span class="p">)</span>
<span class="n">subject</span><span class="o">.</span><span class="n">notify</span><span class="p">()</span>  <span class="c1"># Вывод: &quot;Observer updated&quot;</span>
</pre></div></div>
</div>