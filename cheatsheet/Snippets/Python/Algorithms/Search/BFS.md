# BFS (Поиск в ширину)

В отличие от [`DFS`](?Snippets/Python/Algorithms/Search/DFS) алгоритм `Breadth-first search` (`BFS`) перебирает в первую очередь вершины с одинаковым расстоянием от корня,
и только потом идет **вглубь**

```python
# https://codereview.stackexchange.com/questions/135156/bfs-implementation-in-python-3
import collections


def breadth_first_search(graph, root):
    visited, queue = set(), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == "__main__":
    graph = {0: [1, 2], 1: [2], 2: []}
    breadth_first_search(graph, 0)
# deque([])
```