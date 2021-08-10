class DSU:
    def __init__(self, graph):
        self.p = {i:i for i in graph}

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
    def groups(self):
        ans = defaultdict(list)
        for el in self.p.keys():
            ans[self.find(el)].append(el)
        return ans
        
class Solution:
    def matrixRankTransform(self, M):
        n, m = len(M), len(M[0])
        rank = [0] * (m + n)
        d = defaultdict(list)
        
        for i, j in product(range(n), range(m)):
            d[M[i][j]].append([i, j])

        for a in sorted(d):
            graph = [i for i, j in d[a]] + [j + n for i, j in d[a]]
            dsu = DSU(graph)
            for i, j in d[a]: dsu.union(i, j + n)

            for group in dsu.groups().values():
                mx = max(rank[i] for i in group)
                for i in group: rank[i] = mx + 1
                    
            for i, j in d[a]: M[i][j] = rank[i]
            
        return M



# My original DIY solution

# def verticalCheck_second(m: List[List[int]], new_m: List[List[int]], row: int) -> List[List[int]]:
#     temp = []
#     for i in range(len(m)):
#         #Put the values in a list, and sort them, then give them their ranks in the new_matrix using the ranks
#         temp.append(m[i][row])
#     temp.sort()
#     print(temp)
#     for i in range(1,len(m)):
#         new_m[i][row] = new_m[0][row]+temp.index(m[i][row])
#     print(new_m)
#     return new_m

# def verticalCheck(m: List[List[int]], new_m: List[List[int]], row: int) -> List[List[int]]:
#     temp = []
#     for i in range(len(m)):
#         #Put the values in a list, and sort them, then give them their ranks in the new_matrix using the ranks
#         temp.append(m[i][row])
#     temp.sort()
#     print(temp)
#     for i in range(len(m)):
#         new_m[i][row] = temp.index(m[i][row])+1
#     print(new_m)
#     return new_m

# class Solution:
#     def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
#         #Divide and conquer
#         #Start looking at the matrix from a horizontal and vertical perspective starting at the first index
#         #Rank them all together, then maintain all their ranks
#         #Start from the next index on the top
#         #Rank each collumn, maintaining the rank of the index on top from the first iteration

#         # Initiate the list containing our answer
#         rows, cols = (len(matrix), len(matrix))
#         new_m = [[0 for i in range(cols)] for j in range(rows)] # This method makes the List recognize that it's 2 Dimensional
#         print(new_m)
        
#         # Temporary list for generic use
#         temp = []
        
#         # Initial check is vertical individually, then horizontal
        
#         # Vertical part
#         new_m = verticalCheck(matrix,new_m,0)
        
# #         # Horizontal part
#         for i in range(len(matrix)):
#             #Put the values in a list, and sort them, then give them their ranks in the new_matrix using the ranks
#             temp.append(matrix[0][i])
        
#         temp.sort()
      
#         for i in range(len(matrix)):
#             #Make sure to remove a number once you locate its index, the index() function only finds the first occurence
#             new_m[0][i] = temp.index(matrix[0][i])+1
        
#         for i in range(1,len(matrix)):
#             new_m = verticalCheck_second(matrix,new_m,i)

#         return new_m
            
            