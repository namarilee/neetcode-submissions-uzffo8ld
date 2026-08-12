class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort() #lets us stop early when sum exceeds target

        def backtrack(i, combo, total):
                
            if total == target: #base case
                output.append(combo.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target: #exceeds, so stop the loop
                    return
                
                combo.append(nums[j])
                backtrack(j, combo, total + nums[j]) #add current number to total
                combo.pop() #undo

        backtrack(0, [], 0)
        return output
