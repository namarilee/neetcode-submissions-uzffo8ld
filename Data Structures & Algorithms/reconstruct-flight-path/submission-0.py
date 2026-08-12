class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ['JFK']

        def dfs(src):
            if len(res) == len(tickets) + 1: #found the solution
                return True
            
            if src not in adj: #doesn't have any outgoing edges
                return False
            
            neighbors = list(adj[src])
            for i, nei in enumerate(neighbors):
                adj[src].pop(i) #try visiting it
                res.append(nei)

                if dfs(nei): #check the above conditions
                    return True
                
                #backtrack if didn't return true
                adj[src].insert(i, nei)
                res.pop()
            
            return False
        
        dfs('JFK')
        return res