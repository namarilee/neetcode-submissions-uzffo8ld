class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse=True)

        for src, dst in tickets:
            adj[src].append(dst)
        
        res = []

        def dfs(src):
            while adj[src]:
                next_dest = adj[src].pop()
                dfs(next_dest)

            #once it has no more next destinations
            res.append(src)
        
        dfs('JFK')
        return res[::-1]