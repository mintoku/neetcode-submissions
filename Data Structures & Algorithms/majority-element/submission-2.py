from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # brute force: use counter

        # increment for each value up-down, the positive value at the end of the loop is the answer
        
        counted = Counter(nums)
        maximum = (0, 0) # index, count

        for value, count in counted.items():
            if maximum[1] < count:
                maximum = (value, count)
        return maximum[0]