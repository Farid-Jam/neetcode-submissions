class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        l = 0
        r = l + 1
        maxP = 0
        
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        
        return maxP

