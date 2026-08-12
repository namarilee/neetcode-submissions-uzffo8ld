import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        freq_count = Counter(nums)

        for n, freq in freq_count.items():
            heapq.heappush(maxheap, (-freq, n))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(maxheap)[1])

        return result