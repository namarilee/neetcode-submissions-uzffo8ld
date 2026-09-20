class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #nlogn
 
 
        output = []

        #have a loop to go through nums
        for i in range(len(nums)):
            #early exit
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                triplet = nums[i] + nums[l] + nums[r]
                # if triplet == 0, append triplet
                if triplet == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                # if triplet > 0, decrement r
                if triplet > 0:
                    r -= 1
                # if triplet < 0, increment l
                if triplet < 0:
                    l += 1
        
        return output