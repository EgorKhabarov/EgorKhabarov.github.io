<p>Цикл for в JavaScript используется для выполнения одного 
или нескольких операторов многократно, пока условие в цикле истинно. 
Синтаксис цикла for выглядит следующим образом:</p>
<div class="code-element">
    <div class="lang-line">
        <text>js</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="nx">initialization</span><span class="p">;</span><span class="w"> </span><span class="nx">condition</span><span class="p">;</span><span class="w"> </span><span class="kr">final</span><span class="o">-</span><span class="nx">expression</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="nx">statement</span><span class="p">(</span><span class="nx">s</span><span class="p">)</span>
<span class="p">}</span>
</pre></div></div>
</div>

<p>initialization     выполняется один раз перед началом цикла 
                   и обычно используется для инициализации счетчика цикла.
condition          условие, которое проверяется перед каждой итерацией цикла. 
                   Если условие истинно, то тело цикла выполняется, иначе цикл завершается.
final-expression   выполняется после каждой итерации цикла 
                   и обычно используется для изменения счетчика цикла.
statement(s)       один или несколько операторов, которые выполняются в теле цикла.</p>
<div class="code-element">
    <div class="lang-line">
        <text>js</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kd">let</span><span class="w"> </span><span class="nx">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0</span><span class="p">;</span><span class="w"> </span><span class="nx">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mf">5</span><span class="p">;</span><span class="w"> </span><span class="nx">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="nx">console</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">i</span><span class="p">);</span>
<span class="p">}</span>
</pre></div></div>
</div>

<p>Цикл по списку</p>
<div class="code-element">
    <div class="lang-line">
        <text>js</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kd">var</span><span class="w"> </span><span class="nx">myArray</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="mf">1</span><span class="p">,</span><span class="w"> </span><span class="mf">2</span><span class="p">,</span><span class="w"> </span><span class="mf">3</span><span class="p">,</span><span class="w"> </span><span class="mf">4</span><span class="p">,</span><span class="w"> </span><span class="mf">5</span><span class="p">];</span>
<span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kd">var</span><span class="w"> </span><span class="nx">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0</span><span class="p">;</span><span class="w"> </span><span class="nx">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="nx">myArray</span><span class="p">.</span><span class="nx">length</span><span class="p">;</span><span class="w"> </span><span class="nx">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="nx">console</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">myArray</span><span class="p">[</span><span class="nx">i</span><span class="p">]);</span>
<span class="p">}</span>
</pre></div></div>
</div>

<p>или</p>
<div class="code-element">
    <div class="lang-line">
        <text>js</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kd">var</span><span class="w"> </span><span class="nx">myArray</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="mf">1</span><span class="p">,</span><span class="w"> </span><span class="mf">2</span><span class="p">,</span><span class="w"> </span><span class="mf">3</span><span class="p">,</span><span class="w"> </span><span class="mf">4</span><span class="p">,</span><span class="w"> </span><span class="mf">5</span><span class="p">];</span>
<span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kd">const</span><span class="w"> </span><span class="nx">element</span><span class="w"> </span><span class="k">of</span><span class="w"> </span><span class="nx">myArray</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="nx">console</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">element</span><span class="p">);</span>
<span class="p">}</span>
</pre></div></div>
</div>