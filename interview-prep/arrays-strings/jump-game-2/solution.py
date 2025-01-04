class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_end = 0
        end_reachable = 0
        result = 0

        for i in range(len(nums) - 1):
            end_reachable = max(end_reachable, i + nums[i])

            # You have reached that max jump that you can take from previous spot
            if i == curr_end:
                result += 1
                # You are updating the next spot to be the max that can be jumped to if you have taken any spot on the way
                curr_end = end_reachable
        return result
        
