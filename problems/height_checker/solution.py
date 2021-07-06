class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_ordered = heights.copy()
        
        heights_ordered.sort()
        
        solution = 0
        
        for i in range(len(heights)):
            if heights_ordered[i] != heights[i]:
                solution += 1
        
        return solution