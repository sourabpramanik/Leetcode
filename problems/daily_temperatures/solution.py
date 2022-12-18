class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        st=[]
        n=len(temps)

        arr=[0]*n

        for i in range(0, n):
            while st and temps[st[-1]]<temps[i]:
                cur = st.pop()
                arr[cur] = i-cur
            
            st.append(i)

        return arr
