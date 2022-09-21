class Solution:
    def sumEvenAfterQueries(self, A, Q) -> List[int]:
        s = sum(a for a in A if a % 2 == 0)
        ans = []
        for val, idx in Q: 
            if A[idx] % 2 == 0:
                s -= A[idx]
            A[idx] += val
            if A[idx] % 2 == 0:
                s += A[idx] 
            ans.append(s)
        return ans