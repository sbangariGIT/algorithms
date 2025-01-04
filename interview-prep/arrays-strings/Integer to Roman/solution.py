class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        nums = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        while num > 0:
            for key, val in nums:
                if num - key >= 0:
                    result += val
                    num -= key
                    break        
        return result


## Beter Solution

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         digits = [
#             (1000, "M"),
#             (900, "CM"),
#             (500, "D"),
#             (400, "CD"),
#             (100, "C"),
#             (90, "XC"),
#             (50, "L"),
#             (40, "XL"),
#             (10, "X"),
#             (9, "IX"),
#             (5, "V"),
#             (4, "IV"),
#             (1, "I"),
#         ]

#         roman_digits = []
#         # Loop through each symbol.
#         for value, symbol in digits:
#             # We don't want to continue looping if we're done.
#             if num == 0:
#                 break
#             count, num = divmod(num, value)
#             # Append "count" copies of "symbol" to roman_digits.
#             roman_digits.append(symbol * count)
#         return "".join(roman_digits)