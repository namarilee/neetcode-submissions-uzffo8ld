class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        # find possible first value

        for i, a in enumerate(nums):
            #not first value and same value as before (duplicate)
            if i > 0 and a == nums[i - 1]:
                continue #skip and check next value
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum == 0:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                # else:
                #     result.append([a, nums[l], nums[r]])
                #     l += 1

                #     while nums[l] == nums[l - 1] and l < r:
                #         l += 1
        
        return result