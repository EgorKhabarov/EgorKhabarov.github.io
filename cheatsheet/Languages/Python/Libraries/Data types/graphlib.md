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
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">graphlib</span>

<span class="n">graph</span> <span class="o">=</span> <span class="n">graphlib</span><span class="o">.</span><span class="n">Graph</span><span class="p">()</span>
<span class="n">graph</span><span class="o">.</span><span class="n">add_edges_from</span><span class="p">([(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">),</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">),</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">)])</span>

<span class="n">sorted_vertices</span> <span class="o">=</span> <span class="n">graphlib</span><span class="o">.</span><span class="n">TopologicalSort</span><span class="p">(</span><span class="n">graph</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sorted_vertices</span><span class="p">)</span>
</pre></div></div></div>

<p>Graph.add_vertex Добавляет новую вершину в граф.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">graphlib</span>

<span class="n">graph</span> <span class="o">=</span> <span class="n">graphlib</span><span class="o">.</span><span class="n">Graph</span><span class="p">()</span>
<span class="n">graph</span><span class="o">.</span><span class="n">add_vertex</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">graph</span><span class="o">.</span><span class="n">add_vertex</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</pre></div></div></div>

<p>DiGraph.add_edge Добавляет новое ребро между двумя вершинами в ориентированном графе.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">graphlib</span>

<span class="n">graph</span> <span class="o">=</span> <span class="n">graphlib</span><span class="o">.</span><span class="n">DiGraph</span><span class="p">()</span>
<span class="n">graph</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
<span class="n">graph</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
</pre></div></div></div>

<p>find_cycles Находит все циклы в графе и возвращает их в виде списка.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">graphlib</span>

<span class="n">graph</span> <span class="o">=</span> <span class="n">graphlib</span><span class="o">.</span><span class="n">Graph</span><span class="p">()</span>
<span class="n">graph</span><span class="o">.</span><span class="n">add_edges_from</span><span class="p">([(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">),</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span> <span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">)])</span>

<span class="n">cycles</span> <span class="o">=</span> <span class="n">graphlib</span><span class="o">.</span><span class="n">find_cycles</span><span class="p">(</span><span class="n">graph</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cycles</span><span class="p">)</span>
</pre></div></div></div>