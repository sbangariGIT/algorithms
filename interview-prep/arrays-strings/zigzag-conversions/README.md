# Zig Zag Conversions

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

# Solution

So the key idea here is to think about it as arrays with numRows. For example

arr = [
    [P, A, H, N],
    [A, P, L, S, I, I, G],
    [Y,  I, R,]
]

Hence everytime you try to enter just keep track of inserting at the top or bottom of your current index.