class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # iterate left to right, store prefix products for each index in a prefix array
        # iterate right to left, store suffix products in suffix array
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]

        return result