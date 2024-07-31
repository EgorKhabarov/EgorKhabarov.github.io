<p>partial(func, <em>args, </em><em>kwargs)              возвращает новую функцию, которая является копией исходной функции func, 
                                            но с некоторыми аргументами, переданными как </em>args и **kwargs, заранее заданными.</p>
<p>reduce(func, iterable[, initializer])       применяет функцию func к первым двум элементам последовательности iterable, 
                                            затем применяет func к результату и следующему элементу, и так далее, пока не будет обработан весь список. 
                                            Если указан initializer, он используется как первый элемент в последовательности.</p>
<p>cache(func)                                 декоратор, который кэширует результаты вызовов функции func с одинаковыми аргументами, чтобы избежать повторных вычислений.</p>
<p>wraps(wrapped[, assigned[, updated]])       декоратор, который копирует информацию об исходной функции wrapped в декорированную функцию. 
                                            Это позволяет сохранить метаданные, такие как имя функции, документацию и атрибуты.</p>
<p>total_ordering(cls)                         декоратор, который автоматически генерирует методы сравнения объектов 
                                            для класса cls на основе определения методов <strong>eq</strong>() и <strong>lt</strong>().</p>
<p>cmp_to_key(func)                            преобразует функцию func для использования в функциях сортировки. 
                                            Функция func(a, b) должна возвращать число, которое указывает порядок элементов a и b.</p>
<p>partialmethod(func, <em>args, </em>*kwargs)        возвращает частичный метод, который может быть вызван как метод экземпляра класса. 
                                            Аргумент func должен быть методом класса.</p>
<p>lru_cache                                   декоратор реализует механизм кеширования результатов функции с помощью алгоритма "Least Recently Used" (LRU).</p>
<p>partial(func, <em>args, </em><em>kwargs)<br />
Возвращает новую функцию, которая является копией исходной функции func, 
но с некоторыми аргументами, переданными как </em>args и **kwargs, заранее заданными.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codea442684887be550527d3d838cf29e61bb"
          onclick="copyCode(codea442684887be550527d3d838cf29e61b, codea442684887be550527d3d838cf29e61bb)">
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
<div class="code" id="codea442684887be550527d3d838cf29e61b"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">partial</span>

