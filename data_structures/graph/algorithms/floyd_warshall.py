"""
Implement Floyd warshall algorithm for a graph to find all pairs shortest path.

The graph is represented as an adjacency matrix
"""
INF = 9999

def floyd_warshall(graph):
    num_vertices = len(graph)
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    # For negative cycle
    for k in range(num_vertices):
        # for i in range(num_vertices):
        #     for j in range(num_vertices):
        #         if graph[i][j] > graph[i][k] + graph[k][j]:
        #             raise "Negative cycle"
        if graph[k][k] < 0:
            raise "Neagtive cycle"
    
    print(graph)


new_graph = [
    [0, -8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF],
    [INF, 2, 9, 1]
]
    
floyd_warshall(new_graph)