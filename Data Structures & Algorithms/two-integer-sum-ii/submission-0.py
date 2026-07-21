class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(numbers):
            complement = target - num
            if (complement in seen):
                solution = [seen[complement]+1, index+1]
                break
            seen[num] = index

        if solution[0] > solution[1]:
            solution[0], solution[1] = solution[1], solution[0]
        return solution