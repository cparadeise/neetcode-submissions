class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            curArea = (right - left) * min(heights[left], heights[right])
            maxArea = max(maxArea, curArea)

            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1

        return maxArea