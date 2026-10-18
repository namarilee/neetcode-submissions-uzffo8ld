from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq_map = defaultdict(int)
        max_length = 0
        max_freq = 0

        for r in range(len(s)):
            freq_map[s[r]] += 1
            
            max_freq = max(max_freq, freq_map[s[r]])

            while (r - l + 1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)
        
        return max_length
