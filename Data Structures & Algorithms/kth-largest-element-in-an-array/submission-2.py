class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []

        for n in nums:
            heapq.heappush(minheap, n)
            if len(minheap) > k:
                heapq.heappop(minheap)

        return minheap[0]