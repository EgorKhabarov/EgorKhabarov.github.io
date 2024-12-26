<p>ExceptionGroup в Python появился в версии 3.11
Позволяет объединять несколько исключений в одно</p>
<h3>Пример 1: Создание ExceptionGroup</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">try</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">raise</span> <span class="n">ExceptionGroup</span><span class="p">(</span><span class="s2">&quot;Ошибка выполнения операций&quot;</span><span class="p">,</span> <span class="p">[</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Некорректное значение&quot;</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="ne">TypeError</span><span class="p">(</span><span class="s2">&quot;Неверный тип данных&quot;</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="ne">KeyError</span><span class="p">(</span><span class="s2">&quot;Ключ не найден&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="p">])</span>
<span class="unselectable"><span class="o">...</span> </span><span class="k">except</span> <span class="n">ExceptionGroup</span> <span class="k">as</span> <span class="n">eg</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Произошло </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">eg</span><span class="o">.</span><span class="n">exceptions</span><span class="p">)</span><span class="si">}</span><span class="s2"> исключений:&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">for</span> <span class="n">exc</span> <span class="ow">in</span> <span class="n">eg</span><span class="o">.</span><span class="n">exceptions</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;- </span><span class="si">{</span><span class="n">exc</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">exc</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="n">Произошло</span> <span class="mi">3</span> <span class="n">исключений</span><span class="p">:</span></span>
<span class="unselectable"><span class="o">-</span> <span class="ne">ValueError</span><span class="p">:</span> <span class="n">Некорректное</span> <span class="n">значение</span></span>
<span class="unselectable"><span class="o">-</span> <span class="ne">TypeError</span><span class="p">:</span> <span class="n">Неверный</span> <span class="n">тип</span> <span class="n">данных</span></span>
<span class="unselectable"><span class="o">-</span> <span class="ne">KeyError</span><span class="p">:</span> <span class="s1">&#39;Ключ не найден&#39;</span></span>
</pre></div></div></div>

<h3>Пример 2: Обработка отдельных исключений внутри группы</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">try</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">raise</span> <span class="n">ExceptionGroup</span><span class="p">(</span><span class="s2">&quot;Ошибка выполнения операций&quot;</span><span class="p">,</span> <span class="p">[</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Некорректное значение&quot;</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="ne">TypeError</span><span class="p">(</span><span class="s2">&quot;Неверный тип данных&quot;</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="ne">KeyError</span><span class="p">(</span><span class="s2">&quot;Ключ не найден&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="p">])</span>
<span class="unselectable"><span class="o">...</span> </span><span class="k">except</span><span class="o">*</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">v_errors</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">for</span> <span class="n">error</span> <span class="ow">in</span> <span class="n">v_errors</span><span class="o">.</span><span class="n">exceptions</span><span class="p">:</span>  <span class="c1"># Итерируемся по списку исключений внутри группы</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Обработан ValueError: </span><span class="si">{</span><span class="n">error</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span><span class="k">except</span><span class="o">*</span> <span class="ne">TypeError</span> <span class="k">as</span> <span class="n">t_errors</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">for</span> <span class="n">error</span> <span class="ow">in</span> <span class="n">t_errors</span><span class="o">.</span><span class="n">exceptions</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Обработан TypeError: </span><span class="si">{</span><span class="n">error</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span></span>
<span class="unselectable"><span class="n">Обработан</span> <span class="ne">ValueError</span><span class="p">:</span> <span class="n">Некорректное</span> <span class="n">значение</span></span>
<span class="unselectable"><span class="n">Обработан</span> <span class="ne">TypeError</span><span class="p">:</span> <span class="n">Неверный</span> <span class="n">тип</span> <span class="n">данных</span></span>
<span class="unselectable">  <span class="o">+</span> <span class="ne">Exception</span> <span class="n">Group</span> <span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span></span>
<span class="unselectable">  <span class="o">|</span>   <span class="n">File</span> <span class="s2">&quot;&lt;stdin&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">2</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span></span>
<span class="unselectable">  <span class="o">|</span> <span class="n">ExceptionGroup</span><span class="p">:</span> <span class="n">Ошибка</span> <span class="n">выполнения</span> <span class="n">операций</span> <span class="p">(</span><span class="mi">1</span> <span class="n">sub</span><span class="o">-</span><span class="n">exception</span><span class="p">)</span></span>
<span class="unselectable">  <span class="o">+-+----------------</span> <span class="mi">1</span> <span class="o">----------------</span></span>
<span class="unselectable">    <span class="o">|</span> <span class="ne">KeyError</span><span class="p">:</span> <span class="s1">&#39;Ключ не найден&#39;</span></span>
<span class="unselectable">    <span class="o">+------------------------------------</span></span>
</pre></div></div></div>

<h3>Пример 3: Вложенные ExceptionGroup</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="k">raise</span> <span class="n">ExceptionGroup</span><span class="p">(</span><span class="s2">&quot;Основная группа&quot;</span><span class="p">,</span> <span class="p">[</span>
        <span class="n">ExceptionGroup</span><span class="p">(</span><span class="s2">&quot;Первая подгруппа&quot;</span><span class="p">,</span> <span class="p">[</span>
            <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Некорректное значение&quot;</span><span class="p">),</span>
            <span class="ne">KeyError</span><span class="p">(</span><span class="s2">&quot;Ключ не найден&quot;</span><span class="p">),</span>
        <span class="p">]),</span>
        <span class="ne">TypeError</span><span class="p">(</span><span class="s2">&quot;Неверный тип данных&quot;</span><span class="p">),</span>
    <span class="p">])</span>
<span class="k">except</span> <span class="n">ExceptionGroup</span> <span class="k">as</span> <span class="n">eg</span><span class="p">:</span>
    <span class="k">pass</span>
</pre></div></div></div>

<h3>Пример 4: Комбинирование и повторное создание ExceptionGroup</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">function_that_raises</span><span class="p">():</span>
    <span class="n">errors</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Первый ValueError&quot;</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">errors</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s2">&quot;Первый TypeError&quot;</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">TypeError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">errors</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">errors</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">ExceptionGroup</span><span class="p">(</span><span class="s2">&quot;Группа исключений в функции&quot;</span><span class="p">,</span> <span class="n">errors</span><span class="p">)</span>

<span class="k">try</span><span class="p">:</span>
    <span class="n">function_that_raises</span><span class="p">()</span>
<span class="k">except</span> <span class="n">ExceptionGroup</span> <span class="k">as</span> <span class="n">eg</span><span class="p">:</span>
    <span class="k">pass</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">try</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">raise</span> <span class="n">ExceptionGroup</span><span class="p">(</span><span class="s2">&quot;Ошибка выполнения операций&quot;</span><span class="p">,</span> <span class="p">[</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Некорректное значение&quot;</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="ne">TypeError</span><span class="p">(</span><span class="s2">&quot;Неверный тип данных&quot;</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="ne">KeyError</span><span class="p">(</span><span class="s2">&quot;Ключ не найден&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="p">])</span>
<span class="unselectable"><span class="o">...</span> </span><span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">exceptions</span><span class="p">)</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="go">(ValueError(&#39;Некорректное значение&#39;), TypeError(&#39;Неверный тип данных&#39;), KeyError(&#39;Ключ не найден&#39;))</span>
</span></pre></div></div></div>