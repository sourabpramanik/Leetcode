class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        
        return self.divide(nums, 0, len(nums)-1)
    
    def divide(self,arr, l, r):
        if l>=r: return 0
        mid=(l+r)//2
        count = self.divide(arr, l, mid)
        count += self.divide(arr, mid+1, r)
        count += self.merge(arr, l, mid, r)
        return count
    
    def merge(self, arr, low, mid, high):
        count=0
        j=mid+1
        ds=[]
        for i in range(low, mid+1):
            while j<=high and arr[i]>2*arr[j]:
                j+=1
            
            count+=j-(mid+1)
        
        i=low
        j=mid+1
        
        while i<=mid and j<=high:
            if arr[i]<=arr[j]:
                ds.append(arr[i])
                i+=1
            else:
                ds.append(arr[j])
                j+=1
        
        while i<=mid:
            ds.append(arr[i])
            i+=1
        
        while j<=high:
            ds.append(arr[j])
            j+=1
        
        for i in range(low, high+1):
            arr[i] = ds[i-low]
        
        return count
        
        
            
        
        