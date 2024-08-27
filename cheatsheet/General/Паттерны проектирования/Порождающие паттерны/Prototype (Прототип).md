<h1>Prototype (Прототип)</h1>
<p><strong>Описание</strong>: Позволяет создавать новые объекты путем копирования существующих экземпляров (прототипов).</p>
<p><strong>Когда использовать</strong>: Когда создание объектов дорогое или сложное, а также когда нужно избежать повторного выполнения инициализационного кода.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">copy</span>


<span class="k">class</span> <span class="nc">Prototype</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span>

    <span class="k">def</span> <span class="nf">clone</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>


<span class="n">prototype</span> <span class="o">=</span> <span class="n">Prototype</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>
<span class="n">clone</span> <span class="o">=</span> <span class="n">prototype</span><span class="o">.</span><span class="n">clone</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">clone</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>  <span class="c1"># 42</span>
</pre></div></div></div>