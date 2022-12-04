class Solution:
    def trap(self, H: List[int]) -> int:
        n=len(H)
        ans=0
        leftMax=0
        rightMax=0
        l=0
        r=n-1
        
        while l<=r:
            if H[l]<=H[r]:
                if leftMax < H[l]:
                    leftMax=H[l]
                else:
                    ans+=leftMax-H[l]
                l+=1
            else:
                if rightMax < H[r]:
                    rightMax=H[r]
                else:
                    ans+=rightMax-H[r]
                r-=1
        return ans
            