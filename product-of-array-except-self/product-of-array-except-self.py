from numpy import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        sol,sol2 = [],[]
        
        curProd = 1
        sol.append(curProd)
        for i in range(1,len(nums)):
            curProd = nums[i-1]*curProd
            sol.append(curProd)
        
        curProd = 1
        sol2.insert(0,curProd)
        for i in range(len(nums)-2,-1,-1):
            curProd = nums[i+1]*curProd
            sol2.insert(0,curProd)
        
        for i in range(len(sol2)):
            sol[i] = int(sol[i]*sol2[i])
            
        return sol