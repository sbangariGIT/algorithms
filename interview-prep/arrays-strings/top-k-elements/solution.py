from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        book = Counter(nums)
        frequencies = [[] for i in range(len(nums) + 1)]
        for key in book:
            frequencies[book.get(key)].append(key)
        result = []
        for i in range(len(frequencies) - 1, -1, -1):
            # print(i)
            if k == 0:
                break
            if len(frequencies[i]) <= k:
                # print("adding", frequencies[i])
                result += frequencies[i]
                k -= len(frequencies[i])
                # print("k", k)
                continue
            if len(frequencies[i]) > k:
                # print("adding", frequencies[i])
                result += frequencies[i][:k]
                k -= len(frequencies[i][:k])
        return result
