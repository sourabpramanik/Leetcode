class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temp)
        
        for i, t in enumerate(temp):
            while stack and temp[stack[-1]]<t:
                cur = stack.pop()
                ans[cur] = i-cur
            
            stack.append(i)
        
        return ans