class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        book = {}
        for c in s:
            if c not in book:
                book[c] = 0
            book[c] += 1

        for c in t:
            if c not in book:
                return False
            book[c] -= 1
            if book[c] == 0:
                del book[c]
        return len(book) == 0