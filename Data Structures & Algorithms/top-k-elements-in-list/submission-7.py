import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        for num, count in Counter(nums).items():
            heapq.heappush(minHeap, (count, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        for count, val in minHeap:
            res.append(val)
        return res