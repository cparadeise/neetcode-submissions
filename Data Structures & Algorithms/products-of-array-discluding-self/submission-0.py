class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # do math
        p = []
        # for every num, multiply each other index except the current num
        for i, num in enumerate(nums):
            t = 1
            for j, num in enumerate(nums):
                if i != j:
                    t = t * nums[j]

            p.append(t)
        return p