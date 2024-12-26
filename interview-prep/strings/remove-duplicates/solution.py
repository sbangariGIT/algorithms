class Solution:
    def removeDuplicates(self, nums) -> int:
        current = None
        current_index = 0
        for index in range(len(nums)):
            if nums[index] != current:
                nums[current_index] = nums[index]
                current = nums[current_index]
                current_index += 1
                continue
        return current_index