class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        currMax = 0
        for number in nums:
            if number-1 in setNums:
                continue
            add = 0
            while number+add in setNums:
                add += 1
            currMax = max(currMax, add)

        return currMax