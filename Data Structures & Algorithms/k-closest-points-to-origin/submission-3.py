import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []
        res = []
        for point in points:

            distance = math.sqrt((abs(point[0]) - 0)**2 + (abs(point[1]) - 0)**2)
            print(distance)
            distances.append((distance, point))

        distances.sort()
        print(distances)
                
        for index in range(k):
            res.append(distances[index][1])

        return res