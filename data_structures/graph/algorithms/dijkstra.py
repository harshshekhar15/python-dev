"""
Create two classes Node and Edge representing vertex and edge respectively in a gvien graph.

Edge class will have the following attributes:
- weight : Weight of the given edge.
- end_vertex : The vertex with which the current node is connected to.

Node class will have the following attributes:
- name : Name of the vertex
- min_distance : Minimum distance of the current node from the starting vertex.This will be set to infinity by default.
- visited : A boolean value to represent whether this node was visited or not while running the algo.
- neighbours : A list containing the adjacent vertices of the given node.
- predecessor : This will store the node from which the current node was visited (parent node).

Node class will have the following methods:
- add_edge : This method will add a new edge to the current node.
- __lt__ : This method will be used by min heap to compare the minimum distance of two node objects.


Create a Dijkstra's class to implement the Dijkstra's algorithm.

Dijkstra's class will have the following methods:
- calculate : This method will take start_vertex as the parameter and will update the minimum distance of all
              the vertices in the graph with the minimum distance from the starting vertex.
- shortest_distance : This will take a vertex as the parameter and will print the shortest distance of the
                      provided vertex from the starting vertex. This will also print the shortest path.
              
"""

import heapq

class Edge:
    def __init__(self, weight, end_vertex):
        self.weight = weight
        self.end_vertex = end_vertex

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.neighbours = []
        self.min_distance = float("inf")
        self.predecessor = None
        # self.visited = False
    
    def add_edge(self, edge: Edge):
        self.neighbours.append(edge)
    
    def __lt__(self, node):
        return self.min_distance < node.min_distance

class Dijkstra:
    def __init__(self) -> None:
        self.visited = set()
        self.min_heap = []
    
    def calculate_distance(self, start_vertex: Node):
        start_vertex.min_distance = float(0)
        heapq.heappush(self.min_heap, start_vertex)
        
        while self.min_heap:
            current_vertex = heapq.heappop(self.min_heap)
            if current_vertex in self.visited:
                continue
            for edge in current_vertex.neighbours:
                new_distance = current_vertex.min_distance + edge.weight
                if new_distance < edge.end_vertex.min_distance:
                    edge.end_vertex.min_distance = new_distance
                    heapq.heappush(self.min_heap, edge.end_vertex)
                    edge.end_vertex.predecessor = current_vertex
            self.visited.add(current_vertex)
    
    def shortest_path(self, vertex: Node):
        print(f"Shortest path to the given vertex is: {vertex.min_distance}")
        current_vertex = vertex
        path = []
        while current_vertex:
            # print(current_vertex.name)
            path.append(current_vertex.name)
            current_vertex = current_vertex.predecessor
        while path:
            print(f"{path.pop()} ->", end=" ")


nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

nodeA.add_edge(Edge(weight=6, end_vertex=nodeB))
nodeA.add_edge(Edge(weight=9, end_vertex=nodeD))
nodeA.add_edge(Edge(weight=10, end_vertex=nodeC))
nodeB.add_edge(Edge(weight=5, end_vertex=nodeD))
nodeB.add_edge(Edge(weight=16, end_vertex=nodeE))
nodeB.add_edge(Edge(weight=13, end_vertex=nodeF))
nodeC.add_edge(Edge(weight=6, end_vertex=nodeD))
nodeC.add_edge(Edge(weight=5, end_vertex=nodeH))
nodeC.add_edge(Edge(weight=21, end_vertex=nodeG))
nodeD.add_edge(Edge(weight=8, end_vertex=nodeF))
nodeD.add_edge(Edge(weight=7, end_vertex=nodeH))
nodeE.add_edge(Edge(weight=10, end_vertex=nodeG))
nodeF.add_edge(Edge(weight=4, end_vertex=nodeE))
nodeH.add_edge(Edge(weight=2, end_vertex=nodeF))
nodeH.add_edge(Edge(weight=14, end_vertex=nodeG))


algo = Dijkstra()
algo.calculate_distance(nodeA)
algo.shortest_path(nodeE)
print(algo.min_heap)