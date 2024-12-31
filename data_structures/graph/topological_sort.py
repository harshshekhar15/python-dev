


from collections import defaultdict

class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices
    
    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)