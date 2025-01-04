class Solution:
    def valid(self, s):
        return s != ''
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        res = list(filter(self.valid,arr))
        return " ".join(res[::-1])
    # Simiply " ".join(reversed(s.split()))