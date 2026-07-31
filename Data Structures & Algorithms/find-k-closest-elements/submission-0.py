class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        best_l, best_r = 0, k-1
        for right in range(k, len(arr)):
            left += 1
            if abs(arr[best_l] - x) > abs(arr[right] - x):
                best_l = left
                best_r = right
        return arr[best_l:best_r+1]