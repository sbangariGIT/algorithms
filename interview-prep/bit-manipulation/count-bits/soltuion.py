class Solution:
    def countBits(self, n: int):
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        result = [0, 1]
        offset = 1
        for i in range(2, n+1):
            if i == offset * 2:
                offset = i
            result.append(1+result[i-offset])
        return result
        