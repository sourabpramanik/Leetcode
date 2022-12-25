class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact=1
        nums=[]
        ans=""

        for i in range(1, n):
            fact*=i
            nums.append(i)
        
        nums.append(n)
        k-=1
        while True:
            i=k//fact
            ans+=str(nums[i])
            nums.pop(i)
            if len(nums)==0:
                break
            k=k%fact
            fact=fact//len(nums)
        
        return ans
