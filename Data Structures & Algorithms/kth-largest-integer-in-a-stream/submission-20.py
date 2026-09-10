import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.value: int = k
        self.heap: list = []
        for index in range(len(nums)):
            if len(self.heap) < k:
                heapq.heappush(self.heap, nums[index])
            elif nums[index] > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, nums[index])
        print(self.heap)

    def add(self, val):

        if len(self.heap) < self.value:
            heapq.heappush(self.heap, val)
        
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        
        return self.heap[0]
        