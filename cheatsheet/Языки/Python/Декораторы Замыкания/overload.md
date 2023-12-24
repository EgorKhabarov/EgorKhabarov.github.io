<p>@overload - это декоратор в Python, который используется для определения перегрузки метода внутри класса. 
Перегрузка метода - это механизм, позволяющий определить несколько версий метода с разными параметрами. 
При вызове метода, интерпретатор Python выберет версию метода, которая соответствует переданным аргументам.</p>
<p>Пример использования @overload:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code473b" onclick="copyCode(code473, code473b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code473"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">overload</span>

<span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="nd">@overload</span>
    <span class="k">def</span> <span class="nf">my_method</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg1</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="nd">@overload</span>
    <span class="k">def</span> <span class="nf">my_method</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg1</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">my_method</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg1</span><span class="p">):</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg1</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">arg1</span> <span class="o">*</span> <span class="mi">2</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg1</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">arg1</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>

<span class="n">obj</span> <span class="o">=</span> <span class="n">MyClass</span><span class="p">()</span>
<span class="n">result1</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">my_method</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result1</span><span class="p">)</span> <span class="c1"># 4</span>

<span class="n">result2</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">my_method</span><span class="p">(</span><span class="s2">&quot;hello&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result2</span><span class="p">)</span> <span class="c1"># HELLO</span>
</pre></div></div></div>

<p>В этом примере мы определили класс MyClass и внутри него определили метод my_method с помощью декоратора @overload. 
Мы определили две версии метода: одна принимает целое число и возвращает его удвоенное значение, а другая принимает строку и возвращает ее в верхнем регистре. 
Наконец, мы определили основную версию метода, которая выбирает нужную версию метода в зависимости от типа переданного аргумента.</p>