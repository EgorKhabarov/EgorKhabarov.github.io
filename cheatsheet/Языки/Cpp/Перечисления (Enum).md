<p>За счёт перечислений вы можете указать список элементов для выбора и далее в программе можете пользоваться данным списком.
Перечисления служат для удобства программистов, так как особой функциональности они не несут. 
Представим, что у вас большая программа со множеством массивов данных, которые человек попросту не способен запомнить. 
По причине неспособности все запомнить вы можете создать перечисление, что будет хранить список со всеми доступными значениями и названиями.</p>
<p>Создав такой список вы можете обращаться к нему и выбирать подходящий для вас вариант.</p>
<p>Для создания перечислений используйте пропишите слово enum, назовите его и укажите инициализацию всех вариантов.</p>
<p>Обьяснение от ChatGPT:</p>
<p>Перечисления (Enum) - это специальный тип данных в C++, который позволяет определять именованные константы. 
Это полезно, когда вы хотите указать набор допустимых значений для переменной.</p>
<p>Определение перечисления выглядит так:</p>
<div class="code-element"><div class="lang-line"><text>cpp</text><button class="copy-button" id="code333b" onclick="copyCode(code333, code333b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code333"><div class="highlight"><pre><span></span><span class="k">enum</span><span class="w"> </span><span class="nc">Color</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">RED</span><span class="p">,</span>
<span class="w">  </span><span class="n">GREEN</span><span class="p">,</span>
<span class="w">  </span><span class="n">BLUE</span>
<span class="p">};</span>
</pre></div></div></div>

<p>В этом примере мы определили перечисление Color, которое содержит три константы: RED, GREEN и BLUE. 
Эти константы могут использоваться в качестве значений для переменных типа Color.</p>
<p>По умолчанию каждая константа присваивается значение равным ее позиции в перечислении, начиная с нуля. 
Однако, вы также можете явно указать значение для каждой константы:</p>
<div class="code-element"><div class="lang-line"><text>cpp</text><button class="copy-button" id="code334b" onclick="copyCode(code334, code334b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code334"><div class="highlight"><pre><span></span><span class="k">enum</span><span class="w"> </span><span class="nc">Color</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">RED</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
<span class="w">  </span><span class="n">GREEN</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span>
<span class="w">  </span><span class="n">BLUE</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">4</span>
<span class="p">};</span>
</pre></div></div></div>

<p>В этом примере мы явно указали значение для каждой константы в перечислении.</p>