class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        minheap = [(0, k)] #weight, start node
        shortest_times = defaultdict(int)

        while minheap:
            weight, node = heapq.heappop(minheap)

            if node in shortest_times:
                continue
            
            shortest_times[node] = weight

            for nei, nei_w in graph[node]:
                if nei not in shortest_times:
                    heapq.heappush(minheap, (weight + nei_w, nei))
        if len(shortest_times) < n:
            return -1
        return max(shortest_times.values())

