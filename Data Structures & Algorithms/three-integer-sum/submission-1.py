class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        result = []

        for i, val in enumerate(sortedNums):
            if i > 0 and sortedNums[i-1] == sortedNums[i]:
                continue
            left, right = i+1, len(sortedNums)-1
            while left < right:
                currTotal = sortedNums[left] + sortedNums[right] + val
                if currTotal > 0:
                    right -= 1
                elif currTotal < 0:
                    left += 1
                elif currTotal == 0:
                    result.append([val,sortedNums[left],sortedNums[right]])
                    left += 1
                    while sortedNums[left] == sortedNums[left - 1] and left < right:
                        left += 1
        return result

