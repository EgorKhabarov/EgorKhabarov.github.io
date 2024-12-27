<p><code>malloc</code> (<strong>memory allocation</strong>) — это функция стандартной библиотеки языка программирования C,
которая используется для динамического выделения памяти в куче (<code>heap</code>).
Она выделяет запрашиваемое количество байт памяти и возвращает указатель на первый байт выделенной области.
Функция объявлена в заголовочном файле <code>&lt;stdlib.h&gt;</code>.</p>
<h3>Синтаксис</h3>
<div class="code_element"><div class="lang_line"><text>c</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-c"><div class="highlight"><pre><span></span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="nf">malloc</span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>
</pre></div></div></div>

<h3>Параметры</h3>
<ul>
<li><strong>size</strong>: Количество байт, которое нужно выделить.</li>
</ul>
<h3>Возвращаемое значение:</h3>
<ul>
<li>Указатель на выделенную память, если операция прошла успешно.</li>
<li>Если памяти недостаточно для выделения, возвращается <code>NULL</code>.</li>
</ul>
<h3>Пример использования</h3>
<div class="code_element"><div class="lang_line"><text>c</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-c"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;stdio.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;stdlib.h&gt;</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// Выделяем память для массива из 5 целых чисел</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">arr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="p">)</span><span class="w"> </span><span class="n">malloc</span><span class="p">(</span><span class="mi">5</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Проверяем, успешно ли выделена память</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">arr</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="nb">NULL</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">printf</span><span class="p">(</span><span class="s">&quot;Ошибка: недостаточно памяти!</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">);</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Заполняем массив значениями</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">5</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">arr</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Выводим массив</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">5</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">printf</span><span class="p">(</span><span class="s">&quot;%d &quot;</span><span class="p">,</span><span class="w"> </span><span class="n">arr</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Освобождаем выделенную память</span>
<span class="w">    </span><span class="n">free</span><span class="p">(</span><span class="n">arr</span><span class="p">);</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div></div></div>

<h3>Важные моменты</h3>
<ol>
<li><strong>Инициализация памяти</strong>: Память, выделенная с помощью <code>malloc</code>, не инициализируется.
Это значит, что она содержит произвольные данные. Если требуется инициализация нулями, нужно использовать функцию <code>calloc</code>.</li>
<li><strong>Освобождение памяти</strong>: Память, выделенная через <code>malloc</code>, должна быть освобождена с помощью функции <code>free()</code>,
чтобы избежать утечек памяти.</li>
<li><strong>Тип возвращаемого значения</strong>: <code>malloc</code> возвращает указатель типа <code>void*</code>,
который может быть преобразован в указатель любого другого типа.</li>
</ol>
<h3>Разница с другими функциями выделения памяти</h3>
<ul>
<li><strong><code>calloc</code></strong>: Выделяет память и инициализирует её нулями.</li>
<li><strong><code>realloc</code></strong>: Изменяет размер уже выделенной области памяти.</li>
<li><strong><code>free</code></strong>: Освобождает ранее выделенную память.</li>
</ul>
<h3>Пример с использованием <code>calloc</code></h3>
<div class="code_element"><div class="lang_line"><text>c</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-c"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">arr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="p">)</span><span class="w"> </span><span class="n">calloc</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">));</span><span class="w">  </span><span class="c1">// выделяет память для 5 элементов и заполняет её нулями</span>
</pre></div></div></div>