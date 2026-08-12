class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            # [rob1, rob2, n, n + 1, ...]
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2