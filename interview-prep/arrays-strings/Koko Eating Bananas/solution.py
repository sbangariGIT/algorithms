class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 0
        min_speed = r
        def canKokoFinishWithk(k, piles, h) -> bool:
            required_hours = 0
            for pile in piles:
                required_hours += math.ceil(pile / k)
            return required_hours <= h
        while l <= r:
            mid = (l + r) // 2
            if mid == 0:
                break
            if canKokoFinishWithk(mid, piles, h):
                min_speed = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_speed
