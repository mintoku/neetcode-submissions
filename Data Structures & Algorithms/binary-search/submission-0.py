class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = int((high-low) / 2) + low
            if target < nums[middle]:
                high = middle-1
            elif target > nums[middle]:
                low = middle+1
            elif target == nums[middle]: return middle
        return -1
        