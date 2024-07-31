<p>Библиотека "graphlib" в Python используется для работы с графами и решения различных задач на графах,
таких как поиск кратчайшего пути, определение связности графа и других алгоритмических задач.</p>
<p>Таблица методов модуля "graphlib" и его подмодулей:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>graphlib.TopologicalSort</td>
<td>Реализует сортировку вершин графа в топологическом порядке.</td>
</tr>
<tr>
<td>graphlib.Graph</td>
<td>Представляет граф и предоставляет методы для добавления вершин и ребер, проверки наличия ребер и других операций.</td>
</tr>
<tr>
<td>graphlib.DiGraph</td>
<td>Представляет ориентированный граф и предоставляет методы для работы с ним, аналогичные методам Graph.</td>
</tr>
<tr>
<td>graphlib.find_cycles</td>
<td>Позволяет найти все циклы в графе и предоставляет их в виде списка.</td>
</tr>
</tbody>
</table>
<p>Список самых частых методов, их краткое описание и</p>
<p>TopologicalSort Сортирует вершины графа в топологическом порядке.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code3e916bc4f8a7c6208f3deff30f133af5b"onclick="copyCode(code3e916bc4f8a7c6208f3deff30f133af5, code3e916bc4f8a7c6208f3deff30f133af5b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code3e916bc4f8a7c6208f3deff30f133af5"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">graphlib</span>

<span class="n">graph</span> <span class="o">=</span> <span class="n">graphlib</span><span class="o">.</span><span class="n">Graph</span><span class="p">()</span>
<span class="n">graph</span><span class="o">.</span><span class="n">add_edges_from</span><span class="p">([(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">),</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">),</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">)])</span>

<span class="n">sorted_vertices</span> <span class="o">=</span> <span class="n">graphlib</span><span class="o">.</span><span class="n">TopologicalSort</span><span class="p">(</span><span class="n">graph</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sorted_vertices</span><span class="p">)</span>
</pre></div></div></div>

<p>Graph.add_vertex Добавляет новую вершину в граф.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codeafb2e5c982a8bd847a2cf9545c9d68a4b"onclick="copyCode(codeafb2e5c982a8bd847a2cf9545c9d68a4, codeafb2e5c982a8bd847a2cf9545c9d68a4b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeafb2e5c982a8bd847a2cf9545c9d68a4"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">graphlib</span>

<span class="n">graph</span> <span class="o">=</span> <span class="n">graphlib</span><span class="o">.</span><span class="n">Graph</span><span class="p">()</span>
<span class="n">graph</span><span class="o">.</span><span class="n">add_vertex</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">graph</span><span class="o">.</span><span class="n">add_vertex</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</pre></div></div></div>

<p>DiGraph.add_edge Добавляет новое ребро между двумя вершинами в ориентированном графе.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code93f6481d07474e0d6e653b9cf8aae323b"onclick="copyCode(code93f6481d07474e0d6e653b9cf8aae323, code93f6481d07474e0d6e653b9cf8aae323b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code93f6481d07474e0d6e653b9cf8aae323"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">graphlib</span>

<span class="n">graph</span> <span class="o">=</span> <span class="n">graphlib</span><span class="o">.</span><span class="n">DiGraph</span><span class="p">()</span>
<span class="n">graph</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
<span class="n">graph</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
</pre></div></div></div>

<p>find_cycles Находит все циклы в графе и возвращает их в виде списка.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codec4c6565fd7fab12bbd67005223c89385b"onclick="copyCode(codec4c6565fd7fab12bbd67005223c89385, codec4c6565fd7fab12bbd67005223c89385b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codec4c6565fd7fab12bbd67005223c89385"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">graphlib</span>

<span class="n">graph</span> <span class="o">=</span> <span class="n">graphlib</span><span class="o">.</span><span class="n">Graph</span><span class="p">()</span>
<span class="n">graph</span><span class="o">.</span><span class="n">add_edges_from</span><span class="p">([(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">),</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span> <span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">)])</span>

<span class="n">cycles</span> <span class="o">=</span> <span class="n">graphlib</span><span class="o">.</span><span class="n">find_cycles</span><span class="p">(</span><span class="n">graph</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cycles</span><span class="p">)</span>
</pre></div></div></div>