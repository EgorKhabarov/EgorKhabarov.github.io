<h1 id="Бесконечныеитераторы">Бесконечные итераторы</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Результат</th>
</tr>
</thead>
<tbody>
<tr>
<td>count(start, [step])</td>
<td>count(3, 2)</td>
<td>3 5 7 9…</td>
</tr>
<tr>
<td>cycle(p)</td>
<td>cycle("ABC")</td>
<td>A B С А В…</td>
</tr>
<tr>
<td>repeat(elem [,n])</td>
<td>repeat("x", 5)</td>
<td>x x x x x</td>
</tr>
</tbody>
</table>
<h1 id="Итераторы,которыезавершаютсянасамойкороткойпоследовательности">Итераторы, которые завершаются на самой короткой последовательности</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Результат</th>
</tr>
</thead>
<tbody>
<tr>
<td>accumulate(p [,func])</td>
<td>accumulate([1,2,3,4,5])</td>
<td>1 3 6 10 15</td>
</tr>
<tr>
<td>chain(p, q)</td>
<td>chain("ABC", "DE")</td>
<td>A B C D E</td>
</tr>
<tr>
<td>chain.from_iterable(p)</td>
<td>chain.from_iterable(["ABC", "DE"])</td>
<td>A B C D E</td>
</tr>
<tr>
<td>compress(data, selectors)</td>
<td>compress("ABCDE", (0, 1, 0, 0, 1))</td>
<td>B E</td>
</tr>
<tr>
<td>dropwhile(pred, seq)</td>
<td>dropwhile(lambda x: x &lt; 0, [1, 0, -1, 1, -1])</td>
<td>1 0 -1 1 -1</td>
</tr>
<tr>
<td>filterfalse(pred, seq)</td>
<td>filterfalse(lambda x: x &lt; 0, [1, 0, -1, 1, -1])</td>
<td>1 0 1</td>
</tr>
<tr>
<td>groupby(iterable[, key])</td>
<td>groupby((3, 4, 0, -1), key=lambda x: x &gt; 0)</td>
<td>True [3, 4] False [0, -1]</td>
</tr>
<tr>
<td>islice(seq, [start,] stop [, step])</td>
<td>islice("ABCDEFGH", 1, 6, 2)</td>
<td>B D F</td>
</tr>
<tr>
<td>pairwise(iterable)</td>
<td>pairwise("ABcd12")</td>
<td>AB Bc cd d1 12</td>
</tr>
<tr>
<td>starmap(func, seq)</td>
<td>starmap(operator.mul, ((1, 2), (3, 4)))</td>
<td>2 12</td>
</tr>
<tr>
<td>takewhile(pred, seq)</td>
<td>takewhile(lambda x: x &lt; 0, [1, 0, -1, 1, -1])</td>
<td></td>
</tr>
<tr>
<td>tee(it, n)</td>
<td>tee([1, 2], 3)</td>
<td>[1, 2], [1, 2], [1, 2]</td>
</tr>
<tr>
<td>zip_longest(p, q, …[, fillvalue=None])</td>
<td>zip_longest((1, 2), ("A",), fillvalue="_")</td>
<td>(1, "A") (2, "_")</td>
</tr>
</tbody>
</table>
<h1 id="Комбинаторныеитераторы">Комбинаторные итераторы</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Результат</th>
</tr>
</thead>
<tbody>
<tr>
<td>product(p, q, …[, repeat=1])</td>
<td>product(("A", "B"), repeat=2)</td>
<td>(A, A) (A, B) (B A) (B B)</td>
</tr>
<tr>
<td>permutations(p[, r])</td>
<td>permutations(("a", "b", "c"), 2)</td>
<td>("a", "b") ("a", "c") ("b", "a") ("b", "c") ("c", "a") ("c", "b")</td>
</tr>
<tr>
<td>combinations(p, r)</td>
<td>combinations("ABC", 2)</td>
<td>("A", "B") ("A", "C") ("B", "C")</td>
</tr>
<tr>
<td>combinations_with_replacement(p, r)</td>
<td>combinations_with_replacement("ABC", 2)</td>
<td>("A", "A") ("A", "B") ("A", "C") ("B", "B") ("B", "C") ("C", "C")</td>
</tr>
</tbody>
</table>
<h1 id="Модульitertools">Модуль itertools</h1>
<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">def</span> <span class="nf">print_iterator</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="k">try</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>            <span class="nb">print</span><span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="n">x</span><span class="p">),</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="k">except</span> <span class="ne">StopIteration</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>            <span class="k">break</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">()</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Генерирует бесконечный ряд чисел, начиная с start, с шагом step</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">count</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">count</span><span class="p">(</span><span class="n">start</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">step</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="unselectable"><span class="go">0 1 2 3 4</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Бесконечно циклит элементы в iterable</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">cycle</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">cycle</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">])</span>
<span class="unselectable"><span class="go">1 2 3 1 2</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Генерирует все возможные перестановки элементов iterable с длиной r</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># по умолчанию длина равна длине iterable</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">permutations</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">permutations</span><span class="p">(</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span> <span class="n">r</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
<span class="unselectable"><span class="go">(&quot;1&quot;, &quot;2&quot;, &quot;3&quot;, &quot;4&quot;, &quot;5&quot;) (&quot;1&quot;, &quot;2&quot;, &quot;3&quot;, &quot;5&quot;, &quot;4&quot;) (&quot;1&quot;, &quot;2&quot;, &quot;4&quot;, &quot;3&quot;, &quot;5&quot;) (&quot;1&quot;, &quot;2&quot;, &quot;4&quot;, &quot;5&quot;, &quot;3&quot;) (&quot;1&quot;, &quot;2&quot;, &quot;5&quot;, &quot;3&quot;, &quot;4&quot;)</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">permutations</span><span class="p">(</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span> <span class="n">r</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="unselectable"><span class="go">(&quot;1&quot;, &quot;2&quot;) (&quot;1&quot;, &quot;3&quot;) (&quot;1&quot;, &quot;4&quot;) (&quot;1&quot;, &quot;5&quot;) (&quot;2&quot;, &quot;1&quot;)</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Генерирует все возможные комбинации элементов iterable с длиной r</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">combinations</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">combinations</span><span class="p">(</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span> <span class="n">r</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="unselectable"><span class="go">(&quot;1&quot;, &quot;2&quot;) (&quot;1&quot;, &quot;3&quot;) (&quot;1&quot;, &quot;4&quot;) (&quot;1&quot;, &quot;5&quot;) (&quot;2&quot;, &quot;3&quot;)</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Генерирует все возможные комбинации элементов iterable с длиной r, с повторением элементов</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">combinations_with_replacement</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">combinations_with_replacement</span><span class="p">(</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span> <span class="n">r</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="unselectable"><span class="go">(&quot;1&quot;, &quot;1&quot;) (&quot;1&quot;, &quot;2&quot;) (&quot;1&quot;, &quot;3&quot;) (&quot;1&quot;, &quot;4&quot;) (&quot;1&quot;, &quot;5&quot;)</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">Объединяет</span> <span class="n">несколько</span> <span class="n">итераторов</span> <span class="n">в</span> <span class="n">один</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">chain</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">chain</span><span class="p">((</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">))</span>
<span class="unselectable"><span class="go">1 2 4 5</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Объединяет элементы из каждого итератора в кортежи</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Если итераторы разных длин, то элементы для дополнения берутся из fillvalue</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">zip_longest</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">zip_longest</span><span class="p">((</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;A&quot;</span><span class="p">,),</span> <span class="n">fillvalue</span><span class="o">=</span><span class="s2">&quot;_&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">(1, &quot;A&quot;) (2, &quot;_&quot;)</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Группирует элементы iterable по значениям функции key</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">groupby</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">groupby</span><span class="p">((</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">),</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span>
<span class="unselectable"><span class="go">True [3, 4] False [0, -1]</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Выдаёт элементы из iterable, начиная с start, и заканчивая stop, с шагом step</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">islice</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">islice</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">start</span><span class="p">,</span> <span class="n">stop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">step</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Применяет функцию function к каждому элементу iterable, который представлен в виде кортежа</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">starmap</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">starmap</span><span class="p">(</span><span class="n">function</span><span class="p">,</span> <span class="n">iterable</span><span class="p">)</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Выдаёт все возможные пары (или кортежи) элементов из каждого из iterables</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># repeat определяет, сколько раз каждый итератор будет повторен</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">product</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">product</span><span class="p">((</span><span class="s2">&quot;A&quot;</span><span class="p">,</span> <span class="s2">&quot;B&quot;</span><span class="p">),</span> <span class="n">repeat</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="unselectable"><span class="go">(&quot;A&quot;, &quot;A&quot;) (&quot;A&quot;, &quot;B&quot;) (&quot;B&quot;, &quot;A&quot;) (&quot;B&quot;, &quot;B&quot;)</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Выдаёт сумму (или другую комбинацию) элементов iterable, используя функцию func</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">accumulate</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># accumulate(iterable, func=operator.add)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">accumulate</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">])</span>
<span class="unselectable"><span class="go">1 3 6 10 15</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Выдаёт элементы data, соответствующие истинным значениям selectors</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">compress</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">compress</span><span class="p">(</span><span class="s2">&quot;ABCDE&quot;</span><span class="p">,</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
<span class="unselectable"><span class="go">B E</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Выдаёт элементы iterable после первого элемента, для которого predicate вернёт ложное значение</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">dropwhile</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">dropwhile</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">iterable</span><span class="p">)</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Выдаёт элементы iterable, для которых predicate вернёт ложное значение</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">filterfalse</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">filterfalse</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">])</span>
<span class="unselectable"><span class="go">1 0 1</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Выдаёт пары соседних элементов из iterable</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">pairwise</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">pairwise</span><span class="p">(</span><span class="s2">&quot;ABcd12&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">AB Bc cd d1 12</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Выдаёт object times раз</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Если times не указан бесконечное количество раз</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">repeat</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">repeat</span><span class="p">(</span><span class="s2">&quot;x&quot;</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
<span class="unselectable"><span class="go">x x x x x</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Выдаёт элементы iterable до первого элемента, для которого predicate вернёт ложное значение</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">takewhile</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">takewhile</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">iterable</span><span class="p">)</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Возвращает n независимых итераторов</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Каждый из которых может быть использован независимо для перебора элементов исходного iterable</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">tee</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">tee</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">],</span> <span class="mi">3</span><span class="p">)</span>
<span class="unselectable"><span class="go">[1, 2], [1, 2], [1, 2]</span>
<span class="o">&gt;&gt;&gt; </span></span>
</pre></div></div>
</div>