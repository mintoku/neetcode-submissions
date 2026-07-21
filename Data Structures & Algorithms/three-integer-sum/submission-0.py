class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        sortedNums = sorted(nums)
        for fixedIndex in range(len(sortedNums)):
            left = fixedIndex + 1
            right = len(sortedNums) - 1

            target = -(sortedNums[fixedIndex])
            while left < right:
                curSum = sortedNums[left] + sortedNums[right]
                if curSum == target:
                    if [sortedNums[left], sortedNums[right], sortedNums[fixedIndex]] not in answer:
                        answer.append([sortedNums[left], sortedNums[right], sortedNums[fixedIndex]])
                    left += 1
                if curSum < target:
                    left += 1
                if curSum > target:
                    right -= 1
        return answer