class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = self.sort(nums)
        return nums[len(nums)-k]
    def sort(self, arr):
        if len(arr)==1: return arr
        mid = len(arr)//2
        
        L = self.sort(arr[0:mid])        
        R = self.sort(arr[mid:])
        
        return self.merger(arr, L, R)
    
    def merger(self,arr, L, R):
        k=0
        l=0
        r=0
        while l<len(L) and r<len(R):
            if L[l]<R[r]:
                arr[k]=L[l]                
                l+=1
            else:
                arr[k]=R[r]                
                r+=1
            k+=1
        
        while l<len(L):
            arr[k]=L[l]
            k+=1
            l+=1
            
        while r<len(R):
            arr[k]=R[r]
            k+=1
            r+=1
        
        return arr
        