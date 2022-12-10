class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        k=k%n

        self.reverse(0, n-1, nums)
        self.reverse(0, k-1, nums)
        self.reverse(k, n-1, nums)
    
    def reverse(self, left, right, nums):
        while left<=right:
            nums[left], nums[right]=nums[right], nums[left]
            left+=1
            right-=1
        
        return nums

        
        
        
        