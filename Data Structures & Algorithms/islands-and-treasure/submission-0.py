from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        #main idea: run bfs on each gate simultaneously

        #add all gates to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        def add_room(r, c):
            #check if position is out of bounds, already visited, or is an obstacle
            if (r not in range(rows) or c not in range(cols) or
            (r, c) in visited or grid[r][c] == -1):
                return #invalid
            
            visited.add((r, c))
            queue.append((r, c))
            
        dist = 0
        while queue:
            # for each gate, 
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                # add every neighbor
                add_room(r + 1, c)
                add_room(r - 1, c)
                add_room(r, c + 1)
                add_room(r, c - 1)

            dist += 1