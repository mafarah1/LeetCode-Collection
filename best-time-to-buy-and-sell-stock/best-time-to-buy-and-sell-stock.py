# Previous solution that was O(n) to O(n^2)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxProfit = 0
#         numberOfDays = len(prices)

#         # Was receiving time exceeded messages, so I elminated redundancy using Kadane's algorithm (basically, stop trying to find the same number again, as long as the maximum has already been established)
#         maximumInTheInterval = max(prices)
    
    
#         for i in range(numberOfDays):
            
#             prevMax = maxProfit
            
#             if i == numberOfDays-1:
#                 break
                            
#             if prices[i] == maximumInTheInterval:
#                 maximumInTheInterval = max(prices[i+1:numberOfDays])
            
#             maxProfit = max(prevMax, 
#                             maximumInTheInterval - prices[i]
#                            )

#         return maxProfit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # I was overthinking it, I just need one pass through and find the minimum, then the profit relative to the last minimum and the current price, then find their max
        
        minimum, maximum, maximumProfit = float("inf"), 0, 0
        
        for price in prices:
            minimum = min(minimum, price)
            profit = price - minimum
            maximumProfit = max(profit, maximumProfit)

        return maximumProfit