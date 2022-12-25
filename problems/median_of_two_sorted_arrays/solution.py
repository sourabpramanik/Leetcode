class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m=len(nums1)
        n=len(nums2)

        l=0
        h=m

        while l<=h:
            mid=(l+h)>>1
            cut1=mid
            cut2=(n+m+1)//2-cut1

            l1=float("-inf") if cut1==0 else nums1[cut1-1]
            l2=float("-inf") if cut2==0 else nums2[cut2-1]

            r1=float("inf") if cut1==m else nums1[cut1]
            r2=float("inf") if cut2==n else nums2[cut2]

            if l1<=r2 and l2<=r1:
                if (n+m)%2==0:
                    return (max(l1, l2)+min(r1, r2))/2
                else:
                    return max(l1, l2)
            elif l1>r2:
                h=mid-1
            else:
                l=mid+1
        return 0.0