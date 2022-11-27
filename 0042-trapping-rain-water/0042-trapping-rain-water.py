class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ans=0
        pre=[1]*n        
        suf=[1]*n
        pre[0]=height[0]        
        suf[-1]=height[-1]
        
        for i in range(1, n):
            pre[i]=max(pre[i-1],height[i])
        
        for i in range(n-2, -1, -1):
            suf[i]=max(suf[i+1],height[i])
        
        for i in range(0, n):
            ans += min(pre[i], suf[i]) - height[i]
        
        return ans