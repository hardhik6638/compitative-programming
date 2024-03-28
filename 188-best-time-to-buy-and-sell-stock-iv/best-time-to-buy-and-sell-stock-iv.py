class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[float('-inf')]*(k+1) for i in range(2)] for j in range(len(prices))]
        for i in range(len(prices)):
            dp[i][0][0]=0
        dp[0][1][0]=-prices[0]
        for t in range(k+1):
            for i in range(1,len(prices)):
                dp[i][1][t]=max(dp[i-1][0][t]-prices[i],dp[i-1][1][t])
                dp[i][0][t] = max(dp[i-1][0][t], dp[i-1][1][t-1] + prices[i])
        return max(dp[len(prices)-1][0])


        