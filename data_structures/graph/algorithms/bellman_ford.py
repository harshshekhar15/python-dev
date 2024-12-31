"""
Implement Bellman Ford Algorithm


"""

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
    
    def add_vertex(self, vertex):
        self.vertices.append(vertex)
    
    def add_edge(self, start_vertex, end_vertex, weight):
        self.edges.append([start_vertex, end_vertex, weight])

class BellmanFord:
    def __init__(self, graph: Graph):
        self.graph = graph
    
    def calculate(self, starting_vertex):
        min_weights = {}
        for vertex in self.graph.vertices:
            min_weights[vertex] = float("inf")
        min_weights[starting_vertex] = 0
        
        for index in range(len(self.graph.vertices)-2):
            for s, e, w in self.graph.edges:
                if min_weights[s] != float("inf") and min_weights[s] + w < min_weights[e]:
                    min_weights[e] = min_weights[s] + w
        
        for _ in range(1):
            for s, e, w in self.graph.edges:
                if min_weights[s] != float("inf") and min_weights[s] + w < min_weights[e]:
                    return "Graph has negative cycle"
        return min_weights
    
    def all_pairs_shortest_path(self):
        shortest_paths = {}
        for vertex in self.graph.vertices:
            shortest_paths[vertex] = self.calculate(vertex)
            print(f"{vertex} --> {shortest_paths[vertex]}")
        

new_graph = Graph()
new_graph.add_vertex(vertex="A")
new_graph.add_vertex("B")
new_graph.add_vertex("C")
new_graph.add_vertex("D")
new_graph.add_vertex("E")
new_graph.add_edge("A", "C", 6)
new_graph.add_edge("A", "D", 6)
new_graph.add_edge("B", "A", 3)
new_graph.add_edge("C", "D", 1)
new_graph.add_edge("D", "C", 2)
new_graph.add_edge("D", "B", 1)
new_graph.add_edge("E", "B", 4)
new_graph.add_edge("E", "D", 2)

algo = BellmanFord(new_graph)
algo.all_pairs_shortest_path()