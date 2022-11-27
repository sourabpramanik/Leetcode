class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m!=0:
            gap=ceil((m+n)/2)
            while gap!=0:
                p=0
                q=gap
                
                while q<(m+n):
                    if q<m and nums1[p]>nums1[q]:
                        nums1[p], nums1[q] = nums1[q], nums1[p]
                
                    elif p<m and q>=m and nums1[p]>nums2[q-m]:
                        nums1[p], nums2[q-m] = nums2[q-m], nums1[p]

                    elif p>=m and q>=m and nums2[p-m]>nums2[q-m]:
                        nums2[p-m], nums2[q-m] = nums2[q-m], nums2[p-m]

                    p+=1
                    q+=1
                
                if gap==1:
                    gap=0
                else:
                    gap = ceil(gap/2)
                
               
          
        for num in nums2:
            nums1[m] = num
            m+=1
            