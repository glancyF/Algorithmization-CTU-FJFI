def dijkstra(graph,src):
    dist = {node: float('inf') for node in graph}
    dist[src]=0
    visited = set()

    while len(visited)< len(graph):
        min_dist = float('inf')
        u = None
        for node in graph:
            if node not in visited and dist[node]<min_dist:
                min_dist = dist[node]
                u = node
        visited.add(u)
        for v,weight in graph[u].items():
            if v not in visited and dist[v] > dist[u]+weight:
                dist[v] = dist[u] + weight
    return dist


graph = {
    0: {1: 4, 2: 8},
    1: {0: 4, 4: 6},
    2: {0: 8, 3: 2},
    3: {2: 2, 4: 10},
    4: {1: 6, 3: 10}
}

print(dijkstra(graph, 0))