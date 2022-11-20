class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count=0
        self.mergeSort(nums, 0, len(nums)-1)
        return self.count
    
    def mergeSort(self, nums, l, r):
        if l==r:
            return 0
        mid = (l+r)//2
        self.count=self.mergeSort(nums, l, mid)        
        self.count+=self.mergeSort(nums, mid+1, r)
        self.count+=self.merge(nums, l, mid, r)
        
        return self.count
    
    def merge(self, nums, left, mid, right):
        ds=[]
        count=0
        j=mid+1
        for i in range(left, mid+1):            
            while j<=right and nums[i]>2*nums[j]:                
                j+=1
            count+=(j-(mid+1))
        
        i=left
        j=mid+1
    
        while i<=mid and j<=right:
            if nums[i]<=nums[j]:
                ds.append(nums[i])
                i+=1
            else:
                ds.append(nums[j])
                j+=1
           
            
        while i<=mid:
            ds.append(nums[i])
            i+=1
        
        while j<=right:
            ds.append(nums[j])
            j+=1
        
        for i in range(left, right+1):
            nums[i] = ds[i-left]
        return count