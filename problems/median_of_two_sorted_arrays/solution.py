class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)

        nums1.sort()

        mid=(len(nums1))//2
        if len(nums1)%2==0:
            return (nums1[mid]+nums1[mid-1])/2
        return nums1[mid]
