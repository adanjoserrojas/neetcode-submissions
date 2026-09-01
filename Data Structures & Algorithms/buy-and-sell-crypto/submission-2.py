class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # I can use a sliding window that checks intervals of 2 in order
        # I actually can sell days later after buying... Meaning, I do not have to stick
        # to interval of 2 days...
        # result starts at 0 and if (sellDay - buyDay) > res, update res.
        # if all values are negative, meaning I lose money on every possible trade then
        # return 0, meaning no trade was done.

        # I just noticed that if I keep the left pointer static at a small value and keep
        # checking for a bigger profit, I can maximize that profit.
        # so my window starts at lenght 2, but if I find a number smaller for my left pointer
        # then I can move my left to that index and my right to the one after

        left = 0
        right = left + 1
        res = 0

        while right < len(prices):

            cur_profit = prices[right] - prices[left]

            if cur_profit > res:
                res = cur_profit

            if prices[left] >= prices[right]:
                left = right
            right += 1

        return res





        