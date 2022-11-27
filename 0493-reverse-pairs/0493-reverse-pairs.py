class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count=0
        return self.divide(nums, 0, len(nums)-1)
    
    def divide(self, nums, l, r):
        count=0
        if l<r:
            mid=(l+r)//2
            count+= self.divide(nums, l, mid)            
            count+= self.divide(nums, mid+1, r)
            count+= self.merge(nums, l, mid, r)
        
        return count
    
    def merge(self, nums, l, mid, r):
        ds=[]
        count=0
        j=mid+1        
        for i in range(l, mid+1):
            while j<=r and nums[i]>2*nums[j]:
                j+=1
            count+=(j-(mid+1))
            
        i=l
        j=mid+1
        
        while i<=mid and j<=r:
            if nums[i]<=nums[j]:
                ds.append(nums[i])
                i+=1
            else:
                ds.append(nums[j])
                j+=1
        
        while i<=mid:
            ds.append(nums[i])
            i+=1
        
        while j<=r:
            ds.append(nums[j])
            j+=1
            
        for i in range(l, r+1):
            nums[i]=ds[i-l]
        
        return count