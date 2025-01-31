class Solution:
    def searchRange(self, nums, target: int):
        i = 0
        j = len(nums) - 1
        result = [-1, -1]
        found = False
        while j >= i:
            mid = (j + i) // 2
            if nums[mid] == target:
                if result[0] == -1:
                    found = True
                    result = [mid, mid]
                    break
            if nums[mid] > target:
                j = mid - 1
                continue
            i = mid + 1
        if found:
            # we want to calulate the start and the end
            # [5,7,7,8,8,10] and result = [4,4]

            # find the start index
            j = result[0] - 1
            i = 0
            while j >= i:
                mid = (i + j) // 2
                if nums[mid] == target:
                    result[0] = mid
                    j = mid - 1
                    continue
                i = mid + 1
            
            # find the last index
            j = len(nums) - 1
            i = result[1] + 1
            while j >= i:
                mid = (i + j) // 2
                if nums[mid] == target:
                    result[1] = mid
                    i = mid + 1
                    continue
                j = mid - 1
        return result