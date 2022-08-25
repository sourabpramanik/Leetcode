class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(A, i, j):
            t=A[i]
            A[i]=A[j]
            A[j]=t
        
        def rev(A, i, j):
            while(i<j):
                swap(A, i, j)
                i+=1
                j-=1
                
        idx1=len(nums)-2
        
        
        while(idx1>=0 and nums[idx1]>=nums[idx1+1]): idx1-=1
        
        if(idx1>=0):
            idx2=len(nums)-1
            while(nums[idx2]<=nums[idx1]):idx2-=1
            
            swap(nums, idx1, idx2)
        
        rev(nums, idx1+1, len(nums)-1)
                