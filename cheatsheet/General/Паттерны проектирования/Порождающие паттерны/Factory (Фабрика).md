<h2>Factory (Фабрика)</h2>
<p><strong>Описание:</strong> Предоставляет интерфейс для создания объектов в суперклассе,
но позволяет подклассам изменять тип создаваемых объектов.</p>
<p><strong>Когда использовать:</strong> Когда нужно делегировать создание объектов подклассам
или когда тип создаваемых объектов заранее неизвестен.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Car</span><span class="p">:</span>
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
</pre></div></div>
</div>