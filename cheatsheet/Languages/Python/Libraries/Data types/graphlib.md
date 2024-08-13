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
<pre><code class="language-python">import graphlib

graph = graphlib.Graph()
graph.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])

sorted_vertices = graphlib.TopologicalSort(graph)
print(sorted_vertices)
</code></pre>
<p>Graph.add_vertex Добавляет новую вершину в граф.</p>
<pre><code class="language-python">import graphlib

graph = graphlib.Graph()
graph.add_vertex(1)
graph.add_vertex(2)
</code></pre>
<p>DiGraph.add_edge Добавляет новое ребро между двумя вершинами в ориентированном графе.</p>
<pre><code class="language-python">import graphlib

graph = graphlib.DiGraph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
</code></pre>
<p>find_cycles Находит все циклы в графе и возвращает их в виде списка.</p>
<pre><code class="language-python">import graphlib

graph = graphlib.Graph()
graph.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 5)])

cycles = graphlib.find_cycles(graph)
print(cycles)
</code></pre>