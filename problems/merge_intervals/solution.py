class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort(key=lambda x:x[0])
        ans=[]
        pair=arr[0]
        for i in range(1, len(arr)):
            if pair[1]>=arr[i][0]:
                pair[1]=max(pair[1], arr[i][1])
            else:
                ans.append(pair)
                pair=arr[i]
        ans.append(pair)
        return ans