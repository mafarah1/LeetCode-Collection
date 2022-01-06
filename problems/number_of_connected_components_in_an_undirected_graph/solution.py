class disjointSet:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size
        
    def find(self, x):
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])
        
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            self.count -= 1
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        djset = disjointSet(n)
        
        for edge in edges:
            djset.union(*edge)
            
        return djset.count
        