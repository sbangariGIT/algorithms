class Solution:
    def productExceptSelf(self, nums):
        # [1, 2, 3, 4]
        # [1, 1, 2, 6] ?? left[i] = left[i-1] * nums[i-1]
        # [24, 12, 4, 1] ?? right[i] = right[i+1] * nums[i+1]
        result = [1] * len(nums)
    
        # Calculate left products directly in the result array
        left_product = 1
        for i in range(len(nums)):
            result[i] = left_product
            left_product *= nums[i]
        
        # Multiply by right products directly in the result array
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result

