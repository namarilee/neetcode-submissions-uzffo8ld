class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occurS = {}
        occurT = {}

        for i in range(len(s)):
            if s[i] not in occurS:
                occurS[s[i]] = s.count(s[i])
            if t[i] not in occurT:
                occurT[t[i]] = t.count(t[i])
        
        return occurS == occurT