class Solution:
    def canJump(self, nums) -> bool:
        last_good_index = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_good_index:
                last_good_index = i
            
        return last_good_index == 0