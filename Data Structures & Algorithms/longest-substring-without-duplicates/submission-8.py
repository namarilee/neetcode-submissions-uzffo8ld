class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = 0
        longest = 0        
        
        if len(s) <= 1:
            return len(s)

        l = 0

        for r in range(len(s)):
            while s[r] in seen: #if repeating
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1) #current window size



        return longest