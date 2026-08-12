class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)] #each list represents each node, contains nodes that are adjacent
        visited = set() # keep track of visited
        for u, v in edges: # add both connections
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        output = 0

        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                output += 1
        
        return output