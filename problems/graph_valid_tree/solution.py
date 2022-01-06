class disjointSet:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        
    def find(self, x):
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])
        
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.root[x]
        rootY = self.root[y]
        
        if rootX != rootY:
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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        count = 0
        seconds = [edges[i][1] for i in range(len(edges))]
        
        djset = disjointSet(n)
        
        for pair in edges:
            djset.union(pair[0], pair[1])
        
        for i in range(len(djset.root)):
            if i == djset.root[i]:
                count += 1
        
        return count < 2 and len(edges) == n-1            
            