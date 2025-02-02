class Solution:
    def subarraySum(self, nums, k) -> int:
        # prefix sum, prefix that can be removed and count
        book = {}
        # this one is to count the case where no subarray needs to be removed
        book[0] = 1
        c_sum = 0
        result = 0
        for num in nums:
            c_sum += num
            prefix = c_sum - k
            if prefix in book:
                result += book[prefix]
            if c_sum not in book:
                book[c_sum] = 0
            book[c_sum] += 1
        return result
