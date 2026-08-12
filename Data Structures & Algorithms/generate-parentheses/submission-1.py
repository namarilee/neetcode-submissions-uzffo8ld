class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        paren = []

        def backtrack(opens, closes):
            if opens == closes == n:
                output.append("".join(paren))
                return
            
            if opens < n:
                paren.append("(")
                backtrack(opens + 1, closes)
                paren.pop()

            if closes < opens: #ensures that the open/close is valid
                paren.append(")")
                backtrack(opens, closes + 1)
                paren.pop()
        
        backtrack(0, 0)
        return output