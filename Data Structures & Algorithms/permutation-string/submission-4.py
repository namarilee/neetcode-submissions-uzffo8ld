class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        for r in range(len(s1), len(s2) + 1):
            substr = s2[l : r]
            if "".join(sorted(s1)) == "".join(sorted(substr)):
                return True
            l += 1
        return False