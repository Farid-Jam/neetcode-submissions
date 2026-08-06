class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        
        res = 0
        l = 0
        r = l + 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                profit = prices[r] - prices[l]
                res = max(res, profit)
                r += 1
        return res