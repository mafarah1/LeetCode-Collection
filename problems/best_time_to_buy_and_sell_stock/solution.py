class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit, minprice = 0, float("inf")
        
        for price in prices:
            minprice = min(price, minprice)
            profit = price - minprice
            maxprofit = max(maxprofit, profit)
        
        return maxprofit