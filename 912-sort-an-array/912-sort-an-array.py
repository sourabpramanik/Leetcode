class Solution:
    
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        
        mid = len(nums)//2
        
        L = self.sortArray(nums[:mid])
        R = self.sortArray(nums[mid:])
        
        return self.merge(nums, L, R)
    
    def merge(self,arr, L, R):
        l=0
        r=0
        k=0
        
        while(l<len(L) and r<len(R)):
            if L[l]<=R[r]:
                arr[k]=L[l]
                l+=1
            else:
                arr[k]=R[r]
                r+=1
            k+=1
        
        while l<len(L):
            arr[k]=L[l]
            l+=1
            k+=1
        
        while r<len(R):
            arr[k]=R[r]
            r+=1
            k+=1
        
        return arr
    
    