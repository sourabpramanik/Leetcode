class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort(key=lambda x:x[0])
        pair=intervals[0]
        ans=[]
        for i in range(1, n):
           
            if intervals[i][0]<=pair[1]:
                pair[1]=max(pair[1], intervals[i][1])
            else:
                ans.append(pair)
                pair=intervals[i]
        ans.append(pair)
        return ans