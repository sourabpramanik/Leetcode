class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]
        n=len(prices)
        for i in range(1, n):
            buy=min(buy, prices[i])
            profit = max(profit, prices[i]-buy)
        
        return profit