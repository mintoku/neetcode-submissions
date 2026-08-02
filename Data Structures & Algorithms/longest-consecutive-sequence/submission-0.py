class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for number in nums:
            if number - 1 not in numSet:
                j = 1
                while number + j in numSet:
                    j += 1
                longest = max(longest, j)

        return longest