class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxq = deque()
        output = []

        for i in range(len(nums)):
            while maxq and nums[i] >= nums[maxq[-1]]:
                maxq.pop()
            
            maxq.append(i)

            if maxq[0] < i - k + 1:
                maxq.popleft()
            
            if i >= k - 1:
                output.append(nums[maxq[0]])
        
        return output