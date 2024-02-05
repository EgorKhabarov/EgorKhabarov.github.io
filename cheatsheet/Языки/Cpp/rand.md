<p>Случайные числа
Для генерации случайных чисел необходимо использовать метод rand(). Чтобы создать случайное число в диапазоне от 1 до 20 потребуется следующий код:</p>
<div class="code-element"><div class="lang-line"><text>cpp</text><button class="copy-button" id="code649b" onclick="copyCode(code649, code649b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code649"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">rand</span><span class="p">()</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="mi">20</span><span class="p">;</span>
</pre></div></div></div>

<p>При использовании такого кода число будет генерироваться случайны образом, но всегда будет неизменным. 
Чтобы каждый раз при запуске программы выводилось новое случайное число необходимо использовать библиотеку: </p>
<h1>include <time.h>.</h1>
<p>После её подключения в функции main пропишите команду: srand(time(NULL));</p>
<p>Пример реализации:</p>
<div class="code-element"><div class="lang-line"><text>cpp</text><button class="copy-button" id="code650b" onclick="copyCode(code650, code650b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code650"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;time.h&gt;</span>
<span class="k">using</span><span class="w"> </span><span class="k">namespace</span><span class="w"> </span><span class="nn">std</span><span class="p">;</span><span class="w"> </span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">setlocale</span><span class="p">(</span><span class="n">LC_ALL</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;Russian&quot;</span><span class="p">);</span><span class="w"> </span><span class="c1">// Русская локализация консоли</span>
<span class="w">    </span><span class="n">srand</span><span class="p">(</span><span class="n">time</span><span class="p">(</span><span class="nb">NULL</span><span class="p">));</span><span class="w"> </span><span class="c1">// Генерирует случайное число, используя текущую дату как параметр</span>
<span class="w">    </span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">rand</span><span class="p">()</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="mi">20</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">rand</span><span class="p">()</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="mi">20</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="n">cin</span><span class="p">.</span><span class="n">get</span><span class="p">();</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span>
<span class="p">}</span>
</pre></div></div></div>

<p>Функции для строк
Для работы со строками необходимо подключить библиотеку #include <string>. </p>
<p>Для получения целой строки от пользователя используйте функцию «getline(cin, value)». 
В функции параметр value является названием переменной, в которую будет записано значение от пользователя.</p>