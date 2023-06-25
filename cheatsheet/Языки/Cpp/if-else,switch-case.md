<p>&amp;&amp; (И)
|| (ИЛИ)
! (НЕ)</p>
<p>Если необходимо проверить несколько условий в одном операторе, 
то можно воспользоваться логическим «и» или же логическим «или»:</p>
<div class="code-element">
    <div class="lang-line">cpp<button class="copy-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">a</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">&amp;&amp;</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="n">b</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// Код будет выполнен, если и первое, и второе условие</span>
<span class="w">    </span><span class="c1">// окажутся верными</span>
<span class="p">}</span>

<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">a</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">||</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">b</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// Код будет выполнен, если или первое, или второе условие</span>
<span class="w">    </span><span class="c1">// окажется верным</span>
<span class="p">}</span>
</pre></div></div>
</div>

<p>Тернарная операция
Это сокращенная форма if else. Записывается следующим образом:</p>
<div class="code-element">
    <div class="lang-line">cpp<button class="copy-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">90</span><span class="p">,</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">8</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">a</span><span class="p">)</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">a</span><span class="p">);</span>
<span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">res</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">endl</span><span class="p">;</span>
</pre></div></div>
</div>

<p>Проверяем: если “x” будет меньше “а”, то в переменную res устанавливаем их сумму, иначе – их разницу. </p>
<p>Конструкция switch
Конструкция case обладает более удобным форматом для проверки множественных условий на совпадение значения. 
В конструкцию записывается переменная, что проверяется, а также значения на которые происходит проверка.</p>
<p>Пример оператора:</p>
<div class="code-element">
    <div class="lang-line">cpp<button class="copy-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">23</span><span class="p">;</span>
<span class="k">switch</span><span class="w"> </span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="c1">// Проверяем переменную x</span>
<span class="w">    </span><span class="k">case</span><span class="w"> </span><span class="mi">1</span><span class="p">:</span><span class="w"> </span><span class="c1">// Если переменная будет равна 1, то здесь сработает код</span>
<span class="w">        </span><span class="c1">// Может быть множество строк, а не только одна</span>
<span class="w">        </span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Переменная равна 1&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">break</span><span class="p">;</span><span class="w"> </span><span class="c1">// Указываем конец для кода для этой проверки</span>
<span class="w">    </span><span class="k">case</span><span class="w"> </span><span class="mi">56</span><span class="p">:</span><span class="w"> </span><span class="c1">// Если переменная будет равна 56, то здесь сработает код</span>
<span class="w">        </span><span class="c1">// Может быть множество строк, а не только одна</span>
<span class="w">        </span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Переменная равна 56&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">break</span><span class="p">;</span><span class="w"> </span><span class="c1">// Указываем конец для кода для этой проверки</span>
<span class="w">        </span><span class="c1">// По аналогии таких проверок может быть множество</span>
<span class="w">        </span><span class="c1">// Также можно добавить проверку, которая сработает в случае</span>
<span class="w">        </span><span class="c1">// если все остальные проверки не сработают</span>
<span class="w">    </span><span class="k">default</span><span class="o">:</span>
<span class="w">        </span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Что-то другое&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">break</span><span class="p">;</span><span class="w"> </span><span class="c1">// Можно и не ставить, так как это последние условие</span>
<span class="p">}</span>
</pre></div></div>
</div>

<p>Операторы &amp;&amp; и || ведут себя лениво: если первого аргумента уже достаточно для ответа, то второй аргумент вычисляться не будет. 
Например, в выражении condition1 &amp;&amp; condition2 второе условие не вычисляется, если первое ложно.</p>
<p>Сравнение чисел с плавающей точкой
Рассмотрим программу, которая проверяет равенство 0.1 + 0.2 == 0.3:</p>
<div class="code-element">
    <div class="lang-line">cpp<button class="copy-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="w"> </span>
<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0.1</span><span class="p">,</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0.2</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mf">0.3</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;EQUAL &quot;</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;NOT EQUAL &quot;</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w"> </span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">;</span>
<span class="p">}</span>
</pre></div></div>
</div>

<p>Логично было бы предположить, что программа выведет EQUAL 0.3, потому что . 
Однако программа напечатает NOT EQUAL 0.3. 
Данная «ошибка вычисления» встречается в большинстве современных языков программирования и обусловлена погрешностью представления этих чисел. 
Если повысить число знаков дробной части в выводе, мы увидим, что 0.1 + 0.2 == 0.30000000000000004.</p>
<p>Поскольку операции над числами с плавающей точкой могут содержать погрешность, обычное сравнение через == некорректно. 
Поэтому правильнее сравнивать модуль разности величин с некой допустимой для нас погрешностью. 
Модуль дробного числа можно получить с помощью функции std::abs из заголовочного файла cmath. 
Исходную программу можно было бы переписать так:</p>
<div class="code-element">
    <div class="lang-line">cpp<button class="copy-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cmath&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="w"> </span>
<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">delta</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0.000001</span><span class="p">;</span>
<span class="w"> </span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0.1</span><span class="p">,</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0.2</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">sum</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">y</span><span class="p">;</span>
<span class="w"> </span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">abs</span><span class="p">(</span><span class="n">sum</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="mf">0.3</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">delta</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;EQUAL &quot;</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;NOT EQUAL &quot;</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w"> </span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">sum</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">;</span>
<span class="p">}</span>
<span class="c1">// Теперь программа выведет EQUAL 0.3.</span>
</pre></div></div>
</div>