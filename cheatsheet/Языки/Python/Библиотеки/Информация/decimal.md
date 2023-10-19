<p>from decimal import Decimal</p>
<p>Библиотека decimal предоставляет более точный способ работы с десятичными числами, чем встроенные типы данных float и double. 
Она позволяет представлять числа с фиксированной точностью и позволяет управлять точностью вычислений. 
Это может быть полезно в тех случаях, когда требуется точный результат, например, при финансовых расчетах.</p>
<p>Класс Decimal
Класс Decimal используется для создания и работы с десятичными числами с фиксированной точностью. Вот несколько примеров:i</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code320b" onclick="copyCode(code320, code320b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code320"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">decimal</span> <span class="kn">import</span> <span class="n">Decimal</span>

<span class="c1"># Создание десятичного числа</span>
<span class="n">a</span> <span class="o">=</span> <span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;10.5&#39;</span><span class="p">)</span>

<span class="c1"># Арифметические операции</span>
<span class="n">b</span> <span class="o">=</span> <span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;2&#39;</span><span class="p">)</span>
<span class="n">a</span> <span class="o">+</span> <span class="n">b</span> <span class="c1"># 12.5</span>
<span class="n">a</span> <span class="o">-</span> <span class="n">b</span> <span class="c1"># 8.5</span>
<span class="n">a</span> <span class="o">*</span> <span class="n">b</span> <span class="c1"># 21.0</span>
<span class="n">a</span> <span class="o">/</span> <span class="n">b</span> <span class="c1"># 5.25</span>

<span class="c1"># Округление</span>
<span class="n">a</span><span class="o">.</span><span class="n">quantize</span><span class="p">(</span><span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;1.00&#39;</span><span class="p">))</span> <span class="c1"># 10.50</span>
<span class="n">a</span><span class="o">.</span><span class="n">quantize</span><span class="p">(</span><span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;0.1&#39;</span><span class="p">))</span>  <span class="c1"># 10.5</span>

<span class="c1"># Преобразование в разные форматы</span>
<span class="n">a</span><span class="o">.</span><span class="n">to_eng_string</span><span class="p">()</span>    <span class="c1"># &#39;10.5&#39;</span>
<span class="n">a</span><span class="o">.</span><span class="n">as_integer_ratio</span><span class="p">()</span> <span class="c1"># (21, 2)</span>
</pre></div></div></div>

<p>Класс Context
Класс Context представляет контекст округления, который управляет поведением операций с десятичными числами. Вот несколько примеров:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code321b" onclick="copyCode(code321, code321b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code321"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">decimal</span> <span class="kn">import</span> <span class="n">Decimal</span><span class="p">,</span> <span class="n">Context</span>

<span class="c1"># Создание контекста округления</span>
<span class="n">ctx</span> <span class="o">=</span> <span class="n">Context</span><span class="p">(</span><span class="n">prec</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">rounding</span><span class="o">=</span><span class="n">ROUND_HALF_UP</span><span class="p">)</span>

<span class="c1"># Создание десятичного числа с использованием контекста</span>
<span class="n">a</span> <span class="o">=</span> <span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;10.5&#39;</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">ctx</span><span class="p">)</span>

<span class="c1"># Арифметические операции с использованием контекста</span>
<span class="n">b</span> <span class="o">=</span> <span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;2&#39;</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">ctx</span><span class="p">)</span>
<span class="n">c</span> <span class="o">=</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">a</span> <span class="o">-</span> <span class="n">b</span>
<span class="n">e</span> <span class="o">=</span> <span class="n">a</span> <span class="o">*</span> <span class="n">b</span>
<span class="n">f</span> <span class="o">=</span> <span class="n">a</span> <span class="o">/</span> <span class="n">b</span>

<span class="c1"># Округление с использованием контекста</span>
<span class="n">g</span> <span class="o">=</span> <span class="n">a</span><span class="o">.</span><span class="n">quantize</span><span class="p">(</span><span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;1.00&#39;</span><span class="p">),</span> <span class="n">context</span><span class="o">=</span><span class="n">ctx</span><span class="p">)</span>
<span class="n">h</span> <span class="o">=</span> <span class="n">a</span><span class="o">.</span><span class="n">quantize</span><span class="p">(</span><span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;0.1&#39;</span><span class="p">),</span> <span class="n">context</span><span class="o">=</span><span class="n">ctx</span><span class="p">)</span>
</pre></div></div></div>

<p>Функции округления
Модуль decimal также предоставляет несколько функций округления, которые можно использовать с десятичными числами. Вот несколько примеров:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code322b" onclick="copyCode(code322, code322b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code322"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">decimal</span> <span class="kn">import</span> <span class="n">Decimal</span><span class="p">,</span> <span class="n">ROUND_HALF_UP</span><span class="p">,</span> <span class="n">ROUND_HALF_DOWN</span><span class="p">,</span> <span class="n">ROUND_CEILING</span><span class="p">,</span> <span class="n">ROUND_FLOOR</span>

<span class="n">a</span> <span class="o">=</span> <span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;10.555&#39;</span><span class="p">)</span>

<span class="c1"># Округление до двух знаков с округлением до ближайшего</span>
<span class="n">a</span><span class="o">.</span><span class="n">quantize</span><span class="p">(</span><span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;1.00&#39;</span><span class="p">),</span> <span class="n">rounding</span><span class="o">=</span><span class="n">ROUND_HALF_UP</span><span class="p">)</span> <span class="c1"># 10.56    </span>

<span class="c1"># Округление до двух знаков с округлением в меньшую сторону</span>
<span class="n">a</span><span class="o">.</span><span class="n">quantize</span><span class="p">(</span><span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;1.00&#39;</span><span class="p">),</span> <span class="n">rounding</span><span class="o">=</span><span class="n">ROUND_FLOOR</span><span class="p">)</span>   <span class="c1"># 10.55</span>

<span class="c1"># Округление до целого числа, округление до ближайшего</span>
<span class="n">a</span><span class="o">.</span><span class="n">quantize</span><span class="p">(</span><span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;1&#39;</span><span class="p">),</span> <span class="n">rounding</span><span class="o">=</span><span class="n">ROUND_HALF_UP</span><span class="p">)</span>    <span class="c1"># 11</span>

<span class="c1"># Округление до целого числа, округление в большую сторону</span>
<span class="n">a</span><span class="o">.</span><span class="n">quantize</span><span class="p">(</span><span class="n">Decimal</span><span class="p">(</span><span class="s1">&#39;1&#39;</span><span class="p">),</span> <span class="n">rounding</span><span class="o">=</span><span class="n">ROUND_CEILING</span><span class="p">)</span>    <span class="c1"># 11</span>
</pre></div></div></div>