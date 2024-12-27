class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}
        max_len = 0
        j = 0
        for i in range(len(s)):
            if s[i] in index:
                # why max? Consider the case "abbadcf", then j = 0 at the start, then when we see b for the second time we make j = 2.
                # However when we see the 'a' second time j is already at 2 and index['a'] = 0. Hence we cannot move j back to j = 1. since that would bring the duplicate b back.
                j = max(index[s[i]] + 1, j)
            index[s[i]] = i
            max_len = max(i - j + 1, max_len)
        return max_len
    


s = Solution()
print(s.lengthOfLongestSubstring("abbcdcdabba"))