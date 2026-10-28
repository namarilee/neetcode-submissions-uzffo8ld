class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        minheap = [(0, k)] #weight, start node
        visited = set()
        result = 0

        while minheap:
            weight, node = heapq.heappop(minheap)

            if node in visited:
                continue
            
            visited.add(node)
            result = max(result, weight)

            for nei, nei_w in graph[node]:
                if nei not in visited:
                    heapq.heappush(minheap, (weight + nei_w, nei))
        return result if len(visited) == n else -1

