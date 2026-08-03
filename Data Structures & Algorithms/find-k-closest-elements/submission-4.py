class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        bestRight = k-1

        for right in range(k, len(arr)):
            if (abs(arr[right] - x)) < abs(arr[right-k] - x):
                bestRight = right
        bestLeft = bestRight - k + 1
        return arr[bestLeft:bestRight+1]