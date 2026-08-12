class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valIndex = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in valIndex:
                return [valIndex[diff], i]
            else:
                valIndex[n] = i