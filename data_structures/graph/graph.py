"""
Implement a Graph data structure using adjacency lists

Example:
graph = {
            "A": [B, C],
            "B": [A, C],
            "C": [A, B]
        }
"""
from queue_linkedlist import QueueLL

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices.keys():
            self.vertices[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices.keys() and vertex2 in self.vertices.keys():
            self.vertices[vertex1].append(vertex2)
            # self.vertices[vertex2].append(vertex1)
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices.keys() and vertex2 in self.vertices.keys():
            self.vertices[vertex1].remove(vertex2)
            self.vertices[vertex2].remove(vertex1)
    
    def remove_vertex(self, vertex):
        if vertex in self.vertices.keys():
            for connecting_vertex in self.vertices[vertex]:
                self.vertices[connecting_vertex].remove(vertex)
            del self.vertices[vertex]
    
    def print(self):
        for vertex in self.vertices:
            print(f"{vertex}: {self.vertices[vertex]}")
    
    def bfs(self, vertex):
        if vertex in self.vertices.keys():
            visited = set()
            custom_queue = QueueLL()
            visited.add(vertex)
            custom_queue.enqueue(vertex)
            while not custom_queue.isEmpty():
                current_vertex = custom_queue.dequeue()
                print(current_vertex)
                for adjacent_vertex in self.vertices[current_vertex]:
                    if adjacent_vertex not in visited:
                        visited.add(adjacent_vertex)
                        custom_queue.enqueue(adjacent_vertex)
    
    def dfs(self, vertex):
        if vertex in self.vertices.keys():
            visited = set()
            stack = []
            stack.append(vertex)
            while stack:
                current_vertex = stack.pop()
                if current_vertex not in visited:
                    print(current_vertex)
                    visited.add(current_vertex)
                for adjacent_vertex in self.vertices[current_vertex]:
                    if adjacent_vertex not in visited:
                        stack.append(adjacent_vertex)
    
    def topological_sort_edges(self, vertex, visited, stack):
        visited.add(vertex)
        
        for adjacent_vertex in self.vertices[vertex]:
            if adjacent_vertex not in visited:
                self.topological_sort_edges(adjacent_vertex, visited, stack)
        
        stack.insert(0, vertex)
    
    def topological_sort(self):
        visited = set()
        stack = []
        
        for vertex in self.vertices:
            if vertex not in visited:
                self.topological_sort_edges(vertex, visited, stack)
        
        print(stack)
        

new_graph = Graph()
new_graph.add_vertex("A")
new_graph.add_vertex("B")
new_graph.add_vertex("C")
new_graph.add_vertex("D")
new_graph.add_vertex("E")
new_graph.add_vertex("F")
new_graph.add_vertex("G")
new_graph.add_vertex("H")
new_graph.add_edge("A", "C")
new_graph.add_edge("B", "C")
new_graph.add_edge("B", "D")
new_graph.add_edge("C", "E")
new_graph.add_edge("D", "F")
new_graph.add_edge("E", "H")
new_graph.add_edge("E", "F")
new_graph.add_edge("F", "G")
new_graph.print()
# new_graph.remove_edge("D", "C")
# new_graph.remove_edge("D", "A")
# print(f"Graph post removal of vertex")
# new_graph.print()
# print(f"DFS traversal of current graph")
# new_graph.dfs("D")
new_graph.topological_sort()

