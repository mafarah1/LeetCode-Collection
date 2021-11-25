class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums2 = set()
        
        for n in nums:
            if n in nums2: return True 
            nums2.add(n)
        
        return False