class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        
    def reverse(self, arr, s, e):
        while(s<e):
            t = arr[s]
            arr[s] = arr[e]
            arr[e] = t
            s+=1
            e-=1
        