class Solution:
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1

        while l < r:
            if (numbers[l] + numbers[r]) == target:
                return [l+1, r+1]
            if (numbers[l] + numbers[r]) > target:
                r -= 1
            if (numbers[l] + numbers[r]) < target:
                l += 1
        return []

