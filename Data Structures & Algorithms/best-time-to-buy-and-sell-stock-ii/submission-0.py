class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1
        best = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                best += prices[r] - prices[l]
            l += 1
            r += 1
        
        return best
        