<span class="k">def</span> <span class="nf">power</span><span class="p">(</span><span class="n">base</span><span class="p">,</span> <span class="n">exponent</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">base</span> <span class="o">**</span> <span class="n">exponent</span>

<span class="c1"># Создаем функцию возведения в квадрат, используя partial</span>
<span class="n">square</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">power</span><span class="p">,</span> <span class="n">exponent</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>

<span class="c1"># Вызываем функции</span>
<span class="nb">print</span><span class="p">(</span><span class="n">square</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>  <span class="c1"># 4</span>
<span class="nb">print</span><span class="p">(</span><span class="n">square</span><span class="p">(</span><span class="mi">3</span><span class="p">))</span>  <span class="c1"># 9</span>
</pre></div></div>
</div>

<p>reduce(func, iterable[, initializer]) 
Применяет функцию func к первым двум элементам последовательности iterable, затем применяет func к результату и следующему элементу, 
и так далее, пока не будет обработан весь список. Если указан initializer, он используется как первый элемент в последовательности.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codec98929e1ee7dd37078a9a4f9926eed9fb"
          onclick="copyCode(codec98929e1ee7dd37078a9a4f9926eed9f, codec98929e1ee7dd37078a9a4f9926eed9fb)">
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
<div class="code" id="codec98929e1ee7dd37078a9a4f9926eed9f"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">reduce</span>

<span class="n">numbers</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>

<span class="c1"># Найдем произведение всех чисел в списке</span>
<span class="n">product</span> <span class="o">=</span> <span class="n">reduce</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="n">x</span><span class="o">*</span><span class="n">y</span><span class="p">,</span> <span class="n">numbers</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">product</span><span class="p">)</span>  <span class="c1"># 120</span>
</pre></div></div>
</div>

<p>cache(func): 
Декоратор, который кэширует результаты вызовов функции func с одинаковыми аргументами, чтобы избежать повторных вычислений.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codec884722e357145ff85af8472b3a77177b"
          onclick="copyCode(codec884722e357145ff85af8472b3a77177, codec884722e357145ff85af8472b3a77177b)">
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
<div class="code" id="codec884722e357145ff85af8472b3a77177"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">cache</span>

<span class="nd">@cache</span>
<span class="k">def</span> <span class="nf">factorial</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">1</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">n</span> <span class="o">*</span> <span class="n">factorial</span><span class="p">(</span><span class="n">n</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">factorial</span><span class="p">(</span><span class="mi">5</span><span class="p">))</span>  <span class="c1"># 120</span>
</pre></div></div>
</div>

<p>wraps(wrapped[, assigned[, updated]]) 
Декоратор, который копирует информацию об исходной функции wrapped в декорированную функцию. 
Это позволяет сохранить метаданные, такие как имя функции, документацию и атрибуты.
| сохраняет имя и документацию функции так как обычный декоратор заменяет собой функцию</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code568a794f9a6ea95574515e493bd220dab"
          onclick="copyCode(code568a794f9a6ea95574515e493bd220da, code568a794f9a6ea95574515e493bd220dab)">
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
<div class="code" id="code568a794f9a6ea95574515e493bd220da"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">wraps</span>

<span class="k">def</span> <span class="nf">my_decorator</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
    <span class="nd">@wraps</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Calling function:&quot;</span><span class="p">,</span> <span class="n">func</span><span class="o">.</span><span class="vm">__name__</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">wrapper</span>

<span class="nd">@my_decorator</span>
<span class="k">def</span> <span class="nf">my_function</span><span class="p">():</span>
<span class="w">    </span><span class="sd">&quot;&quot;&quot;This is my function.&quot;&quot;&quot;</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Hello, World!&quot;</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">my_function</span><span class="o">.</span><span class="vm">__name__</span><span class="p">)</span>  <span class="c1"># my_function</span>
<span class="nb">print</span><span class="p">(</span><span class="n">my_function</span><span class="o">.</span><span class="vm">__doc__</span><span class="p">)</span>   <span class="c1"># This is my function.</span>
</pre></div></div>
</div>

<div class="code-element">
<div class="lang-line">
  <text>pycon</text>
  <button class="copy-button"
          id="codee9a7a7ef13184870265b7d8053930b58b"
          onclick="copyCode(codee9a7a7ef13184870265b7d8053930b58, codee9a7a7ef13184870265b7d8053930b58b)">
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
<div class="code" id="codee9a7a7ef13184870265b7d8053930b58"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">def</span> <span class="nf">dec</span><span class="p">(</span><span class="n">f</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">def</span> <span class="nf">w</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="k">return</span> <span class="n">f</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">return</span> <span class="n">w</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nd">@dec</span>
<span class="unselectable"><span class="o">...</span> </span><span class="k">def</span> <span class="nf">foo</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span><span class="w">    </span><span class="sd">&quot;&quot;&quot;comment&quot;&quot;&quot;</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span class="n">y</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">foo</span>
<span class="unselectable"><span class="go">&lt;function dec.&lt;locals&gt;.w at 0x00000182FB1982C0&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">foo</span><span class="o">.</span><span class="vm">__name__</span>
<span class="unselectable"><span class="go">&quot;w&quot;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">wraps</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">def</span> <span class="nf">dec</span><span class="p">(</span><span class="n">f</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nd">@wraps</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">def</span> <span class="nf">w</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="k">return</span> <span class="n">f</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">return</span> <span class="n">w</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nd">@dec</span>
<span class="unselectable"><span class="o">...</span> </span><span class="k">def</span> <span class="nf">foo</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span><span class="w">    </span><span class="sd">&quot;&quot;&quot;comment&quot;&quot;&quot;</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span class="n">y</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">foo</span>
<span class="unselectable"><span class="go">&lt;function foo at 0x00000182FB198400&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">foo</span><span class="o">.</span><span class="vm">__name__</span>
<span class="unselectable"><span class="go">&quot;foo&quot;</span></span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
</pre></div></div>
</div>

<p>total_ordering(cls) 
Декоратор, который автоматически генерирует методы сравнения объектов 
для класса cls на основе определения методов <strong>eq</strong>() и <strong>lt</strong>().</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code22db9c06702f2ad078bcc7842eb96e66b"
          onclick="copyCode(code22db9c06702f2ad078bcc7842eb96e66, code22db9c06702f2ad078bcc7842eb96e66b)">
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
<div class="code" id="code22db9c06702f2ad078bcc7842eb96e66"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">total_ordering</span>

<span class="nd">@total_ordering</span>
<span class="k">class</span> <span class="nc">Person</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">age</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">age</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">age</span>

    <span class="k">def</span> <span class="fm">__lt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">age</span> <span class="o">&lt;</span> <span class="n">other</span><span class="o">.</span><span class="n">age</span>

<span class="n">person1</span> <span class="o">=</span> <span class="n">Person</span><span class="p">(</span><span class="s2">&quot;Alice&quot;</span><span class="p">,</span> <span class="mi">25</span><span class="p">)</span>
<span class="n">person2</span> <span class="o">=</span> <span class="n">Person</span><span class="p">(</span><span class="s2">&quot;Bob&quot;</span><span class="p">,</span> <span class="mi">30</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">person1</span> <span class="o">==</span> <span class="n">person2</span><span class="p">)</span>  <span class="c1"># False</span>
<span class="nb">print</span><span class="p">(</span><span class="n">person1</span> <span class="o">!=</span> <span class="n">person2</span><span class="p">)</span>  <span class="c1"># True</span>
<span class="nb">print</span><span class="p">(</span><span class="n">person1</span> <span class="o">&lt;</span> <span class="n">person2</span><span class="p">)</span>   <span class="c1"># True</span>
<span class="nb">print</span><span class="p">(</span><span class="n">person1</span> <span class="o">&gt;</span> <span class="n">person2</span><span class="p">)</span>   <span class="c1"># False</span>
</pre></div></div>
</div>

<p>cmp_to_key(cmp) 
Преобразует функцию сравнения cmp в ключ-функцию, которая может быть использована для сортировки объектов. 
Эта функция полезна, когда необходимо отсортировать список объектов с использованием пользовательской функции сравнения.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code3f6c4ac8a9e9cad22d323226ab21020fb"
          onclick="copyCode(code3f6c4ac8a9e9cad22d323226ab21020f, code3f6c4ac8a9e9cad22d323226ab21020fb)">
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
<div class="code" id="code3f6c4ac8a9e9cad22d323226ab21020f"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">cmp_to_key</span>

<span class="k">def</span> <span class="nf">my_cmp</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">a</span> <span class="o">&lt;</span> <span class="n">b</span><span class="p">:</span>
        <span class="k">return</span> <span class="o">-</span><span class="mi">1</span>
    <span class="k">elif</span> <span class="n">a</span> <span class="o">&gt;</span> <span class="n">b</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">1</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">0</span>

<span class="n">numbers</span> <span class="o">=</span> <span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>

<span class="n">sorted_numbers</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">numbers</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="n">cmp_to_key</span><span class="p">(</span><span class="n">my_cmp</span><span class="p">))</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sorted_numbers</span><span class="p">)</span>  <span class="c1"># [1, 2, 3, 4, 7]</span>
</pre></div></div>
</div>

<p>lru_cache — это декоратор в модуле functools в Python, который реализует 
механизм кеширования результатов функции с помощью алгоритма "Least Recently Used" (LRU).</p>
<p>LRU-кеширование позволяет сохранять недавно использованные результаты функции в кеше, 
чтобы повторно использовать их при последующих вызовах функции с теми же параметрами. 
Когда кеш заполнен до определенной максимальной величины, самые редко используемые 
элементы будут удалены из кеша, чтобы освободить место для новых элементов.</p>
<p>Для использования lru_cache необходимо импортировать модуль functools и применить декоратор @functools.lru_cache() к функции, 
которую нужно кешировать. Опционально можно передать в декоратор максимальное количество 
элементов в кеше (maxsize). Если параметр не задан, по умолчанию используется maxsize=128.</p>
<p>Например, вот как можно использовать lru_cache для кеширования результата функции fibonacci(n):</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codee1e80147bfdf5fa53aea64ff5a0e54b7b"
          onclick="copyCode(codee1e80147bfdf5fa53aea64ff5a0e54b7, codee1e80147bfdf5fa53aea64ff5a0e54b7b)">
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
<div class="code" id="codee1e80147bfdf5fa53aea64ff5a0e54b7"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">lru_cache</span>

<span class="nd">@lru_cache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">128</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">fibonacci</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;=</span> <span class="mi">1</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">n</span>
    <span class="k">return</span> <span class="n">fibonacci</span><span class="p">(</span><span class="n">n</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span> <span class="o">+</span> <span class="n">fibonacci</span><span class="p">(</span><span class="n">n</span><span class="o">-</span><span class="mi">2</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Этот код создает кеш для fibonacci с максимальным размером 128 элементов. 
При вызове fibonacci(n) для любого n, результат будет сохранен в кеше. 
При повторном вызове fibonacci(n) с тем же n, результат будет возвращен из кеша без повторного вычисления.</p>