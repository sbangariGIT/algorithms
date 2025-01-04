class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1 or len(s) <= numRows):
            return s
        result = []
        for _ in range(numRows):
            result.append([])
        current = 0
        increasing = True
        for c in s:
            result[current].append(c)
            if current == (numRows - 1):
                increasing = False
            if current == 0:
                increasing = True
            if increasing:
                current += 1
                continue
            current -= 1
        answer = ""
        for i in result:
            for c in i:
                answer += c
        return answer