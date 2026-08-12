from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #edge case: empty grid
        if not grid:
            return 0

        #get dimensions
        rows, cols = len(grid), len(grid[0])
        visited = set()

        num_islands = 0

        def bfs(r, c):
            #each item in the queue is the cell's coordinates
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                #check its neighbors in all directions
                for dr, dc in directions:
                    #compute the new coordinate
                    r, c = row + dr, col + dc
                    #make sure it is in range, is a "1", and not visited yet
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c) #check all of its neighbors
                    num_islands += 1
        return num_islands

