class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        currMax = 0
        for num in nums:
            if num-1 in numSet:
                continue
            i = 1
            while num + i in numSet:
                i+=1
            currMax = max(i, currMax)
        return currMax