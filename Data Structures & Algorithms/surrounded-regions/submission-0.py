class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        #main idea: capture everything except unsurrounded regions ('O's that are not surrounded)

        #find 'O' regions that are not surrounded, change to 'T' (temporary)
        #function is only run on 'O's on the border, which we know for sure
        # it's unsurrounded
        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols) or
            board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        def on_boarder(r, c):
            return (r in [0, rows - 1]) or (c in [0, cols - 1])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and on_boarder(r, c):
                    dfs(r, c)

        #change all other 'O's to 'X' 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        #change 'T's back to 'O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'