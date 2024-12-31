"""
Implment BFS to traverse a graph stored as adjacency list

"""

class Graph:
    def __init__(self, vertices):
        self.adjacency_list = [[] for _ in range(vertices+1)]
    
    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

def bfs(starting_vertex, graph: Graph):
    """
    BFS picks the starting node add it to a queue and marks it as visited.
    Then while the queue is not empty, pop the element and print it. Then
    get all the vertices attached to that popped vertex and add it to the
    queue if it is not already visited and then mark it as visited.
    
    """
    queue = []
    visited = set() # To mark the visited nodes
    queue.append(starting_vertex)
    visited.add(starting_vertex)
    result = []
    
    while queue:
        current_vertex = queue.pop(0)
        result.append(current_vertex)
        for vertex in graph.adjacency_list[current_vertex]:
            if vertex not in visited:
                queue.append(vertex)
                visited.add(vertex)
    
    print(result)

new_graph = Graph(9)
# print(new_graph.adjacency_list)
new_graph.add_edge(1,2)
# print(new_graph.adjacency_list)
new_graph.add_edge(1,6)
new_graph.add_edge(2,3)
new_graph.add_edge(2,4)
new_graph.add_edge(6,7)
new_graph.add_edge(6,9)
new_graph.add_edge(4,5)
new_graph.add_edge(7,8)
new_graph.add_edge(8,5)
print(new_graph.adjacency_list)
print(f"*****************")
bfs(6, new_graph)



# def bfs(graph, vertex):
    