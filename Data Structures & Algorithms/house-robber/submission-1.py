class Solution:
    def rob(self, nums: List[int]) -> int:
        # starting from the last house, can either rob house (i) and (i-2) OR house (i-1)

        #base case 1: no houses
        if len(nums) == 0:
            return 0
        
        #base case 2: one house
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            #recurrence relation
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[-1]
