class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(opens, closes):
            if opens == closes == n:
                result.append("".join(stack))
                return

            if opens < n:
                stack.append("(")
                backtrack(opens + 1, closes)
                stack.pop()

            if closes < opens:
                stack.append(")")
                backtrack(opens, closes + 1)
                stack.pop()
        
        backtrack(0, 0)
        return result