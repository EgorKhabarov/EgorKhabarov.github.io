<h2>Factory (Фабрика)</h2>
<p><strong>Описание:</strong> Предоставляет интерфейс для создания объектов в суперклассе,
но позволяет подклассам изменять тип создаваемых объектов.</p>
<p><strong>Когда использовать:</strong> Когда нужно делегировать создание объектов подклассам
или когда тип создаваемых объектов заранее неизвестен.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Car</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">drive</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>


<span class="k">class</span> <span class="nc">ElectricCar</span><span class="p">(</span><span class="n">Car</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">drive</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;Driving an electric car&quot;</span>


<span class="k">class</span> <span class="nc">PetrolCar</span><span class="p">(</span><span class="n">Car</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">drive</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;Driving a petrol car&quot;</span>


<span class="k">class</span> <span class="nc">CarFactory</span><span class="p">:</span>
    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">create_car</span><span class="p">(</span><span class="n">car_type</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">car_type</span> <span class="o">==</span> <span class="s2">&quot;electric&quot;</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">ElectricCar</span><span class="p">()</span>
        <span class="k">elif</span> <span class="n">car_type</span> <span class="o">==</span> <span class="s2">&quot;petrol&quot;</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">PetrolCar</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Unknown car type&quot;</span><span class="p">)</span>
</pre></div></div></div>