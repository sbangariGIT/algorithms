# Radix Sort

This sort is for numbers you already know the length of. We do stable sort inorder to maintain the correctness.

The runtime for this algorithm is

O(d (n + k))

d - number of digits in eeach number
k - each digit can have k distinct values
n - total number of numbers in an array

In order to sort for each round we use merge sort which is O(nlogn).

Choosing the correct d and k is very important for the efficiency of this algorithm. Have a bigger k than d by making the number into smaller chucks is better than each digit.