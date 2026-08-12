class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n^2) SOLUTION
        # freq_map = {} # key: num, value: # of occurences
        # res = []
        # for n in nums:
        #     if n not in freq_map:
        #         freq_map[n] = 1
        #     else:
        #         freq_map[n] += 1

        # for n in range(k):
        #     max_value = max(freq_map.values())
        #     print(max_value)
        #     key = list(freq_map.keys())[list(freq_map.values()).index(max_value)]
        #     print(key)
        #     res.append(key)
        #     if key in freq_map:
        #         del freq_map[key]

        # return res

        count = {}  # key: num, value: # of occurences
        freq = [[] for i in range(len(nums) + 1)] # index: # of occurences, 

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        # O(n)