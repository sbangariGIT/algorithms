# String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. Specifically, integers less than -2^31 should be rounded to -2^31, and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.

# Histroy
The atoi() function returns the converted integer value if the execution is successful. If the passed string is not convertible to an integer, it will return a zero. ATOI can stand for ASCII to integer.

## Solution
This is a simple iterative process of each character of the string.

1. We make sure that we remove all the leading spaces i.e iterate over them.
2. Check for sign if present, if not move on
3. Check if the current result = or > than MAX_INT then return MAX_INT
4. Check is the char is a digit and if yes them add it to the result. New result is `result * 10 + digit`. Idea is that everytime you mutiply with 10 we can then add the digit. For Example 43 become 430 and if you are reading digit 8 we get 438.