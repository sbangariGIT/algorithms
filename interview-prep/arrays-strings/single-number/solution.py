class Solution:
    def singleNumber(self, nums) -> int:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
                continue
            s.add(num)
        return s.pop()