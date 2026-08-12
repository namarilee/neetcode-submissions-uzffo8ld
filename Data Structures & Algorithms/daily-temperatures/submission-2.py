class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #[temp, index]

        output = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]: #top item temp
                stack_temp, stack_idx = stack.pop()
                output[stack_idx] = (i - stack_idx)
            
            stack.append([n, i])
        
        return output
