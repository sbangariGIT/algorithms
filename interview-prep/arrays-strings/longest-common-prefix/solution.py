class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            current = 0
            pre = ""
            for c in strs[i]:
                if current < len(prefix) and prefix[current] == c:
                    pre += c
                    current += 1
                    continue
                break
            prefix = pre
            if prefix == "":
                break
        return prefix
                