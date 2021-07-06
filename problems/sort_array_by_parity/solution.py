class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        #Iterate through the array, if there is an odd number, remove it and append it to the end.
        
        j = 0 #Synthetic counter variable
        
        for i in range(len(nums)):
            if nums[j] % 2 != 0:
                nums.append(nums[j])
                nums.pop(j)
                continue
            j += 1 #I just want i to iterate through the array once. j can take care of the operations
                
        return nums