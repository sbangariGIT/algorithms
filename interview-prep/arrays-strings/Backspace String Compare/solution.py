class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        skip = 0
        new_s = ""
        for i in range(len(s) -1, -1, -1):
            if s[i] == '#':
                skip += 1
                continue
            if skip > 0:
                skip -= 1
                continue
            new_s += s[i]
        new_t = ""
        skip = 0
        for i in range(len(t) -1, -1, -1):
            if t[i] == '#':
                skip += 1
                continue
            if skip > 0:
                skip -= 1
                continue
            new_t += t[i]
        return new_s == new_t