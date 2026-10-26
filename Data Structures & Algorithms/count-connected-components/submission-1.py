class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        #[1]
        #[0,2]
        #[1]
        #[4]
        #[3]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        count = 0

        def bfs(node):
            queue = deque([node])
            visited.add(node)

            while queue:
                num = queue.popleft()
                for nei in adj_list[num]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            
            return 1
        
        for i in range(len(adj_list)):
            if i not in visited:
                count += bfs(i)
        
        return count

        
