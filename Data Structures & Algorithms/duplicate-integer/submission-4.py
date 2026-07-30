class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # make nums a set
        # compare set of nums length vs nums length
        return not (len(set(nums)) == len(nums))