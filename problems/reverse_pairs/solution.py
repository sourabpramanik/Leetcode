class Solution:
    def __init__(self):
        self.count=0
        
    def reversePairs(self, nums: List[int]) -> int:
        
                
        return self.mergeSort(nums,0, len(nums)-1)
    def mergeSort(self,nums, l, r):                
        if l>=r: return 0
        mid = (l+r)//2
        self.count= self.mergeSort(nums, l, mid)
        self.count+= self.mergeSort(nums, mid+1, r)
        self.count+= self.merge(l,mid,r,nums)
        return self.count
    
    def merge(self, l, mid, r, nums):
        
        j=mid+1
        
        count=0
        for i in range(l, mid+1):
            while j<=r and nums[i]>2*nums[j]:
                j+=1
            count+=(j-(mid+1))
            
        left=l
        right=mid+1
        ds =[]
        
        while left<=mid and right<=r:
            if nums[left]<=nums[right]:
                ds.append(nums[left])
                left+=1
            else:
                ds.append(nums[right])
                right+=1
        
        while left<=mid:
            ds.append(nums[left])
            left+=1
        
        while right<=r:
            ds.append(nums[right])
            right+=1
            
        for i in range(l, r+1):
            nums[i] = ds[i-l]
        
        return count
           
                