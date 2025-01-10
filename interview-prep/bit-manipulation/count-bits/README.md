# Counting Bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

# Solution

The key here is to write few examples and if you see, after every 2,4,8 we see a repeat in the last digits with the addition of 1 in the significant value.
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101