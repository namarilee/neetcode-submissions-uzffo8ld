class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        combo = []
        output = []

        def backtrack(i):
            if i >= len(digits):
                output.append("".join(combo.copy()))
                return
            
            for letter in letter_map[digits[i]]:
                combo.append(letter)
                backtrack(i + 1)
                combo.pop()

        backtrack(0)
        return output
        