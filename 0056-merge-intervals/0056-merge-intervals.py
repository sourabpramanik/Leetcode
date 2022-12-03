class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort(key=lambda x:x[0])
        ans=[intervals[0]]
        
        for i in range(1, n):
            start=intervals[i][0]            
            end=intervals[i][1]
            
            if start<=ans[-1][-1]:
                ans[-1][-1]=max(ans[-1][1], end)
                continue
            
            j=i+1
            while j<n:
                if intervals[j][0]<=end:
                    end=max(end, intervals[j][1])
                j+=1
                
            end=max(end, intervals[i][1])
            ans.append([start, end])
        return ans