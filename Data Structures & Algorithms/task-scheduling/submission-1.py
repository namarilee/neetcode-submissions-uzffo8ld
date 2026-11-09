class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks) #X: 2, Y: 2
        #next_time_can_be_used, remaining_count
        minheap = [(0, c) for c in freq.values()]
        curr_time = 0

        while minheap:
            #if most urgent task is available
            if minheap[0][0] <= curr_time:
                time, count = heapq.heappop(minheap)
                if count - 1: #if there are still instances of that task left
                    #push it back to heap with updated availability time 
                    heapq.heappush(minheap, (time + n + 1, count - 1))
                curr_time += 1
            else:
                #fast forward to next time a task becomes available
                curr_time = minheap[0][0]
        
        return curr_time