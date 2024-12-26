<p><code>match-case</code> — это мощная конструкция в Python, введённая в версии 3.10,
для реализации сопоставления с образцом (pattern matching).
Она позволяет писать более читаемый и лаконичный код для работы с разными типами данных, структур и условий.</p>
<h2>Синтаксис</h2>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">match</span> <span class="n">значение</span><span class="p">:</span>
    <span class="k">case</span> <span class="n">шаблон1</span><span class="p">:</span>
        <span class="c1"># Код для шаблона1</span>
    <span class="k">case</span> <span class="n">шаблон2</span> <span class="k">if</span> <span class="n">условие</span><span class="p">:</span>
        <span class="c1"># Код для шаблона2 при выполнении условия</span>
    <span class="k">case</span><span class="w"> </span><span class="k">_</span><span class="p">:</span>
        <span class="c1"># Код по умолчанию (аналог else)</span>
</pre></div></div></div>

<h1>Особенности и ключевые фишки</h1>
<h3>Сопоставление по значению</h3>
<p>Простое сопоставление с конкретным значением</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">match</span> <span class="n">x</span><span class="p">:</span>
   <span class="k">case</span> <span class="mi">1</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;x равно 1&quot;</span><span class="p">)</span>
   <span class="k">case</span> <span class="mi">2</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;x равно 2&quot;</span><span class="p">)</span>
   <span class="k">case</span><span class="w"> </span><span class="k">_</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Другое значение&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Сопоставление с переменной</h3>
<p>Переменные в шаблонах записываются как есть, а <code>_</code> используется как "любое значение"</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">match</span> <span class="n">x</span><span class="p">:</span>
   <span class="k">case</span> <span class="n">y</span> <span class="k">if</span> <span class="n">y</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Положительное число: </span><span class="si">{</span><span class="n">y</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
   <span class="k">case</span><span class="w"> </span><span class="k">_</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Не положительное число&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Сопоставление с коллекциями</h3>
<p>Списки, кортежи и их элементы:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">match</span> <span class="n">lst</span><span class="p">:</span>
   <span class="k">case</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Список точно равен [1, 2, 3]&quot;</span><span class="p">)</span>
   <span class="k">case</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="o">*</span><span class="n">rest</span><span class="p">]:</span>  <span class="c1"># Распаковка</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Начинается с 1, остальные элементы: </span><span class="si">{</span><span class="n">rest</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
   <span class="k">case</span><span class="w"> </span><span class="k">_</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Неизвестный список&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Сопоставление с объектами</h3>
<p>Использование <code>attr</code> для проверки полей объекта:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Point</span><span class="p">:</span>
   <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
       <span class="bp">self</span><span class="o">.</span><span class="n">x</span> <span class="o">=</span> <span class="n">x</span>
       <span class="bp">self</span><span class="o">.</span><span class="n">y</span> <span class="o">=</span> <span class="n">y</span>

<span class="n">point</span> <span class="o">=</span> <span class="n">Point</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>

