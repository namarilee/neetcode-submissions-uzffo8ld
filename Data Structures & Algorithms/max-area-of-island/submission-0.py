class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            island_area = 0

            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            while queue:
                island_area += 1
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
            return island_area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    max_area = max(max_area, area)
        return max_area