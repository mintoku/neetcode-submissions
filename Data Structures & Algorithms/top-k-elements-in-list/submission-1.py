import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # naive approach: use counter to count frequency of each number
        # sort frequency and return top k elements
        # this approach is o(nlogn) time

        # faster: use min_heap and pop everytime the heap is larger than k
        min_heap = []
        count = Counter(nums)
        for number, frequency in count.items():
            heapq.heappush(min_heap, (frequency, number))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        # min_heap = [(2,2),(3,3)]
        answer = []
        for pair in min_heap:
            answer.append(pair[1])
        return answer