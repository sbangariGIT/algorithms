class Solution:
    def findPeakElement(self, nums) -> int:
        l = 0
        r = len(nums) - 1  
        while l < r:
            potential_peak = (l + r) // 2
            if nums[potential_peak] > nums[potential_peak + 1] and nums[potential_peak] > nums[potential_peak - 1]:
                return potential_peak
            if nums[potential_peak] < nums[potential_peak + 1]:
                l = potential_peak + 1
                continue
            r = potential_peak - 1
        return max(l,r)