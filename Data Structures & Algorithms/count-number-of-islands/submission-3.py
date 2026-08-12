class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        visited = set()
        num_islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if ((nr, nc) not in visited and nr in range(ROWS)
                        and nc in range(COLS) and grid[nr][nc] == '1'):
                        queue.append((nr, nc))
                        visited.add((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    num_islands += 1

        return num_islands