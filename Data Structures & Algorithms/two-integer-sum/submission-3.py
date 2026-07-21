class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # value : index in nums
        for index, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], index]
            seen[value] = index
            