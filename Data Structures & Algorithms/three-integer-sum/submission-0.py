class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # skip same element to avoid duplicates
            if i > 0 and a == nums[i - 1]:
                continue
            
            # two pointer sum for remaining sub-array
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    # add to results
                    res.append([a, nums[l], nums[r]])
                    # move pointer to keep looking for other pairs
                    l += 1

                    # skip duplicates values for the left pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
        return res
            