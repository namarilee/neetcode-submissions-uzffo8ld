class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        i = 0
        max_area = 0

        while i < len(heights):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                right = i - 1
                left = stack[-1] if stack else -1
                max_area = max(max_area, (right - left) * heights[top])
        
        while stack:
            top = stack.pop()
            width = i - stack[-1] - 1 if stack else i
            max_area = max(max_area, width * heights[top])
        
        return max_area
