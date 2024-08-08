<p>Библиотека "rasutil" (raspberry utility) используется для упрощения
разработки и взаимодействия с Raspberry Pi в языке программирования Python.</p>
<p>Таблица методов для модуля "rasutil":
Method 1: GPIOInit() - Инициализирует пины GPIO на Raspberry Pi.
Method 2: GPIOSet(pin, value) - Устанавливает значение пина GPIO на Raspberry Pi.
Method 3: GPIORead(pin) - Считывает значение с пина GPIO на Raspberry Pi.</p>
<p>Методы модуля "rasutil" позволяют управлять GPIO пинами на Raspberry Pi,
инициализировать их, устанавливать значения и считывать значения с этих пинов.</p>
<p>Список самых частых методов и их описания:
GPIOInit() - Инициализирует пины GPIO на Raspberry Pi.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="n">rasutil</span><span class="o">.</span><span class="n">GPIOInit</span><span class="p">()</span>
</pre></div></div>
</div>
<p>Этот метод инициализирует пины GPIO на Raspberry Pi перед использованием.</p>
<p>GPIOSet(pin, value) - Устанавливает значение пина GPIO на Raspberry Pi.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="n">rasutil</span><span class="o">.</span><span class="n">GPIOSet</span><span class="p">(</span><span class="mi">18</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</pre></div></div>
</div>
<p>Этот метод устанавливает значение 1 на пине GPIO 18 на Raspberry Pi.</p>
<p>GPIORead(pin) - Считывает значение с пина GPIO на Raspberry Pi.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="n">value</span> <span class="o">=</span> <span class="n">rasutil</span><span class="o">.</span><span class="n">GPIORead</span><span class="p">(</span><span class="mi">12</span><span class="p">)</span>
</pre></div></div>
</div>
<p>Этот метод считывает значение с пина GPIO 12 на Raspberry Pi и сохраняет его в переменную "value".</p>
<p>Методы "GPIOSet" и "GPIORead" позволяют управлять значениями пинов GPIO на Raspberry Pi,
устанавливая значения и считывая их соответственно. Метод "GPIOInit" необходим для инициализации пинов GPIO перед их использованием.</p>