class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        i = 0
        result = 0
        # no leading spaces - alternative s.lstrip()
        while i < n:
            if (s[i] != ' '):
                break
            i += 1
        # determine the sign
        sign = 1
        if i < n and s[i] == '-':
            sign = -1
        if i < n and (s[i] == '-' or s[i] == '+'):
            i += 1
        # calculate the value
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        while i < n and s[i] in digits:
            curr_digit = int(s[i])
            # process logic for calculating the result
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and curr_digit > INT_MAX % 10):
                if sign == -1:
                    return INT_MIN
                return INT_MAX
            result = result* 10 + curr_digit
            i += 1
        return result * sign
