class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        while left <= right:
            k = (right - left) // 2 + left
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                right = k - 1
                res = k
            elif hours > h:
                left = k + 1
        return res


        # k = 1
        # while True:
        #     hours = 0
        #     for pile in piles:
        #         hours += math.ceil(pile / k)
        #     if hours <= h:
        #         return k
        #     k += 1