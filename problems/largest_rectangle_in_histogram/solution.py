class Solution:
    def largestRectangleArea(self, H: List[int]) -> int:
        n=len(H)
        st=[]
        maxArea=0

        for i in range(0, n+1):
            while st and (H[st[-1]]>=(H[i] if i<n else 0)):
                height=H[st[-1]]
                st.pop()
                width=0
                if st:
                    width=i-st[-1]-1
                else:
                    width=i
                
                maxArea=max(maxArea, height*width)
            st.append(i)
        return maxArea
                