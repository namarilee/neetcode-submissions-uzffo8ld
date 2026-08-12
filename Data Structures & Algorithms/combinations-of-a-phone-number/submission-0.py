class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        output = []

        def backtrack(i, combo):
            if len(combo) == len(digits):
                output.append("".join(combo))
                return
            
            for char in letters[digits[i]]:
                combo.append(char)
                backtrack(i + 1, combo)
                combo.pop()
            
        if digits:
            backtrack(0, [])
            
        return output