# Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

## Solution

So we need to figure out if we can go from the 0th index to the last. Let's try to do it with an example nums = [2,3,1,1,4].

We can start iterating from the last index and check we there is enough jumps to ready the next "Good Index". A good index is an index that can reach the last index.
So for each i we need to check if `i + nums[i]` can reach the last good index. Check the code to get the better idea.
