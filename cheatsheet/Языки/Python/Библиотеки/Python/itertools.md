<p>Модуль itertools
Возвращает итератор, который генерирует бесконечный ряд чисел, начиная с start, с шагом step.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code0d414e5205c4c6f3e7902998a47f7a8db"onclick="copyCode(code0d414e5205c4c6f3e7902998a47f7a8d, code0d414e5205c4c6f3e7902998a47f7a8db)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code0d414e5205c4c6f3e7902998a47f7a8d"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">count</span>

<span class="n">count</span><span class="p">(</span><span class="n">start</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">step</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который бесконечно циклит элементы в iterable.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codeaf6a0ab92f17d5ed0e537ef56ea2f6e7b"onclick="copyCode(codeaf6a0ab92f17d5ed0e537ef56ea2f6e7, codeaf6a0ab92f17d5ed0e537ef56ea2f6e7b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeaf6a0ab92f17d5ed0e537ef56ea2f6e7"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">cycle</span>

<span class="n">cycle</span><span class="p">(</span><span class="n">iterable</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который генерирует все возможные перестановки 
элементов iterable с длиной r (по умолчанию длина равна длине iterable).
Если r задан, то выдаются только перестановки из r элементов.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code27f68cdc78413f84395bfac4f02068b3b"onclick="copyCode(code27f68cdc78413f84395bfac4f02068b3, code27f68cdc78413f84395bfac4f02068b3b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code27f68cdc78413f84395bfac4f02068b3"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">permutations</span>

<span class="n">permutations</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">r</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который генерирует все возможные комбинации элементов iterable с длиной r.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code5fcf0340813b754f208d373725f67488b"onclick="copyCode(code5fcf0340813b754f208d373725f67488, code5fcf0340813b754f208d373725f67488b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code5fcf0340813b754f208d373725f67488"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">combinations</span>

<span class="n">combinations</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">r</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который генерирует все возможные комбинации элементов iterable с длиной r, с повторением элементов.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code25bc208decdeced2b431457004630b9ab"onclick="copyCode(code25bc208decdeced2b431457004630b9a, code25bc208decdeced2b431457004630b9ab)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code25bc208decdeced2b431457004630b9a"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">combinations_with_replacement</span>

<span class="n">combinations_with_replacement</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">r</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который объединяет несколько итераторов в один.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code0605f4dcd566a068164e8cf7ebd5c7e6b"onclick="copyCode(code0605f4dcd566a068164e8cf7ebd5c7e6, code0605f4dcd566a068164e8cf7ebd5c7e6b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code0605f4dcd566a068164e8cf7ebd5c7e6"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">chain</span>

<span class="n">chain</span><span class="p">(</span><span class="o">*</span><span class="n">iterables</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который объединяет элементы из каждого итератора в кортежи. 
Если итераторы разных длин, то элементы для дополнения берутся из fillvalue.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code444d37f41b5ccc9ce3c128b21dde8c8eb"onclick="copyCode(code444d37f41b5ccc9ce3c128b21dde8c8e, code444d37f41b5ccc9ce3c128b21dde8c8eb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code444d37f41b5ccc9ce3c128b21dde8c8e"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">zip_longest</span>

<span class="n">zip_longest</span><span class="p">(</span><span class="o">*</span><span class="n">iterables</span><span class="p">,</span> <span class="n">fillvalue</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который группирует элементы iterable по значениям функции key.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code57c6d84d0400152dbe81a67e72f53ad5b"onclick="copyCode(code57c6d84d0400152dbe81a67e72f53ad5, code57c6d84d0400152dbe81a67e72f53ad5b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code57c6d84d0400152dbe81a67e72f53ad5"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">groupby</span>

<span class="n">groupby</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт элементы из iterable, начиная с start, и заканчивая stop, с шагом step.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codeab17db25a85a3dcce0cbdd7c1592a592b"onclick="copyCode(codeab17db25a85a3dcce0cbdd7c1592a592, codeab17db25a85a3dcce0cbdd7c1592a592b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeab17db25a85a3dcce0cbdd7c1592a592"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">islice</span>

<span class="n">islice</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">start</span><span class="p">,</span> <span class="n">stop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">step</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который применяет функцию function к каждому элементу iterable, который представлен в виде кортежа.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code0b2fecc246bc78623ee020f57e5017ceb"onclick="copyCode(code0b2fecc246bc78623ee020f57e5017ce, code0b2fecc246bc78623ee020f57e5017ceb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code0b2fecc246bc78623ee020f57e5017ce"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">starmap</span>

<span class="n">starmap</span><span class="p">(</span><span class="n">function</span><span class="p">,</span> <span class="n">iterable</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт все возможные пары (или кортежи) элементов из каждого из iterables. 
repeat определяет, сколько раз каждый итератор будет повторен.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code48b784b816d31f92ff3f9aa3845c664eb"onclick="copyCode(code48b784b816d31f92ff3f9aa3845c664e, code48b784b816d31f92ff3f9aa3845c664eb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code48b784b816d31f92ff3f9aa3845c664e"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">product</span>

<span class="n">product</span><span class="p">(</span><span class="o">*</span><span class="n">iterables</span><span class="p">,</span> <span class="n">repeat</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт сумму (или другую комбинацию) элементов iterable, используя функцию func.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code615ce82d075f5b28bee11aa9d9ce669ab"onclick="copyCode(code615ce82d075f5b28bee11aa9d9ce669a, code615ce82d075f5b28bee11aa9d9ce669ab)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code615ce82d075f5b28bee11aa9d9ce669a"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">accumulate</span>

<span class="n">accumulate</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">func</span><span class="o">=</span><span class="n">operator</span><span class="o">.</span><span class="n">add</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт элементы data, соответствующие истинным значениям selectors.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code0f5a7d49f3f055c60dd507f7bb7df63ab"onclick="copyCode(code0f5a7d49f3f055c60dd507f7bb7df63a, code0f5a7d49f3f055c60dd507f7bb7df63ab)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code0f5a7d49f3f055c60dd507f7bb7df63a"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">compress</span>

<span class="n">compress</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">selectors</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт элементы iterable после первого элемента, для которого predicate вернёт ложное значение.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code0c177d477afba6577f09e95d3374feacb"onclick="copyCode(code0c177d477afba6577f09e95d3374feac, code0c177d477afba6577f09e95d3374feacb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code0c177d477afba6577f09e95d3374feac"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">dropwhile</span>

<span class="n">dropwhile</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">iterable</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт элементы iterable, для которых predicate вернёт ложное значение.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codee14fcd880b44a3298df32ad885fe6e9cb"onclick="copyCode(codee14fcd880b44a3298df32ad885fe6e9c, codee14fcd880b44a3298df32ad885fe6e9cb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codee14fcd880b44a3298df32ad885fe6e9c"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">filterfalse</span>

<span class="n">filterfalse</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">iterable</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт пары соседних элементов из iterable.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codeef8aaad5b43b9fdeac2f7f59e69367f9b"onclick="copyCode(codeef8aaad5b43b9fdeac2f7f59e69367f9, codeef8aaad5b43b9fdeac2f7f59e69367f9b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeef8aaad5b43b9fdeac2f7f59e69367f9"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">pairwise</span>

<span class="n">pairwise</span><span class="p">(</span><span class="n">iterable</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт object times раз (бесконечное количество раз, если times не указан).</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="coded07789435fc6cfcb7b28715bf6249a0eb"onclick="copyCode(coded07789435fc6cfcb7b28715bf6249a0e, coded07789435fc6cfcb7b28715bf6249a0eb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="coded07789435fc6cfcb7b28715bf6249a0e"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">repeat</span>

<span class="n">repeat</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span> <span class="n">times</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает итератор, который выдаёт элементы iterable до первого элемента, для которого predicate вернёт ложное значение.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codebc38a432363b4320474683c792403418b"onclick="copyCode(codebc38a432363b4320474683c792403418, codebc38a432363b4320474683c792403418b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codebc38a432363b4320474683c792403418"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">takewhile</span>

<span class="n">takewhile</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">iterable</span><span class="p">)</span>
</pre></div></div></div>

<p>Возвращает n независимых итераторов, каждый из которых может быть 
использован независимо для перебора элементов исходного iterable.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code070d084902e81e1f41161f24ab372053b"onclick="copyCode(code070d084902e81e1f41161f24ab372053, code070d084902e81e1f41161f24ab372053b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code070d084902e81e1f41161f24ab372053"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">tee</span>

<span class="n">tee</span><span class="p">(</span><span class="n">iterable</span><span class="p">,</span> <span class="n">n</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</pre></div></div></div>