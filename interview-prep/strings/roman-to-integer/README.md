# Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given a roman numeral, convert it to an integer.

# Solution
Iterate through the string for each character is the character in from of the current is greater in value that means that we need to subtract it from the one in front. Once we get that the rest is pretty straight forward.

# Time Complexity

This is O(1) since there is a finite set of roman numerals, the maximum number possible number can be 3999, which in roman numerals is MMMCMXCIX. As such the time complexity is O(1).