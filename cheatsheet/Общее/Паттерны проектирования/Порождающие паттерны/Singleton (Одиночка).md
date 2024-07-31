<h2>Singleton (Одиночка)</h2>
<p><strong>Описание:</strong> Гарантирует, что у класса есть только <strong>один экземпляр</strong>,
и предоставляет глобальную точку доступа к этому экземпляру.</p>
<p><strong>Когда использовать:</strong> Когда нужно ограничить создание объекта одним экземпляром,
например, для логгера, подключения к базе данных, конфигурационного объекта.</p>
<p><strong>Пример реализации:</strong></p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code97ae331c2f9e2cff435765a32057fa33b"onclick="copyCode(code97ae331c2f9e2cff435765a32057fa33, code97ae331c2f9e2cff435765a32057fa33b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code97ae331c2f9e2cff435765a32057fa33"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Singleton</span><span class="p">:</span>
    <span class="n">_instance</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_instance</span><span class="p">:</span>
            <span class="bp">cls</span><span class="o">.</span><span class="n">_instance</span> <span class="o">=</span> <span class="nb">super</span><span class="p">(</span><span class="n">Singleton</span><span class="p">,</span> <span class="bp">cls</span><span class="p">)</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_instance</span>


<span class="n">singleton1</span> <span class="o">=</span> <span class="n">Singleton</span><span class="p">()</span>
<span class="n">singleton2</span> <span class="o">=</span> <span class="n">Singleton</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">singleton1</span> <span class="ow">is</span> <span class="n">singleton2</span><span class="p">)</span>  <span class="c1"># True</span>
</pre></div></div></div>