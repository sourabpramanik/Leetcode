class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1 = 0        
        element2 = 0        
        count1 = 0        
        count2 = 0
        ans=[]
        for num in nums:
            if element1==num:
                count1+=1
                
            elif element2==num:                
                count2+=1
                
            elif count1==0:
                element1=num
                count1+=1
                
            elif count2==0:
                element2=num
                count2+=1
            
            else:
                count1-=1                
                count2-=1
        
        count1 = 0        
        count2 = 0
        for num in nums:
            if element1==num:
                count1+=1
            elif element2==num:
                count2+=1
        
        if count1>len(nums)/3:
            ans.append(element1)
        
        if count2>len(nums)/3:
            ans.append(element2)
        
        return ans