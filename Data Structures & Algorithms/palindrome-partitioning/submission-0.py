class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        output = []

        def backtrack(i, partition):
            if i >= len(s):
                output.append(partition.copy())
                return

            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    partition.append(s[i : j + 1])
                    backtrack(j + 1, partition)
                    partition.pop()
                    

        backtrack(0, [])
        return output
