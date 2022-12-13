class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=1
        h=n

        while l<=h:
            mid=(l+h)>>1
            if n>=mid*(mid+1)/2:
                l=mid+1
            else:
                h=mid-1
        
        return l-1