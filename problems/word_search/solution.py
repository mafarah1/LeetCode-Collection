class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board: 
            
            # Quick response for empty board
            return False
        
        h, w = len(board), len(board[0])
      
        # ------------------------------------------------------
    
        def dfs_search(idx: int, x: int, y: int) -> bool:
            
            if x < 0 or x == w or y < 0 or y == h or word[idx] != board[y][x]:
                # Reject if out of boundary, or current grid cannot match the character word[idx]
                return False

            if idx == len(word) - 1: 
                # Accept when we match all characters of word during DFS
                return True

            cur = board[y][x]
            
            # mark as '#' to avoid repeated traversal
            board[y][x] = '#'
            
            # visit next four neighbor grids
            found = dfs_search(idx + 1, x + 1, y) or dfs_search(idx + 1, x - 1, y) or dfs_search(idx + 1, x, y + 1) or dfs_search(idx + 1, x, y - 1)
            
            # recover original grid character after DFS is completed
            board[y][x] = cur
            
            return found

        # ------------------------------------------------------
        
        return any(dfs_search(0, x, y) for y in range(h) for x in range(w))