class Solution:
    def hIndex(self, citations) -> int:
        counting = [0] * (len(citations) + 1)

        for i in range(len(citations)):
            counting[min(citations[i], len(citations))] += 1
        print(counting)
        h = len(counting)
        z = 0
        i = len(counting) - 1
        while h > z:
            print(z, "papers have atleast", h, "citations")
            z += counting[i]
            i -= 1
            h -= 1
        print(z, "papers have atleast", h, "citations")
        return h
