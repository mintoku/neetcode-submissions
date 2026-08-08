class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        minFound = right
        while left <= right:
            middle = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/middle)
            if hours <= h:
                minFound = middle
                right = middle - 1
            else:
                left = middle + 1
            
        return minFound