class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            if char in brackets: #is open
                stack.append(char)
            else: #is closed
                if not stack or brackets[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
        
        return not stack