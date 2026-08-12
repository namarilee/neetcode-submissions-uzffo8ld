class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
        #nlargest returns a list of the n largest elements
        #[-1] gets the last element
        #example: k = 3 largest elements: [6, 5, 4]
        # returns 4