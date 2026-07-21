class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        for i in range(len(nums)-1):
            j = 1
            while j + i < len(nums):
                if nums[i+j] == nums[i]:
                    return True
                j+=1

        return False