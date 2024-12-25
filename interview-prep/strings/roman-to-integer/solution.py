# Questions you want ask?
# Can we assume that the string is a valid roman number?
# What do you want to return if we get an empty string?

# Thought process.
# We need to consider two things
# 1. Normal Roman String to Value
# 2. In the event that we have I, V, X, L, C, D before a larger roman value it subtracts

class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        result = 0
        roman_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(s) - 1):
            if roman_value[s[i+1]] > roman_value[s[i]]:
                # this means we need to subtract this value from the result
                result -= roman_value[s[i]]
                continue
            result += roman_value[s[i]]
        result += roman_value[s[-1]] # account for the last character
        return result
        