class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        res = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l
            else:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            r += 1
        return res