<span class="k">match</span> <span class="n">point</span><span class="p">:</span>
   <span class="k">case</span> <span class="n">Point</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Точка в начале координат&quot;</span><span class="p">)</span>
   <span class="k">case</span> <span class="n">Point</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span> <span class="k">if</span> <span class="n">x</span> <span class="o">==</span> <span class="n">y</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Точка на линии y = x: (</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s2">, </span><span class="si">{</span><span class="n">y</span><span class="si">}</span><span class="s2">)&quot;</span><span class="p">)</span>
   <span class="k">case</span> <span class="n">Point</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Координаты точки: (</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s2">, </span><span class="si">{</span><span class="n">y</span><span class="si">}</span><span class="s2">)&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Вложенные структуры</h3>
<p>Сопоставление сложных вложенных структур:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">match</span> <span class="n">data</span><span class="p">:</span>
   <span class="k">case</span><span class="w"> </span><span class="p">{</span><span class="s2">&quot;user&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;id&quot;</span><span class="p">:</span> <span class="nb">int</span><span class="p">(</span><span class="nb">id</span><span class="k">_</span><span class="p">),</span> <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">name</span><span class="p">)}}:</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;ID: </span><span class="si">{</span><span class="n">id_</span><span class="si">}</span><span class="s2">, Name: </span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
   <span class="k">case</span><span class="w"> </span><span class="k">_</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Неподходящая структура&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Комбинация условий (OR)</h3>
<p>Использование <code>|</code> для нескольких шаблонов:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">match</span> <span class="n">x</span><span class="p">:</span>
   <span class="k">case</span> <span class="mi">1</span> <span class="o">|</span> <span class="mi">2</span> <span class="o">|</span> <span class="mi">3</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;x равно 1, 2 или 3&quot;</span><span class="p">)</span>
   <span class="k">case</span><span class="w"> </span><span class="k">_</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Другое значение&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Сопоставление с литералами и типами</h3>
<p>Проверка типов:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">match</span> <span class="n">obj</span><span class="p">:</span>
   <span class="k">case</span> <span class="nb">int</span><span class="p">():</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Это целое число&quot;</span><span class="p">)</span>
   <span class="k">case</span> <span class="nb">str</span><span class="p">()</span> <span class="k">as</span> <span class="n">s</span> <span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">isdigit</span><span class="p">():</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Это строка с числом: </span><span class="si">{</span><span class="n">s</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
   <span class="k">case</span><span class="w"> </span><span class="k">_</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Другой тип&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h1>Примеры с пояснениями</h1>
<h3>Обработка HTTP-статусов</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">match</span> <span class="n">status_code</span><span class="p">:</span>
   <span class="k">case</span> <span class="mi">200</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;OK&quot;</span><span class="p">)</span>
   <span class="k">case</span> <span class="mi">404</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Not Found&quot;</span><span class="p">)</span>
   <span class="k">case</span> <span class="mi">500</span> <span class="o">|</span> <span class="mi">501</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Server Error&quot;</span><span class="p">)</span>
   <span class="k">case</span><span class="w"> </span><span class="k">_</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Unknown status&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Работа с JSON-данными</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;error&quot;</span><span class="p">,</span> <span class="s2">&quot;code&quot;</span><span class="p">:</span> <span class="mi">500</span><span class="p">}</span>

<span class="k">match</span> <span class="n">data</span><span class="p">:</span>
   <span class="k">case</span> <span class="p">{</span><span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;error&quot;</span><span class="p">,</span> <span class="s2">&quot;code&quot;</span><span class="p">:</span> <span class="n">code</span><span class="p">}</span> <span class="k">if</span> <span class="n">code</span> <span class="o">&gt;=</span> <span class="mi">500</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Критическая ошибка: </span><span class="si">{</span><span class="n">code</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
   <span class="k">case</span> <span class="p">{</span><span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;success&quot;</span><span class="p">,</span> <span class="s2">&quot;data&quot;</span><span class="p">:</span> <span class="n">content</span><span class="p">}:</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Успешный ответ: </span><span class="si">{</span><span class="n">content</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
   <span class="k">case</span><span class="w"> </span><span class="k">_</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Неизвестный формат&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Анализ выражений</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">expr</span> <span class="o">=</span> <span class="p">(</span><span class="s2">&quot;+&quot;</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>

<span class="k">match</span> <span class="n">expr</span><span class="p">:</span>
   <span class="k">case</span> <span class="p">(</span><span class="s2">&quot;+&quot;</span><span class="p">,</span> <span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Сумма: </span><span class="si">{</span><span class="n">a</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">b</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
   <span class="k">case</span> <span class="p">(</span><span class="s2">&quot;*&quot;</span><span class="p">,</span> <span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Произведение: </span><span class="si">{</span><span class="n">a</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">b</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
   <span class="k">case</span><span class="w"> </span><span class="k">_</span><span class="p">:</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Неизвестное выражение&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Пример с сопоставлением точек</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">match</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
   <span class="k">case</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">):</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Начало координат&quot;</span><span class="p">)</span>
   <span class="k">case</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="mi">0</span><span class="p">):</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;На оси X, x = </span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
   <span class="k">case</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;На оси Y, y = </span><span class="si">{</span><span class="n">y</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
   <span class="k">case</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
       <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;В точке (</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s2">, </span><span class="si">{</span><span class="n">y</span><span class="si">}</span><span class="s2">)&quot;</span><span class="p">)</span>
</pre></div></div></div>