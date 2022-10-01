class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l=0
        r=len(nums)
        nums.sort(reverse=True)
        while l<r:
            mid = (l+r)//2
            
            if mid<nums[mid]:
                l = mid+1
            else:
                r=mid
        
        return -1 if l<len(nums) and l==nums[l] else l