class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def bt(r, c, i): #row, col, index of word
            if i == len(word):
                return True
            
            #false if out of bounds, wrong char, or already visited
            if (r not in range(ROWS) or c not in range(COLS) or 
                word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c))

            #check all directions for the next char
            result = (
                bt(r + 1, c, i + 1) or
                bt(r, c + 1, i + 1) or
                bt(r - 1, c, i + 1) or
                bt(r, c - 1, i + 1)
            )

            path.remove((r, c))

            return result
        
        for r in range(ROWS):
            for c in range(COLS):
                if bt(r, c, 0):
                    return True
        
        return False
        