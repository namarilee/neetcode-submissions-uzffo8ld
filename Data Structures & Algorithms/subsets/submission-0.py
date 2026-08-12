class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = [] 

        def backtrack(i): #pass in index
            #base case: if i is out of bounds
            # we know that subset has been generated
            if i >= len(nums):
                output.append(subset.copy()) #subset is being modified, so add a copy
                return
            
            #decision to include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            #decision not to include nums[i]
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return output