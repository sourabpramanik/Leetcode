class Solution:
    def numRollsToTarget(self, n: int, f: int, target: int) -> int:
        memo = {}
        def dp(n, target):
            if n == 0:
                return 0 if target > 0 else 1
            if (n, target) in memo:
                return memo[(n, target)]
            to_return = 0
            for k in range(max(0, target-f), target):
                to_return += dp(n-1, k)
            memo[(n, target)] = to_return
            return to_return
        return dp(n, target) % (10**9 + 7)