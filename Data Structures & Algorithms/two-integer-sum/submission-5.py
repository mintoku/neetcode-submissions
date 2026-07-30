class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # naive: loop through every pair and check if both sum to target
        # naive: O(n^2)
        
        # better:
        # keep a hashmap of all seen values; for each value, if not seen then add to hashmap
        # hashmap value:index
        # when we loop through, find number complement, and check if its in the hashmap

        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i