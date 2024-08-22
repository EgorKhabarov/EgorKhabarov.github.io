<p>Библиотека "bisect" в Python используется для выполнения бинарного поиска в отсортированных последовательностях.
Она предоставляет функции для нахождения места вставки элемента в отсортированный список и для выполнения деления списка на две части.</p>
<p>Методы библиотеки "bisect":
bisect_left(a, x): Возвращает наименьшую позицию для вставки элемента x в отсортированный список а, сохраняя его отсортированность.
bisect_right(a, x): Возвращает наибольшую позицию для вставки элемента x в отсортированный список а, сохраняя его отсортированность.
bisect(a, x): Эквивалентно вызову bisect_right(a, x).
insort_left(a, x): Вставляет элемент x в отсортированный список a на наименьшую позицию, сохраняя его отсортированность.
insort_right(a, x): Вставляет элемент x в отсортированный список a на наибольшую позицию, сохраняя его отсортированность.
insort(a, x): Эквивалентно вызову insort_right(a, x).</p>
<p>bisect_left(a, x) - возвращает индекс наименьшего элемента, который больше или равен x.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">bisect</span>
<span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
<span class="n">x</span> <span class="o">=</span> <span class="mi">4</span>
<span class="n">index</span> <span class="o">=</span> <span class="n">bisect</span><span class="o">.</span><span class="n">bisect_left</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>  <span class="c1"># 2</span>
</pre></div></div></div>

<p>insort_right(a, x) - вставляет элемент x в отсортированный список a на наибольшую позицию, сохраняя его отсортированность.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">bisect</span>
<span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
<span class="n">x</span> <span class="o">=</span> <span class="mi">4</span>
<span class="n">bisect</span><span class="o">.</span><span class="n">insort_right</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>  <span class="c1"># [1, 3, 4, 5, 7]</span>
</pre></div></div></div>

<p>bisect_right(a, x) - возвращает индекс первого элемента, который больше x.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">bisect</span>
<span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
<span class="n">x</span> <span class="o">=</span> <span class="mi">4</span>
<span class="n">index</span> <span class="o">=</span> <span class="n">bisect</span><span class="o">.</span><span class="n">bisect_right</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>  <span class="c1"># 3</span>
</pre></div></div></div>