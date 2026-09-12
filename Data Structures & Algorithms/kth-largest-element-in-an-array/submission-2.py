import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [number * (-1) for number in nums]
        heapq.heapify(min_heap)

        for number in range(k):
            result = -heapq.heappop(min_heap)
    
        return result