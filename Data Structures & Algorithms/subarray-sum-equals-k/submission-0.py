class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #keep a running prefix sum
        prefix = 0
        #keep track of how many times the prefix sum was seen
        counts = defaultdict(int)
        counts[0] = 1
        subarrays = 0

        for n in nums:
            prefix += n
            if prefix - k in counts:
                subarrays += counts[prefix - k]
            counts[prefix] = counts.get(prefix, 0) + 1
        
        return subarrays
