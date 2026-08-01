import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        min_heap = []
        count = Counter(nums)
        for number, frequency in count.items():
            min_heap.append((-frequency, number))

        heapq.heapify(min_heap)

        answer = []
        for _ in range(k):
            freq, num = heapq.heappop(min_heap)
            answer.append(num)
        return answer