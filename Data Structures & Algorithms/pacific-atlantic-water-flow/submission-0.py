class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #main problem: find cells that can reach both pacific and atlantic
        #water can only flow if its neighbor's height is less or equal

        rows, cols = len(heights), len(heights[0])
        # contains positions that can reach pacific and atlantic
        pac, atl = set(), set()

        def dfs(r, c, visit, prev_height):
            # can't flow through if already visited, out of range, 
            # or less than previous (going from edge to center so condition is opposite)
            if ((r, c) in visit or r not in range(rows) or c not in range(cols)
            or heights[r][c] < prev_height):
                return
            visit.add((r, c))
            #check all neighbors
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])


        for c in range(cols):
            #every position in first row (pacific)
            #pass in previous height, default value is height of start position
            dfs(0, c, pac, heights[0][c])
            #every position in last row (atlantic)
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            #every position is leftmost column (pacific)
            dfs(r, 0, pac, heights[r][0])
            #every position is rightmost column (atlantic)
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        #in every cell, if position in both pac and atl (can reach both oceans), add to result
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])
        
        return result

