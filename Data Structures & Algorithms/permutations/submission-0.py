class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        output = []

        def backtrack():
            if len(stack) == len(nums):
                output.append(stack.copy())
                return
            
            for num in nums:
                if num not in stack:
                    stack.append(num)
                    backtrack()
                    stack.pop()
        
        backtrack()
        return output