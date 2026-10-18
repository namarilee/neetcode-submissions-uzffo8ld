from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_q = deque() #decreasing order
        output = []

        for i in range(len(nums)):
            while max_q and nums[i] >= nums[max_q[-1]]:
                max_q.pop()
            
            max_q.append(i)

            if max_q[0] < i - k + 1:
                max_q.popleft()
            
            if i >= k - 1:
                output.append(nums[max_q[0]])
        
        return output

