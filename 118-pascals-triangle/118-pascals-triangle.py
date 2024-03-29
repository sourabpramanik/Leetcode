class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()        
        pre = None
        
        for i in range(0, numRows):
            row=[]
            for j in range(0, i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(pre[j-1]+pre[j])
                
            pre = row
            res.append(row)
        return res