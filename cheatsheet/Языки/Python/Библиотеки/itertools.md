<p>Модуль itertools
Возвращает итератор, который генерирует бесконечный ряд чисел, начиная с start, с шагом step.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code81b" onclick="copyCode(code81, code81b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code81"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">count</span>

<span class="n">count</span><span class="p">(</span><span class="n">start</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">step</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который бесконечно циклит элементы в iterable.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code82b" onclick="copyCode(code82, code82b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code82"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">cycle</span>

<span class="n">cycle</span><span class="p">(</span><span class="n">iterable</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который генерирует все возможные перестановки 
элементов iterable с длиной r (по умолчанию длина равна длине iterable).
Если r задан, то выдаются только перестановки из r элементов.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code83b" onclick="copyCode(code83, code83b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code83"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">permutations</span>

<span class="n">permutations</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">r</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который генерирует все возможные комбинации элементов iterable с длиной r.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code84b" onclick="copyCode(code84, code84b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code84"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">combinations</span>

<span class="n">combinations</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">r</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который генерирует все возможные комбинации элементов iterable с длиной r, с повторением элементов.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code85b" onclick="copyCode(code85, code85b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code85"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">combinations_with_replacement</span>

<span class="n">combinations_with_replacement</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">r</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который объединяет несколько итераторов в один.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code86b" onclick="copyCode(code86, code86b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code86"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">chain</span>

<span class="n">chain</span><span class="p">(</span><span class="o">*</span><span class="n">iterables</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который объединяет элементы из каждого итератора в кортежи. 
Если итераторы разных длин, то элементы для дополнения берутся из fillvalue.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code87b" onclick="copyCode(code87, code87b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code87"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">zip_longest</span>

<span class="n">zip_longest</span><span class="p">(</span><span class="o">*</span><span class="n">iterables</span><span class="p">,</span> <span class="n">fillvalue</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который группирует элементы iterable по значениям функции key.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code88b" onclick="copyCode(code88, code88b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code88"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">groupby</span>

<span class="n">groupby</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт элементы из iterable, начиная с start, и заканчивая stop, с шагом step.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code89b" onclick="copyCode(code89, code89b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code89"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">islice</span>

<span class="n">islice</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">start</span><span class="p">,</span> <span class="n">stop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">step</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который применяет функцию function к каждому элементу iterable, который представлен в виде кортежа.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code90b" onclick="copyCode(code90, code90b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code90"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">starmap</span>

<span class="n">starmap</span><span class="p">(</span><span class="n">function</span><span class="p">,</span> <span class="n">iterable</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт все возможные пары (или кортежи) элементов из каждого из iterables. 
repeat определяет, сколько раз каждый итератор будет повторен.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code91b" onclick="copyCode(code91, code91b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code91"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">product</span>

<span class="n">product</span><span class="p">(</span><span class="o">*</span><span class="n">iterables</span><span class="p">,</span> <span class="n">repeat</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт сумму (или другую комбинацию) элементов iterable, используя функцию func.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code92b" onclick="copyCode(code92, code92b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code92"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">accumulate</span>

<span class="n">accumulate</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">func</span><span class="o">=</span><span class="n">operator</span><span class="o">.</span><span class="n">add</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт элементы data, соответствующие истинным значениям selectors.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code93b" onclick="copyCode(code93, code93b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code93"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">compress</span>

<span class="n">compress</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">selectors</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт элементы iterable после первого элемента, для которого predicate вернёт ложное значение.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code94b" onclick="copyCode(code94, code94b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code94"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">dropwhile</span>

<span class="n">dropwhile</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">iterable</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт элементы iterable, для которых predicate вернёт ложное значение.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code95b" onclick="copyCode(code95, code95b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code95"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">filterfalse</span>

<span class="n">filterfalse</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">iterable</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт пары соседних элементов из iterable.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code96b" onclick="copyCode(code96, code96b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code96"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">pairwise</span>

<span class="n">pairwise</span><span class="p">(</span><span class="n">iterable</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт object times раз (бесконечное количество раз, если times не указан).</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code97b" onclick="copyCode(code97, code97b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code97"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">repeat</span>

<span class="n">repeat</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span> <span class="n">times</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт элементы iterable до первого элемента, для которого predicate вернёт ложное значение.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code98b" onclick="copyCode(code98, code98b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code98"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">takewhile</span>

<span class="n">takewhile</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">iterable</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает n независимых итераторов, каждый из которых может быть 
использован независимо для перебора элементов исходного iterable.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code99b" onclick="copyCode(code99, code99b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code99"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">tee</span>

<span class="n">tee</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">n</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</pre></div></div></div>