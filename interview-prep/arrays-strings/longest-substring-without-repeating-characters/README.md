# Problem
Given a string s, find the length of the longest substring without repeating characters.


# Explaining the Solution

Here we use the sliding window method to solve the problem. The idea is two have two pointers and a table to keep the latest index of a given Char. While you traverse through each character is the character alrady exists in the list, update the max and get your pointers to reset considering the newest substring.

## Time Complexity is

O(N) ~ where N is the lenght of the string. All the look ups are O(1) since we are using dict.
Space is O(m) where m ~ is number of unique chars that can be in an array.
