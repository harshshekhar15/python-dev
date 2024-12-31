"""
Implment DFS to traverse a graph stored as adjacency list

"""

class Graph:
    def __init__(self, vertices):
        self.adjacency_list = [[] for _ in range(vertices+1)]
    
    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

def dfs(current_vertex, visited, result, graph: Graph):
    result.append(current_vertex)
    visited.add(current_vertex)
    for vertex in graph.adjacency_list[current_vertex]:
        if vertex not in visited:
            dfs(vertex, visited, result, graph)


def dfsOfGraph(starting_vertex, graph: Graph):
    """
    DFS takes the starting vertex and adds it to visited.
    Then it traverses through all of its neighbours and
    if it's not visited calls recursively dfs for each of
    it's neightbours if it's not already visited.
    """
    visited = set()
    result = []
    # result.append(starting_vertex)
    # visited.add(starting_vertex)
    
    dfs(starting_vertex, visited, result, graph)
    print(result)


new_graph = Graph(8)
new_graph.add_edge(1,2)
new_graph.add_edge(1,3)
new_graph.add_edge(2,5)
new_graph.add_edge(2,6)
new_graph.add_edge(3,4)
new_graph.add_edge(3,7)
new_graph.add_edge(4,8)
new_graph.add_edge(7,8)
print(new_graph.adjacency_list)
dfsOfGraph(3, new_graph)