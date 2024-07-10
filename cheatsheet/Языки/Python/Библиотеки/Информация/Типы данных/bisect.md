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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code002b824f50e290d43bebf1ad821e2084b" onclick="copyCode(code002b824f50e290d43bebf1ad821e2084, code002b824f50e290d43bebf1ad821e2084b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code002b824f50e290d43bebf1ad821e2084"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">bisect</span>
<span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
<span class="n">x</span> <span class="o">=</span> <span class="mi">4</span>
<span class="n">index</span> <span class="o">=</span> <span class="n">bisect</span><span class="o">.</span><span class="n">bisect_left</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>  <span class="c1"># Output: 2</span>
</pre></div></div></div>

<p>insort_right(a, x) - вставляет элемент x в отсортированный список a на наибольшую позицию, сохраняя его отсортированность.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeb45f00399120e0bf619210e441d14114b" onclick="copyCode(codeb45f00399120e0bf619210e441d14114, codeb45f00399120e0bf619210e441d14114b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeb45f00399120e0bf619210e441d14114"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">bisect</span>
<span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
<span class="n">x</span> <span class="o">=</span> <span class="mi">4</span>
<span class="n">bisect</span><span class="o">.</span><span class="n">insort_right</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>  <span class="c1"># Output: [1, 3, 4, 5, 7]</span>
</pre></div></div></div>

<p>bisect_right(a, x) - возвращает индекс первого элемента, который больше x.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codee936c35879723ee6dc41942e4ccc5e71b" onclick="copyCode(codee936c35879723ee6dc41942e4ccc5e71, codee936c35879723ee6dc41942e4ccc5e71b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codee936c35879723ee6dc41942e4ccc5e71"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">bisect</span>
<span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
<span class="n">x</span> <span class="o">=</span> <span class="mi">4</span>
<span class="n">index</span> <span class="o">=</span> <span class="n">bisect</span><span class="o">.</span><span class="n">bisect_right</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>  <span class="c1"># Output: 3</span>
</pre></div></div></div>