class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #convert all to negative since we're creating a max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: #stop when 1 item left
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            #if the stones are equal, don't do anything as they are already removed
            if second > first: #comparing negatives, so second largest would be "less"
            # -7 > -8
                heapq.heappush(stones, first - second)
        if len(stones) == 0:
            stones.append(0)
        return stones[0] * -1
