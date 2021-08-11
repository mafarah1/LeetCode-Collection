class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        #     Explanation: Our array "S" must be generally sorted as [0]*a + [1]*b
        #         - Examples: 000, 001, 011, 111
        #         - We can sweep through each configuration computing their cost
        # To get started, we assume that we have an array of 1's (111), and every zero must be changed
        # Compute this cost:
        cost = 0
        for x in S:
            if x=='0':
                cost += 1
        # This is our baseline guess for the best answer
        best = cost
        #     Now we will start allowing zeros up to x=S[i] (last allowed zero)
        #         Check how many zeros can stay for free, and..
        #         How many 1's must be force to change as we advance
        #
        for x in S: # last 0 allowed
            if x=='0':
                cost -= 1 # this "zero" no longer is a problem (subtract from original cost)
            else:
                cost += 1 # this "one" must be forced to change (higher cost)
            best = min(best,cost)
        return best
            #Pick an index, for each index, see how many changes it take for everything in the left to be 0 and everything on the right to be 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

# My previous solution that worked for 72/93 test cases

# class Solution:
#     def minFlipsMonoIncr(self, s: str) -> int:
#         # Start counting from after the first 1
#         # If the number of 1s are greater than the number of 0s, return the number of 0s
#         # and vice versa

#         for i in range(len(s)):
#             if int(s[i]) == 1:
#                 index = i
#                 break
                
#         one, zero, one_right_side, zero_right_side = 0, 0, 0, 0
        
#         for i in range(index, len(s)):
#             print(one)
#             print(zero)
#             print()
#             if int(s[i]) == 1:
#                 one += 1
#             if int(s[i]) == 0:
#                 zero += 1
                
#         #in case it's all ones
#         if zero == 0:
#             return 0
#         # In case it's all 1s
#         if one == 0:
#             return 0

#         #for counting the 0s on one side
#         for i in range(len(s)-1,0,-1):
#             zero_right_side += 1
#             if int(s[i]) == 1:
#                 break

#         for i in range(len(s)-1,0,-1):
#             if int(s[i]) == 0:
#                 index2 = i
#                 break

#         for i in range(index2, 0, -1):
#             if int(s[i]) == 1:
#                 one_right_side += 1
    
#         # In case it's perfect
#         if one_right_side == 0:
#             return 0    
        
#         print(one,zero,one_right_side,zero_right_side)
        
#         #If the zeros on the right are more than the ones on the right, don't bother with them
#         if zero_right_side > one_right_side:
#             one_right_side = 9999
        
#         return min(one,zero,one_right_side)        