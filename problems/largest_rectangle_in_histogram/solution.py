class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=[-1]*n
        right=[-1]*n
        stack=[]

        for i in range(0, n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                left[i]=stack[-1]+1
            else:
                left[i]=0
            stack.append(i)

        while stack:
            stack.pop()

        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                right[i]=stack[-1]-1
            else:
                right[i]=n-1
            stack.append(i)

        ans=0
        for i in range(0, n):
            ans=max(ans, heights[i]*(right[i]-left[i]+1))
        return ans
