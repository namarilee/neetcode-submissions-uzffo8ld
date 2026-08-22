class Solution {
    func numIslands(_ grid: [[Character]]) -> Int {
        var grid = grid
        let rows = grid.count
        let cols = grid[0].count

        var islands = 0
        let directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        func bfs(_ r: Int, _ c: Int) {
            var queue = Deque<(Int, Int)>()
            queue.append((r, c))
            grid[r][c] = "0"
            while !queue.isEmpty {
                let (row, col) = queue.popFirst()!
                for dir in directions {
                    let nr = row + dir[0]
                    let nc = col + dir[1]
                    if nr >= 0 && nc >= 0 && nr < rows && nc < cols && grid[nr][nc] == "1" {
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))
                    }
                }
            }
        }

        for r in 0..<rows {
            for c in 0..<cols {
                if grid[r][c] == "1" {
                    bfs(r, c)
                    islands += 1
                }
            }
        }
        return islands
    }
}
