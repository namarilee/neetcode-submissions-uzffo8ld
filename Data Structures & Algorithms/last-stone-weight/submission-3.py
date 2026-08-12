class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #convert all to negative since we're creating a max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: #stop when 1 item left
            first = heapq.heappop(stones) * -1
            second = heapq.heappop(stones) * -1
            #if the stones are equal, don't do anything as they are already removed
            if first > second:
                heapq.heappush(stones, second - first) #push negative value back

        #edge case: if array is empty
        if len(stones) == 0:
            stones.append(0)

        return stones[0] * -1
