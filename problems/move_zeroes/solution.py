import collections

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if nums.count(0) < 1:
            return None
        
        total_freq = collections.Counter(nums)
        
        freq = total_freq.get(0)
        
        for i in range(total_freq.get(0)):
            nums.remove(0)
        
        for i in range(freq):
            nums.append(0)
        