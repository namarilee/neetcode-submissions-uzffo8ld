class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combo = []

        def backtrack(i, currsum):
            if currsum == target:
                result.append(combo.copy())
                return

            if currsum > target:
                return
            
            if i >= len(nums):
                return

            combo.append(nums[i])
            currsum += nums[i]
            backtrack(i, currsum)

            currsum -= nums[i]
            combo.pop()
            backtrack(i + 1, currsum)
        
        backtrack(0, 0)
        return result