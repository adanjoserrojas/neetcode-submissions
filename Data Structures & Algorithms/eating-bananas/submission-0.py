import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        k_upper = max(piles)
        k_lower = 1
        ans = k_upper

        while k_lower <= k_upper:

            mid = k_lower + (k_upper - k_lower) // 2

            total_hours = sum(math.ceil(pile / mid) for pile in piles)
            if total_hours <= h:
                ans = mid
                k_upper = mid - 1
            else:
                k_lower = mid + 1

        return ans