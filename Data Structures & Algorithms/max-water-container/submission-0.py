class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        # res = 0

        # for l in range(len(heights)):
        #     for r in range(l + 1, len(heights)):
        #         area = (r - l) * min(heights[l] , heights[r])
        #         res = max(res, area)
        
        # return res

        # O(n)

        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res