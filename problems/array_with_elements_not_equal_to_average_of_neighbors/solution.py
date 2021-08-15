class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        for num in range(len(nums)-1):
            if nums[num] == ((nums[num-1] + nums[num+1])/2):
                nums[num], nums[num-1] = nums[num-1], nums[num]

        for num in range(len(nums)-1):
            if nums[num] == ((nums[num-1] + nums[num+1])/2):
                self.rearrangeArray(nums)
        
        return nums