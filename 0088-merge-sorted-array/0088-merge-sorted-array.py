class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m!=0:
            gap = math.ceil((m+n)/2)
            p1=0

            while gap!=0:
                p1=0
                p2=gap

                while p2<(n+m):
                    
                    if p2<m and nums1[p1]>nums1[p2]:
                        nums1[p1], nums1[p2] = nums1[p2], nums1[p1]
                        
                    elif p2>=m and p1<m and nums1[p1]>nums2[p2-m]:
                        nums1[p1],nums2[p2-m] = nums2[p2-m],nums1[p1]
                        
                    elif p2>=m and p1>=m and nums2[p1-m]>nums2[p2-m]:
                        nums2[p1-m],nums2[p2-m] = nums2[p2-m],nums2[p1-m]
                        

                    p1+=1
                    p2+=1

                if gap==1:
                    gap=0
                else:
                    gap = math.ceil(gap/2)
                    
        for num in nums2:
            nums1[m]=num
            m+=1