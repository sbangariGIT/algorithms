# Traping Rainwater

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Solution
Consider that for each part of the array you just need the units that are stored at that particular index.

Amount of water stored at an index is
a[i] = min(maxL, maxR) - height[i] 

Since we do min we can ignore the least element from the array and move the window.