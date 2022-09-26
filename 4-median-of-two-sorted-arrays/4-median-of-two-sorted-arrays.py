class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr = self.merge(nums1, nums2)
        n = len(arr)
        
        if n%2==0:
            m=n//2
            p=arr[m]
            q=arr[m-1]
            return (p+q)/2
        else:
            m=n//2
            return arr[m]
    
    def merge(self, A, B):
        c1=0
        c2=0
        arr=[]
        
        while c1<len(A) and c2<len(B):
            if A[c1]<=B[c2]:
                arr.append(A[c1])
                c1+=1
            else:
                arr.append(B[c2])
                c2+=1
        
        while c1<len(A):
            arr.append(A[c1])
            c1+=1
        
        while c2<len(B):
            arr.append(B[c2])
            c2+=1
            
        return arr