class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach: # stuck current index i is beyond the furthest reachable index
                return False
            max_reach = max(max_reach, i + nums[i])
        
        return True
            
                 