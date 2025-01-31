"""
Log(n) divide and conquer
"""

class Solution:
    def myPowHelper(self, x, n):
        # print("Caluclating for", x, "to the power", n)
        if x == 0.0:
            return x
        if n == 0:
            return 1.0
        if n == 1:
            return x

        if n % 2 == 0:
            ans = self.myPow(x, n/2)
            # print("Got", ans, "from", x, "to the power", n/2)
            # print("Returning", ans * ans)
            return ans * ans
        else:
            ans = self.myPow(x, n//2)
            # print("Got", ans, "from", x, "to the power", n//2)
            # print("Returning", 2.0 * ans * ans)
            return x * ans * ans

    def myPow(self, x: float, n: int) -> float:
        ans = self.myPowHelper(x, abs(n))
        if n < 0:
            return 1/ans
        return ans
        
        
        