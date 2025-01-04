# Jump Game 2

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Solution

To really understand this solution, as we need to understand that as we go through the array we need to keep track of what the best possible place we can reach if we take any of the steps. That is for:
[2,3,1,1,4]

from nums[0] we can jump to nums[1] and nums[2], this means that we need to keep track of entry the best we can reach between nums[1] and nums[2] and make that our far end.