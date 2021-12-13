def twoSumII(nums, i, solution):
    
    # sum = nums[0]

    low = i + 1
    high = len(nums)-1
    
    while low < high:
        sum = nums[i] + nums[low] + nums[high]
        if sum < 0:
            low += 1
        elif sum > 0:
            high -= 1
        else:
            solution.append([nums[i], nums[low], nums[high]])
            # Keep looking for other solutions, but make sure there are no duplicates after nums[low]
            low += 1
            high -= 1
            while low < high and nums[low] == nums[low-1]:
                low += 1
                # what if nums[high] has a duplicate you might ask? It doesn't matter because if it is part of a new solution, that solution would be unique
            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Sort first, because your Big O allows you to afford it. And it makes duplicates easier to deal with
        nums = sorted(nums)
        solution = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSumII(nums, i, solution)
        
        res = []
        
        [res.append(i) for i in solution if i not in res]
        
        return res