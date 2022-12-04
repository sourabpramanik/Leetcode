class Solution:
    def trap(self, H: List[int]) -> int:
        n=len(H)
        ans=0
        pre=[0]*n
        suf=[0]*n
        pre[0]=H[0]
        suf[-1]=H[-1]
        
        for i in range(1, n):
            pre[i]=max(pre[i-1], H[i])
        
        for i in range(n-2, -1, -1):
            suf[i]=max(suf[i+1], H[i])
        
        for i in range(0, n):
            ans+=min(pre[i], suf[i])-H[i]
        return ans
            