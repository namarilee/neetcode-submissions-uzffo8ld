class Solution:
    def isValid(self, s: str) -> bool:
        charmap = { ")": "(", 
                    "]": "[",
                    "}": "{" }
        stack = []

        for c in s:
            if c in charmap: # is closed
                if stack and stack[-1] == charmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack