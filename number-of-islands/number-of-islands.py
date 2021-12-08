sys.setrecursionlimit(1500000)

def dfs(grid,r,c):
    nr = len(grid)
    nc = len(grid[0])

    if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == '0':
        return

    grid[r][c] = '0'
    dfs(grid, r - 1, c)
    dfs(grid, r + 1, c)
    dfs(grid, r, c - 1)
    dfs(grid, r, c + 1)
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or grid == None:
            return 0
        
        count = 0
        
        # Reader
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(grid,i,j)
                    count += 1
        
        return count