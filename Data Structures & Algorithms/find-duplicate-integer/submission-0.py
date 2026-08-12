class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = set()

        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return nums[i]
        #     else:
        #         seen.add(nums[i])

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow