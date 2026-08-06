class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                # Minimum is strictly to the right of middle.
                left = middle + 1
            else:
                # Middle could be the minimum, so keep it.
                right = middle

        return nums[left]