class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k > len(arr):
            return []
        if k == len(arr):
            return arr
        
        for right in range(k, len(arr)):
            left = right - k
            if arr[right] == arr[left]:
                continue
            if abs(arr[right] - x) >= abs(arr[left]-x):
                return arr[left:right]

        return arr[-k:]