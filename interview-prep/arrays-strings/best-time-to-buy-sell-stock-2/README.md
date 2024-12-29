# Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

# Solution

The key to such problems is to visualize the graph. Once you draw the graph of the prices you realize that the max profit is the amount of money that you can make going from a valley in the graph to any peak i.e anytime there is an increase in value you want to collect it. This sums up to the max profit you can generate in a graph.

# Complexity

`O(n)` - Time
`O(1)` - Space