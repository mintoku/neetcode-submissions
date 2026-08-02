import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # push every num into into minheap. if minheap len > k, pop the smallest and 
        min_heap = []
        counted = Counter(nums)
        for number, count in counted.items():
            heapq.heappush(min_heap, (count, number))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        result = []
        for i in min_heap:
            result.append(i[1])
        return result