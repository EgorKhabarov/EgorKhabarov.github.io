<p><code>@staticmethod</code> - это декоратор в Python, который используется для определения статического метода внутри класса. 
Статический метод - это метод, который может быть вызван на классе, а не на экземпляре класса. 
Он не имеет доступа к экземпляру класса и не может изменять его состояние.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="nd">@staticmethod</span>
    <span class="k">def</span> <span class="nf">my_static_method</span><span class="p">(</span><span class="n">arg1</span><span class="p">,</span> <span class="n">arg2</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">arg1</span> <span class="o">+</span> <span class="n">arg2</span>

<span class="nb">print</span><span class="p">(</span><span class="n">MyClass</span><span class="o">.</span><span class="n">my_static_method</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>  <span class="c1"># 3</span>
</pre></div></div>
</div>

<p>В этом примере мы определили класс <code>MyClass</code> и внутри него определили статический метод <code>my_static_method</code>. 
Этот метод принимает два аргумента <code>arg1</code> и <code>arg2</code> и возвращает их сумму. 
Затем мы вызвали этот метод на классе <code>MyClass</code>, а не на экземпляре класса.</p>