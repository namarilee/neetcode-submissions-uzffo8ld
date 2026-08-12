class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(i, combo, total):
                
            if total == target: #base case
                output.append(combo.copy())
                return

            if i >= len(nums) or total > target: #index out of bounds or total exceeds target
                return
                
            combo.append(nums[i])
            backtrack(i, combo, total + nums[i]) #backtrack with same index and add current number to total

            combo.pop() #undo
            backtrack(i + 1, combo, total) #try next index, don't add number to total


        backtrack(0, [], 0)
        return output
