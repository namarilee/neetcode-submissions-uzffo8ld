from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minheap.append([dist, x, y])
        
        heapq.heapify(minheap)
        points = []

        #pop k number of times and add point to result list
        for _ in range(k):
            dist, x, y = heapq.heappop(minheap)
            points.append([x, y])
        
        return points