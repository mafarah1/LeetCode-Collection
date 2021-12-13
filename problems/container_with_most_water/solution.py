class Solution:
    def maxArea(self, nums: List[int]) -> int:
        
        lo, hi = 0, len(nums)-1
       
        maximum = 0
        
        while lo < hi:
            maximum = max(((hi-lo)*min(nums[hi],nums[lo])), maximum)
                  
            if nums[lo] < nums[hi]:
                lo += 1
            else:
                hi -= 1
                          
        return maximum