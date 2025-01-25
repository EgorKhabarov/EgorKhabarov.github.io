Библиотека "graphlib" в Python используется для работы с графами и решения различных задач на графах,
таких как поиск кратчайшего пути, определение связности графа и других алгоритмических задач.

Таблица методов модуля "graphlib" и его подмодулей:

Метод                    | Описание
------------------------ | -----------------------------
graphlib.TopologicalSort | Реализует сортировку вершин графа в топологическом порядке.
graphlib.Graph           | Представляет граф и предоставляет методы для добавления вершин и ребер, проверки наличия ребер и других операций.
graphlib.DiGraph         | Представляет ориентированный граф и предоставляет методы для работы с ним, аналогичные методам Graph.
graphlib.find_cycles     | Позволяет найти все циклы в графе и предоставляет их в виде списка.

Список самых частых методов, их краткое описание и

TopologicalSort Сортирует вершины графа в топологическом порядке.

```python
import graphlib

graph = graphlib.Graph()
graph.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])

sorted_vertices = graphlib.TopologicalSort(graph)
print(sorted_vertices)
```

Graph.add_vertex Добавляет новую вершину в граф.

```python
import graphlib

graph = graphlib.Graph()
graph.add_vertex(1)
graph.add_vertex(2)
```

DiGraph.add_edge Добавляет новое ребро между двумя вершинами в ориентированном графе.

```python
import graphlib

graph = graphlib.DiGraph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
```

find_cycles Находит все циклы в графе и возвращает их в виде списка.

```python
import graphlib

graph = graphlib.Graph()
graph.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 5)])

cycles = graphlib.find_cycles(graph)
print(cycles)
```
