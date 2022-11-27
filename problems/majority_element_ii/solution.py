class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1=0        
        ele2=0
        c1=0
        c2=0
        
        for num in nums:
            if ele1==num:
                c1+=1
            elif ele2==num:
                c2+=1
            elif c1==0:
                ele1=num
                c1+=1
            elif c2==0:
                ele2=num
                c2+=1
            else:
                c1-=1
                c2-=1
        
        c1=0
        c2=0
        
        for num in nums:
            if num==ele1:
                c1+=1
            elif num==ele2:
                c2+=1
        
        ans=[]
        if c1>len(nums)/3:
            ans.append(ele1)
            
        if c2>len(nums)/3:
            ans.append(ele2)
        
        return ans