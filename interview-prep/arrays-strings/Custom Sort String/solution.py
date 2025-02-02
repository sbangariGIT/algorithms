from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        result = ""
        # preserve the order
        for c in order:
            if c in count:
                result += c * count[c]
                del count[c]
        for c in count.keys():
            result += c * count[c]
        return result
