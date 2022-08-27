class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        obj=dict()
        res=[]
        
        for i, v in enumerate(nums):
            if v in obj:
                obj[v]+=1
            else:
                obj[v]=1
        
        for v in obj:
            if(obj[v]>len(nums)/3):
                res.append(v)
        
        return res