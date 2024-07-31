<p>Название библиотеки: "pylab"</p>
<p>Краткое описание: Библиотека "pylab" является комбинацией библиотеки "matplotlib" и "NumPy"
для выполнения научных и инженерных вычислений в Python.
Она предоставляет функции для создания графиков, визуализации данных и выполнения математических операций.</p>
<p>Таблица методов:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>plot</code></td>
<td>Построить график из данных</td>
</tr>
<tr>
<td><code>scatter</code></td>
<td>Создать точечную диаграмму</td>
</tr>
<tr>
<td><code>hist</code></td>
<td>Построить гистограмму из данных</td>
</tr>
<tr>
<td><code>imshow</code></td>
<td>Отобразить изображение</td>
</tr>
<tr>
<td><code>xlabel</code></td>
<td>Задать подпись для оси x</td>
</tr>
<tr>
<td><code>ylabel</code></td>
<td>Задать подпись для оси y</td>
</tr>
<tr>
<td><code>title</code></td>
<td>Задать заголовок графика</td>
</tr>
<tr>
<td><code>legend</code></td>
<td>Вывести легенду графика</td>
</tr>
<tr>
<td><code>grid</code></td>
<td>Отобразить сетку на графике</td>
</tr>
<tr>
<td><code>sin</code></td>
<td>Вычислить синус значения</td>
</tr>
<tr>
<td><code>cos</code></td>
<td>Вычислить косинус значения</td>
</tr>
<tr>
<td><code>exp</code></td>
<td>Вычислить экспоненту значения</td>
</tr>
</tbody>
</table>
<p>Метод <code>plot</code> позволяет строить графики из предоставленных данных.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code5208b4ba0fba81560219131b53678bdfb"onclick="copyCode(code5208b4ba0fba81560219131b53678bdf, code5208b4ba0fba81560219131b53678bdfb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code5208b4ba0fba81560219131b53678bdf"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pylab</span>

<span class="n">x</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="n">y</span> <span class="o">=</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">50</span><span class="p">]</span>

<span class="n">pylab</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div></div></div>

<p>Метод <code>scatter</code> используется для создания точечной диаграммы.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codeebbae971c90137d5fe636fbda4e582cfb"onclick="copyCode(codeebbae971c90137d5fe636fbda4e582cf, codeebbae971c90137d5fe636fbda4e582cfb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeebbae971c90137d5fe636fbda4e582cf"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pylab</span>

<span class="n">x</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="n">y</span> <span class="o">=</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">50</span><span class="p">]</span>

<span class="n">pylab</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div></div></div>

<p>Метод <code>hist</code> позволяет создать гистограмму из предоставленных данных.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code309c30418941507bb967630b91887604b"onclick="copyCode(code309c30418941507bb967630b91887604, code309c30418941507bb967630b91887604b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code309c30418941507bb967630b91887604"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pylab</span>

<span class="n">data</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>

<span class="n">pylab</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div></div></div>

<p>Метод <code>imshow</code> используется для отображения изображений.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code8c7099b3d51f88d0cdbb3c1d3a83f693b"onclick="copyCode(code8c7099b3d51f88d0cdbb3c1d3a83f693, code8c7099b3d51f88d0cdbb3c1d3a83f693b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code8c7099b3d51f88d0cdbb3c1d3a83f693"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pylab</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="n">image</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">random</span><span class="p">((</span><span class="mi">10</span><span class="p">,</span> <span class="mi">10</span><span class="p">))</span>

<span class="n">pylab</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div></div></div>

<p>Метод <code>xlabel</code> задает подпись для оси x на графике.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code587f3c2bd371e06189832f4c3e181ddbb"onclick="copyCode(code587f3c2bd371e06189832f4c3e181ddb, code587f3c2bd371e06189832f4c3e181ddbb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code587f3c2bd371e06189832f4c3e181ddb"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pylab</span>

<span class="n">x</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="n">y</span> <span class="o">=</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">50</span><span class="p">]</span>

<span class="n">pylab</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;X-axis&quot;</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div></div></div>

<p>Метод <code>ylabel</code> задает подпись для оси y на графике.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="coded09ba91197f3de285c6a7e303a1e931ab"onclick="copyCode(coded09ba91197f3de285c6a7e303a1e931a, coded09ba91197f3de285c6a7e303a1e931ab)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="coded09ba91197f3de285c6a7e303a1e931a"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pylab</span>

<span class="n">x</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="n">y</span> <span class="o">=</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">50</span><span class="p">]</span>

<span class="n">pylab</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;Y-axis&quot;</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div></div></div>

<p>Метод <code>title</code> задает заголовок для графика.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="coded256423f8b6e8ae2720538342e01f438b"onclick="copyCode(coded256423f8b6e8ae2720538342e01f438, coded256423f8b6e8ae2720538342e01f438b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="coded256423f8b6e8ae2720538342e01f438"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pylab</span>

<span class="n">x</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="n">y</span> <span class="o">=</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">50</span><span class="p">]</span>

<span class="n">pylab</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;My Plot&quot;</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div></div></div>

<p>Метод <code>legend</code> выводит легенду на графике.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codef88049d3d4f32afc8d0b76e40cf4026eb"onclick="copyCode(codef88049d3d4f32afc8d0b76e40cf4026e, codef88049d3d4f32afc8d0b76e40cf4026eb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codef88049d3d4f32afc8d0b76e40cf4026e"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pylab</span>

<span class="n">x</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="n">y</span> <span class="o">=</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">50</span><span class="p">]</span>

<span class="n">pylab</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;Data&quot;</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div></div></div>

<p>Метод <code>grid</code> отображает сетку на графике.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codef9b3188380480a1d7e45799674dfbabab"onclick="copyCode(codef9b3188380480a1d7e45799674dfbaba, codef9b3188380480a1d7e45799674dfbabab)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codef9b3188380480a1d7e45799674dfbaba"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pylab</span>

<span class="n">x</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="n">y</span> <span class="o">=</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">50</span><span class="p">]</span>

<span class="n">pylab</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
<span class="n">pylab</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div></div></div>

<p>Метод <code>sin</code> используется для вычисления синуса значения.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code0327fa3cbba4d7e909ad761a48e6cf51b"onclick="copyCode(code0327fa3cbba4d7e909ad761a48e6cf51, code0327fa3cbba4d7e909ad761a48e6cf51b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code0327fa3cbba4d7e909ad761a48e6cf51"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pylab</span>


<span class="nb">print</span><span class="p">(</span><span class="n">pylab</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="mf">0.5</span><span class="p">))</span>
</pre></div></div></div>

<p>Метод <code>cos</code> используется для вычисления косинуса значения.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code05eaf6c283f64510036d7dca3345bd28b"onclick="copyCode(code05eaf6c283f64510036d7dca3345bd28, code05eaf6c283f64510036d7dca3345bd28b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code05eaf6c283f64510036d7dca3345bd28"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pylab</span>


<span class="nb">print</span><span class="p">(</span><span class="n">pylab</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mf">0.5</span><span class="p">))</span>
</pre></div></div></div>

<p>Метод <code>exp</code> используется для вычисления экспоненты значения.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code517ce7cc0d04293e9df3e1375af4eb14b"onclick="copyCode(code517ce7cc0d04293e9df3e1375af4eb14, code517ce7cc0d04293e9df3e1375af4eb14b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code517ce7cc0d04293e9df3e1375af4eb14"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pylab</span>


<span class="nb">print</span><span class="p">(</span><span class="n">pylab</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>
</pre></div></div></div>