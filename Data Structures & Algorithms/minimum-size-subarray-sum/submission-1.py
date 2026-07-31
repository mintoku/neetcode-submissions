class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # start two pointers left (beg) and right (beg)
        # constantly (while loop) check if window adds to >= target
        # shrink while keeping condition valid (left/right depending on smaller)
        # when condition not valid, return previous valid
        if sum(nums) < target: return 0
        
        left, right = 0, 0
        curr_sum = nums[0]
        curr_max = len(nums)
        while left <= right and right < len(nums):
            while curr_sum >= target:
                curr_max = min(curr_max, right-left+1)
                left += 1
                curr_sum -= nums[left-1]
            right += 1
            if right < len(nums):
                curr_sum += nums[right]
        return curr_max

    