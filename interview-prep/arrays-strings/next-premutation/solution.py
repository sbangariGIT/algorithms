# 574883
class Solution:
    def swap_digits(self, a: int, b: int, nums):
        interim = nums[a]
        nums[a] = nums[b]
        nums[b] = interim
        
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        digit_swap_a = None
        digit_swap_b = None
        # [4, 5, 7, 5, 6, 3] 
        for index in range(len(nums)-1, 0, -1):
            if nums[index-1] < nums[index]:
                digit_swap_a = index - 1 
                break
        if digit_swap_a is None:
            return nums.reverse()
        
        for i in range(len(nums) - 1, digit_swap_a, -1):
            if nums[i] > nums[digit_swap_a]:
                digit_swap_b = i
                break
        self.swap_digits(digit_swap_a, digit_swap_b, nums)
        
        # from digit_swap_a + 1 till len(nums) we swap
        i = digit_swap_a + 1
        j = len(nums) - 1
        while i < j:
            self.swap_digits(i, j, nums)
            i += 1
            j -= 1
