"""
Implement Prim's algorithm to find out the Minimum Spanning Tree of a given graph.

The graph is represented using adjacency list, as shown below:
{
    vertex1: [[adjacent_vertex1, edge_weight1], [adjacent_vertex2, edge_weight2], ..],
    vertex2: [[adjacent_vertex1, edge_weight1], [adjacent_vertex2, edge_weight2], ..]
}

{
    1 : [[5,4], [4,1], [2,2]],
    2 : [[1,2],[4,3],[3,3],[6,7]],
    3 : [[4,5],[2,3],[6,8]],
    4 : [[5,9],[1,1],[2,3],[3,5]],
    5 : [[4,9],[1,4]],
    6 : [[3,8],[2,7]]
}
"""


from typing import List
import heapq

class Edge:
    def __init__(self, weight, vertex, parentVertex):
        self.weight = weight
        self.vertex = vertex
        self.parent = parentVertex
    
    def __lt__(self, node):
        return self.weight < node.weight
        
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        min_heap = []
        visited = set()
        mst = []
        
        new_node = Edge(0, list(adj.keys())[0], -1)
        heapq.heappush(min_heap, new_node)
        mst_sum = 0
        
        # while priority queue is not empty pop the
        # elements and add it to MST
        while min_heap:
            node = heapq.heappop(min_heap)
            current_vertex = node.vertex
            weight = node.weight
            parent = node.parent
            
            if current_vertex in visited:
                continue
            visited.add(node.vertex)
            if parent != -1:
                mst.append([current_vertex, parent])
            mst_sum += weight
            
            for i in range(len(adj[current_vertex])):
                # print(adj[current_vertex])
                adjacent_vertex = adj[current_vertex][i][0]
                edge_weight = adj[current_vertex][i][1]
                if adjacent_vertex not in visited:
                    heapq.heappush(min_heap, Edge(edge_weight, adjacent_vertex, current_vertex))

        print(f"MST: {mst}\nSum: {mst_sum}")
        return mst_sum

new_graph = {
    1 : [[5,4], [4,1], [2,2]],
    2 : [[1,2], [4,3], [3,3], [6,7]],
    3 : [[4,5], [2,3], [6,8]],
    4 : [[5,9], [1,1], [2,3], [3,5]],
    5 : [[4,9], [1,4]],
    6 : [[3,8], [2,7]]
}

Solution().spanningTree(6, new_graph)