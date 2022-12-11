class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor=nums[0]
        n=len(nums)

        for i in range(1, n):
            xor^=nums[i]
        
        for i in range(1, n+1):
            xor^=i

        set_bit=xor&~(xor-1)
        x=0
        y=0
        for i in range(0, n):
            if set_bit&nums[i]:
                x=x^nums[i]
            else:
                y=y^nums[i]
        
        for i in range(1, n+1):
            if set_bit&i:
                x=x^i
            else:
                y=y^i
        
        count=0

        for n in nums:
            if x==n:
                count+=1
        
        if count==0:
            return x
        
        return y