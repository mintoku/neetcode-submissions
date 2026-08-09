class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # dp[i] = number of ways to reach step i
        dp = [0] * (n+1) # +1 because we're using 1 index
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]