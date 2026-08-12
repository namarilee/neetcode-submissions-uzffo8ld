class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        output = []

        nums.sort()

        def backtrack(i):
            if i >= len(nums):
                output.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()

            #move index to skip over duplicate(s)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1)
        
        backtrack(0)
        return output