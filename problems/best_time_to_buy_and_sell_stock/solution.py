class Solution:
    def maxProfit(self, p: List[int]) -> int:
        maxProfit=0
        buy=p[0]
        for i in range(1, len(p)):
            buy = min(buy, p[i])
            maxProfit = max(maxProfit, p[i]-buy)
        
        return maxProfit