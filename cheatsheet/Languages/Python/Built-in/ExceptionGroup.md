<p>ExceptionGroup в Python появился в версии 3.11
Позволяет объединять несколько исключений в одно</p>
<h3>Пример 1: Создание ExceptionGroup</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="k">raise</span> <span class="n">ExceptionGroup</span><span class="p">(</span><span class="s2">&quot;Ошибка выполнения операций&quot;</span><span class="p">,</span> <span class="p">[</span>
        <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Некорректное значение&quot;</span><span class="p">),</span>
        <span class="ne">TypeError</span><span class="p">(</span><span class="s2">&quot;Неверный тип данных&quot;</span><span class="p">),</span>
        <span class="ne">KeyError</span><span class="p">(</span><span class="s2">&quot;Ключ не найден&quot;</span><span class="p">)</span>
    <span class="p">])</span>
<span class="k">except</span> <span class="n">ExceptionGroup</span> <span class="k">as</span> <span class="n">eg</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Произошло </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">eg</span><span class="o">.</span><span class="n">exceptions</span><span class="p">)</span><span class="si">}</span><span class="s2"> исключений:&quot;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">exc</span> <span class="ow">in</span> <span class="n">eg</span><span class="o">.</span><span class="n">exceptions</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;- </span><span class="si">{</span><span class="n">exc</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">exc</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>

<details>
<summary>output</summary>

<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>Произошло 3 исключений:
- ValueError: Некорректное значение
- TypeError: Неверный тип данных
- KeyError: &#39;Ключ не найден&#39;
</pre></div></div></div>

</details>

<h3>Пример 2: Обработка отдельных исключений внутри группы</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="k">raise</span> <span class="n">ExceptionGroup</span><span class="p">(</span><span class="s2">&quot;Ошибка выполнения операций&quot;</span><span class="p">,</span> <span class="p">[</span>
        <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Некорректное значение&quot;</span><span class="p">),</span>
        <span class="ne">TypeError</span><span class="p">(</span><span class="s2">&quot;Неверный тип данных&quot;</span><span class="p">),</span>
        <span class="ne">KeyError</span><span class="p">(</span><span class="s2">&quot;Ключ не найден&quot;</span><span class="p">)</span>
    <span class="p">])</span>
<span class="k">except</span><span class="o">*</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">v_errors</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">error</span> <span class="ow">in</span> <span class="n">v_errors</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Обработан ValueError: </span><span class="si">{</span><span class="n">error</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="k">except</span><span class="o">*</span> <span class="ne">TypeError</span> <span class="k">as</span> <span class="n">t_errors</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">error</span> <span class="ow">in</span> <span class="n">t_errors</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Обработан TypeError: </span><span class="si">{</span><span class="n">error</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>

<details>
<summary>output</summary>

<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>| ExceptionGroup:  (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Exception Group Traceback (most recent call last):
    |   File &quot;&lt;stdin&gt;&quot;, line 2, in &lt;module&gt;
    | ExceptionGroup: Ошибка выполнения операций (1 sub-exception)
    +-+---------------- 1 ----------------
      | ValueError: Некорректное значение
      +------------------------------------
    |
    | During handling of the above exception, another exception occurred:
    |
    | Traceback (most recent call last):
    |   File &quot;&lt;stdin&gt;&quot;, line 8, in &lt;module&gt;
    | TypeError: &#39;ExceptionGroup&#39; object is not iterable
    +---------------- 2 ----------------
    | Exception Group Traceback (most recent call last):
    |   File &quot;&lt;stdin&gt;&quot;, line 2, in &lt;module&gt;
    | ExceptionGroup: Ошибка выполнения операций (1 sub-exception)
    +-+---------------- 1 ----------------
      | TypeError: Неверный тип данных
      +------------------------------------
    |
    | During handling of the above exception, another exception occurred:
    |
    | Traceback (most recent call last):
    |   File &quot;&lt;stdin&gt;&quot;, line 11, in &lt;module&gt;
    | TypeError: &#39;ExceptionGroup&#39; object is not iterable
    +---------------- 3 ----------------
    | Exception Group Traceback (most recent call last):
    |   File &quot;&lt;stdin&gt;&quot;, line 2, in &lt;module&gt;
    | ExceptionGroup: Ошибка выполнения операций (1 sub-exception)
    +-+---------------- 1 ----------------
      | KeyError: &#39;Ключ не найден&#39;
      +------------------------------------
</pre></div></div></div>

</details>

<h3>Пример 3: Вложенные ExceptionGroup</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">try</span><span class="p">:</span>
    <span class="k">raise</span> <span class="n">ExceptionGroup</span><span class="p">(</span><span class="s2">&quot;Основная группа&quot;</span><span class="p">,</span> <span class="p">[</span>
        <span class="n">ExceptionGroup</span><span class="p">(</span><span class="s2">&quot;Первая подгруппа&quot;</span><span class="p">,</span> <span class="p">[</span>
            <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Некорректное значение&quot;</span><span class="p">),</span>
            <span class="ne">KeyError</span><span class="p">(</span><span class="s2">&quot;Ключ не найден&quot;</span><span class="p">)</span>
        <span class="p">]),</span>
        <span class="ne">TypeError</span><span class="p">(</span><span class="s2">&quot;Неверный тип данных&quot;</span><span class="p">)</span>
    <span class="p">])</span>
<span class="k">except</span> <span class="n">ExceptionGroup</span> <span class="k">as</span> <span class="n">eg</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Основная группа исключений: </span><span class="si">{</span><span class="n">eg</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">exc</span> <span class="ow">in</span> <span class="n">eg</span><span class="o">.</span><span class="n">exceptions</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;- </span><span class="si">{</span><span class="n">exc</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>

<details>
<summary>output</summary>

<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>Основная группа исключений: Основная группа (2 sub-exceptions)
- Первая подгруппа (2 sub-exceptions)
- Неверный тип данных
</pre></div></div></div>

</details>

<h3>Пример 4: Комбинирование и повторное создание ExceptionGroup</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">function_that_raises</span><span class="p">():</span>
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
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Обработан ExceptionGroup: </span><span class="si">{</span><span class="n">eg</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">exc</span> <span class="ow">in</span> <span class="n">eg</span><span class="o">.</span><span class="n">exceptions</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;- </span><span class="si">{</span><span class="n">exc</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>
<details>
<summary>output</summary>

<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>Обработан ExceptionGroup: Группа исключений в функции (2 sub-exceptions)
- Первый ValueError
- Первый TypeError
</pre></div></div></div>

</details>