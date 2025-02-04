from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l = 0
        r = 0
        tmap = Counter(t)
        fmap = {}
        formed = 0
        result_length = float('inf')
        result = ""
        while r < len(s):
            if s[r] in tmap:
                if s[r] not in fmap:
                    fmap[s[r]] = 0
                fmap[s[r]] += 1
                if fmap[s[r]] == tmap[s[r]]:
                    formed += 1
            while formed == len(tmap) and l <= r:
                if r+1 - l < result_length:
                    result = s[l:r+1]
                    result_length = r+1 - l
                # remove the s[l]
                if s[l] in tmap:
                    fmap[s[l]] -= 1
                    if fmap[s[l]] < tmap[s[l]]:
                        formed -= 1
                l += 1
            r += 1
            
        return result
