class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u, v, w in times:
            adj_list[u].append((v, w))
        
        minheap = [(0, k)] #weight, node
        visited = set()
        result = 0

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visited:
                continue
            visited.add(n1)
            result = max(result, w1)

            for n2, w2 in adj_list[n1]: #go through neighbors
                if n2 not in visited:
                    heapq.heappush(minheap, (w1 + w2, n2)) #add total path
        
        #return result if we visited all the nodes
        return result if len(visited) == n else -1

        #O(E * logV)