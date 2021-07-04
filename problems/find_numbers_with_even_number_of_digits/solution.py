class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        solution = 0
        for i in range(0, len(nums)):
            if len(str(nums[i])) % 2 == 0:
                solution = solution + 1
        return solution