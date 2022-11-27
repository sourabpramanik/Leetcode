class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s=0
        e=len(nums)-1
        n1=0
        n2=0
        tmp = []
        for i in range(0, len(nums)):
            tmp.append(nums[i])
        tmp.sort()
        while s<e:
            if tmp[s]+tmp[e]==target:
                n1=tmp[s]
                n2=tmp[e]
                break
            elif tmp[s]+tmp[e]>target:
                e-=1
            else:
                s+=1
                
        res=[]
        
        for i in range(0, len(nums)):
            if nums[i]==n1:
                res.append(i)
            elif nums[i]==n2:
                res.append(i)
        return res