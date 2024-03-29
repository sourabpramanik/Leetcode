class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)

        i=n-1

        while i>=0:
            if i<n-1 and nums[i]<nums[i+1]:
                break
            i-=1

        if i>=0:
            j=n-1
            while j>=0 and nums[j]<=nums[i]:
                j-=1         

            nums[i], nums[j] = nums[j], nums[i]

        i=i+1
        j=n-1

        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
        

