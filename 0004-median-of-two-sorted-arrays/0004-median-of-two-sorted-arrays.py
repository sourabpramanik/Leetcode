class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=[]
        
        j=0
        i=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        
        while i<len(nums1):
            nums.append(nums1[i])
            i+=1   
        
        while j<len(nums2):
            nums.append(nums2[j])
            j+=1    
        
        n=len(nums)
        
        if n%2==1:
            return nums[n//2]
        return (nums[(n//2)-1]+nums[(n//2)])/2