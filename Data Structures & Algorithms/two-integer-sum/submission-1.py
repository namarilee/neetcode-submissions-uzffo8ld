class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valIndex = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in valIndex:
                return [valIndex[diff], i]
            else:
                valIndex[nums[i]] = i