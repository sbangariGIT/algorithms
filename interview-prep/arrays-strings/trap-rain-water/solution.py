class Solution:
    def trap(self, height) -> int:
        if height == None:
            return 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                maxL = max(maxL, height[l])
                res += maxL - height[l]
                l += 1
                continue
            maxR = max(maxR, height[r])
            res += maxR - height[r]
            r -= 1
        return res