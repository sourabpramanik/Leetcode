class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals)<2: return intervals
        ans=[]
        intervals = sorted(intervals)
        print(intervals)
        
        for i in range(0,len(intervals)):
                        
            col=intervals[i]
            if(len(ans)==0 or ans[-1][1]<col[0]):
                ans.append(col)
            else:
                ans[-1][1]=max(col[1], ans[-1][1])                    
                    
                    
        
        return ans