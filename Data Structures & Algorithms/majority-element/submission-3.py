from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # brute force: use counter

        # increment for each value up-down, the positive value at the end of the loop is the answer
        
        # counted = Counter(nums)
        # maximum = (0, 0) # index, count

        # for value, count in counted.items():
        #     if maximum[1] < count:
        #         maximum = (value, count)
        # return maximum[0]

        placeholder = nums[0]
        count = 0
        for i in nums:
            if placeholder == i:
                count += 1
            else:
                count -= 1
            if count < 0:
                placeholder = i
        return placeholder