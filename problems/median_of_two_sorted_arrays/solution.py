class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n1=len(nums1)
        n2=len(nums2)

        low=0
        high=n1
        
        while low<=high:
            mid = (low+high)//2
            cut1=mid
            cut2=(n1+n2+1)//2-cut1

            l1= float("-inf") if cut1==0 else nums1[cut1-1]
            l2= float("-inf") if cut2==0 else nums2[cut2-1]

            r1= float("inf") if cut1==n1 else nums1[cut1]
            r2= float("inf") if cut2==n2 else nums2[cut2]

            if l1 <= r2 and l2 <= r1:
                if (n1+n2)%2==1:
                    return max(l1, l2)
                    
                else:
                    return (max(l1, l2) + min(r1, r2))/2
            elif l1>r2:
                high=cut1-1
            else:
                low=cut1+1
        
        return 0.0



