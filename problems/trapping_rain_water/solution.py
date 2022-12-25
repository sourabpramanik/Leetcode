class Solution:
    def trap(self, heights: List[int]) -> int:
        n=len(heights)
        ans=0
        leftMax=0
        rightMax=0
        low=0
        high=n-1
        while low<=high:
            if heights[low]<=heights[high]:
                if leftMax<heights[low]:
                    leftMax=heights[low]
                else:
                    ans+=leftMax-heights[low]
                low+=1
            else:
                if rightMax<heights[high]:
                    rightMax=heights[high]
                else:
                    ans+=rightMax-heights[high]
                high-=1
            
        return ans