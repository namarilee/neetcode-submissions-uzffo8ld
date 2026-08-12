from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        #add all rotten ones to the queue first
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    queue.append((r, c))

        def make_rotten(r, c):
            #check if is fresh fruit, in range, and not visited
            if (r not in range(rows) or c not in range(cols) 
                or grid[r][c] == 0 or (r, c) in visited):
                return
            visited.add((r, c))
            queue.append((r, c))

        #simultaneously go run bfs on all rotten fruits
        #for each layer, change fresh to rotten and increment minute 
        minutes = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = 2
                #visit each neighbor and if it's a fresh fruit, change it to rotten
                make_rotten(r + 1, c)
                make_rotten(r - 1, c)
                make_rotten(r, c + 1)
                make_rotten(r, c - 1)
            if queue:  #only increment minute if rotting happened
                minutes += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return minutes
