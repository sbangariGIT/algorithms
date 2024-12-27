# Next Permutation

One of the questions that I think I will remember for a very long time. So lets break it down.

## Problem
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.


## Solution

The idea is to look at a lot of examples to see the pattern. Given an array and get the lexicographical larger rearrangement we need to find the index that we need to swap and with the digit.

1. [5,3,8,4,3,2,1] => we see that the first `valley` happend at [3,8]. 
2. Now we know that we need to swap `3`, but with the number that is the next biggest from [8,4,3,2,1].
3. That would be `4`. Once swapped we get the array [5,4,8,3,3,2,1]. However this is not the final answer.
4. Since we swapped `3` and `4` the remaining elements from [8,3,3,2,1] need to be sorted. In which case since they are already in decending order can just be swapped. Making this operation O(n).
5. The final result is [5,4,1,2,3,3,8]. 

## Time Complexity

`O(n)` is the time complexity of this algo.
 