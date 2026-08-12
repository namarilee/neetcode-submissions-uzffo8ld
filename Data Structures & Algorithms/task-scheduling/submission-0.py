class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxheap = [-count for count in freq.values()] #remaining counts of task
        heapq.heapify(maxheap)

        time = 0
        queue = deque() #[remaining_count_after_running, next_available_time]

        while maxheap or queue:
            time += 1
            if not maxheap: #empty
                time = queue[0][1] #next avail time for front element
            else:
                count = 1 + heapq.heappop(maxheap) #"decreasing" the count since all values in maxheap are negative
                if count != 0:
                    queue.append([count, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue.popleft()[0]) #push remaining count
        
        return time                                                