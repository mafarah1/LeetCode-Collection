class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        
        if len(nums) == 0:
            return nums[0]
        
        largestSum = -10**4
        res = []
        
        # Trust the process
        for num in nums:     
            largestSum = max(num, (largestSum+num))
            res.append(largestSum)
        
        return max(res)