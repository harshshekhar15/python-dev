"""
Implement a Disjoint set data structure in python.

Disjoint set is a data structure which is used in case of a graph with multiple components
to find out if two nodes have the same ultimate parent.
"""

class DisjointSet:
    def __init__(self, nodes):
        self.parent = [i for i in range(nodes+1)]
        self.rank = [0 for _ in range(nodes+1)]
        self.size = [1 for _ in range(nodes+1)]
    
    def find_ultimate_parent(self, node):
        """
        This will return the ultimate parent of node and will do path
        compression along it's way by updating the parent of the current
        node to the ultimate parent as returned by the recursive call.
        """
        if self.parent[node] == node:
           return node
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]
    
    def union_by_rank(self, u, v):
        """
        - Find the ultimate parent of u and v.
        - Find the rank of the ultimate parents and compare them.
            - If the rank of ultimate parent of u is greater than the
              rank of the ultimate parent of v, then attach the ultimate
              parent of v to u and vice versa.
            - If the rank of ultimate parent of u is equal to the rank of
              ultimate parent of v then attach either way. Here we'll attach
              the ultimate parent of v to ultimate parent of u and we'll increase
              the rank of ultimate parent of u by 1.
            - If the ultimate parent of both u and v are same thne just return.
            
        NOTE: We only increase the rank of any node if the rank of the ultimate parents
              of the both the nodes are same. Otherwise we keep the same rank.
        """
        ulp_u = self.find_ultimate_parent(u)
        ulp_v = self.find_ultimate_parent(v)
        
        # if the ultimate parent of both the nodes are same then just return
        if ulp_u == ulp_v:
            return
        
        rank_ulp_u = self.rank[ulp_u]
        rank_ulp_v = self.rank[ulp_v]
        
        if rank_ulp_u < rank_ulp_v:
            self.parent[ulp_u] = ulp_v
        elif rank_ulp_u > rank_ulp_v:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
    
    def union_by_size(self, u, v):
        ulp_u = self.find_ultimate_parent(u)
        ulp_v = self.find_ultimate_parent(v)
        
        size_ulp_u = self.size[ulp_u]
        size_ulp_v = self.size[ulp_v]
        
        if size_ulp_u > size_ulp_v:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        elif size_ulp_u < size_ulp_v:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        

new_set = DisjointSet(7)
new_set.union_by_size(1,2)
new_set.union_by_size(2,3)
new_set.union_by_size(4,5)
new_set.union_by_size(6,7)
new_set.union_by_size(5,6)
if new_set.find_ultimate_parent(3) == new_set.find_ultimate_parent(7):
    print("Same parent")
else:
    print("Not same")
new_set.union_by_size(3,7)
if new_set.find_ultimate_parent(3) == new_set.find_ultimate_parent(7):
    print("Same parent")
else:
    print("Not same")
print(new_set.parent)
print(new_set.size)