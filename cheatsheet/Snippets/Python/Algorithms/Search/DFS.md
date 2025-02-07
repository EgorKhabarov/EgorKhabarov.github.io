# DFS (Поиск в глубину)

Метод обхода графа
`Depth-first search` (`DFS`) можно чуть точнее перевести как **поиск в первую очередь в глубину**
Соответственно, рекурсивный алгоритм поиска идет **вглубь** графа, насколько это возможно
Есть нерекурсивные варианты алгоритма, разгружающие стек вызовов

```
    5
   / \
  3   7
 / \   \
2   4 — 8
```

```python
graph = {
  "5" : ["3","7"],
  "3" : ["2", "4"],
  "7" : ["8"],
  "2" : [],
  "4" : ["8"],
  "8" : []
}

visited = set() # Set to keep track of visited nodes of graph

def dfs(visited, graph, node):  # Function for DFS
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, "5")
# 5
# 3
# 2
# 4
# 8
# 7
```