class Solution:
    def maxArea(self, height) -> int:
        maxima = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = (r-l) * min(height[r], height[l])
            maxima = max(maxima, area)
            if height[r] < height[l]:
                r -= 1
                continue
            l += 1
        return maxima
