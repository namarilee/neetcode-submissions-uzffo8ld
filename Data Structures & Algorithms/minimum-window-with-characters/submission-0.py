class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        t_freq = Counter(t)
        window = defaultdict(int)
        have = 0
        need = len(t_freq)
        result = [-1, -1] #l, r for best window
        res_len = float("inf") 

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            if char in t_freq and window[char] == t_freq[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    result = [l, r]
                    res_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1

        l, r = result
        return s[l : r + 1] if res_len != float('inf') else ""