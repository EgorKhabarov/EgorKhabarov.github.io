<p>from fractions import Fraction</p>
<p>Модуль fractions предоставляет класс Fraction, который позволяет работать с дробными числами в виде объектов.
Класс Fraction позволяет представлять дробное число в виде числителя и знаменателя. 
Он автоматически упрощает дробь, позволяет выполнять арифметические операции с дробями 
и конвертировать дроби в различные форматы (например, вещественные числа или строки).</p>
<p>Вот примеры использования класса Fraction:</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">Fraction</span>

<span class="c1"># создание дроби с помощью числителя и знаменателя</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">))</span>    <span class="c1"># вывод: 3/4</span>

<span class="c1"># создание дроби из вещественного числа</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="p">(</span><span class="mf">0.5</span><span class="p">))</span>    <span class="c1"># вывод: 1/2</span>

<span class="c1"># арифметические операции с дробями</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span> <span class="o">+</span> <span class="n">Fraction</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>    <span class="c1"># вывод: 3/4</span>

<span class="c1"># конвертирование дроби в вещественное число</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="n">Fraction</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">)))</span>    <span class="c1"># вывод: 0.75</span>

<span class="c1"># конвертирование дроби в строку</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">Fraction</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">)))</span>    <span class="c1"># вывод: &quot;3/4&quot;</span>
</pre></div></div>
</div>

<p>Класс Fraction может быть полезен в тех случаях, когда требуется более точный 
и удобный способ работы с дробными числами, чем встроенные типы данных. 
Он может использоваться, например, при работе с финансовыми расчетами, 
при расчете вероятностей или в других задачах, связанных с математикой.</p>
<p>Fraction <br />
Класс для представления рациональных чисел. 
Этот класс позволяет создавать объекты, которые представляют дроби в виде числителя и знаменателя. 
Например, Fraction(3, 4) создаст дробь 3/4.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">Fraction</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span> <span class="o">+</span> <span class="n">Fraction</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>  <span class="c1"># выводит 5/4</span>
</pre></div></div>
</div>

<p>gcd</p>
<p>Функция для вычисления наибольшего общего делителя двух чисел.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">gcd</span>

<span class="nb">print</span><span class="p">(</span><span class="n">gcd</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="mi">9</span><span class="p">))</span>  <span class="c1"># выводит 3</span>
</pre></div></div>
</div>

<p>lcm
Функция для вычисления наименьшего общего кратного двух чисел.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">lcm</span>

<span class="nb">print</span><span class="p">(</span><span class="n">lcm</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="mi">9</span><span class="p">))</span>  <span class="c1"># выводит 18</span>
</pre></div></div>
</div>

<p>limit_denominator
Метод объекта Fraction, который позволяет получить рациональное число, 
ближайшее к данному, с знаменателем не превосходящим указанное значение.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">Fraction</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="mi">12</span><span class="p">)</span><span class="o">.</span><span class="n">limit_denominator</span><span class="p">(</span><span class="mi">5</span><span class="p">))</span>  <span class="c1"># выводит 3/5</span>
</pre></div></div>
</div>

<p>Fraction.from_float
Метод класса Fraction, который позволяет создать рациональное число, 
представляющее указанное число с плавающей точкой.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">Fraction</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="o">.</span><span class="n">from_float</span><span class="p">(</span><span class="mf">0.5</span><span class="p">))</span>  <span class="c1"># выводит 1/2</span>
</pre></div></div>
</div>

<p>Fraction.from_decimal
Метод класса Fraction, который позволяет создать рациональное число, представляющее указанное десятичное число.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">Fraction</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="o">.</span><span class="n">from_decimal</span><span class="p">(</span><span class="s2">&quot;0.75&quot;</span><span class="p">))</span>  <span class="c1"># выводит 3/4</span>
</pre></div></div>
</div>

<p>is_integer
Метод объекта Fraction, который возвращает True, если данная дробь представляет целое число, и False в противном случае.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">Fraction</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span><span class="o">.</span><span class="n">is_integer</span><span class="p">())</span>  <span class="c1"># выводит False</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span><span class="o">.</span><span class="n">is_integer</span><span class="p">())</span>  <span class="c1"># выводит True</span>
</pre></div></div>
</div>

<p>Fraction.as_integer_ratio
Метод объекта Fraction, который возвращает кортеж из двух целых чисел, 
представляющих данную дробь в виде несократимой простой дроби.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">Fraction</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">15</span><span class="p">)</span><span class="o">.</span><span class="n">as_integer_ratio</span><span class="p">())</span>  <span class="c1"># выводит (1, 3)</span>
</pre></div></div>
</div>

<p>Fraction.from_ratio
Метод класса Fraction, который позволяет создать рациональное число на основе заданного отношения двух целых чисел.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">Fraction</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="o">.</span><span class="n">from_ratio</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">15</span><span class="p">))</span>  <span class="c1"># выводит 1/3</span>
</pre></div></div>
</div>

<p>Fraction.limit_denominator(max_denominator=1000000): 
Метод объекта Fraction, который возвращает рациональное число, ближайшее к данному, 
с знаменателем не превосходящим указанное значение. 
Если аргумент max_denominator не указан, то по умолчанию он равен 1 миллиону.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">Fraction</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span><span class="o">.</span><span class="n">limit_denominator</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>  <span class="c1"># выводит 1/1</span>
</pre></div></div>
</div>

<p>Fraction.from_jedec
Метод класса Fraction, который позволяет создать рациональное число на основе заданной строки в формате JEDEC.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">Fraction</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="o">.</span><span class="n">from_jedec</span><span class="p">(</span><span class="s2">&quot;1/2&quot;</span><span class="p">))</span>  <span class="c1"># выводит 1/2</span>
</pre></div></div>
</div>

<p>Fraction.from_tuple
Метод класса Fraction, который позволяет создать рациональное число на основе заданного кортежа из двух целых чисел (числителя и знаменателя).</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fractions</span> <span class="kn">import</span> <span class="n">Fraction</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Fraction</span><span class="o">.</span><span class="n">from_tuple</span><span class="p">((</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">)))</span>  <span class="c1"># выводит 3/4</span>
</pre></div></div>
</div>