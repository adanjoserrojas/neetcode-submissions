import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [stone * (-1) for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 2:

            diff = 0
            if max_heap[1] > max_heap[2]:

                if (max_heap[0] * (-1)) > (max_heap[2] * (-1)):
                    diff = (max_heap[0] * (-1)) - (max_heap[2] * (-1))

                elif (max_heap[0] * (-1)) < (max_heap[2] * (-1)):
                    diff = (max_heap[2] * (-1)) - (max_heap[0] * (-1))

                max_heap.pop(2)
                heapq.heappop(max_heap)

                if diff != 0:
                    heapq.heappush(max_heap, diff * (-1))
            else:

                if (max_heap[0] * (-1)) > (max_heap[1] * (-1)):
                    diff = (max_heap[0] * (-1)) - (max_heap[1] * (-1))

                elif (max_heap[0] * (-1)) < (max_heap[1] * (-1)):
                    diff = (max_heap[1] * (-1)) - (max_heap[0] * (-1))

                max_heap.pop(1)
                heapq.heappop(max_heap)

                if diff != 0:
                    heapq.heappush(max_heap, diff * (-1))
            heapq.heapify(max_heap)
            
        if len(max_heap) == 0:
            return 0
        elif len(max_heap) == 1:
            return max_heap[0] * (-1)
        elif len(max_heap) == 2:
            return (max_heap[0] * (-1)) - (max_heap[1] * (-1))

        return max_heap[0] * (-1)

        
