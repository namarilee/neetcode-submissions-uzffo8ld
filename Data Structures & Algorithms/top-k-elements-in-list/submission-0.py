class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {} # key: num, value: # of occurences
        res = []
        for n in nums:
            if n not in freq_map:
                freq_map[n] = 1
            else:
                freq_map[n] += 1

        for n in range(k):
            max_value = max(freq_map.values())
            print(max_value)
            key = list(freq_map.keys())[list(freq_map.values()).index(max_value)]
            print(key)
            res.append(key)
            if key in freq_map:
                del freq_map[key]

        return res