class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]

        curSum = 0

        for n in nums:
            if curSum < 0: #negative
                curSum = 0 #reset to 0 (start new subarray)
            curSum += n 
            maxSub = max(maxSub, curSum) #keep track of the max
        
        return maxSub