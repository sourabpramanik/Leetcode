class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ans=0
        l=0
        r=n-1
        leftMax=0
        rightMax=0
        while l<r:
            if height[l]<=height[r]:
                if leftMax<height[l]:
                    leftMax=height[l]
                else:
                    ans += leftMax-height[l]
                l+=1
            else:
                if rightMax<height[r]:
                    rightMax=height[r]
                else:
                    ans += rightMax-height[r]
                r-=1
            
        
        return ans