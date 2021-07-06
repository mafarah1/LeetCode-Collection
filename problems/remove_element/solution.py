import collections

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        while val in nums: #While an instance of val exists in nums
            nums.remove(val)
        
        return len(nums)