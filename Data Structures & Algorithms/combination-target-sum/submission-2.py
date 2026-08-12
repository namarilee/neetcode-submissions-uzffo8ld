class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        combo = []

        def backtrack(i, total):
            if total == target:
                output.append(combo.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            combo.append(nums[i])
            backtrack(i, total + nums[i])

            combo.pop()
            backtrack(i + 1, total)
        
        backtrack(0, 0)
        return output