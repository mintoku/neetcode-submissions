class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        left, right = 0, 1
        profit = 0
        while left <= right and right < len(prices):
            if prices[right] < prices[left]:
                left = right
            
            profit = max(profit, prices[right] - prices[left])
            right += 1
        return profit