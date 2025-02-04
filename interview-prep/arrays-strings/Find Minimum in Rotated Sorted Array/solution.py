class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        current_min = float('inf')
        while l < r:
            mid = (l+r) // 2
            current_min = min(current_min, nums[mid])
            if nums[mid] < nums[r]:
                r = mid - 1
            elif nums[mid] > nums[r]:
                l = mid + 1
        return min(current_min, nums[l])

