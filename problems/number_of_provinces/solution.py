class disjointSet:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        # RECURSION!
        
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])

        # For all the other calls that aren't the base        
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        provinces = disjointSet(len(isConnected))
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    provinces.union(i, j)
        
        for i in range(len(provinces.root)):
            if provinces.root[i] == i:
                count += 1
        
        return count
        