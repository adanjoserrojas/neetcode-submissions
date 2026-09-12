import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        time = 0
        count = Counter(tasks)
        max_heap = [-value for value in count.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque()

        print(max_heap)
        print(count)

        while max_heap or q:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time


        